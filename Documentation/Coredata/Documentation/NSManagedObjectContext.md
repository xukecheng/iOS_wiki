Initializer

# init(_:)

Creates a context that uses the specified concurrency type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    convenience init(_ type: NSManagedObjectContext.ConcurrencyType)

##  Parameters

`type`

    

The context’s concurrency type. For possible values, see
`NSManagedObjectContext.ConcurrencyType`.

## Discussion

For more information, see Concurrency.

## See Also

### Creating a context

`struct NSManagedObjectContext.ConcurrencyType`

The concurrency types to use with a managed object context.

`enum NSManagedObjectContextConcurrencyType`

The concurrency types you can use with a managed object context.

Instance Property

# persistentStoreCoordinator

The persistent store coordinator of the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get set }

## Return Value

The persistent store coordinator of the receiver.

## Discussion

The coordinator provides the managed object model and handles persistency.
Note that multiple contexts can share a coordinator. May not be `nil`.

Setting `persistentStoreCoordinator` to `nil` will raise an exception. If you
want to “disconnect" a context from its persistent store coordinator, you
should simply set all strong references to the context to `nil` and allow it
to be deallocated normally.

For more details, see Parent store.

## See Also

### Configuring a context

`var parent: NSManagedObjectContext?`

The parent of the context.

`var name: String?`

The developer-provided name of the context.

`var userInfo: NSMutableDictionary`

The user information for the context.

Instance Property

# parent

The parent of the context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var parent: NSManagedObjectContext? { get set }

## Discussion

`nil` indicates there is no parent context. For more details, see Parent
store.

## See Also

### Configuring a context

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator of the context.

`var name: String?`

The developer-provided name of the context.

`var userInfo: NSMutableDictionary`

The user information for the context.

Instance Property

# name

The developer-provided name of the context.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String? { get set }

## See Also

### Configuring a context

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator of the context.

`var parent: NSManagedObjectContext?`

The parent of the context.

`var userInfo: NSMutableDictionary`

The user information for the context.

Instance Property

# userInfo

The user information for the context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: NSMutableDictionary { get }

## See Also

### Configuring a context

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator of the context.

`var parent: NSManagedObjectContext?`

The parent of the context.

`var name: String?`

The developer-provided name of the context.

Instance Method

# fetch(_:)

Returns an array of objects that meet the criteria of the specified fetch
request.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 13.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 6.0.1+

    
    
    func fetch(_ request: NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]

##  Parameters

`request`

    

A fetch request that specifies the search criteria for the fetch.

`error`

    

If there is a problem executing the fetch, upon return contains an instance of
`NSError` that describes the problem.

## Return Value

An array of objects that meet the criteria specified by `request` fetched from
the receiver and from the persistent stores associated with the receiver’s
persistent store coordinator. If an error occurs, returns `nil`. If no objects
match the criteria specified by `request`, returns an empty array.

## Discussion

Returned objects are registered with the receiver.

The following points are important to consider:

  * If the fetch request has no predicate, then all instances of the specified entity are retrieved, modulo other criteria below.

  * An object that meets the criteria specified by `request` (it is an instance of the entity specified by the request, and it matches the request’s predicate if there is one) and that has been inserted into a context but which is not yet saved to a persistent store, is retrieved if the fetch request is executed on that context.

  * If an object in a context has been modified, a predicate is evaluated against its modified state, not against the current state in the persistent store. Therefore, if an object in a context has been modified such that it meets the fetch request’s criteria, the request retrieves it even if changes have not been saved to the store and the values in the store are such that it does not meet the criteria. Conversely, if an object in a context has been modified such that it does not match the fetch request, the fetch request will not retrieve it even if the version in the store does match.

  * If an object has been deleted from the context, the fetch request does not retrieve it even if that deletion has not been saved to a store.

Objects that have been realized (populated, faults fired, “read from”, and so
on) as well as pending updated, inserted, or deleted, are never changed by a
fetch operation without developer intervention. If you fetch some objects,
work with them, and then execute a new fetch that includes a superset of those
objects, you do not get new instances or update data for the existing
objects—you get the existing objects with their current in-memory state.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Registering and fetching objects

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

### Related Documentation

Core Data Programming Guide

Predicate Programming Guide

Core Data Snippets

Generic Instance Method

# fetch(_:)

Returns an array of items of the specified type that meet the fetch request’s
critieria.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 8.0+

    
    
    func fetch<T>(_ request: NSFetchRequest<T>) throws -> [T] where T : NSFetchRequestResult

##  Parameters

`request`

    

The fetch request that specifies the search criteria.

## Discussion

This method fetches objects from the context and the persistent stores that
you associate with the context’s persistent store coordinator. The method
registers any objects it retrieves from a store with the context.

Consider the following when fetching:

  * If the fetch request doesn’t have a predicate, it returns all instances of the specified entity.

  * The fetch results include any object in the context that’s an instance of the request’s entity, and that meets the request’s criteria, even if the context has yet to save the object to a persistent store.

  * The fetch request evalutes the in-memory state of each object. Therefore, the fetch results include any unsaved objects with changes that cause them to meet the request’s criteria, even if their counterparts in the persistent store don’t. Conversely, the results don’t include unsaved objects with in-memory changes that mean they no longer meet the criteria, even if their store versions do.

  * The fetch results don’t include deleted objects, even if the context has yet to save the deletion to the persistent store.

