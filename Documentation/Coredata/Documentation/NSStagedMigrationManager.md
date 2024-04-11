Initializer

# init(_:)

Creates a migration manager with the specified stages.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    convenience init(_ stages: [NSMigrationStage])

##  Parameters

`stages`

    

The array of migration stages to execute.

## Discussion

Important

Core Data processes the migration stages in the order that you provide them.

Instance Property

# container

The container that provides access to the migrating persistent store.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var container: NSPersistentContainer? { get }

Instance Property

# stages

The migration stages.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var stages: [NSMigrationStage] { get }

## Discussion

Core Data sets this property to the `stages` parameter you specify when
creating the migration manager.

