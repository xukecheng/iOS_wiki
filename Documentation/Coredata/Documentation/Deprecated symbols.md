Global Variable

# NSXMLExternalRecordType

Specifies an XML file format.

macOS 10.6–10.13  Deprecated

    
    
    let NSXMLExternalRecordType: String

## See Also

### Deprecated constants

`let NSBinaryExternalRecordType: String`

Specifies a binary file format

Deprecated

Global Variable

# NSBinaryExternalRecordType

Specifies a binary file format

macOS 10.6–10.13  Deprecated

    
    
    let NSBinaryExternalRecordType: String

## See Also

### Deprecated constants

`let NSXMLExternalRecordType: String`

Specifies an XML file format.

Deprecated

Type Property

# NSPersistentStoreDidImportUbiquitousContentChanges

Posted after records are imported from the ubiquitous content store.

iOS 5.0–10.0  Deprecated  iPadOS 5.0–10.0  Deprecated  macOS 10.7–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name

## Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator`
instance which registered the store. The notification’s `userInfo` dictionary
contains the same keys as the `NSManagedObjectContextObjectsDidChange`
notification (`NSInsertedObjectsKey`,
`NSUpdatedObjectsKey``NSDeletedObjectsKey`), however the values are sets of
`NSManagedObjectID` objects rather than sets of `NSManagedObject` objects.

## See Also

### Core Data

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

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

Type Method

# elementsDerived(fromExternalRecordAt:)

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

macOS 10.6–10.13  Deprecated

    
    
    class func elementsDerived(fromExternalRecordAt fileURL: URL) -> [AnyHashable : Any]

##  Parameters

`fileURL`

    

A file URL specifying the location of a Spotlight external record file.

## Return Value

A dictionary containing the parsed elements derived from the Spotlight support
file specified by `fileURL`.

## Discussion

Dictionary keys and the corresponding values are described in Spotlight record
keys.

## See Also

### Deprecated type methods

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

Type Method

# metadataForPersistentStore(with:)

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

macOS 10.4–10.5  Deprecated  Mac Catalyst 13.1–13.1  Deprecated

    
    
    class func metadataForPersistentStore(with url: URL) throws -> [AnyHashable : Any]

Deprecated

Use `metadataForPersistentStore(ofType:at:)` instead.

##  Parameters

`url`

    

An URL object that specifies the location of a persistent store.

`error`

    

If no store is found at `url` or if there is a problem accessing its contents,
upon return contains an instance of `NSError` that describes the problem.

## Return Value

A dictionary containing the metadata for the persistent store at `url`. If no
store is found, or there is a problem accessing its contents, returns `nil`.

The keys guaranteed to be in this dictionary are `NSStoreTypeKey` and
`NSStoreUUIDKey`.

## Discussion

This method allows you to access the metadata in a persistent store without
initializing a Core Data stack.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

### Related Documentation

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

Type Method

# metadataForPersistentStore(ofType:at:)

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

iOS 3.0–9.0  Deprecated  iPadOS 3.0–9.0  Deprecated  macOS 10.5–10.11
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–9.0  Deprecated
watchOS 2.0–2.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    class func metadataForPersistentStore(
        ofType storeType: String?,
        at url: URL
    ) throws -> [String : Any]

##  Parameters

`storeType`

    

The type of the store at `url`. If this value is `nil`, Core Data determines
which store class should be used to get or set the store file's metadata by
inspecting the file contents.

`url`

    

The location of a persistent store.

`error`

    

If no store is found at `url` or if there is a problem accessing its contents,
upon return contains an `NSError` object that describes the problem.

## Return Value

A dictionary containing the metadata stored in the persistent store at `url`,
or `nil` if the store cannot be opened or if there is a problem accessing its
contents.

The keys guaranteed to be in this dictionary are `NSStoreTypeKey` and
`NSStoreUUIDKey`.

## Discussion

You can use this method to retrieve the metadata from a store without the
overhead of creating a Core Data stack.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

### Related Documentation

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

Type Method

# metadataForPersistentStore(ofType:at:options:)

Returns the metadata of a specific type of persistent store at the provided
location.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func metadataForPersistentStore(
        ofType storeType: String,
        at url: URL,
        options: [AnyHashable : Any]? = nil
    ) throws -> [String : Any]

Deprecated

Use `metadataForPersistentStore(type:at:options:)` instead.

##  Parameters

`storeType`

    

The type of the store. If `nil`, Core Data automatically attempts to determine
the store class to use.

`url`

    

The file URL of the store.

`options`

    