A fetch never changes realized objects, or those with pending changes, without
developer intervention. If you fetch objects, modify them, and then execute a
new fetch that includes a superset of those objects, you don’t receive new
instances of those objects. Instead, you receive the existing objects with
their current in-memory state.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# count(for:)

Returns the number of objects the specified request fetches when it executes.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func count(for request: NSFetchRequest<any NSFetchRequestResult>) throws -> Int

##  Parameters

`request`

    

A fetch request that specifies the search criteria for the fetch.

`error`

    

If there is a problem executing the fetch, upon return contains an instance of
`NSError` that describes the problem.

## Return Value

The number of objects a given fetch request would have returned if it had been
passed to `fetch(_:)`, or `NSNotFound` if an error occurs.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# registeredObject(for:)

Returns an object that exists in the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func registeredObject(for objectID: NSManagedObjectID) -> NSManagedObject?

##  Parameters

`objectID`

    

The identifier of the object to retrieve. For more information, see
`NSManagedObjectID`.

## Return Value

The identified object, if it’s known to the context; otherwise, `nil`.

## Discussion

This method provides a convenient way to retrieve an object from the context’s
`registeredObjects` property. A `nil` return value means the context doesn’t
recognize the specified object; the object might still exist in the persistent
store. If you need to query both the context and the store, use
`existingObject(with:)` instead.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# object(with:)

Returns either an existing object from the context or a fault that represents
that object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func object(with objectID: NSManagedObjectID) -> NSManagedObject

##  Parameters

`objectID`

    

The identifier of the object to retrieve. For more information, see
`NSManagedObjectID`.

## Return Value

The identified object, if its known to the context; otherwise, a fault with
its `objectID` property set to `objectID`.

## Discussion

If the context doesn’t recognize the specified object, this method returns a
_fault_ — a placeholder object that doesn’t load its properties until your
code accesses them. The context then fetches the corresponding values from the
persistent store and uses those values to turn the fault into a fully realized
object.

When this method returns a fault, Core Data makes no attempts to verify the
existence of the underlying object in the persistent store. If the object
doesn’t exist when the context tries to the fetch the object’s values, the
framework throws an exception.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# existingObject(with:)

Returns an existing object from either the context or the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func existingObject(with objectID: NSManagedObjectID) throws -> NSManagedObject

##  Parameters

`objectID`

    

The identifier of the object to retrieve. For more information, see
`NSManagedObjectID`.

## Return Value

The identified object from either the context or the persistent store.

## Discussion

If the context recognizes the specified object, the method returns that
object. Otherwise, the context fetches and returns a fully realized object
from the persistent store; unlike `object(with:)`, this method never returns a
fault. If the object doesn’t exist in both the context and the persistent
store, the method throws an error.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Property

# registeredObjects

The set of registered managed objects in the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var registeredObjects: Set<NSManagedObject> { get }

## Discussion

A managed object context does not post key-value observing notifications when
the return value of `registeredObjects` changes.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

### Related Documentation

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

Generic Instance Method

# count(for:)

