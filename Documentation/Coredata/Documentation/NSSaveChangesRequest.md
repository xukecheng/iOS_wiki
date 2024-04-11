Initializer

# init(inserted:updated:deleted:locked:)

Initializes a save changes request with collections of given changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        inserted insertedObjects: Set<NSManagedObject>?,
        updated updatedObjects: Set<NSManagedObject>?,
        deleted deletedObjects: Set<NSManagedObject>?,
        locked lockedObjects: Set<NSManagedObject>?
    )

##  Parameters

`insertedObjects`

    

Objects that were inserted into the calling context.

`updatedObjects`

    

Objects that were updated in the calling context.

`deletedObjects`

    

Objects that were deleted in the calling context.

`lockedObjects`

    

Objects that were flagged for optimistic locking on the calling context.

## Return Value

A save changes request initialized with the given changes.

Instance Property

# insertedObjects

The objects that were inserted into the calling context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var insertedObjects: Set<NSManagedObject>? { get }

## See Also

### Getting Information about a Request

`var updatedObjects: Set<NSManagedObject>?`

The objects that were modified in the calling context.

`var deletedObjects: Set<NSManagedObject>?`

The objects that were deleted in the calling context.

`var lockedObjects: Set<NSManagedObject>?`

The objects that were flagged for optimistic locking on the calling context.

Instance Property

# updatedObjects

The objects that were modified in the calling context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var updatedObjects: Set<NSManagedObject>? { get }

## See Also

### Getting Information about a Request

`var insertedObjects: Set<NSManagedObject>?`

The objects that were inserted into the calling context.

`var deletedObjects: Set<NSManagedObject>?`

The objects that were deleted in the calling context.

`var lockedObjects: Set<NSManagedObject>?`

The objects that were flagged for optimistic locking on the calling context.

Instance Property

# deletedObjects

The objects that were deleted in the calling context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var deletedObjects: Set<NSManagedObject>? { get }

## See Also

### Getting Information about a Request

`var insertedObjects: Set<NSManagedObject>?`

The objects that were inserted into the calling context.

`var updatedObjects: Set<NSManagedObject>?`

The objects that were modified in the calling context.

`var lockedObjects: Set<NSManagedObject>?`

The objects that were flagged for optimistic locking on the calling context.

Instance Property

# lockedObjects

The objects that were flagged for optimistic locking on the calling context.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var lockedObjects: Set<NSManagedObject>? { get }

## Discussion

Objects are flagged for optimistic locking with `detectConflicts(for:)`.

## See Also

### Getting Information about a Request

`var insertedObjects: Set<NSManagedObject>?`

The objects that were inserted into the calling context.

`var updatedObjects: Set<NSManagedObject>?`

The objects that were modified in the calling context.

`var deletedObjects: Set<NSManagedObject>?`

The objects that were deleted in the calling context.