A dictionary that contains options for the store.

## Return Value

A dictionary that contains, at a minimum, values for the `NSStoreTypeKey` and
`NSStoreUUIDKey` keys.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

Type Method

# registerStoreClass(_:forStoreType:)

Registers a persistent store subclass using the specified store type
identifier.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func registerStoreClass(
        _ storeClass: AnyClass?,
        forStoreType storeType: String
    )

Deprecated

Use `registerStoreClass(_:type:)` instead.

##  Parameters

`storeClass`

    

The `NSPersistentStore` subclass to use for the store of type `storeType`.

`storeType`

    

A unique string that identifies a store type.

## Discussion

You must invoke this method before a custom subclass of `NSPersistentStore`
can be loaded into a persistent store coordinator.

You can pass `nil` for `storeClass` to unregister the store type.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

Type Method

# removeUbiquitousContentAndPersistentStore(at:options:)

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

iOS 5.0–10.0  Deprecated  iPadOS 5.0–10.0  Deprecated  macOS 10.7–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    class func removeUbiquitousContentAndPersistentStore(
        at storeURL: URL,
        options: [AnyHashable : Any]? = nil
    ) throws

##  Parameters

`storeURL`

    

The URL of the store to delete.

`options`

    

A dictionary containing the options normally passed to
`addPersistentStore(ofType:configurationName:at:options:)`.

`error`

    

If the operation fails, upon return contains an `NSError` object that
describes the problem.

## Return Value

`true` if the store was deleted, otherwise `false`.

## Discussion

Errors may be returned as a result of file I/O, iCloud network or iCloud
account issues.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

Type Method

# setMetadata(_:forPersistentStoreOfType:at:)

Sets the metadata for a given store.

iOS 3.0–9.0  Deprecated  iPadOS 3.0–9.0  Deprecated  macOS 10.5–10.11
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–9.0  Deprecated
watchOS 2.0–2.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    class func setMetadata(
        _ metadata: [String : Any]?,
        forPersistentStoreOfType storeType: String?,
        at url: URL
    ) throws

##  Parameters

`metadata`

    

A dictionary containing metadata for the store.

`storeType`

    

The type of the store at `url`. If this value is `nil`, Core Data will
determine which store class should be used to get or set the store file's
metadata by inspecting the file contents.

`url`

    

The location of a persistent store.

`error`

    

If no store is found at `url` or if there is a problem setting its metadata,
upon return contains an `NSError` object that describes the problem.

## Return Value

`true` if the metadata was set correctly, otherwise `false`.

## Discussion

You can use this method to set the metadata for a store without the overhead
of creating a Core Data stack.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at:
URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

### Related Documentation

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

Type Method

# setMetadata(_:forPersistentStoreOfType:at:options:)

Updates the metadata of a specific type of persistent store at the provided
location.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func setMetadata(
        _ metadata: [String : Any]?,
        forPersistentStoreOfType storeType: String,
        at url: URL,
        options: [AnyHashable : Any]? = nil
    ) throws

Deprecated

Use `setMetadata(_:type:at:options:)` instead.

##  Parameters

`metadata`

    

A dictionary that contains the metadata to store.

`storeType`

    

The type of store. If `nil`, Core Data automatically attempts to determine the
store class to use.

`url`

    

The file URL of the store.

`options`

    

A dictionary that contains options for the store.

## See Also

### Deprecated type methods

`class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]`

Returns a dictionary containing the parsed elements derived from the Spotlight
external record file that is specified by the given URL.

Deprecated

`class func metadataForPersistentStore(with: URL) -> [AnyHashable : Any]`

Returns a dictionary that contains the metadata stored in the persistent store
at the specified location.

Deprecated

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Deprecated

