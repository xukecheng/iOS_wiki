Instance Method

# execute(_:with:)

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func execute(
        _ request: NSPersistentStoreRequest,
        with context: NSManagedObjectContext?
    ) throws -> Any

##  Parameters

`request`

    

A fetch request.

`context`

    

The managed object context used to execute `request`.

`error`

    

If an error occurs, on return contains an `NSError` object that describes the
problem.

## Return Value

A value as appropriate for `request`, or `nil` if the request cannot be
completed

## Discussion

The value to return depends on the result type (see `resultType`) of
`request`:

  * If it is `NSManagedObjectResultType`, `NSManagedObjectIDResultType`, or `NSDictionaryResultType`, the method should return an array containing all objects in the store matching the request.

  * If it is `NSCountResultType`, the method should return an array containing an `NSNumber` whose value is the count of all objects in the store matching the request.

  * If the request is a save request, the method should return an empty array.

If the save request contains nil values for the
inserted/updated/deleted/locked collections; you should treat it as a request
to save the store metadata.

You should implement this method conservatively, and expect that unknown
request types may at some point be passed to the method. The correct behavior
in these cases is to return `nil` and an error.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Manipulating Managed Objects

`func newValuesForObject(with: NSManagedObjectID, with:
NSManagedObjectContext) -> NSIncrementalStoreNode`

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

`func newValue(forRelationship: NSRelationshipDescription, forObjectWith:
NSManagedObjectID, with: NSManagedObjectContext?) -> Any`

Returns the relationship for the given relationship of the object with a given
object ID.

`func obtainPermanentIDs(for: [NSManagedObject]) -> [NSManagedObjectID]`

Returns an array containing the object IDs for a given array of newly-inserted
objects.

`func newObjectID(for: NSEntityDescription, referenceObject: Any) ->
NSManagedObjectID`

Returns a new object ID that uses given data as the key.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference data used to construct a given object ID.

Instance Method

# newValuesForObject(with:with:)

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func newValuesForObject(
        with objectID: NSManagedObjectID,
        with context: NSManagedObjectContext
    ) throws -> NSIncrementalStoreNode

##  Parameters

`objectID`

    

The ID of the object for which values are requested.

`context`

    

The managed object context into which values will be returned.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

An incremental store node encapsulating the persistent external values of the
object with object ID `objectID`, or `nil` if the corresponding object cannot
be found.

## Discussion

The returned node should include all attributes values and may include to-one
relationship values as instances of `NSManagedObjectID`.

If an object with object ID `objectID` cannot be found, the method should
return `nil` and—if `error` is not `NULL`—create and return an appropriate
error object in `error`.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Manipulating Managed Objects

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) -> Any`

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

`func newValue(forRelationship: NSRelationshipDescription, forObjectWith:
NSManagedObjectID, with: NSManagedObjectContext?) -> Any`

Returns the relationship for the given relationship of the object with a given
object ID.

`func obtainPermanentIDs(for: [NSManagedObject]) -> [NSManagedObjectID]`

Returns an array containing the object IDs for a given array of newly-inserted
objects.

`func newObjectID(for: NSEntityDescription, referenceObject: Any) ->
NSManagedObjectID`

Returns a new object ID that uses given data as the key.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference data used to construct a given object ID.

Instance Method

# newValue(forRelationship:forObjectWith:with:)

Returns the relationship for the given relationship of the object with a given
object ID.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func newValue(
        forRelationship relationship: NSRelationshipDescription,
        forObjectWith objectID: NSManagedObjectID,
        with context: NSManagedObjectContext?
    ) throws -> Any

##  Parameters

`relationship`

    

The relationship for which values are requested.

`objectID`

    

The ID of the object for which values are requested.

`context`

    

The managed object context into which values will be returned.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

The value of the relationship specified `relationship` of the object with
object ID `objectID`, or `nil` if an error occurs.

## Discussion

If the relationship is a to-one, the method should return an
`NSManagedObjectID` instance that identifies the destination, or an instance
of `NSNull` if the relationship value is `nil`.

If the relationship is a to-many, the method should return a collection object
containing `NSManagedObjectID` instances to identify the related objects.
Using an `NSArray` instance is preferred because it will be the most
efficient. A store may also return an instance of `NSSet` or `NSOrderedSet`;
an instance of `NSDictionary` is not acceptable.

If an object with object ID `objectID` cannot be found, the method should
return `nil` and—if `error` is not `NULL`—create and return an appropriate
error object in `error`.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Manipulating Managed Objects

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) -> Any`

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

