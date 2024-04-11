Global Variable

# NSStoreModelVersionHashesKey

Key to represent the version hash information for the model used to create the
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSStoreModelVersionHashesKey: String

## Discussion

This key is used in the metadata for a persistent store.

Global Variable

# NSStoreModelVersionIdentifiersKey

Key to represent the version identifiers for the model used to create the
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSStoreModelVersionIdentifiersKey: String

## Discussion

If you add your own annotations to a model’s version identifier (see
`versionIdentifiers`), they are stored in the persistent store’s metadata. You
can use this key to retrieve the identifiers from the metadata dictionaries
available from `NSPersistentStore` (`metadata`) and
`NSPersistentStoreCoordinator` (`metadata(for:)` and related methods). The
corresponding value is a Foundation collection (an `NSArray` or `NSSet`
object).

Global Variable

# NSPersistentStoreOSCompatibility

Key to represent the earliest version of the operation system that the
persistent store supports.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSPersistentStoreOSCompatibility: String

## Discussion

The corresponding value is an `NSNumber` object that takes the form of the
constants defined by the availability macros defined in
`/usr/include/AvailabilityMacros.h`; for example `1040` represents OS X
version 10.4.0.

Backward compatibility may preclude some features.

