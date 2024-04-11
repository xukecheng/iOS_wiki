Initializer

# init(managedObjectModel:)

Creates a persistent store coordinator with the specified managed object
model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(managedObjectModel model: NSManagedObjectModel)

##  Parameters

`model`

    

A managed object model.

## Return Value

The receiver, initialized with `model`.

## See Also

### Creating a persistent store coordinator

API Reference

Store options

The options keys that configure the behavior and characteristics of a
persistent store.

API Reference

Migration options

The options keys that configure the migration behavior of a persistent store.

API Reference

Store versions

The metadata keys you use when comparing store versions.

Instance Property

# name

The coordinator’s name.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String? { get set }

## See Also

### Managing configuration

`var managedObjectModel: NSManagedObjectModel`

The coordinator’s managed object model.

`var persistentStores: [NSPersistentStore]`

The coordinator’s persistent stores.

Instance Property

# managedObjectModel

The coordinator’s managed object model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var managedObjectModel: NSManagedObjectModel { get }

## See Also

### Managing configuration

`var name: String?`

The coordinator’s name.

`var persistentStores: [NSPersistentStore]`

The coordinator’s persistent stores.

Instance Property

# persistentStores

The coordinator’s persistent stores.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var persistentStores: [NSPersistentStore] { get }

## See Also

### Managing configuration

`var name: String?`

The coordinator’s name.

`var managedObjectModel: NSManagedObjectModel`

The coordinator’s managed object model.

Type Method

# registerStoreClass(_:type:)

Registers a persistent store subclass using the specified store type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    class func registerStoreClass(
        _ storeClass: AnyClass?,
        type: NSPersistentStore.StoreType
    )

##  Parameters

`storeClass`

    

A subclass of `NSPersistentStore`.

`type`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

## Discussion

You must register the subclass before you load instances of it into the
persistent store coordinator. To unregister a subclass for a specific store
type, use `nil` for `storeClass`.

## See Also

### Registering store types

`class var registeredStoreTypes: [String : NSValue]`

The coordinator’s registered store types.

Type Property

# registeredStoreTypes

The coordinator’s registered store types.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class var registeredStoreTypes: [String : NSValue] { get }

## Return Value

A dictionary of the registered store types—the keys are the store type
strings, and the values are the `NSPersistentStore` subclasses.

## See Also

### Registering store types

`class func registerStoreClass(AnyClass?, type: NSPersistentStore.StoreType)`

Registers a persistent store subclass using the specified store type.

Instance Method

# addPersistentStore(type:configuration:at:options:)

Adds a specific type of persistent store at the provided location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func addPersistentStore(
        type: NSPersistentStore.StoreType,
        configuration: String? = nil,
        at storeURL: URL,
        options: [AnyHashable : Any]? = nil
    ) throws -> NSPersistentStore

##  Parameters

`type`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

`configuration`

    

The name of the configuration to use. You must define this configuration in
the coordinator’s managed object model.

`storeURL`

    

The store’s location.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

## See Also

### Adding or removing a store

`func addPersistentStore(with: NSPersistentStoreDescription,
completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)`

Adds a persistent store using the provided description.

`func remove(NSPersistentStore)`

Removes the specified persistent store from the coordinator.

Instance Method

# addPersistentStore(with:completionHandler:)

Adds a persistent store using the provided description.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func addPersistentStore(
        with storeDescription: NSPersistentStoreDescription,
        completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void
    )

##  Parameters

`storeDescription`

    

A description object used to create and load a persistent store.

`block`

    

The completion handler block that’s invoked after the store is added.

## Return Value

The newly created store or, if an error occurs, `nil`.

## See Also

### Adding or removing a store

`func addPersistentStore(type: NSPersistentStore.StoreType, configuration:
String?, at: URL, options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func remove(NSPersistentStore)`

Removes the specified persistent store from the coordinator.

Instance Method

# remove(_:)

Removes the specified persistent store from the coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func remove(_ store: NSPersistentStore) throws

##  Parameters

`store`

    

A persistent store.

`error`

    

If an error occurs, upon return contains an instance of `NSError` that
describes the problem.

## Return Value

`true` if the store is removed, otherwise `false`.

## Discussion

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Adding or removing a store

