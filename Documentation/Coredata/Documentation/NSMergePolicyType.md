Enumeration Case

# NSMergePolicyType.errorMergePolicyType

The default merge policy for all managed object contexts.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case errorMergePolicyType = 0

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those
objects in error’s `userInfo` dictionary. Use the `NSInsertedObjectsKey` and
`NSUpdatedObjectsKey` keys to extract the object IDs.

## See Also

### Policies

`case mergeByPropertyStoreTrumpMergePolicyType`

A property-based merge policy that applies external changes.

`case mergeByPropertyObjectTrumpMergePolicyType`

A property-based merge policy that applies in-memory changes.

`case overwriteMergePolicyType`

A merge policy type that overwrites the entire stored object.

`case rollbackMergePolicyType`

A merge policy that discards unsaved changes.

Enumeration Case

# NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType

A property-based merge policy that applies external changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case mergeByPropertyStoreTrumpMergePolicyType = 1

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with external
changes trumping in-memory changes.

## See Also

### Policies

`case errorMergePolicyType`

The default merge policy for all managed object contexts.

`case mergeByPropertyObjectTrumpMergePolicyType`

A property-based merge policy that applies in-memory changes.

`case overwriteMergePolicyType`

A merge policy type that overwrites the entire stored object.

`case rollbackMergePolicyType`

A merge policy that discards unsaved changes.

Enumeration Case

# NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType

A property-based merge policy that applies in-memory changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case mergeByPropertyObjectTrumpMergePolicyType = 2

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with in-
memory changes trumping external changes.

## See Also

### Policies

`case errorMergePolicyType`

The default merge policy for all managed object contexts.

`case mergeByPropertyStoreTrumpMergePolicyType`

A property-based merge policy that applies external changes.

`case overwriteMergePolicyType`

A merge policy type that overwrites the entire stored object.

`case rollbackMergePolicyType`

A merge policy that discards unsaved changes.

Enumeration Case

# NSMergePolicyType.overwriteMergePolicyType

A merge policy type that overwrites the entire stored object.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case overwriteMergePolicyType = 3

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by saving the entire in-memory object
to the persistent store.

## See Also

### Policies

`case errorMergePolicyType`

The default merge policy for all managed object contexts.

`case mergeByPropertyStoreTrumpMergePolicyType`

A property-based merge policy that applies external changes.

`case mergeByPropertyObjectTrumpMergePolicyType`

A property-based merge policy that applies in-memory changes.

`case rollbackMergePolicyType`

A merge policy that discards unsaved changes.

Enumeration Case

# NSMergePolicyType.rollbackMergePolicyType

A merge policy that discards unsaved changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case rollbackMergePolicyType = 4

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by discarding unsaved changes.

## See Also

### Policies

`case errorMergePolicyType`

The default merge policy for all managed object contexts.

`case mergeByPropertyStoreTrumpMergePolicyType`

A property-based merge policy that applies external changes.

`case mergeByPropertyObjectTrumpMergePolicyType`

A property-based merge policy that applies in-memory changes.

`case overwriteMergePolicyType`

A merge policy type that overwrites the entire stored object.