`class func metadataForPersistentStore(ofType: String, at: URL, options:
[AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`class func registerStoreClass(AnyClass?, forStoreType: String)`

Registers a persistent store subclass using the specified store type
identifier.

`class func removeUbiquitousContentAndPersistentStore(at: URL, options:
[AnyHashable : Any]?)`

Deletes all ubiquitous content for all peers for the persistent store at a
given URL and also delete the local store file.

Deprecated

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

Deprecated

Instance Method

# addPersistentStore(ofType:configurationName:at:options:)

Adds a specific type of persistent store at the provided location.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func addPersistentStore(
        ofType storeType: String,
        configurationName configuration: String?,
        at storeURL: URL?,
        options: [AnyHashable : Any]? = nil
    ) throws -> NSPersistentStore

Deprecated

Use `addPersistentStore(type:configuration:at:options:)` instead.

##  Parameters

`storeType`

    

A string constant (such as `NSSQLiteStoreType`) that specifies the store
type—see Persistent Store Types for possible values.

`configuration`

    

The name of a configuration in the receiver's managed object model that will
be used by the new store. The configuration can be `nil`, in which case no
other configurations are allowed.

`storeURL`

    

The file location of the persistent store.

`options`

    

A dictionary containing key-value pairs that specify whether the store should
be read-only, and whether (for an XML store) the XML file should be validated
against the DTD before it is read. For key definitions, see Store options and
Migration options. This value may be `nil`.

`error`

    

If a new store cannot be created, upon return contains an instance of
`NSError` that describes the problem

## Return Value

The newly created store or, if an error occurs, `nil`.

## Discussion

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated instance methods

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

### Related Documentation

`func remove(NSPersistentStore)`

Removes the specified persistent store from the coordinator.

Instance Method

# destroyPersistentStore(at:ofType:options:)

Deletes a specific type of persistent store at the provided location.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func destroyPersistentStore(
        at url: URL,
        ofType storeType: String,
        options: [AnyHashable : Any]? = nil
    ) throws

Deprecated

Use `destroyPersistentStore(at:type:options:)` instead.

##  Parameters

`url`

    

The store’s location.

`storeType`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

#
importStore(withIdentifier:fromExternalRecordsDirectoryAt:to:options:ofType:)

Creates and populates a store with the external records found at a given URL.

macOS 10.6–10.13  Deprecated

    
    
    func importStore(
        withIdentifier storeIdentifier: String?,
        fromExternalRecordsDirectoryAt externalRecordsURL: URL,
        to destinationURL: URL,
        options: [AnyHashable : Any]? = nil,
        ofType storeType: String
    ) throws -> NSPersistentStore

##  Parameters

`storeIdentifier`

    

The identifier for a store.

If this value is `nil` then the method imports the records for the first store
found.

`externalRecordsURL`

    

The location of the directory containing external records.

`destinationURL`

    

An URL object that specifies the location for the new store.

There should be no existing store at this location, as the store will be
created from scratch (appending to an existing store is not allowed).

`options`

    

A dictionary containing key-value pairs that specify whether the store should
be read-only, and whether (for an XML store) the XML file should be validated
against the DTD before it is read. For key definitions, see Store options.

`storeType`

    

A string constant (such as `NSSQLiteStoreType`) that specifies the type of the
new store—see Persistent Store Types.

`error`

    

If an error occurs, upon return contains an instance of `NSError` that
describes the problem.

## Return Value

An object representing the newly-created store.

## Discussion

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

### Related Documentation

`func remove(NSPersistentStore)`

Removes the specified persistent store from the coordinator.

Instance Method

# lock()

Attempts to acquire a lock.

iOS 3.0–8.0  Deprecated  iPadOS 3.0–8.0  Deprecated  macOS 10.4–10.10
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func lock()

## Discussion

This method blocks a thread’s execution until the lock can be acquired. An
application protects a critical section of code by requiring a thread to
acquire a lock before executing the code. Once the critical section is past,
the thread relinquishes the lock by invoking unlock.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

# migratePersistentStore(_:to:options:withType:)

Changes the location and, if necessary, the store type of the specified
persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func migratePersistentStore(
        _ store: NSPersistentStore,
        to URL: URL,
        options: [AnyHashable : Any]? = nil,
        withType storeType: String
    ) throws -> NSPersistentStore

Deprecated

Use `migratePersistentStore(_:to:options:type:)` instead.

##  Parameters

`store`

    

A persistent store.

`URL`

    

An URL object that specifies the location for the new store.

`options`

    

A dictionary containing key-value pairs that specify whether the store should
be read-only, and whether (for an XML store) the XML file should be validated
against the DTD before it is read. For key definitions, see Store options.

`storeType`

    

A string constant (such as `NSSQLiteStoreType`) that specifies the type of the
new store—see Persistent Store Types.

`error`

    

If an error occurs, upon return contains an instance of `NSError` that
describes the problem.

## Return Value

If the migration is successful, the new store, otherwise `nil`.

## Discussion

This method is typically used for “Save As” operations. Performance may vary
depending on the type of old and new store. For more details of the action of
this method, see Persistent Store Features in Core Data Programming Guide.

Important

After invocation of this method, the specified store is removed from the
coordinator thus `store` is no longer a useful reference.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

### Related Documentation

`func remove(NSPersistentStore)`

Removes the specified persistent store from the coordinator.

Instance Method

#
replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:ofType:)

Replaces one persistent store with another.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func replacePersistentStore(
        at destinationURL: URL,
        destinationOptions: [AnyHashable : Any]? = nil,
        withPersistentStoreFrom sourceURL: URL,
        sourceOptions: [AnyHashable : Any]? = nil,
        ofType storeType: String
    ) throws

Deprecated

Use
`replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)`
instead.

##  Parameters

`destinationURL`

    

The location of the store to replace.

`destinationOptions`

    

A dictionary containing key-value pairs that specify the behavior and
characteristics of the store to replace. For more information, see Store
options.

`sourceURL`

    

The location of the store to use as the replacement.

`sourceOptions`

    

A dictionary containing key-value pairs that specify the behavior and
characteristics of the replacement store. For more information, see Store
options.

`storeType`

    

The store type of the replacement store. For possible values, see
`NSPersistentStore.StoreType`.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

# tryLock()

Attempts to acquire a lock.

iOS 3.0–8.0  Deprecated  iPadOS 3.0–8.0  Deprecated  macOS 10.4–10.10
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func tryLock() -> Bool

## Return Value

`true` if successful, otherwise `false`.

## Discussion

Returns immediately—contrast `lock()` which blocks.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

# unlock()

Relinquishes a previously acquired lock.

iOS 3.0–8.0  Deprecated  iPadOS 3.0–8.0  Deprecated  macOS 10.4–10.10
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func unlock()

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

# perform(_:)

Executes the provided closure asynchronously on the coordinator’s queue.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func perform(_ block: @escaping () -> Void)

Deprecated

Use `perform(_:)` instead.

##  Parameters

`block`

    

The closure to execute.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func performAndWait(() -> Void)`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Instance Method