Returns a count of the objects the specified request fetches when it executes.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 8.0+

    
    
    func count<T>(for request: NSFetchRequest<T>) throws -> Int where T : NSFetchRequestResult

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# execute(_:)

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func execute(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Method

# refreshAllObjects()

Refreshes all of the registered managed objects in the context.

iOS 8.3+  iPadOS 8.3+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func refreshAllObjects()

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`var retainsRegisteredObjects: Bool`

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

Instance Property

# retainsRegisteredObjects

A Boolean value that indicates whether the context keeps strong references to
all registered managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var retainsRegisteredObjects: Bool { get set }

## Discussion

If set to `true`, the receiver keeps strong references to all registered
managed objects. If set to `false`, then the receiver keeps strong references
to registered objects only when they are inserted, updated, deleted, or
locked. The default is `false`.

## See Also

### Registering and fetching objects

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

`func fetch<T>(NSFetchRequest<T>) -> [T]`

Returns an array of items of the specified type that meet the fetch request’s
critieria.

`func count(for: NSFetchRequest<any NSFetchRequestResult>) -> Int`

Returns the number of objects the specified request fetches when it executes.

`func registeredObject(for: NSManagedObjectID) -> NSManagedObject?`

Returns an object that exists in the context.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func existingObject(with: NSManagedObjectID) -> NSManagedObject`

Returns an existing object from either the context or the persistent store.

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`func count<T>(for: NSFetchRequest<T>) -> Int`

Returns a count of the objects the specified request fetches when it executes.

`func execute(NSPersistentStoreRequest) -> NSPersistentStoreResult`

Passes a request to the persistent store without affecting the contents of the
managed object context, and returns a persistent store result.

`func refreshAllObjects()`

Refreshes all of the registered managed objects in the context.

Instance Property

# shouldDeleteInaccessibleFaults

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var shouldDeleteInaccessibleFaults: Bool { get set }

## Discussion

Use this property to control how the context behaves when it encounters an
_inaccessible fault_ — an object with no underlying data in the persistent
store. For example, you might fetch an object that has a to-many relationship,
but then a background context deletes the related objects from the store
before you traverse that relationship.

When this property is set to `true`, the context returns a managed object with
the following characteristics:

  * The object’s attributes, including scalars, nullable, and mandatory attributes are all set to `nil` or `0`.

  * The object’s `isDeleted` property is set to `true`, which adds the object to the context’s `deletedObjects` set.

  * The object is exempt from validation rules, including optionality, because the object is nonexistent and the context discards it when you next call `save()` or `reset()`.

When the context returns an object with these characteristics, your app can
continue running and process this object in the same way as any other deleted
object.

When this property is set to `false`, the context throws an exception.

The default value is `true`.

Note

You can use query generations to pin a context to a stable view of the store’s
data and isolate that context from changes that other contexts or processes
make. For more information, see Accessing data when the store changes.

## See Also

### Handling managed objects

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

Instance Property

# insertedObjects

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var insertedObjects: Set<NSManagedObject> { get }

## Discussion

A managed object context does not post key-value observing notifications when
the return value of `insertedObjects` changes—it does, however, post a
`NSManagedObjectContextObjectsDidChange` notification when a change is made,
and a `NSManagedObjectContextWillSave` and a `NSManagedObjectContextDidSave`
notification before and after changes are committed respectively.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

Instance Property

# updatedObjects

The set of objects registered with the context that have uncommitted changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var updatedObjects: Set<NSManagedObject> { get }

## Discussion

A managed object context does not post key-value observing notifications when
the return value of `updatedObjects` changes. A context does, however, post a
`NSManagedObjectContextObjectsDidChange` notification when a change is made,
and a `NSManagedObjectContextWillSave` notification and a
`NSManagedObjectContextDidSave` notification before and after changes are
committed respectively.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

Instance Property

# deletedObjects

The set of objects that will be removed from their persistent store during the
next save operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var deletedObjects: Set<NSManagedObject> { get }

## Discussion

The returned set does not necessarily include all the objects that have been
deleted (using `delete(_:)`)—if an object has been inserted and deleted
without an intervening save operation, it may not be included in the set.

A managed object context does not post key-value observing notifications when
the return value of `deletedObjects` changes. A context does, however, post a
`NSManagedObjectContextObjectsDidChange` notification when a change is made,
and a `NSManagedObjectContextWillSave` notification and a
`NSManagedObjectContextDidSave` notification before and after changes are
committed respectively (although again the set of deleted objects given for an
`NSManagedObjectContextDidSave` does not include objects that were inserted
and deleted without an intervening save operation—that is, they had never been
saved to a persistent store).

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var registeredObjects: Set<NSManagedObject>`

The set of registered managed objects in the context.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

Instance Method

# shouldHandleInaccessibleFault(_:for:triggeredByProperty:)

Creates a log of the inaccessible fault.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func shouldHandleInaccessibleFault(
        _ fault: NSManagedObject,
        for oid: NSManagedObjectID,
        triggeredByProperty property: NSPropertyDescription?
    ) -> Bool

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

Instance Method

# insert(_:)

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func insert(_ object: NSManagedObject)

##  Parameters

`object`

    

A managed object.

## Discussion

The managed object (`object`) is registered in the receiver with a temporary
global ID. It is assigned a permanent global ID when changes are committed. If
the current transaction is rolled back (for example, if the receiver is sent a
`rollback()` message) before a save operation, the object is unregistered from
the receiver.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

Instance Method

# delete(_:)

Specifies an object that should be removed from its persistent store when
changes are committed.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func delete(_ object: NSManagedObject)

##  Parameters

`object`

    

A managed object.

## Discussion

When changes are committed, `object` will be removed from the uniquing tables.
If `object` has not yet been saved to a persistent store, it is simply removed
from the receiver.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

Instance Method

# assign(_:to:)

Specifies the store in which a newly inserted object will be saved.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func assign(
        _ object: Any,
        to store: NSPersistentStore
    )

##  Parameters

`object`

    

A managed object.

`store`

    

A persistent store.

## Discussion

You can obtain a store from the persistent store coordinator, using for
example `persistentStore(for:)`.

### Special Considerations

It is only necessary to use this method if the receiver’s persistent store
coordinator manages multiple writable stores that have `object`’s entity in
their configuration. Maintaining configurations in the managed object model
can eliminate the need for invoking this method directly in many situations.
If the receiver’s persistent store coordinator manages only a single writable
store, or if only one store has `object`’s entity in its model, `object` will
automatically be assigned to that store.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator of the context.

Instance Method

# obtainPermanentIDs(for:)

Converts to permanent IDs the object IDs of the objects in a given array.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func obtainPermanentIDs(for objects: [NSManagedObject]) throws

##  Parameters

`objects`

    

An array of managed objects.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if permanent IDs are obtained for all the objects in `objects`,
otherwise `false`.

## Discussion

This method converts the object ID of each managed object in `objects` to a
permanent ID. Although the object will have a permanent ID, it will still
respond positively to `isInserted` until it is saved. Any object that already
has a permanent ID is ignored.

Any object not already assigned to a store is assigned based on the same rules
Core Data uses for assignment during a save operation (first writable store
supporting the entity, and appropriate for the instance and its related
items).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

### Special Considerations

This method results in a transaction with the underlying store which changes
the file’s modification date.

In macOS, this results an additional consideration if you invoke this method
on the managed object context associated with an instance of
`NSPersistentDocument`. Instances of `NSDocument` need to know that they are
in sync with the underlying content. To avoid problems, after invoking this
method you must therefore update the document’s modification date (using
`fileModificationDate`).

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

Instance Method

# detectConflicts(for:)

Marks an object for conflict detection.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func detectConflicts(for object: NSManagedObject)

##  Parameters

`object`

    

A managed object.

## Discussion

If on the next invocation of `save()` `object` has been modified in its
persistent store, the save fails. This allows optimistic locking for unchanged
objects. Conflict detection is always performed on changed or deleted objects.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

Instance Method

# refresh(_:mergeChanges:)

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func refresh(
        _ object: NSManagedObject,
        mergeChanges flag: Bool
    )

##  Parameters

`object`

    

A managed object.

`flag`

    

A Boolean value.

If `flag` is `false`, the context discards pending changes and the managed
object becomes a fault. Upon next access, the context reloads the object’s
values from the persistent store or last cached state.

If `flag` is `true`, the context reloads the object’s property values from the
store or the cache. Then the context applies local changes over the newly
loaded values. Merging the local values into `object` always succeeds, and
never results in a merge conflict.

## Discussion

If you call this method before the `stalenessInterval` expires, the context
reloads the data from the cache instead of fetching from the store. If `flag`
is `true`, this method doesn’t affect any transient properties. If `flag` is
`false`, the object disposes the value of transient properties.

You typically use this method to ensure data freshness if multiple managed
object contexts share a single persistent store. You can use this method to
resolve an optimistic locking failure when attempting to save.

Turning `object` into a fault by setting `flag` to `false` breaks strong
references to related managed objects. You can use this method to release a
portion of your object graph if you want to constrain memory usage.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`var stalenessInterval: TimeInterval`

The maximum length of time that may have elapsed since the store previously
fetched data before fulfilling a fault issues a new fetch.

`func reset()`

Returns the context to its base state.

Instance Method

# processPendingChanges()

Forces the context to process changes to the object graph.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func processPendingChanges()

## Discussion

This method causes changes to registered managed objects to be recorded with
the undo manager.

In AppKit-based applications, this method is invoked automatically at least
once during the event loop (at the end of the loop)—it may be called more
often than that if the framework needs to coalesce your changes before doing
something else. You can also invoke it manually to coalesce any pending
unprocessed changes.

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?,
context: UnsafeMutableRawPointer?)`

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

### Related Documentation

`func undo()`

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

`var undoManager: UndoManager?`

The object that provides undo support for the context.

`func redo()`

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

Instance Method

# observeValue(forKeyPath:of:change:context:)

Allows a context that has registered as an observer of a value to be notified
of a change to that value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func observeValue(
        forKeyPath keyPath: String?,
        of object: Any?,
        change: [String : Any]?,
        context: UnsafeMutableRawPointer?
    )

## See Also

### Handling managed objects

`var shouldDeleteInaccessibleFaults: Bool`

A Boolean value that determines whether the context turns inaccessible faults
into deleted objects.

`var insertedObjects: Set<NSManagedObject>`

The set of objects that have been inserted into the context but not yet saved
in a persistent store.

`var updatedObjects: Set<NSManagedObject>`

The set of objects registered with the context that have uncommitted changes.

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID,
triggeredByProperty: NSPropertyDescription?) -> Bool`

Creates a log of the inaccessible fault.

`func insert(NSManagedObject)`

Registers an object to be inserted in the context’s persistent store the next
time changes are saved.

`func delete(NSManagedObject)`

Specifies an object that should be removed from its persistent store when
changes are committed.

`func assign(Any, to: NSPersistentStore)`

Specifies the store in which a newly inserted object will be saved.

`func obtainPermanentIDs(for: [NSManagedObject])`

Converts to permanent IDs the object IDs of the objects in a given array.

`func detectConflicts(for: NSManagedObject)`

Marks an object for conflict detection.

`func refresh(NSManagedObject, mergeChanges: Bool)`

Updates the persistent properties of a managed object to use the latest values
from the persistent store.

`func processPendingChanges()`

Forces the context to process changes to the object graph.

Global Variable

# NSManagedObjectContextQueryGenerationKey

Constant used to reference the query generation token.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    let NSManagedObjectContextQueryGenerationKey: String

## See Also

### Managing concurrency

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Type Method

# mergeChanges(fromRemoteContextSave:into:)

Handles changes from other processes or from a serialized state.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func mergeChanges(
        fromRemoteContextSave changeNotificationData: [AnyHashable : Any],
        into contexts: [NSManagedObjectContext]
    )

## Discussion

This method more efficiently merges changes into multiple contexts as well as
nested contexts. The dictionary keys should be one or more from an
`NSManagedObjectContextObjectsDidChange`: `NSInsertedObjectsKey`,
`NSUpdatedObjectsKey`, `NSDeletedObjectsKey`. The values should be an
`NSArray` of either `NSManagedObjectID` or `NSURL` objects conforming to valid
results from `uriRepresentation()`.

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Property