`func addPersistentStore(type: NSPersistentStore.StoreType, configuration:
String?, at: URL, options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

`func addPersistentStore(with: NSPersistentStoreDescription,
completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)`

Adds a persistent store using the provided description.

### Related Documentation

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, withType: String) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func addPersistentStore(ofType: String, configurationName: String?, at: URL?,
options: [AnyHashable : Any]?) -> NSPersistentStore`

Adds a specific type of persistent store at the provided location.

Instance Method

# destroyPersistentStore(at:type:options:)

Deletes a specific type of persistent store at the provided location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func destroyPersistentStore(
        at url: URL,
        type storeType: NSPersistentStore.StoreType,
        options: [AnyHashable : Any]? = nil
    ) throws

##  Parameters

`url`

    

The store’s location.

`storeType`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

## See Also

### Modifying a store

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, type: NSPersistentStore.StoreType) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
type: NSPersistentStore.StoreType)`

Replaces one persistent store with another.

Instance Method

# migratePersistentStore(_:to:options:type:)

Changes the location and, if necessary, the store type of the specified
persistent store.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func migratePersistentStore(
        _ store: NSPersistentStore,
        to storeURL: URL,
        options: [AnyHashable : Any]? = nil,
        type storeType: NSPersistentStore.StoreType
    ) throws -> NSPersistentStore

##  Parameters

`store`

    

The peristent store to migrate.

`storeURL`

    

The location of the new persistent store.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

`storeType`

    

The new store type. For possible values, see `NSPersistentStore.StoreType`.

## Discussion

Performance may vary depending on the store types of the old and new stores.
Invoking this method removes the specified store from the coordinator.

## See Also

### Modifying a store

`func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType,
options: [AnyHashable : Any]?)`

Deletes a specific type of persistent store at the provided location.

`func replacePersistentStore(at: URL, destinationOptions: [AnyHashable :
Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?,
type: NSPersistentStore.StoreType)`

Replaces one persistent store with another.

Instance Method

#
replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)

Replaces one persistent store with another.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func replacePersistentStore(
        at destinationURL: URL,
        destinationOptions: [AnyHashable : Any]? = nil,
        withPersistentStoreFrom sourceURL: URL,
        sourceOptions: [AnyHashable : Any]? = nil,
        type sourceType: NSPersistentStore.StoreType
    ) throws

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

`sourceType`

    

The store type of the replacement store. For possible values, see
`NSPersistentStore.StoreType`.

## See Also

### Modifying a store

`func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType,
options: [AnyHashable : Any]?)`

Deletes a specific type of persistent store at the provided location.

`func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable
: Any]?, type: NSPersistentStore.StoreType) -> NSPersistentStore`

Changes the location and, if necessary, the store type of the specified
persistent store.

Instance Method

# setURL(_:for:)

Changes the location of the specified persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setURL(
        _ url: URL,
        for store: NSPersistentStore
    ) -> Bool

##  Parameters

`url`

    

The new location for `store`.

`store`

    

A persistent store associated with the receiver.

## Return Value

`true` if the store was relocated, otherwise `false`.

## Discussion

For atomic stores, this method alters the location to which the next save
operation will write the file; for non-atomic stores, invoking this method
will relinquish the existing connection and create a new one at the specified
URL. (For non-atomic stores, a store must already exist at the destination
URL; a new store will not be created.)

## See Also

### Managing a store’s location

`func persistentStore(for: URL) -> NSPersistentStore?`

Returns the persistent store for the specified file URL.

`func url(for: NSPersistentStore) -> URL`

Returns the location of the provided persistent store.

Instance Method

# persistentStore(for:)

Returns the persistent store for the specified file URL.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func persistentStore(for URL: URL) -> NSPersistentStore?

##  Parameters

`URL`

    

An URL object that specifies the location of a persistent store.

## Return Value

The persistent store at the location specified by `URL`.

## See Also

### Managing a store’s location

`func setURL(URL, for: NSPersistentStore) -> Bool`

Changes the location of the specified persistent store.

`func url(for: NSPersistentStore) -> URL`

Returns the location of the provided persistent store.

Instance Method

# url(for:)

Returns the location of the provided persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func url(for store: NSPersistentStore) -> URL

##  Parameters

`store`

    

A persistent store.

## Return Value

The URL for `store`.

## See Also

### Managing a store’s location

`func setURL(URL, for: NSPersistentStore) -> Bool`

Changes the location of the specified persistent store.

`func persistentStore(for: URL) -> NSPersistentStore?`

Returns the persistent store for the specified file URL.

### Related Documentation

`var persistentStores: [NSPersistentStore]`

The coordinator’s persistent stores.

Type Method

# setMetadata(_:type:at:options:)

Updates the metadata of a specific type of persistent store at the provided
location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    class func setMetadata(
        _ metadata: [String : Any]?,
        type storeType: NSPersistentStore.StoreType,
        at storeURL: URL,
        options: [AnyHashable : Any]? = nil
    ) throws

##  Parameters

`metadata`

    

A dictionary that contains the metadata to associate with the store.

`storeType`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

`storeURL`

    

The store’s location.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

## See Also

### Managing a store’s metadata

`class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at:
URL, options: [AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`let NSStoreTypeKey: String`

A key that identifies the store type.

`let NSStoreUUIDKey: String`

A key that provides the store’s UUID.

Type Method

# metadataForPersistentStore(type:at:options:)

Returns the metadata of a specific type of persistent store at the provided
location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    class func metadataForPersistentStore(
        type storeType: NSPersistentStore.StoreType,
        at storeURL: URL,
        options: [AnyHashable : Any]? = nil
    ) throws -> [String : Any]

##  Parameters

`storeType`

    

The store type. For possible values, see `NSPersistentStore.StoreType`.

`storeURL`

    

The store’s location.

`options`

    

A dictionary containing key-value pairs that specify store behavior and
characteristics. For more information, see Store options.

## See Also

### Managing a store’s metadata

`class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType,
at: URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`let NSStoreTypeKey: String`

A key that identifies the store type.

`let NSStoreUUIDKey: String`

A key that provides the store’s UUID.

Instance Method

# metadata(for:)

Returns the metadata of the specified persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func metadata(for store: NSPersistentStore) -> [String : Any]

##  Parameters

`store`

    

A persistent store.

## Return Value

A dictionary that contains the metadata currently stored or to-be-stored in
`store`.

## See Also

### Managing a store’s metadata

`class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType,
at: URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

`class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at:
URL, options: [AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`let NSStoreTypeKey: String`

A key that identifies the store type.

`let NSStoreUUIDKey: String`

A key that provides the store’s UUID.

### Related Documentation

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Instance Method

# setMetadata(_:for:)

Updates the metadata for the specified persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setMetadata(
        _ metadata: [String : Any]?,
        for store: NSPersistentStore
    )

##  Parameters

`metadata`

    

A dictionary containing metadata for the store.

`store`

    

A persistent store.

## Discussion

The store type and UUID (`NSStoreTypeKey` and `NSStoreUUIDKey`) are always
added automatically, however `NSStoreUUIDKey` is only added if it is not set
manually as part of the dictionary argument.

Important

Setting the metadata for a store does not change the information on disk until
the store is actually saved.

## See Also

### Managing a store’s metadata

`class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType,
at: URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

`class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at:
URL, options: [AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

`let NSStoreTypeKey: String`

A key that identifies the store type.

`let NSStoreUUIDKey: String`

A key that provides the store’s UUID.

### Related Documentation

`class func setMetadata([String : Any]?, forPersistentStoreOfType: String?,
at: URL)`

Sets the metadata for a given store.

`class func metadataForPersistentStore(ofType: String?, at: URL) -> [String :
Any]`

Returns a dictionary containing the metadata stored in the persistent store at
a given URL.

Global Variable

# NSStoreTypeKey

A key that identifies the store type.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSStoreTypeKey: String

## See Also

### Managing a store’s metadata

`class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType,
at: URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

`class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at:
URL, options: [AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`let NSStoreUUIDKey: String`

A key that provides the store’s UUID.

Global Variable

# NSStoreUUIDKey

A key that provides the store’s UUID.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSStoreUUIDKey: String

## Discussion

The store UUID is useful to identify stores through URI representations, but
it is _not_ guaranteed to be unique. The UUID generated for new stores is
unique—users can freely copy files and thus the UUID stored inside—so if you
track or reference stores explicitly you need to be aware of duplicate UUIDs
and potentially override the UUID when a new store is added to the list of
known stores in your application.

## See Also

### Managing a store’s metadata

`class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType,
at: URL, options: [AnyHashable : Any]?)`

Updates the metadata of a specific type of persistent store at the provided
location.

`class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at:
URL, options: [AnyHashable : Any]?) -> [String : Any]`

Returns the metadata of a specific type of persistent store at the provided
location.

`func metadata(for: NSPersistentStore) -> [String : Any]`

Returns the metadata of the specified persistent store.

`func setMetadata([String : Any]?, for: NSPersistentStore)`

Updates the metadata for the specified persistent store.

`let NSStoreTypeKey: String`

A key that identifies the store type.

Global Variable

# NSPersistentStoreDeferredLightweightMigrationOptionKey

The key for enabling deferred lightweight migrations.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    let NSPersistentStoreDeferredLightweightMigrationOptionKey: String

## Discussion

As your managed object model changes, Core Data can use lightweight migrations
to synchronize the underlying store data with those evolving entity
definitions. These migrations happen at runtime, so they need to be fast or
they can lead to a poor experience, because a migration must complete before
your app can continue. Reduce the impact of migrations by deferring expensive
cleanup tasks — such as dropping a table — until a more opportune time.

Important

This key is dual-purpose. When adding a persistent store to the coordinator,
you use it to enable deferred lightweight migrations for that store.
Afterward, Core Data uses it to indicate whether there are deferred cleanup
tasks to run. Therefore, don’t use this key to later determine whether you
enabled deferred lightweight migrations on a specific store.

Deferred lightweight migrations are off by default. To enable them, add
`NSPersistentStoreDeferredLightweightMigrationOptionKey`, with a value of
`true`, to the options dictionary you provide when adding a persistent store
to the coordinator.

After you enable deferred lightweight migrations, Core Data continues to
perform your lightweight migrations as usual, but defers any time-consuming
cleanup tasks that don’t impact the execution of your app. Those tasks still
need to run, but you choose when to run them. To determine whether there are
deferred tasks to finish, query the store’s metadata with
`NSPersistentStoreDeferredLightweightMigrationOptionKey`. If the returned
value is `true`, execute those tasks using the coordinator. A single migration
may defer several distinct tasks and you can execute them all at once using
`finishDeferredLightweightMigration()`, or individually using
`finishDeferredLightweightMigrationTask()`.

## See Also

### Deferring a store’s migrations

`func finishDeferredLightweightMigrationTask()`

Executes a single pending task of a deferred lightweight migration.

`func finishDeferredLightweightMigration()`

Executes all remaining tasks of a deferred lightweight migration.

Instance Method

# finishDeferredLightweightMigrationTask()

Executes a single pending task of a deferred lightweight migration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func finishDeferredLightweightMigrationTask() throws

## Discussion

Note

Enable deferred lightweight migrations before using this method. For more
information, see `NSPersistentStoreDeferredLightweightMigrationOptionKey`.

## See Also

### Deferring a store’s migrations

`let NSPersistentStoreDeferredLightweightMigrationOptionKey: String`

The key for enabling deferred lightweight migrations.

`func finishDeferredLightweightMigration()`

Executes all remaining tasks of a deferred lightweight migration.

Instance Method

# finishDeferredLightweightMigration()

Executes all remaining tasks of a deferred lightweight migration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func finishDeferredLightweightMigration() throws

## Discussion

Note

Enable deferred lightweight migrations before using this method. For more
information, see `NSPersistentStoreDeferredLightweightMigrationOptionKey`.

## See Also

### Deferring a store’s migrations

`let NSPersistentStoreDeferredLightweightMigrationOptionKey: String`

The key for enabling deferred lightweight migrations.

`func finishDeferredLightweightMigrationTask()`

Executes a single pending task of a deferred lightweight migration.

Generic Instance Method

# perform(_:)

Executes the provided closure asynchronously on the coordinator’s queue and
awaits the result.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func perform<T>(_ block: @escaping () throws -> T) async rethrows -> T

##  Parameters

`block`

    

The closure to execute.

## See Also

### Performing tasks

`func performAndWait<T>(() -> T) -> T`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) -> Any`