# performAndWait(_:)

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func performAndWait(_ block: () -> Void)

Deprecated

Use `performAndWait(_:)` instead.

##  Parameters

`block`

    

The closure to execute.

## See Also

### Deprecated instance methods

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable :
Any]?)`

Deletes a specific type of persistent store at the provided location.

`func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt:
URL, to: URL, options: [AnyHashable : Any]?, ofType: String) ->
NSPersistentStore`

Creates and populates a store with the external records found at a given URL.

Deprecated

`func lock()`

Attempts to acquire a lock.

Deprecated

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
ofType: String)`

Replaces one persistent store with another.

`func tryLock() -> Bool`

Attempts to acquire a lock.

Deprecated

`func unlock()`

Relinquishes a previously acquired lock.

Deprecated

`func perform(() -> Void)`

Executes the provided closure asynchronously on the coordinator’s queue.

Instance Property

# expressionResultType

The attribute type of the expression’s result.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var expressionResultType: NSAttributeType { get set }

Deprecated

Use `resultType` instead.

Instance Method

#
migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)

Migrates the store at a given source URL to the store at a given destination
URL, performing all of the mappings specified in a given mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func migrateStore(
        from sourceURL: URL,
        sourceType sStoreType: String,
        options sOptions: [AnyHashable : Any]? = nil,
        with mappings: NSMappingModel?,
        toDestinationURL dURL: URL,
        destinationType dStoreType: String,
        destinationOptions dOptions: [AnyHashable : Any]? = nil
    ) throws

Deprecated

Use `migrateStore(from:type:options:mapping:to:type:options:)` instead.

##  Parameters

`sourceURL`

    

The location of an existing persistent store. A store must exist at this URL.

`sStoreType`

    

The type of store at `sourceURL` (see `NSPersistentStoreCoordinator` for
possible values).

`sOptions`

    

A dictionary of options for the source (see `NSPersistentStoreCoordinator` for
possible values).

`mappings`

    

The mapping model to use to effect the migration.

`dURL`

    

The location of the destination store.

`dStoreType`

    

The type of store at `dURL` (see `NSPersistentStoreCoordinator` for possible
values).

`dOptions`

    

A dictionary of options for the destination (see
`NSPersistentStoreCoordinator` for possible values).

`error`

    

If an error occurs during the validation or migration, upon return contains an
`NSError` object that describes the problem.

## Return Value

`true` if the migration proceeds without errors during the compatibility
checks or migration, otherwise `false`.

## Discussion

This method performs compatibility checks on the source and destination models
and the mapping model.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

### Special Considerations

If a store does not exist at the destination URL (`dURL`), one is created;
otherwise, the migration appends to the existing store.

## See Also

### Related Documentation

`func cancelMigrationWithError(any Error)`

Cancels the migration with a given error.

