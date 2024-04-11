Global Variable

# NSAddedPersistentStoresKey

Key for the array of stores that were added.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSAddedPersistentStoresKey: String

Global Variable

# NSRemovedPersistentStoresKey

Key for the array of stores that were removed.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSRemovedPersistentStoresKey: String

Global Variable

# NSUUIDChangedPersistentStoresKey

Key for an array containing the old and new stores.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSUUIDChangedPersistentStoresKey: String

## Discussion

The object at index `0` is the old store instance, and the object at index `1`
the new. When migration happens, the array contains a third object (at index
`2`) that is an array containing the new objectIDs for all the migrated
objects.

Global Variable

# NSPersistentStoreConnectionPoolMaxSizeKey

The maximum connection pool size to use on a store that supports concurrent
request handling.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    let NSPersistentStoreConnectionPoolMaxSizeKey: String

## Discussion

Values that you specify for this key are of type `NSNumber`. The connection
pool size determines the number of requests a store can handle concurrently,
and is a function of how many contexts attempt to access store data at any
time. Generally, you don’t set this, and use the default value instead.

The default connection pool size is implementation-dependent and may vary by
store type or platform.

Global Variable

# NSPersistentStoreSaveConflictsErrorKey

The key for the array of merge conflict objects (instances of
`NSMergeConflict`).

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSPersistentStoreSaveConflictsErrorKey: String

Global Variable

# NSPersistentStoreUbiquitousTransitionTypeKey

In the `NSPersistentStoreCoordinatorStoresWillChange` and
`NSPersistentStoreCoordinatorStoresDidChange` userInfo dictionaries, this
identifies the type of event. The corresponding value is one of the
`NSPersistentStoreUbiquitousTransitionType` enum values as an `NSNumber`
object.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreUbiquitousTransitionTypeKey: String

