Enumeration Case

# NSManagedObjectContext.ScheduledTaskType.enqueued

The enqueued scheduled task type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case enqueued

## Discussion

Enqueued tasks execute asynchronously on the context’s queue. An enqueued task
encapsulates an autorelease pool and a call to `processPendingChanges()`, and
its behavior is analogous to `perform(_:)`. The context’s queue executes tasks
in the order you add them.

## See Also

### Scheduled Task Types

`case immediate`

The immediate scheduled task type.

Enumeration Case

# NSManagedObjectContext.ScheduledTaskType.immediate

The immediate scheduled task type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case immediate

## Discussion

Immediate tasks execute right away if the context operates within the current
scope; otherwise, the context enqueues the task. Tasks of this type are
reentrant, nonblocking, and continuation-aware.

## See Also

### Scheduled Task Types

`case enqueued`

The enqueued scheduled task type.

Instance Property

# hashValue

The scheduled task type’s computed hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Hashing a Scheduled Task Type

`func hash(into: inout Hasher)`

Hashes the components of the scheduled task type using the provided hasher.

Instance Method

# hash(into:)

Hashes the components of the scheduled task type using the provided hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining components of this scheduled task type.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Hashing a Scheduled Task Type

`var hashValue: Int`

The scheduled task type’s computed hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two scheduled task types are
equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: NSManagedObjectContext.ScheduledTaskType, b: NSManagedObjectContext.ScheduledTaskType) -> Bool

##  Parameters

`a`

    

A scheduled task type to compare.

`b`

    

Another scheduled task type to compare.

## See Also

### Comparing Scheduled Task Types

`static func != (NSManagedObjectContext.ScheduledTaskType,
NSManagedObjectContext.ScheduledTaskType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: NSManagedObjectContext.ScheduledTaskType, rhs: NSManagedObjectContext.ScheduledTaskType) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing Scheduled Task Types

`static func == (NSManagedObjectContext.ScheduledTaskType,
NSManagedObjectContext.ScheduledTaskType) -> Bool`

Returns a Boolean value that indicates whether two scheduled task types are
equal.

