Global Variable

# NSIgnorePersistentStoreVersioningOption

Key to ignore the built-in versioning provided by Core Data.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSIgnorePersistentStoreVersioningOption: String

## Discussion

The corresponding value is an `NSNumber` object. If the `boolValue` of the
number is `true`, Core Data will not compare the version hashes between the
managed object model in the coordinator and the metadata for the loaded store.
(It will, however, continue to update the version hash information in the
metadata.) This key and corresponding value of `true` is specified by default
for all applications linked on or before OS X v10.4.

Global Variable

# NSMigratePersistentStoresAutomaticallyOption

Key to automatically attempt to migrate versioned stores.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSMigratePersistentStoresAutomaticallyOption: String

## Discussion

The corresponding value is an `NSNumber` object. If the `boolValue` of the
number is `true` and if the version hash information for the added store is
determined to be incompatible with the model for the coordinator, Core Data
will attempt to locate the source and mapping models in the application
bundles, and perform a migration.

Global Variable

# NSInferMappingModelAutomaticallyOption

Key to attempt to create the mapping model automatically.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSInferMappingModelAutomaticallyOption: String

## Discussion

The corresponding value is an `NSNumber` object. If the `boolValue` of the
number is `true` and the value of the
`NSMigratePersistentStoresAutomaticallyOption` is `true`, the coordinator will
attempt to infer a mapping model if none can be found.

