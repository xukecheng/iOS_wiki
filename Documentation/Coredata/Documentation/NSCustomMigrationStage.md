Initializer

# init(migratingFrom:to:)

Creates a custom migration stage with the specified source and destination
model references.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    convenience init(
        migratingFrom currentModel: NSManagedObjectModelReference,
        to nextModel: NSManagedObjectModelReference
    )

##  Parameters

`currentModel`

    

The reference that represents the migration’s source model.

`nextModel`

    

The reference that represents the migration’s destination model.

## See Also

### Creating a custom migration stage

`class NSManagedObjectModelReference`

An object that describes a specific version of an object model.

Instance Property

# currentModel

The reference that represents the migration’s source model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var currentModel: NSManagedObjectModelReference { get }

## Discussion

Core Data sets this property to the `currentModel` parameter you specify when
creating the migration stage.

## See Also

### Accessing model references

`var nextModel: NSManagedObjectModelReference`

The reference that represents the migration’s destination model.

Instance Property

# nextModel

The reference that represents the migration’s destination model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var nextModel: NSManagedObjectModelReference { get }

## Discussion

Core Data sets this property to the `nextModel` parameter you specify when
creating the migration stage.

## See Also

### Accessing model references

`var currentModel: NSManagedObjectModelReference`

The reference that represents the migration’s source model.

Instance Property

# willMigrateHandler

The handler to execute before the stage runs.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var willMigrateHandler: ((_ migrationManager: NSStagedMigrationManager, _ migrationStage: NSCustomMigrationStage) throws -> Void)? { get set }

## Discussion

Use this handler to prepare the persistent store’s data for the pending
migration. Access the store using the `container` property of the handler’s
`migrationManager` parameter.

## See Also

### Assigning event handlers

`var didMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) ->
Void)?`

The handler to execute after the stage runs.

Instance Property

# didMigrateHandler

The handler to execute after the stage runs.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var didMigrateHandler: ((_ migrationManager: NSStagedMigrationManager, _ migrationStage: NSCustomMigrationStage) throws -> Void)? { get set }

## Discussion

Use this handler to perform any cleanup tasks on the persistent store’s data
after the migration has run. Access the store using the `container` property
of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers

`var willMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage)
-> Void)?`

The handler to execute before the stage runs.

