Initializer

# init(merge:)

Returns a merge policy initialized with a given policy type.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(merge ty: NSMergePolicyType)

##  Parameters

`ty`

    

A merge policy type.

## Return Value

A merge policy initialized with a given policy type.

## Discussion

If you override this method in a subclass, you should invoke the superclass’s
implementation with the merge policy that is closest to the behavior you want.

  * This will make it easier to use the superclass’s implementation of `resolve(mergeConflicts:)` and then customize the results.

  * Due to the complexity of merging to-many relationships, this class is designed with the expectation that you call super as the base implementation.

## See Also

### Getting a Merge Policy

`var mergeType: NSMergePolicyType`

The merge type.

### Related Documentation

Core Data Model Versioning and Data Migration Programming Guide

Instance Property

# mergeType

The merge type.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var mergeType: NSMergePolicyType { get }

## See Also

### Getting a Merge Policy

`init(merge: NSMergePolicyType)`

Returns a merge policy initialized with a given policy type.

Instance Method

# resolve(mergeConflicts:)

Resolves the conflicts in a given list.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func resolve(mergeConflicts list: [Any]) throws

##  Parameters

`list`

    

An array of merge conflicts (instances of `NSMergeConflict`).

`error`

    

If an error occurs, upon return contains an `NSError` object that describes
the problem.

## Return Value

`true` if the conflicts were resolved successfully, otherwise `false`.

## Discussion

If you override this method in a subclass, you should typically invoke the
superclass’s implementation in addition to performing your own operations.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Resolving a Conflict

`func resolve(constraintConflicts: [NSConstraintConflict])`

Resolves the conflicts in a given list.

`func resolve(optimisticLockingConflicts: [NSMergeConflict])`

Resolves the conflicts in a given list.

Instance Method

# resolve(constraintConflicts:)

Resolves the conflicts in a given list.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func resolve(constraintConflicts list: [NSConstraintConflict]) throws

## See Also

### Resolving a Conflict

`func resolve(mergeConflicts: [Any])`

Resolves the conflicts in a given list.

`func resolve(optimisticLockingConflicts: [NSMergeConflict])`

Resolves the conflicts in a given list.

Instance Method

# resolve(optimisticLockingConflicts:)

Resolves the conflicts in a given list.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func resolve(optimisticLockingConflicts list: [NSMergeConflict]) throws

## See Also

### Resolving a Conflict

`func resolve(mergeConflicts: [Any])`

Resolves the conflicts in a given list.

`func resolve(constraintConflicts: [NSConstraintConflict])`

Resolves the conflicts in a given list.

Type Property

# error

The default merge policy for all managed object contexts.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class var error: NSMergePolicy { get }

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those
objects in error’s `userInfo` dictionary. Use the `NSInsertedObjectsKey` and
`NSUpdatedObjectsKey` keys to extract the object IDs.

## See Also

### Defining Merge Policies

`class var mergeByPropertyStoreTrump: NSMergePolicy`

A property-based merge policy that applies external changes.

`class var mergeByPropertyObjectTrump: NSMergePolicy`

A property-based merge policy that applies in-memory changes.

`class var overwrite: NSMergePolicy`

A merge policy that overwrites the entire stored object.

`class var rollback: NSMergePolicy`

A merge policy that discards unsaved changes.

API Reference

Merge Policies

Define standard ways to handle conflicts during a save operation.

Type Property

# mergeByPropertyStoreTrump

A property-based merge policy that applies external changes.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class var mergeByPropertyStoreTrump: NSMergePolicy { get }

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with external
changes trumping in-memory changes.

## See Also

### Defining Merge Policies

`class var error: NSMergePolicy`

The default merge policy for all managed object contexts.

`class var mergeByPropertyObjectTrump: NSMergePolicy`

A property-based merge policy that applies in-memory changes.

`class var overwrite: NSMergePolicy`

A merge policy that overwrites the entire stored object.

`class var rollback: NSMergePolicy`

A merge policy that discards unsaved changes.

API Reference

Merge Policies

Define standard ways to handle conflicts during a save operation.

Type Property

# mergeByPropertyObjectTrump

A property-based merge policy that applies in-memory changes.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class var mergeByPropertyObjectTrump: NSMergePolicy { get }

## Discussion

A policy that merges conflicts between the persistent store’s version of the
object and the current in-memory version by individual property, with in-
memory changes trumping external changes.

## See Also

### Defining Merge Policies

`class var error: NSMergePolicy`

The default merge policy for all managed object contexts.

`class var mergeByPropertyStoreTrump: NSMergePolicy`

A property-based merge policy that applies external changes.

`class var overwrite: NSMergePolicy`

A merge policy that overwrites the entire stored object.

`class var rollback: NSMergePolicy`

A merge policy that discards unsaved changes.

API Reference

Merge Policies

Define standard ways to handle conflicts during a save operation.

Type Property

# overwrite

A merge policy that overwrites the entire stored object.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class var overwrite: NSMergePolicy { get }

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by saving the entire in-memory object
to the persistent store.

## See Also

### Defining Merge Policies

`class var error: NSMergePolicy`

The default merge policy for all managed object contexts.

`class var mergeByPropertyStoreTrump: NSMergePolicy`

A property-based merge policy that applies external changes.

`class var mergeByPropertyObjectTrump: NSMergePolicy`

A property-based merge policy that applies in-memory changes.

`class var rollback: NSMergePolicy`

A merge policy that discards unsaved changes.

API Reference

Merge Policies

Define standard ways to handle conflicts during a save operation.

Type Property

# rollback

A merge policy that discards unsaved changes.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class var rollback: NSMergePolicy { get }

## Discussion

This policy merges conflicts between the persistent store’s version of the
object and the current in-memory version by discarding unsaved changes.

## See Also

### Defining Merge Policies

`class var error: NSMergePolicy`

The default merge policy for all managed object contexts.

`class var mergeByPropertyStoreTrump: NSMergePolicy`

A property-based merge policy that applies external changes.

`class var mergeByPropertyObjectTrump: NSMergePolicy`

A property-based merge policy that applies in-memory changes.

`class var overwrite: NSMergePolicy`

A merge policy that overwrites the entire stored object.

API Reference

Merge Policies

Define standard ways to handle conflicts during a save operation.

