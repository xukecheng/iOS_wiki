Initializer

# init(source:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:)

Initializes a merge conflict.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        source srcObject: NSManagedObject,
        newVersion newvers: Int,
        oldVersion oldvers: Int,
        cachedSnapshot cachesnap: [String : Any]?,
        persistedSnapshot persnap: [String : Any]?
    )

##  Parameters

`srcObject`

    

The source object for the conflict.

`newvers`

    

The new version number for the change.

A value of 0 means the object was deleted and the corresponding snapshot is
`nil`.

`oldvers`

    

The old version number for the change.

`cachesnap`

    

A dictionary containing the values of `srcObject` held in the persistent store
coordinator layer.

`persnap`

    

A dictionary containing the values of `srcObject` held in the persistent
store.

## Return Value

A merge conflict object initialized with the given parameters.

## See Also

### Related Documentation

Core Data Model Versioning and Data Migration Programming Guide

Instance Property

# sourceObject

The source object for the conflict.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceObject: NSManagedObject { get }

## See Also

### Accessing Merge Conflict Details

`var objectSnapshot: [String : Any]?`

A dictionary containing the values of the source object.

`var cachedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

`var persistedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store.

`var newVersionNumber: Int`

The new version number for the change.

`var oldVersionNumber: Int`

The old version number for the change.

Instance Property

# objectSnapshot

A dictionary containing the values of the source object.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var objectSnapshot: [String : Any]? { get }

## See Also

### Accessing Merge Conflict Details

`var sourceObject: NSManagedObject`

The source object for the conflict.

`var cachedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

`var persistedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store.

`var newVersionNumber: Int`

The new version number for the change.

`var oldVersionNumber: Int`

The old version number for the change.

Instance Property

# cachedSnapshot

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var cachedSnapshot: [String : Any]? { get }

## See Also

### Accessing Merge Conflict Details

`var sourceObject: NSManagedObject`

The source object for the conflict.

`var objectSnapshot: [String : Any]?`

A dictionary containing the values of the source object.

`var persistedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store.

`var newVersionNumber: Int`

The new version number for the change.

`var oldVersionNumber: Int`

The old version number for the change.

Instance Property

# persistedSnapshot

A dictionary containing the values of the source object held in the persistent
store.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var persistedSnapshot: [String : Any]? { get }

## See Also

### Accessing Merge Conflict Details

`var sourceObject: NSManagedObject`

The source object for the conflict.

`var objectSnapshot: [String : Any]?`

A dictionary containing the values of the source object.

`var cachedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

`var newVersionNumber: Int`

The new version number for the change.

`var oldVersionNumber: Int`

The old version number for the change.

Instance Property

# newVersionNumber

The new version number for the change.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var newVersionNumber: Int { get }

## Discussion

A new version number of 0 means the object was deleted and the corresponding
snapshot is `nil`.

## See Also

### Accessing Merge Conflict Details

`var sourceObject: NSManagedObject`

The source object for the conflict.

`var objectSnapshot: [String : Any]?`

A dictionary containing the values of the source object.

`var cachedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

`var persistedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store.

`var oldVersionNumber: Int`

The old version number for the change.

Instance Property

# oldVersionNumber

The old version number for the change.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var oldVersionNumber: Int { get }

## See Also

### Accessing Merge Conflict Details

`var sourceObject: NSManagedObject`

The source object for the conflict.

`var objectSnapshot: [String : Any]?`

A dictionary containing the values of the source object.

`var cachedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store coordinator layer.

`var persistedSnapshot: [String : Any]?`

A dictionary containing the values of the source object held in the persistent
store.

`var newVersionNumber: Int`

The new version number for the change.