# automaticallyMergesChangesFromParent

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var automaticallyMergesChangesFromParent: Bool { get set }

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Property

# concurrencyType

The concurrency type for the context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var concurrencyType: NSManagedObjectContextConcurrencyType { get }

## Discussion

For more details on concurrency type, see Concurrency.

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

### Related Documentation

`init(concurrencyType: NSManagedObjectContextConcurrencyType)`

Creates a context that uses the specified concurrency type.

Instance Property

# mergePolicy

The merge policy of the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var mergePolicy: Any { get set }

## Discussion

The default is `NSErrorMergePolicy`. For possible values, see `NSMergePolicy`.

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Property

# queryGenerationToken

Returns the token associated with the query generation currently in use by
this context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var queryGenerationToken: NSQueryGenerationToken? { get }

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Property

# transactionAuthor

The author for the context that is used as an identifier in persistent history
transactions.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var transactionAuthor: String? { get set }

## Discussion

Set a managed object context’s `transactionAuthor` before saving it to
differentiate among multiple call sites that modify the same context. Doing
this records an `author` in subsequent transactions.

Reset the context’s `transactionAuthor` to nil after the save to prevent
misattribution of future transactions.

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Method

# mergeChanges(fromContextDidSave:)

Merges the changes specified in a given notification.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func mergeChanges(fromContextDidSave notification: Notification)

##  Parameters

`notification`

    

An instance of an `NSManagedObjectContextDidSave` notification posted by
another context.

## Discussion

This method refreshes any objects which have been updated in the other
context, faults in any newly-inserted objects, and invokes `delete(_:)`: on
those which have been deleted.

You can pass a `NSManagedObjectContextDidSave` notification posted by a
managed object context on another thread, however you must not use the managed
objects in the user info dictionary directly. For more details, see
Concurrency with Core Data.

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func setQueryGenerationFrom(NSQueryGenerationToken?)`

Sets the query generation this context should use.

Instance Method

# setQueryGenerationFrom(_:)

Sets the query generation this context should use.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func setQueryGenerationFrom(_ generation: NSQueryGenerationToken?) throws

## See Also

### Managing concurrency

`let NSManagedObjectContextQueryGenerationKey: String`

Constant used to reference the query generation token.

`class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into:
[NSManagedObjectContext])`

Handles changes from other processes or from a serialized state.

`var automaticallyMergesChangesFromParent: Bool`

A Boolean value that indicates whether the context automatically merges
changes saved to its persistent store coordinator or parent context.

`var concurrencyType: NSManagedObjectContextConcurrencyType`

The concurrency type for the context.

`var mergePolicy: Any`

The merge policy of the context.

`var queryGenerationToken: NSQueryGenerationToken?`

Returns the token associated with the query generation currently in use by
this context.

`var transactionAuthor: String?`

The author for the context that is used as an identifier in persistent history
transactions.

`func mergeChanges(fromContextDidSave: Notification)`

Merges the changes specified in a given notification.

Type Property

# didChangeObjectsNotification

A notification that posts when the context completes a save.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    static let didChangeObjectsNotification: Notification.Name

## Discussion

The notification object is the managed object context. The `userInfo`
dictionary contains the following keys: `NSInsertedObjectsKey`,
`NSUpdatedObjectsKey`, and `NSDeletedObjectsKey`.

You can only use the managed objects in this notification on the same thread
that it posts on.

You can pass the notification object to `mergeChanges(fromContextDidSave:)` on
another thread, however, you must not use the managed object in the user info
dictionary directly on another thread.

## See Also

### Managing notifications

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Type Property

# NSManagedObjectContextObjectsDidChange

A notification of changes made to managed objects associated with this
context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSManagedObjectContextObjectsDidChange: NSNotification.Name

## Discussion

The notification is posted during `processPendingChanges()`, after the changes
have been processed, but before it is safe to call `save()` again (if you try,
you will generate an infinite loop).

The notification object is the managed object context. The userInfo dictionary
contains the following keys: `NSInsertedObjectsKey`, `NSUpdatedObjectsKey`,
and `NSDeletedObjectsKey`.

Note that this notification is posted only when managed objects are _changed_
; it is not posted when managed objects are added to a context as the result
of a fetch.

## See Also

### Core Data

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name`

A notification that posts after a coordinator changes its registered stores.

`static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name`

A notification that posts before the coordinator changes its registered
stores.

`static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name`

A notification that posts before a coordinator removes a store.

