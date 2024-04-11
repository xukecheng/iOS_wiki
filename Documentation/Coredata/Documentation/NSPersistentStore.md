Initializer

# init(persistentStoreCoordinator:configurationName:at:options:)

Returns a store initialized with the given arguments.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        persistentStoreCoordinator root: NSPersistentStoreCoordinator?,
        configurationName name: String?,
        at url: URL,
        options: [AnyHashable : Any]? = nil
    )

##  Parameters

`coordinator`

    

A persistent store coordinator.

`configurationName`

    

The name of the managed object model configuration to use. Pass `nil` if you
do not want to specify a configuration.

`url`

    

The URL of the store to load.

`options`

    

A dictionary containing configuration options. See
`NSPersistentStoreCoordinator` for a list of key names for options in this
dictionary.

## Return Value

A new store object, associated with `coordinator`, that represents a
persistent store at url using the options in `options` and—if it is not
`nil`—the managed object model configuration `configurationName`.

## Discussion

You must ensure that you load metadata during initialization and set it using
`metadata`.

### Special Considerations

This is the designated initializer for persistent stores.

## See Also

### Related Documentation

`var metadata: [String : Any]!`

The metadata for the persistent store.

Core Data Programming Guide

Atomic Store Programming Topics

Incremental Store Programming Guide

Instance Property

# configurationName

The name of the managed object model configuration that creates the persistent
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var configurationName: String { get }

## See Also

### Getting Store Configuration

`var options: [AnyHashable : Any]?`

The options that Core Data uses to create the store.

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator that loads the persistent store.

`var type: String`

The type string of the persistent store.

`struct NSPersistentStore.StoreType`

The types of persistent stores that Core Data supports.

API Reference

Persistent Store Types

Persist data through the available store types.

Instance Property

# options

The options that Core Data uses to create the store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var options: [AnyHashable : Any]? { get }

## Discussion

See `NSPersistentStoreCoordinator` for a list of key names for options in this
dictionary.

## See Also

### Getting Store Configuration

`var configurationName: String`

The name of the managed object model configuration that creates the persistent
store.

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator that loads the persistent store.

`var type: String`

The type string of the persistent store.

`struct NSPersistentStore.StoreType`

The types of persistent stores that Core Data supports.

API Reference

Persistent Store Types

Persist data through the available store types.

Instance Property

# persistentStoreCoordinator

The persistent store coordinator that loads the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }

## See Also

### Getting Store Configuration

`var configurationName: String`

The name of the managed object model configuration that creates the persistent
store.

`var options: [AnyHashable : Any]?`

The options that Core Data uses to create the store.

`var type: String`

The type string of the persistent store.

`struct NSPersistentStore.StoreType`

The types of persistent stores that Core Data supports.

API Reference

Persistent Store Types

Persist data through the available store types.

Instance Property

# type

The type string of the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var type: String { get }

## Discussion

This string is used when specifying the type of store to add to a persistent
store coordinator.

### Special Considerations

Subclasses must override this method to provide a unique type.

## See Also

### Getting Store Configuration

`var configurationName: String`

The name of the managed object model configuration that creates the persistent
store.

`var options: [AnyHashable : Any]?`

The options that Core Data uses to create the store.

`var persistentStoreCoordinator: NSPersistentStoreCoordinator?`

The persistent store coordinator that loads the persistent store.

`struct NSPersistentStore.StoreType`

The types of persistent stores that Core Data supports.

API Reference

Persistent Store Types

Persist data through the available store types.

Instance Property

# identifier

The unique identifier for the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var identifier: String! { get set }

## Discussion

The identifier is used as part of the managed object IDs for each object in
the store.

### Special Considerations

`NSPersistentStore` provides a default implementation to provide a globally
unique identifier for the store instance.

## See Also

### Managing Store Attributes

`var isReadOnly: Bool`

A Boolean value that indicates whether the persistent store is read-only.

`var url: URL?`

The URL for the persistent store.

### Related Documentation

`var metadata: [String : Any]!`

The metadata for the persistent store.

Instance Property

# isReadOnly

A Boolean value that indicates whether the persistent store is read-only.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isReadOnly: Bool { get set }

## Discussion

`true` if the receiver is read-only, otherwise `false`.

## See Also

### Managing Store Attributes

`var identifier: String!`

The unique identifier for the persistent store.

`var url: URL?`

The URL for the persistent store.

Instance Property

# url

The URL for the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var url: URL? { get set }

## Discussion

To alter the location of a store, send the persistent store coordinator a
`setURL(_:for:)` message.

## See Also

### Managing Store Attributes