Executes the specified request on each of the coordinator’s persistent stores.

Generic Instance Method

# performAndWait(_:)

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func performAndWait<T>(_ block: () throws -> T) rethrows -> T

##  Parameters

`block`

    

The closure to execute.

## See Also

### Performing tasks

`func perform<T>(() -> T) -> T`

Executes the provided closure asynchronously on the coordinator’s queue and
awaits the result.

`func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) -> Any`

Executes the specified request on each of the coordinator’s persistent stores.

Instance Method

# execute(_:with:)

Executes the specified request on each of the coordinator’s persistent stores.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func execute(
        _ request: NSPersistentStoreRequest,
        with context: NSManagedObjectContext
    ) throws -> Any

##  Parameters

`request`

    

A fetch or save request.

`context`

    

The context against which `request` should be executed.

`error`

    

If an error occurs, upon return contains an NSError object that describes the
problem.

## Return Value

An array containing managed objects, managed object IDs, or dictionaries as
appropriate for a fetch request; an empty array if `request` is a save
request, or `nil` if an error occurred.

User defined requests return arrays of arrays, where a nested array is the
result returned from a single store.

## Discussion

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Performing tasks

`func perform<T>(() -> T) -> T`

Executes the provided closure asynchronously on the coordinator’s queue and
awaits the result.

