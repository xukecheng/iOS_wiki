Initializer

# init(persistentStoreCoordinator:configurationName:at:options:)

Creates an atomic store at the specified location.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?,
        configurationName: String?,
        at url: URL,
        options: [AnyHashable : Any]? = nil
    )

##  Parameters

`coordinator`

    

The persistent store coordinator.

`configurationName`

    

The name of the store’s configuration in the managed object model.

`url`

    

The URL of the store to load. This value can’t be `nil`.

`options`

    

A dictionary that contains the store’s options. For possible values, see Store
options.

## Discussion

Typically, you don’t invoke this method yourself; instead, the persistent
store coordinator invokes the method when it creates a new store or adds an
existing one.

In your implementation, check whether a file exists at `url`. If it doesn’t
exist, create a zero-length file at `url` so that the file exists before the
coordinator calls the store’s `load()` method. A zero-length file indicates to
the system that it should create a new store at that location. If the
coordinator removes the store without first calling `save()`, delete the zero-
length file.

It’s your responsibility to load the store’s metadata during initialization
and set it using the `setMetadata(_:forPersistentStoreAt:)` method.

Important

If you override this method, you must invoke the superclass implementation to
ensure that Core Data correctly initializes the store.

Instance Method

# load()

Loads the cache nodes for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func load() throws

##  Parameters

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the cache nodes were loaded correctly, otherwise `false`.

## Discussion

You override this method to load the data from the URL specified in
`init(persistentStoreCoordinator:configurationName:at:options:)` and create
cache nodes for the represented objects. You must respect the configuration
specified for the store, as well as the options.

Any subclass of `NSAtomicStore` must be able to handle being initialized with
a URL pointing to a zero-length file. This serves as an indicator that a new
store is to be constructed at the specified location and allows you to
securely create reservation files in known locations which can then be passed
to Core Data to construct stores. You may choose to create zero-length
reservation files during
`init(persistentStoreCoordinator:configurationName:at:options:)` or `load()`.
If you do so, you must remove the reservation file if the store is removed
from the coordinator before it is saved.

You must override this method in a subclass of `NSAtomicStore`.

## See Also

### Loading a Store

`func objectID(for: NSEntityDescription, withReferenceObject: Any) ->
NSManagedObjectID`

Returns a managed object ID from the reference data for a specified entity.

`func addCacheNodes(Set<NSAtomicStoreCacheNode>)`

Registers a set of cache nodes with the receiver.

Instance Method

# objectID(for:withReferenceObject:)

Returns a managed object ID from the reference data for a specified entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func objectID(
        for entity: NSEntityDescription,
        withReferenceObject data: Any
    ) -> NSManagedObjectID

##  Parameters

`entity`

    

An entity description object.

`data`

    

Reference data for which the managed object ID is required.

## Return Value

The managed object ID from the reference data for a specified entity

## Discussion

You use this method to create managed object IDs which are then used to create
cache nodes for information being loaded into the store.

### Special Considerations

You should not override this method.

## See Also

### Loading a Store

`func load()`

Loads the cache nodes for the receiver.

`func addCacheNodes(Set<NSAtomicStoreCacheNode>)`

Registers a set of cache nodes with the receiver.

Instance Method

# addCacheNodes(_:)

Registers a set of cache nodes with the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)

##  Parameters

`cacheNodes`

    

A set of cache nodes.

## Discussion

You should invoke this method in a subclass during the call to `load()` to
register the loaded information with the store.

## See Also

### Loading a Store

`func load()`

Loads the cache nodes for the receiver.

`func objectID(for: NSEntityDescription, withReferenceObject: Any) ->
NSManagedObjectID`

Returns a managed object ID from the reference data for a specified entity.

Instance Method

# newCacheNode(for:)

Returns a new cache node for a given managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func newCacheNode(for managedObject: NSManagedObject) -> NSAtomicStoreCacheNode

##  Parameters

`managedObject`

    

A managed object.

## Return Value

A new cache node for `managedObject`.

## Discussion

This method is invoked by the framework during a save operation, once for each
newly-inserted managed object. It should pull information from the managed
object and return a cache node containing the information (the node will be
registered by the framework).

### Special Considerations

You must override this method.

## See Also

### Updating Cache Nodes

`func newReferenceObject(for: NSManagedObject) -> Any`

Returns a new reference object for a given managed object.

`func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)`

Updates the given cache node using the values in a given managed object.

`func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)`

Method invoked before the store removes the given collection of cache nodes.

Instance Method

# newReferenceObject(for:)

Returns a new reference object for a given managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func newReferenceObject(for managedObject: NSManagedObject) -> Any

