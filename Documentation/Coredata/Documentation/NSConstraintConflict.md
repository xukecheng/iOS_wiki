Initializer

# init(constraint:database:databaseSnapshot:conflicting:conflictingSnapshots:)

Initializes a constraint conflict.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        constraint contraint: [String],
        database databaseObject: NSManagedObject?,
        databaseSnapshot: [AnyHashable : Any]?,
        conflicting conflictingObjects: [NSManagedObject],
        conflictingSnapshots: [Any]
    )

Instance Property

# conflictingObjects

The managed objects that are in conflict.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var conflictingObjects: [NSManagedObject] { get }

## See Also

### Inspecting a Conflict

`var conflictingSnapshots: [[AnyHashable : Any]]`

The original property values of objects in violation of the constraint.

`var constraint: [String]`

The constraint that has been violated.

`var constraintValues: [String : Any]`

The values that the conflicting objects had when the conflict was created.

`var databaseObject: NSManagedObject?`

The object whose database row is using constraint values.

`var databaseSnapshot: [String : Any]?`

The values currently stored in the database.

Instance Property

# conflictingSnapshots

The original property values of objects in violation of the constraint.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var conflictingSnapshots: [[AnyHashable : Any]] { get }

## See Also

### Inspecting a Conflict

`var conflictingObjects: [NSManagedObject]`

The managed objects that are in conflict.

`var constraint: [String]`

The constraint that has been violated.

`var constraintValues: [String : Any]`

The values that the conflicting objects had when the conflict was created.

`var databaseObject: NSManagedObject?`

The object whose database row is using constraint values.

`var databaseSnapshot: [String : Any]?`

The values currently stored in the database.

Instance Property

# constraint

The constraint that has been violated.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var constraint: [String] { get }

## See Also

### Inspecting a Conflict

`var conflictingObjects: [NSManagedObject]`

The managed objects that are in conflict.

`var conflictingSnapshots: [[AnyHashable : Any]]`

The original property values of objects in violation of the constraint.

`var constraintValues: [String : Any]`

The values that the conflicting objects had when the conflict was created.

`var databaseObject: NSManagedObject?`

The object whose database row is using constraint values.

`var databaseSnapshot: [String : Any]?`

The values currently stored in the database.

Instance Property

# constraintValues

The values that the conflicting objects had when the conflict was created.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var constraintValues: [String : Any] { get }

## See Also

### Inspecting a Conflict

`var conflictingObjects: [NSManagedObject]`

The managed objects that are in conflict.

`var conflictingSnapshots: [[AnyHashable : Any]]`

The original property values of objects in violation of the constraint.

`var constraint: [String]`

The constraint that has been violated.

`var databaseObject: NSManagedObject?`

The object whose database row is using constraint values.

`var databaseSnapshot: [String : Any]?`

The values currently stored in the database.

Instance Property

# databaseObject

The object whose database row is using constraint values.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var databaseObject: NSManagedObject? { get }

## See Also

### Inspecting a Conflict

`var conflictingObjects: [NSManagedObject]`

The managed objects that are in conflict.

`var conflictingSnapshots: [[AnyHashable : Any]]`

The original property values of objects in violation of the constraint.

`var constraint: [String]`

The constraint that has been violated.

`var constraintValues: [String : Any]`

The values that the conflicting objects had when the conflict was created.

`var databaseSnapshot: [String : Any]?`

The values currently stored in the database.

Instance Property

# databaseSnapshot

The values currently stored in the database.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var databaseSnapshot: [String : Any]? { get }

## See Also

### Inspecting a Conflict

`var conflictingObjects: [NSManagedObject]`

The managed objects that are in conflict.

`var conflictingSnapshots: [[AnyHashable : Any]]`

The original property values of objects in violation of the constraint.

`var constraint: [String]`

The constraint that has been violated.

`var constraintValues: [String : Any]`

The values that the conflicting objects had when the conflict was created.

`var databaseObject: NSManagedObject?`

The object whose database row is using constraint values.