`var identifier: String!`

The unique identifier for the persistent store.

`var isReadOnly: Bool`

A Boolean value that indicates whether the persistent store is read-only.

Type Method

# metadataForPersistentStore(with:)

Returns the metadata from the persistent store at the given URL.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func metadataForPersistentStore(with url: URL) throws -> [String : Any]

##  Parameters

`url`

    

The location of the store.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

The metadata from the persistent store at `url`. Returns `nil` if there is an
error.

## Discussion

Subclasses must override this method.

### Discussion

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Store Metadata

`class func setMetadata([String : Any]?, forPersistentStoreAt: URL)`

Sets the metadata for the store at a given URL.

`func loadMetadata()`

Instructs the persistent store to load its metadata.

`var metadata: [String : Any]!`

The metadata for the persistent store.

Type Method

# setMetadata(_:forPersistentStoreAt:)

Sets the metadata for the store at a given URL.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func setMetadata(
        _ metadata: [String : Any]?,
        forPersistentStoreAt url: URL
    ) throws

##  Parameters

`metadata`

    

The metadata for the store at `url`.

`url`

    

The location of the store.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the metadata was written correctly, otherwise `false`.

## Discussion

Subclasses must override this method to set metadata appropriately.

### Discussion

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Store Metadata

`class func metadataForPersistentStore(with: URL) -> [String : Any]`

Returns the metadata from the persistent store at the given URL.

`func loadMetadata()`

Instructs the persistent store to load its metadata.

`var metadata: [String : Any]!`

The metadata for the persistent store.

Instance Method

# loadMetadata()

Instructs the persistent store to load its metadata.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func loadMetadata() throws

##  Parameters

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the metadata was loaded correctly, otherwise `false`.

## Discussion

There is no way to return an error if the store is invalid.

### Discussion

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Store Metadata

`class func metadataForPersistentStore(with: URL) -> [String : Any]`

Returns the metadata from the persistent store at the given URL.

`class func setMetadata([String : Any]?, forPersistentStoreAt: URL)`

Sets the metadata for the store at a given URL.

`var metadata: [String : Any]!`

The metadata for the persistent store.

Instance Property

# metadata

The metadata for the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var metadata: [String : Any]! { get set }

## Discussion

The dictionary must include the store type (`NSStoreTypeKey`) and UUID
(`NSStoreUUIDKey`).

### Special Considerations

Subclasses must override this property to provide storage and persistence for
the store metadata.

## See Also

### Managing Store Metadata

`class func metadataForPersistentStore(with: URL) -> [String : Any]`

Returns the metadata from the persistent store at the given URL.

`class func setMetadata([String : Any]?, forPersistentStoreAt: URL)`

Sets the metadata for the store at a given URL.

`func loadMetadata()`

Instructs the persistent store to load its metadata.

Instance Method

# didAdd(to:)

Invoked after the persistent store has been added to the persistent store
coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didAdd(to coordinator: NSPersistentStoreCoordinator)

##  Parameters

`coordinator`

    

The persistent store coordinator to which the receiver was added.

## Discussion

The default implementation does nothing. You can override this method in a
subclass in order to perform any kind of setup necessary before the load
method is invoked.

## See Also

### Responding to the Store Life Cycle

`func willRemove(from: NSPersistentStoreCoordinator?)`

Invoked before the persistent store is removed from the persistent store
coordinator.

Instance Method

# willRemove(from:)

Invoked before the persistent store is removed from the persistent store
coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willRemove(from coordinator: NSPersistentStoreCoordinator?)

##  Parameters

`coordinator`

    

The persistent store coordinator from which the receiver was removed.

## Discussion

The default implementation does nothing. You can override this method in a
subclass in order to perform any clean-up before the store is removed from the
coordinator (and deallocated).

## See Also

### Responding to the Store Life Cycle

`func didAdd(to: NSPersistentStoreCoordinator)`

Invoked after the persistent store has been added to the persistent store
coordinator.

Instance Property

# coreSpotlightExporter

The spotlight exporter associated with this persistent store.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    var coreSpotlightExporter: NSCoreDataCoreSpotlightDelegate { get }

## Discussion

Spotlight support isn’t available in a compatible iPad or iPhone app running
in visionOS.

Type Method

# migrationManagerClass()

Returns the migration manager class for this store class.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func migrationManagerClass() -> AnyClass

## Return Value

The `NSMigrationManager` class for this store class

## Discussion

In a subclass of `NSPersistentStore`, you can override this to provide a
custom migration manager subclass (for example, to take advantage of store-
specific functionality to improve migration performance).

