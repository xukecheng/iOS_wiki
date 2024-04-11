Global Variable

# NSErrorMergePolicy

The default merge policy for all managed object contexts.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSErrorMergePolicy: AnyObject

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those
objects in error’s `userInfo` dictionary. Use the `NSInsertedObjectsKey` and
`NSUpdatedObjectsKey` keys to extract the object IDs.

## See Also

### Policies

`var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject`

A property-based merge policy that applies external changes.

`var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject`

A property-based merge policy that applies in-memory changes.

`var NSOverwriteMergePolicy: AnyObject`

A merge policy that overwrites the entire stored object.

`var NSRollbackMergePolicy: AnyObject`

A merge policy that discards unsaved changes.

`enum NSMergePolicyType`

Constants that define merge policy types.

Global Variable

# NSMergeByPropertyStoreTrumpMergePolicy

A property-based merge policy that applies external changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with external
changes trumping in-memory changes.

## See Also

### Policies

`var NSErrorMergePolicy: AnyObject`

The default merge policy for all managed object contexts.

`var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject`

A property-based merge policy that applies in-memory changes.

`var NSOverwriteMergePolicy: AnyObject`

A merge policy that overwrites the entire stored object.

`var NSRollbackMergePolicy: AnyObject`

A merge policy that discards unsaved changes.

`enum NSMergePolicyType`

Constants that define merge policy types.

Global Variable

# NSMergeByPropertyObjectTrumpMergePolicy

A property-based merge policy that applies in-memory changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with in-
memory changes trumping external changes.

## See Also

### Policies

`var NSErrorMergePolicy: AnyObject`

The default merge policy for all managed object contexts.

`var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject`

A property-based merge policy that applies external changes.

`var NSOverwriteMergePolicy: AnyObject`

A merge policy that overwrites the entire stored object.

`var NSRollbackMergePolicy: AnyObject`

A merge policy that discards unsaved changes.

`enum NSMergePolicyType`

Constants that define merge policy types.

Global Variable

# NSOverwriteMergePolicy

A merge policy that overwrites the entire stored object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSOverwriteMergePolicy: AnyObject

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by saving the entire in-memory object
to the persistent store.

## See Also

### Policies

`var NSErrorMergePolicy: AnyObject`

The default merge policy for all managed object contexts.

`var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject`

A property-based merge policy that applies external changes.

`var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject`

A property-based merge policy that applies in-memory changes.

`var NSRollbackMergePolicy: AnyObject`

A merge policy that discards unsaved changes.

`enum NSMergePolicyType`

Constants that define merge policy types.

Global Variable

# NSRollbackMergePolicy

A merge policy that discards unsaved changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSRollbackMergePolicy: AnyObject

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by discarding unsaved changes.

## See Also

### Policies

`var NSErrorMergePolicy: AnyObject`

The default merge policy for all managed object contexts.

`var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject`

A property-based merge policy that applies external changes.

`var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject`

A property-based merge policy that applies in-memory changes.

`var NSOverwriteMergePolicy: AnyObject`

A merge policy that overwrites the entire stored object.

`enum NSMergePolicyType`

Constants that define merge policy types.

