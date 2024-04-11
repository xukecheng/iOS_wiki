Initializer

# init(sourceModel:destinationModel:)

Initializes a migration manager instance with given source and destination
models.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        sourceModel: NSManagedObjectModel,
        destinationModel: NSManagedObjectModel
    )

##  Parameters

`sourceModel`

    

The source managed object model for the migration manager.

`destinationModel`

    

The destination managed object model for the migration manager.

## Return Value

A migration manager instance initialized to migrate data in a store that uses
`sourceModel` to a store that uses `destinationModel`.

## Discussion

You specify the mapping model in the migration method,
`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`.

### Special Considerations

This is the designated initializer for `NSMigrationManager`.

Although validation of the models is performed during
`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`,
as with `NSPersistentStoreCoordinator` once models are added to the migration
manager they are immutable and cannot be altered.

## See Also

### Related Documentation

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func migrateStore(from: URL, sourceType: String, options: [AnyHashable :
Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String,
destinationOptions: [AnyHashable : Any]?)`

Migrates the store at a given source URL to the store at a given destination
URL, performing all of the mappings specified in a given mapping model.

Core Data Model Versioning and Data Migration Programming Guide

Instance Property

# destinationContext

The managed object context the migration manager uses for writing the
destination persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var destinationContext: NSManagedObjectContext { get }

## Discussion

This context is created on demand as part of the initialization of the Core
Data stacks used for migration.

## See Also

### Getting the Manager’s Configuration

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

Instance Property

# destinationModel

The destination model for the migration manager.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var destinationModel: NSManagedObjectModel { get }

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

### Related Documentation

`init(sourceModel: NSManagedObjectModel, destinationModel:
NSManagedObjectModel)`

Initializes a migration manager instance with given source and destination
models.

Instance Property

# mappingModel

The mapping model for the migration manager.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var mappingModel: NSMappingModel { get }

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

### Related Documentation

`func migrateStore(from: URL, sourceType: String, options: [AnyHashable :
Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String,
destinationOptions: [AnyHashable : Any]?)`

Migrates the store at a given source URL to the store at a given destination
URL, performing all of the mappings specified in a given mapping model.

Instance Property

# sourceContext

The managed object context the migration manager uses for reading the source
persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceContext: NSManagedObjectContext { get }

## Discussion

This context is created on demand as part of the initialization of the Core
Data stacks used for migration.

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

Instance Property

# sourceModel

The source model for the migration manager.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceModel: NSManagedObjectModel { get }

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

### Related Documentation

`init(sourceModel: NSManagedObjectModel, destinationModel:
NSManagedObjectModel)`

Initializes a migration manager instance with given source and destination
models.

Instance Method

# destinationEntity(for:)

Returns the entity description for the destination entity of a given entity
mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func destinationEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?

##  Parameters

`mEntity`

    

An entity mapping.

## Return Value

The entity description for the destination entity of `mEntity`.

## Discussion

Entity mappings do not store the actual description objects, but rather the
name and version information of the entity.

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the source entity of a given entity
mapping.

Instance Method

# sourceEntity(for:)

Returns the entity description for the source entity of a given entity
mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func sourceEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?

##  Parameters

`mEntity`

    

An entity mapping.

## Return Value

The entity description for the source entity of `mEntity`.

## Discussion

Entity mappings do not store the actual description objects, but rather the
name and version information of the entity.

## See Also

### Getting the Manager’s Configuration

`var destinationContext: NSManagedObjectContext`

The managed object context the migration manager uses for writing the
destination persistent store.

`var destinationModel: NSManagedObjectModel`

The destination model for the migration manager.

`var mappingModel: NSMappingModel`

The mapping model for the migration manager.

`var sourceContext: NSManagedObjectContext`

The managed object context the migration manager uses for reading the source
persistent store.

`var sourceModel: NSManagedObjectModel`

The source model for the migration manager.

`func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?`

Returns the entity description for the destination entity of a given entity
mapping.

Instance Property

# userInfo

The user info for the migration manager.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

You can use the user info dictionary to aid the customization of your
migration process.

## See Also

### Customizing the Manager

`var usesStoreSpecificMigrationManager: Bool`

A Boolean value that indicates whether the migration manager tries to use a
store specific migration manager to perform the migration.

Instance Property

# usesStoreSpecificMigrationManager

A Boolean value that indicates whether the migration manager tries to use a
store specific migration manager to perform the migration.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var usesStoreSpecificMigrationManager: Bool { get set }

## Return Value

`true` if the receiver uses a store-specific migration manager, otherwise
`false`.

## Discussion

`true` if the receiver uses a store-specific migration manager, otherwise
`false`. The default value is `true`.

A store-specific migration manager class is not guaranteed to perform any of
the migration manager delegate callbacks or update values for the observable
properties.

## See Also

### Customizing the Manager

`var userInfo: [AnyHashable : Any]?`

The user info for the migration manager.

Instance Method

# associate(sourceInstance:withDestinationInstance:for:)

Associates a given source managed object instance with an array of destination
instances for a given property mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func associate(
        sourceInstance: NSManagedObject,
        withDestinationInstance destinationInstance: NSManagedObject,
        for entityMapping: NSEntityMapping
    )

##  Parameters

`sourceInstance`

    

A source managed object.

`destinationInstance`

    

The destination manage object for `sourceInstance`.

`entityMapping`

    

The entity mapping to use to associate `sourceInstance` with the object in
`destinationInstances`.

## Discussion

Data migration is performed as a three-stage process (first create the data,
then relate the data, then validate the data). You use this method to
associate data between the source and destination stores, in order to allow
for relationship creation or fix-up after the creation stage.

This method is called in the default implementation of
`NSEntityMigrationPolicy`’s
`createDestinationInstances(forSource:in:manager:)` method.

## See Also

### Managing Sources and Destinations

`func destinationInstances(forEntityMappingName: String, sourceInstances:
[NSManagedObject]?) -> [NSManagedObject]`

Returns the managed object instances created in the destination store for the
named entity mapping for the given array of source instances.

`func sourceInstances(forEntityMappingName: String, destinationInstances:
[NSManagedObject]?) -> [NSManagedObject]`

Returns the managed object instances in the source store used to create the
given destination instances for the passed in property mapping.

Instance Method

# destinationInstances(forEntityMappingName:sourceInstances:)

Returns the managed object instances created in the destination store for the
named entity mapping for the given array of source instances.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func destinationInstances(
        forEntityMappingName mappingName: String,
        sourceInstances: [NSManagedObject]?
    ) -> [NSManagedObject]

##  Parameters

`mappingName`

    

The name of an entity mapping in use.

`sourceInstances`

    

A array of managed objects in the source store.

## Return Value

An array containing the managed object instances created in the destination
store for the entity mapping named `mappingName` for `sourceInstances`. If
`sourceInstances` is `nil`, all of the destination instances created by the
specified property mapping are returned.

## Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName`
is not a valid mapping name.

## See Also

### Managing Sources and Destinations

`func associate(sourceInstance: NSManagedObject, withDestinationInstance:
NSManagedObject, for: NSEntityMapping)`

Associates a given source managed object instance with an array of destination
instances for a given property mapping.

`func sourceInstances(forEntityMappingName: String, destinationInstances:
[NSManagedObject]?) -> [NSManagedObject]`

Returns the managed object instances in the source store used to create the
given destination instances for the passed in property mapping.

Instance Method

# sourceInstances(forEntityMappingName:destinationInstances:)

Returns the managed object instances in the source store used to create the
given destination instances for the passed in property mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func sourceInstances(
        forEntityMappingName mappingName: String,
        destinationInstances: [NSManagedObject]?
    ) -> [NSManagedObject]

##  Parameters

`mappingName`

    

The name of an entity mapping in use.

`destinationInstances`

    

A array of managed objects in the destination store.

## Return Value

An array containing the managed object instances in the source store used to
create `destinationInstances` using the entity mapping named `mappingName`. If
`destinationInstances` is `nil`, all of the source instances used to create
the destination instance for this property mapping are returned.

## Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName`
is not a valid mapping name.

## See Also

### Managing Sources and Destinations

`func associate(sourceInstance: NSManagedObject, withDestinationInstance:
NSManagedObject, for: NSEntityMapping)`

Associates a given source managed object instance with an array of destination
instances for a given property mapping.

`func destinationInstances(forEntityMappingName: String, sourceInstances:
[NSManagedObject]?) -> [NSManagedObject]`

Returns the managed object instances created in the destination store for the
named entity mapping for the given array of source instances.

Instance Method

# migrateStore(from:type:options:mapping:to:type:options:)

Migrates the source store to the destination using the specified mapping
model.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func migrateStore(
        from sourceURL: URL,
        type sourceType: NSPersistentStore.StoreType,
        options sourceOptions: [AnyHashable : Any]? = nil,
        mapping: NSMappingModel,
        to destinationURL: URL,
        type destinationType: NSPersistentStore.StoreType,
        options destinationOptions: [AnyHashable : Any]? = nil
    ) throws

##  Parameters

`sourceURL`

    

The location of the store to migrate.

`sourceType`

    

The persistent store type of the store you’re migrating from. For possible
values, see `NSPersistentStore.StoreType`.

`sourceOptions`

    

A dictionary of options to apply to the source store. For possible values, see
`NSPersistentStoreCoordinator`.

`mapping`

    

The mapping model that converts the entities in the source store to those in
the destination store.

`destinationURL`

    

The location of the destination store.

`destinationType`

    

The persistent store type of the store you’re migrating to. For possible
values, see `NSPersistentStore.StoreType`.

`destinationOptions`

    

A dictionary of options to apply to the destination store. For possible
values, see `NSPersistentStoreCoordinator`.

## Discussion

A store must exist at `sourceURL`; otherwise, the migration fails. Before the
migration occurs, the method ensures compatibility between the source model,
the destination model, and the mapping model. If a store doesn’t exist at
`destinationURL`, Core Data creates one as part of the migration; otherwise,
the migration updates the existing store.

Instance Property

# migrationProgress

A number between `0` and `1` that indicates the proportion of completeness of
the migration.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var migrationProgress: Float { get }

## Discussion

If a migration is not taking place, this property is `1`. You can observe this
value using key-value observing.

## See Also

### Monitoring a Migration’s Progress

`var currentEntityMapping: NSEntityMapping`

The entity mapping currently being processed.

Instance Property

# currentEntityMapping

The entity mapping currently being processed.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var currentEntityMapping: NSEntityMapping { get }

## Discussion

Each entity is processed a total of three times—instance creation,
relationship creation, and validation.

### Special Considerations

You can observe this value using key-value observing.

## See Also

### Monitoring a Migration’s Progress

`var migrationProgress: Float`

A number between `0` and `1` that indicates the proportion of completeness of
the migration.

Instance Method

# cancelMigrationWithError(_:)

Cancels the migration with a given error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func cancelMigrationWithError(_ error: any Error)

##  Parameters

`error`

    

An error object that describes the reason why the migration is canceled.

## Discussion

You can invoke this method from anywhere in the migration process to abort the
migration. Calling this method causes
`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`
to abort the migration and return `error`—you should provide an appropriate
error to indicate the reason for the cancellation.

## See Also

### Aborting a Migration

`func reset()`

Resets the association tables for the migration.

Instance Method

# reset()

Resets the association tables for the migration.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func reset()

## Discussion

This method does not reset the source or destination contexts.

## See Also

### Aborting a Migration

`func cancelMigrationWithError(any Error)`

Cancels the migration with a given error.