`func newValuesForObject(with: NSManagedObjectID, with:
NSManagedObjectContext) -> NSIncrementalStoreNode`

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

`func obtainPermanentIDs(for: [NSManagedObject]) -> [NSManagedObjectID]`

Returns an array containing the object IDs for a given array of newly-inserted
objects.

`func newObjectID(for: NSEntityDescription, referenceObject: Any) ->
NSManagedObjectID`

Returns a new object ID that uses given data as the key.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference data used to construct a given object ID.

Instance Method

# obtainPermanentIDs(for:)

Returns an array containing the object IDs for a given array of newly-inserted
objects.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID]

##  Parameters

`array`

    

An array of newly-inserted objects.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

An array containing the object IDs for the objects in `array`.

The returned array must return the object IDs in the same order as the objects
appear in `array`.

## Discussion

This method is called before `execute(_:with:)` with a save request, to assign
permanent IDs to newly-inserted objects.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Manipulating Managed Objects

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) -> Any`

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

`func newValuesForObject(with: NSManagedObjectID, with:
NSManagedObjectContext) -> NSIncrementalStoreNode`

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

`func newValue(forRelationship: NSRelationshipDescription, forObjectWith:
NSManagedObjectID, with: NSManagedObjectContext?) -> Any`

Returns the relationship for the given relationship of the object with a given
object ID.

`func newObjectID(for: NSEntityDescription, referenceObject: Any) ->
NSManagedObjectID`

Returns a new object ID that uses given data as the key.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference data used to construct a given object ID.

Instance Method

# newObjectID(for:referenceObject:)

Returns a new object ID that uses given data as the key.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func newObjectID(
        for entity: NSEntityDescription,
        referenceObject data: Any
    ) -> NSManagedObjectID

##  Parameters

`entity`

    

The entity for the new object ID.

`data`

    

An object of type `NSString` or `NSNumber` to use as the key.

## Return Value

A new object ID for an instance of the entity specified by `entity` and that
uses `data` as the key.

## Discussion

You should not override this method.

## See Also

### Manipulating Managed Objects

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) -> Any`

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

`func newValuesForObject(with: NSManagedObjectID, with:
NSManagedObjectContext) -> NSIncrementalStoreNode`

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

`func newValue(forRelationship: NSRelationshipDescription, forObjectWith:
NSManagedObjectID, with: NSManagedObjectContext?) -> Any`

Returns the relationship for the given relationship of the object with a given
object ID.

`func obtainPermanentIDs(for: [NSManagedObject]) -> [NSManagedObjectID]`

Returns an array containing the object IDs for a given array of newly-inserted
objects.

`func referenceObject(for: NSManagedObjectID) -> Any`

Returns the reference data used to construct a given object ID.

Instance Method

# referenceObject(for:)

Returns the reference data used to construct a given object ID.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func referenceObject(for objectID: NSManagedObjectID) -> Any

##  Parameters

`objectID`

    

An object ID created by the receiver.

## Return Value

The reference data used to construct objectID.

## Discussion

This method raises an `invalidArgumentException` if the object ID was not
created by the receiving store.

You should not override this method.

## See Also

### Manipulating Managed Objects

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) -> Any`

Returns a value as appropriate for the given request, or nil if the request
cannot be completed.

`func newValuesForObject(with: NSManagedObjectID, with:
NSManagedObjectContext) -> NSIncrementalStoreNode`

Returns an incremental store node encapsulating the persistent external values
of the object with a given object ID.

`func newValue(forRelationship: NSRelationshipDescription, forObjectWith:
NSManagedObjectID, with: NSManagedObjectContext?) -> Any`

Returns the relationship for the given relationship of the object with a given
object ID.

`func obtainPermanentIDs(for: [NSManagedObject]) -> [NSManagedObjectID]`

Returns an array containing the object IDs for a given array of newly-inserted
objects.

`func newObjectID(for: NSEntityDescription, referenceObject: Any) ->
NSManagedObjectID`

Returns a new object ID that uses given data as the key.

Instance Method

# managedObjectContextDidRegisterObjects(with:)

Indicates that objects identified by a given array of object IDs are in use in
a managed object context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID])

##  Parameters

`objectIDs`

    

An array of object IDs.

## Discussion

This method and `managedObjectContextDidUnregisterObjects(with:)` allow
managed object contexts to communicate interest in the row data of specific
objects in a manner akin to reference counting. For more details, see
`managedObjectContextDidUnregisterObjects(with:)`.

## See Also

### Responding to Context Changes

`func managedObjectContextDidUnregisterObjects(with: [NSManagedObjectID])`

Indicates that objects identified by a given array of object IDs are no longer
being used by a managed object context.

Instance Method

# managedObjectContextDidUnregisterObjects(with:)

Indicates that objects identified by a given array of object IDs are no longer
being used by a managed object context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func managedObjectContextDidUnregisterObjects(with objectIDs: [NSManagedObjectID])

##  Parameters

`objectIDs`

    

An array of object IDs.

## Discussion

This method is the counterpart to
`managedObjectContextDidRegisterObjects(with:)`.

Passing an object ID in the object IDs array of
`managedObjectContextDidRegisterObjects(with:)` is akin to incrementing the
object ID’s reference count by 1; passing an object ID in the object IDs array
of `managedObjectContextDidUnregisterObjects(with:)` is akin to decrementing
the object ID’s reference count by 1. It is only when an object ID’s reference
count is 0 that no contexts indicate that they are using the corresponding
managed object. (Object IDs start with a reference count of 0.)

For example, if the register methods is invoked on two occasions when the
object IDs array contains a given object ID, and the unregister method is
invoked once when the object IDs array contains that object ID, then a context
is still using the object with the given ID.

## See Also

### Responding to Context Changes

`func managedObjectContextDidRegisterObjects(with: [NSManagedObjectID])`

Indicates that objects identified by a given array of object IDs are in use in
a managed object context.

Type Method

# identifierForNewStore(at:)

Returns the identifier for the store at a given URL.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func identifierForNewStore(at storeURL: URL) -> Any

##  Parameters

`storeURL`

    

The URL of a persistent store.

## Return Value

The identifier for the store at `storeURL`.

## See Also

### Accessing Metadata

`func loadMetadata()`

Loads the metadata for the store.

Instance Method

# loadMetadata()

Loads the metadata for the store.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func loadMetadata() throws

##  Parameters

`error`

    

If an error occurs, on return contains an `NSError` object that describes the
problem.

## Return Value

`true` if the metadata was correctly loaded, otherwise `false`.

## Discussion

In your implementation of this method, you must validate that the URL used to
create the store is usable (the location exists and if necessary is writable,
the schema is compatible, and so on) and return an error if there is an issue.

Any subclass of `NSIncrementalStore` which is file-based must be able to
handle being initialized with a URL pointing to a zero-length file. This
serves as an indicator that a new store is to be constructed at the specified
location and allows applications using the store to securely create
reservation files in known locations.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Accessing Metadata

`class func identifierForNewStore(at: URL) -> Any`

Returns the identifier for the store at a given URL.

### Related Documentation

Incremental Store Programming Guide