`static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate:
NSNotification.Name`

`static let NSManagedObjectContextDidMergeChangesObjectIDs:
NSNotification.Name`

`static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name`

`static let NSPersistentStoreRemoteChange: NSNotification.Name`

A notification that posts for all cross-process writes to a persistent store.

`static let NSPersistentStoreDidImportUbiquitousContentChanges:
NSNotification.Name`

Posted after records are imported from the ubiquitous content store.

Deprecated

Type Property

# didSaveObjectsNotification

A notification that posts when the context completes a save.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    static let didSaveObjectsNotification: Notification.Name

## Discussion

The notification object is the managed object context. The `userInfo`
dictionary contains the following keys: `NSInsertedObjectsKey`,
`NSUpdatedObjectsKey`, and `NSDeletedObjectsKey`.

You can only use the managed objects in this notification on the same thread
that it posts on.

You can pass the notification object to `mergeChanges(fromContextDidSave:)` on
another thread, however, you must not use the managed object in the user info
dictionary directly on another thread.

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Type Property

# NSManagedObjectContextDidSave

A notification that the context completed a save.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSManagedObjectContextDidSave: NSNotification.Name

## Discussion

The notification object is the managed object context. The userInfo dictionary
contains the following keys: `NSInsertedObjectsKey`, `NSUpdatedObjectsKey`,
and `NSDeletedObjectsKey`.

You can only use the managed objects in this notification on the same thread
on which it was posted.

You can pass the notification object to `mergeChanges(fromContextDidSave:)` on
another thread, however you must not use the managed object in the user info
dictionary directly on another thread. For more details, see Concurrency with
Core Data.

## See Also

### Core Data

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name`

A notification that posts after a coordinator changes its registered stores.

`static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name`

A notification that posts before the coordinator changes its registered
stores.

`static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name`

A notification that posts before a coordinator removes a store.

`static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate:
NSNotification.Name`

`static let NSManagedObjectContextDidMergeChangesObjectIDs:
NSNotification.Name`

`static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name`

`static let NSPersistentStoreRemoteChange: NSNotification.Name`

A notification that posts for all cross-process writes to a persistent store.

`static let NSPersistentStoreDidImportUbiquitousContentChanges:
NSNotification.Name`

Posted after records are imported from the ubiquitous content store.

Deprecated

Type Property

# willSaveObjectsNotification

A notification that the context is about to save.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    static let willSaveObjectsNotification: Notification.Name

## Discussion

The notification object is the managed object context. There is no `userInfo`
dictionary.

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Type Property

# NSManagedObjectContextWillSave

A notification that the context is about to save.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSManagedObjectContextWillSave: NSNotification.Name

## Discussion

The notification object is the managed object context. There is no userInfo
dictionary.

## See Also

### Core Data

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name`

A notification that posts after a coordinator changes its registered stores.

`static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name`

A notification that posts before the coordinator changes its registered
stores.

`static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name`

A notification that posts before a coordinator removes a store.

`static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate:
NSNotification.Name`

`static let NSManagedObjectContextDidMergeChangesObjectIDs:
NSNotification.Name`

`static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name`

`static let NSPersistentStoreRemoteChange: NSNotification.Name`

A notification that posts for all cross-process writes to a persistent store.

`static let NSPersistentStoreDidImportUbiquitousContentChanges:
NSNotification.Name`

Posted after records are imported from the ubiquitous content store.

Deprecated

Global Variable

# NSInsertedObjectsKey

A key for the set of objects that were inserted into the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSInsertedObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Global Variable

# NSUpdatedObjectsKey

A key for the set of objects that were updated.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSUpdatedObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Global Variable

# NSDeletedObjectsKey

A key for the set of objects that were marked for deletion during the previous
event.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSDeletedObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Global Variable

# NSRefreshedObjectsKey

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSRefreshedObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Global Variable

# NSInvalidatedObjectsKey

A key for the set of objects that were invalidated.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSInvalidatedObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Global Variable

# NSInvalidatedAllObjectsKey

A key that specifies that all objects in the context have been invalidated.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSInvalidatedAllObjectsKey: String

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Type Property

# didMergeChangesObjectIDsNotification

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    static let didMergeChangesObjectIDsNotification: Notification.Name

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didSaveObjectIDsNotification: Notification.Name`

A notification that posts when the context saves changes.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Type Property

# didSaveObjectIDsNotification

A notification that posts when the context saves changes.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    static let didSaveObjectIDsNotification: Notification.Name

## See Also

### Managing notifications

`static let didChangeObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let didSaveObjectsNotification: Notification.Name`

A notification that posts when the context completes a save.

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let willSaveObjectsNotification: Notification.Name`

A notification that the context is about to save.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

`let NSInsertedObjectsKey: String`

A key for the set of objects that were inserted into the context.

`let NSUpdatedObjectsKey: String`

A key for the set of objects that were updated.

`let NSDeletedObjectsKey: String`

A key for the set of objects that were marked for deletion during the previous
event.

`let NSRefreshedObjectsKey: String`