##  Parameters

`managedObject`

    

A managed object. At the time this method is called, it has a temporary ID.

## Return Value

A new reference object for `managedObject`.

## Discussion

This method is invoked by the framework after a save operation on a managed
object context, once for each newly-inserted managed object. The value
returned is used to create a permanent ID for the object and must be unique
for an instance within its entity's inheritance hierarchy (in this store).

### Special Considerations

You must override this method.

This method must return a stable (unchanging) value for a given object,
otherwise Save As and migration will not work correctly. This means that you
can use arbitrary numbers, UUIDs, or other random values only if they are
persisted with the raw data. If you cannot save the originally-assigned
reference object with the data, then the method must derive the reference
object from the managed object’s values. For more details, see Atomic Store
Programming Topics.

## See Also

### Updating Cache Nodes

`func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode`

Returns a new cache node for a given managed object.

`func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)`

Updates the given cache node using the values in a given managed object.

`func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)`

Method invoked before the store removes the given collection of cache nodes.

Instance Method

# updateCacheNode(_:from:)

Updates the given cache node using the values in a given managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func updateCacheNode(
        _ node: NSAtomicStoreCacheNode,
        from managedObject: NSManagedObject
    )

##  Parameters

`node`

    

The cache node to update.

`managedObject`

    

The managed object with which to update `node`.

## Discussion

This method is invoked by the framework after a save operation on a managed
object context, once for each updated `NSManagedObject` instance.

You override this method in a subclass to take the information from
`managedObject` and update `node`.

### Special Considerations

You must override this method.

## See Also

### Updating Cache Nodes

`func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode`

Returns a new cache node for a given managed object.

`func newReferenceObject(for: NSManagedObject) -> Any`

Returns a new reference object for a given managed object.

`func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)`

Method invoked before the store removes the given collection of cache nodes.

Instance Method

# willRemoveCacheNodes(_:)

Method invoked before the store removes the given collection of cache nodes.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)

##  Parameters

`cacheNodes`

    

The set of cache nodes to remove.

## Discussion

This method is invoked by the store before the call to `save()` with the
collection of cache nodes marked as deleted by a managed object context. You
can override this method to track the nodes which will not be made persistent
in the `save()` method.

You should not invoke this method directly in a subclass.

## See Also

### Updating Cache Nodes

`func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode`

Returns a new cache node for a given managed object.

`func newReferenceObject(for: NSManagedObject) -> Any`

Returns a new reference object for a given managed object.

`func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)`

Updates the given cache node using the values in a given managed object.

### Related Documentation

`func save()`

Saves the cache nodes.

Instance Method

# save()

Saves the cache nodes.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func save() throws

##  Parameters

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Discussion

You override this method to make persistent the necessary information from the
cache nodes to the URL specified for the receiver.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

### Special Considerations

You must override this method.

## See Also

### Related Documentation

`func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)`

Updates the given cache node using the values in a given managed object.

`func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)`

Method invoked before the store removes the given collection of cache nodes.

`func newReferenceObject(for: NSManagedObject) -> Any`

Returns a new reference object for a given managed object.

Instance Method

# cacheNodes()

Returns the set of cache nodes registered with the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func cacheNodes() -> Set<NSAtomicStoreCacheNode>

## Return Value

The set of cache nodes registered with the receiver.

## Discussion

You should modify this collection using `addCacheNodes(_:)`: and
`willRemoveCacheNodes(_:)`.

## See Also

### Utility Methods

`func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?`

Returns the cache node for a given managed object ID.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference object for a given managed object ID.

Instance Method

# cacheNode(for:)

Returns the cache node for a given managed object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?

##  Parameters

`objectID`

    

A managed object ID.

## Return Value

The cache node for `objectID`.

## Discussion

This method is normally used by cache nodes to locate related cache nodes (by
relationships).

## See Also

### Utility Methods

`func cacheNodes() -> Set<NSAtomicStoreCacheNode>`

Returns the set of cache nodes registered with the receiver.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference object for a given managed object ID.

Instance Method

# referenceObject(for:)

Returns the reference object for a given managed object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func referenceObject(for objectID: NSManagedObjectID) -> Any

##  Parameters

`objectID`

    

A managed object ID.

## Return Value

The reference object for `objectID`.

## Discussion

Subclasses should invoke this method to extract the reference data from the
object ID for each cache node if the data is to be made persistent.

## See Also

### Utility Methods

`func cacheNodes() -> Set<NSAtomicStoreCacheNode>`

Returns the set of cache nodes registered with the receiver.

`func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?`

Returns the cache node for a given managed object ID.