`func performAndWait<T>(() -> T) -> T`

Executes the provided closure on the coordinator’s queue and waits for it to
finish.

Global Variable

# NSPersistentHistoryTrackingKey

The key you use to enable persistent history tracking.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    let NSPersistentHistoryTrackingKey: String

## Discussion

Persistent history tracking is off by default.

## See Also

### Maintaining a record of changes

`func currentPersistentHistoryToken(fromStores: [Any]?) ->
NSPersistentHistoryToken?`

Returns a single persistent history token representing all of the specified
stores.

Instance Method

# currentPersistentHistoryToken(fromStores:)

Returns a single persistent history token representing all of the specified
stores.

iOS 12.0+  iPadOS 12.0+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 12.0+  watchOS
5.0+  visionOS 1.0+

    
    
    func currentPersistentHistoryToken(fromStores stores: [Any]?) -> NSPersistentHistoryToken?

##  Parameters

`stores`

    

The persistent stores of interest.

## Return Value

A persistent history token, or `nil` if the coordinator can’t create one.

## Discussion

If you specify `nil` or provide an empty array, the coordinator attempts to
create a token for all of its registered stores.

## See Also

### Maintaining a record of changes

`let NSPersistentHistoryTrackingKey: String`

The key you use to enable persistent history tracking.