A key for the set of objects that were refreshed but were not dirtied in the
scope of this context.

`let NSInvalidatedObjectsKey: String`

A key for the set of objects that were invalidated.

`let NSInvalidatedAllObjectsKey: String`

A key that specifies that all objects in the context have been invalidated.

`static let didMergeChangesObjectIDsNotification: Notification.Name`

A notification that a posts when changes to managed objects with the specified
object identifiers merge into the context.

`enum NSManagedObjectContext.NotificationKey`

Keys to access details in user info dictionaries of managed object context
notifications.

Instance Method

# save()

Attempts to commit unsaved changes to registered objects to the context’s
parent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func save() throws

##  Parameters

`error`

    

A pointer to an `NSError` object. You do not need to create an `NSError`
object. The save operation aborts after the first failure if you pass `NULL`.

## Return Value

`true` if the save succeeds, otherwise `false`.

## Discussion

If there were multiple errors (for example several edited objects had
validation failures) the description of `NSError` returned indicates that
there were multiple errors, and its userInfo dictionary contains the key
`NSDetailedErrors`. The value associated with the `NSDetailedErrors` key is an
array that contains the individual `NSError` objects.

If a context’s parent store is a persistent store coordinator, then changes
are committed to the external store. If a context’s parent store is another
managed object context, then `save()` only updates managed objects in that
parent store. To commit changes to the external store, you must save changes
in the chain of contexts up to and including the context whose parent is the
persistent store coordinator.

Important

Always verify that the context has uncommitted changes (using the `hasChanges`
property) before invoking the `save:` method. Otherwise, Core Data may perform
unnecessary work.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing unsaved and uncommitted changes

`var hasChanges: Bool`

A Boolean value that indicates whether the context has uncommitted changes.

Instance Property

# hasChanges

A Boolean value that indicates whether the context has uncommitted changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var hasChanges: Bool { get }

## Discussion

If you are observing this property using key-value observing (KVO) you should
not touch the context or its objects within your implementation of
`observeValue(forKeyPath:of:change:context:)` for this notification. (This is
because of the intricacy of the locations of the KVO notifications—for
example, the context may be in the middle of an undo operation, or repairing a
merge conflict.) If you need to send messages to the context or change any of
its managed objects as a result of a change to the value of `hasChanges`, you
must do so after the call stack unwinds (typically using
`perform(_:with:afterDelay:)` or a similar method).

### Special Considerations

In macOS 10.6 and later, this property is Key-value observing compliant.

## See Also

### Managing unsaved and uncommitted changes

`func save()`

Attempts to commit unsaved changes to registered objects to the context’s
parent store.

Instance Property

# undoManager

The object that provides undo support for the context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var undoManager: UndoManager? { get set }

## Discussion

Enable undo support for a context by setting this property to an instance of
`UndoManager`. This can be an undo manager that’s exclusive to the context, or
an existing undo manager if you want to integrate the context’s undo
operations with those of the rest of your app.

If your context uses an undo manager, you can realize a performance benefit by
temporarily setting this property to `nil` when performing expensive
operations on that context, such as importing a large number of objects.

The default value is `nil`.

## See Also

### Undoing changes

`func undo()`

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

`func redo()`

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

`func reset()`

Returns the context to its base state.

`func rollback()`

Removes everything from the undo stack, discards all insertions and deletions,
and restores updated objects to their last committed values.

Instance Method

# undo()

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func undo()

## See Also

### Undoing changes

`var undoManager: UndoManager?`

The object that provides undo support for the context.

`func redo()`

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

`func reset()`

Returns the context to its base state.

`func rollback()`

Removes everything from the undo stack, discards all insertions and deletions,
and restores updated objects to their last committed values.

### Related Documentation

`func processPendingChanges()`

Forces the context to process changes to the object graph.

Instance Method

# redo()

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func redo()

## See Also

### Undoing changes

`var undoManager: UndoManager?`

The object that provides undo support for the context.

`func undo()`

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

`func reset()`

Returns the context to its base state.

`func rollback()`

Removes everything from the undo stack, discards all insertions and deletions,
and restores updated objects to their last committed values.

### Related Documentation

`func processPendingChanges()`

Forces the context to process changes to the object graph.

Instance Method

# reset()

Returns the context to its base state.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func reset()

## Discussion

All the receiver's managed objects are “forgotten.” If you use this method,
you should ensure that you also discard references to any managed objects
fetched using the receiver, since they will be invalid afterwards.

## See Also

### Undoing changes

`var undoManager: UndoManager?`

The object that provides undo support for the context.

`func undo()`

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

`func redo()`

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

`func rollback()`

Removes everything from the undo stack, discards all insertions and deletions,
and restores updated objects to their last committed values.

### Related Documentation

`var stalenessInterval: TimeInterval`

The maximum length of time that may have elapsed since the store previously
fetched data before fulfilling a fault issues a new fetch.

Instance Method

# rollback()

Removes everything from the undo stack, discards all insertions and deletions,
and restores updated objects to their last committed values.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func rollback()

## Discussion

This method does not refetch data from the persistent store or stores.

