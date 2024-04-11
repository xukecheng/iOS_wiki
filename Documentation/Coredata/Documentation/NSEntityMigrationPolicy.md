Instance Method

# begin(_:with:)

Sets up state information before the start of a given entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func begin(
        _ mapping: NSEntityMapping,
        with manager: NSMigrationManager
    ) throws

##  Parameters

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the method completes successfully, otherwise `false`.

## Discussion

This method is the precursor to the creation stage. In a custom class, you can
implement this method to set up any state information that will be useful for
the duration of the migration.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

### Related Documentation

Core Data Model Versioning and Data Migration Programming Guide

Instance Method

# createDestinationInstances(forSource:in:manager:)

Creates the destination instance(s) for a given source instance.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func createDestinationInstances(
        forSource sInstance: NSManagedObject,
        in mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`sInstance`

    

The source instance for which to create destination instances.

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the method completes successfully, otherwise `false`.

## Discussion

This method is invoked by the migration manager on each source instance (as
specified by the `sourceExpression` in the mapping) to create the
corresponding destination instance(s). It also associates the source and
destination instances by calling `NSMigrationManager`’s
`associate(sourceInstance:withDestinationInstance:for:)` method.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

### Special Considerations

If you override this method and do not invoke `super`, you must invoke
`NSMigrationManager`’s
`associate(sourceInstance:withDestinationInstance:for:)` to associate the
source and destination instances as required. .

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

Instance Method

# endInstanceCreation(forMapping:manager:)

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func endInstanceCreation(
        forMapping mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the relationships are constructed correctly, otherwise `false`.

## Discussion

You can override this method to clean up state from the creation of
destination or to prepare state for the creation of relationships.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

Instance Method

# createRelationships(forDestination:in:manager:)

Constructs the relationships between the newly-created destination instances.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func createRelationships(
        forDestination dInstance: NSManagedObject,
        in mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`dInstance`

    

The destination instance for which to create relationships.

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the relationships are constructed correctly, otherwise `false`.

## Discussion

You can use this stage to (re)create relationships between migrated
objects—you use the association lookup methods on the `NSMigrationManager`
instance to determine the appropriate relationship targets.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

Instance Method

# endRelationshipCreation(forMapping:manager:)

Indicates the end of the relationship creation stage for the specified entity
mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func endRelationshipCreation(
        forMapping mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the method completes correctly, otherwise `false`.

## Discussion

This method is invoked after
`createRelationships(forDestination:in:manager:)`; you can override it to
clean up state from the creation of relationships, or prepare state for custom
validation in `performCustomValidation(forMapping:manager:)`.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

Instance Method

# performCustomValidation(forMapping:manager:)

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func performCustomValidation(
        forMapping mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the method completes correctly, otherwise `false`.

## Discussion

This method is called before the default save validation is performed by the
framework.

If you implement this method, you must manually obtain the collection of
objects you are interested in validating.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func end(NSEntityMapping, manager: NSMigrationManager)`

Performs cleanup at the end of the migration, from any phase of the mapping.

Instance Method

# end(_:manager:)

Performs cleanup at the end of the migration, from any phase of the mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func end(
        _ mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws

##  Parameters

`mapping`

    

The mapping object in use.

`manager`

    

The migration manager performing the migration.

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the method completes correctly, otherwise `false`.

## Discussion

This is the end to the given entity mapping. You can implement this method to
perform any clean-up at the end of the migration (from any of the three phases
of the mapping).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Customizing Stages of the Mapping Life Cycle

`func begin(NSEntityMapping, with: NSMigrationManager)`

Sets up state information before the start of a given entity mapping.

`func createDestinationInstances(forSource: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Creates the destination instance(s) for a given source instance.

`func endInstanceCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the instance creation stage for the specified entity
mapping, and the precursor to the next migration stage.

`func createRelationships(forDestination: NSManagedObject, in:
NSEntityMapping, manager: NSMigrationManager)`

Constructs the relationships between the newly-created destination instances.

`func endRelationshipCreation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Indicates the end of the relationship creation stage for the specified entity
mapping.

`func performCustomValidation(forMapping: NSEntityMapping, manager:
NSMigrationManager)`

Provides the option to perform custom validation on migrated objects during
the validation stage of the entity migration policy.

Global Variable

# NSMigrationManagerKey

Key for the migration manager.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationManagerKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$manager`.

Global Variable

# NSMigrationSourceObjectKey

Key for the source object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationSourceObjectKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$source`.

Global Variable

# NSMigrationDestinationObjectKey

Key for the destination object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationDestinationObjectKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$destination`.

Global Variable

# NSMigrationEntityMappingKey

Key for the entity mapping object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationEntityMappingKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$entityMapping`.

Global Variable

# NSMigrationPropertyMappingKey

Key for the property mapping object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationPropertyMappingKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$propertyMapping`.

Global Variable

# NSMigrationEntityPolicyKey

Key for the entity migration policy object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigrationEntityPolicyKey: String

## Discussion

To access this key in a custom value expression string in the Xcode mapping
model editor use `$entityPolicy`.