Global Variable

# NSCoreDataCoreSpotlightExporter

The key you use to specify your Core Spotlight delegate.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    let NSCoreDataCoreSpotlightExporter: String

## See Also

### Integrating with Spotlight

`class NSCoreDataCoreSpotlightDelegate`

A set of methods that enable integration with Core Spotlight.

API Reference

Spotlight record keys

The keys for the values that exist in Spotlight’s external record files.

Showcase App Data in Spotlight

​ ​Index app data so users can find it by using Spotlight search. ​​

Instance Method

# managedObjectID(forURIRepresentation:)

Returns the object identifier for the specified URI representation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func managedObjectID(forURIRepresentation url: URL) -> NSManagedObjectID?

##  Parameters

`URL`

    

An URL object containing a URI that specify a managed object.

## Return Value

An object ID for the object specified by `URL`.

## Discussion

The URI representation contains a UUID of the store the ID is coming from, and
the coordinator can match it against the stores added to it.

## See Also

### Related Documentation

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

Type Property

# NSPersistentStoreCoordinatorStoresWillChange

A notification that posts before the coordinator changes its registered
stores.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name

## Discussion

This notification is similar to `NSPersistentStoreCoordinatorStoresDidChange`.
If the application is running, Core Data will post this notification before
responding to iCloud account changes or “Delete All” from Documents & Data.

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

# NSPersistentStoreCoordinatorStoresDidChange

A notification that posts after a coordinator changes its registered stores.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name

## Discussion

The notification's object is the persistent store coordinator that was
affected. The notification’s `userInfo` dictionary contains information about
the stores that were added or removed, specified using the following keys:

  * `NSAddedPersistentStoresKey`

  * `NSRemovedPersistentStoresKey`

  * `NSUUIDChangedPersistentStoresKey`

## See Also

### Core Data

`static let NSManagedObjectContextDidSave: NSNotification.Name`

A notification that the context completed a save.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

`static let NSManagedObjectContextWillSave: NSNotification.Name`

A notification that the context is about to save.

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

# NSPersistentStoreCoordinatorWillRemoveStore

A notification that posts before a coordinator removes a store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name

## Discussion

The notification is sent during the invocation of `NSPersistentStore`’s
`willRemove(from:)` method during store deallocation or removal. The
notification's object is the persistent store coordinator will be removed.

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