## See Also

### Undoing changes

`var undoManager: UndoManager?`

The object that provides undo support for the context.

`func undo()`

Sends an undo message to the context’s undo manager, asking it to reverse the
latest uncommitted changes applied to objects in the object graph.

`func redo()`

Sends a redo message to the context’s undo manager, asking it to reverse the
latest undo operation applied to objects in the object graph.

`func reset()`

Returns the context to its base state.

### Related Documentation

`func processPendingChanges()`

Forces the context to process changes to the object graph.

`var stalenessInterval: TimeInterval`

The maximum length of time that may have elapsed since the store previously
fetched data before fulfilling a fault issues a new fetch.

Instance Property

# propagatesDeletesAtEndOfEvent

A Boolean value that indicates whether the context propagates deletes at the
end of the event in which a change was made.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propagatesDeletesAtEndOfEvent: Bool { get set }

## Discussion

`true` if the receiver propagates deletes at the end of the event in which a
change was made, `false` if it propagates deletes only during a save
operation. The default is `true`.

Instance Property

# stalenessInterval

The maximum length of time that may have elapsed since the store previously
fetched data before fulfilling a fault issues a new fetch.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var stalenessInterval: TimeInterval { get set }

## Discussion

The staleness interval controls whether _fulfilling a fault_ uses data
previously fetched by the application, or issues a new fetch (see also
`refresh(_:mergeChanges:)`). The staleness interval does _not_ affect objects
currently in use (that is, it is _not_ used to automatically update property
values from a persistent store after a certain period of time).

The expiration value is applied on a per object basis. It is the relative time
until cached data (snapshots) should be considered stale. For example, a value
of 300.0 informs the context to utilize cached information for no more than 5
minutes after an object was originally fetched.

Note that the staleness interval is a hint and may not be supported by all
persistent store types. It is not used by XML and binary stores, because these
stores maintain all current values in memory.

The default is a negative value, which represents infinite staleness allowed.
`0.0` represents “no staleness acceptable”.

Instance Method

# perform(_:)

Asynchronously performs the specified closure on the context’s queue.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func perform(_ block: @escaping () -> Void)

##  Parameters

`block`

    

The closure to perform.

## Discussion

This method encapsulates an autorelease pool and a call to
`processPendingChanges()`.

## See Also

### Performing block operations

`func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () -> T)
-> T`

Submits a closure to the context’s queue for asynchronous execution.

`func performAndWait(() -> Void)`

Synchronously performs the specified closure on the context’s queue.

`func performAndWait<T>(() -> T) -> T`

Submits a closure to the context’s queue for synchronous execution.

`enum NSManagedObjectContext.ScheduledTaskType`

The different types of scheduled tasks.

Generic Instance Method

# perform(schedule:_:)

Submits a closure to the context’s queue for asynchronous execution.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func perform<T>(
        schedule: NSManagedObjectContext.ScheduledTaskType = .immediate,
        _ block: @escaping () throws -> T
    ) async rethrows -> T

##  Parameters

`schedule`

    

The required execution schedule. For more information, see
`NSManagedObjectContext.ScheduledTaskType`.

`block`

    

The closure to perform.

## See Also

### Performing block operations

`func perform(() -> Void)`

Asynchronously performs the specified closure on the context’s queue.

`func performAndWait(() -> Void)`

Synchronously performs the specified closure on the context’s queue.

`func performAndWait<T>(() -> T) -> T`

Submits a closure to the context’s queue for synchronous execution.

`enum NSManagedObjectContext.ScheduledTaskType`

The different types of scheduled tasks.

Instance Method

# performAndWait(_:)

Synchronously performs the specified closure on the context’s queue.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func performAndWait(_ block: () -> Void)

##  Parameters

`block`

    

The closure to perform.

## Discussion

This method supports _reentrancy_ — meaning it’s safe to call the method
again, from within the closure, before the previous invocation completes.

## See Also

### Performing block operations

`func perform(() -> Void)`

Asynchronously performs the specified closure on the context’s queue.

`func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () -> T)
-> T`

Submits a closure to the context’s queue for asynchronous execution.

`func performAndWait<T>(() -> T) -> T`

Submits a closure to the context’s queue for synchronous execution.

`enum NSManagedObjectContext.ScheduledTaskType`

The different types of scheduled tasks.

Generic Instance Method

# performAndWait(_:)

Submits a closure to the context’s queue for synchronous execution.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func performAndWait<T>(_ block: () throws -> T) rethrows -> T

##  Parameters

`block`

    

The closure to perform.

## Discussion

This method supports _reentrancy_ — meaning it’s safe to call the method
again, from within the closure, before the previous invocation completes.

## See Also

### Performing block operations

`func perform(() -> Void)`

Asynchronously performs the specified closure on the context’s queue.

`func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () -> T)
-> T`

Submits a closure to the context’s queue for asynchronous execution.

`func performAndWait(() -> Void)`

Synchronously performs the specified closure on the context’s queue.

`enum NSManagedObjectContext.ScheduledTaskType`

The different types of scheduled tasks.

