Type Property

# fetchRequest

A fetch request that has the persistent history change as the entity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get }

## See Also

### Inspecting Change Metadata

`class var entityDescription: NSEntityDescription?`

The entity description of the persistent history change entity.

`class func entityDescription(with: NSManagedObjectContext) ->
NSEntityDescription?`

Requests an entity description for the managed object type affected by the
change using the provided context.

Type Property

# entityDescription

The entity description of the persistent history change entity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class var entityDescription: NSEntityDescription? { get }

## Discussion

The entity description of a `NSPersistentHistoryChange`, includes its
properties, which can be useful for filtering your persistent history change
request.

## See Also

### Inspecting Change Metadata

`class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?`

A fetch request that has the persistent history change as the entity.

`class func entityDescription(with: NSManagedObjectContext) ->
NSEntityDescription?`

Requests an entity description for the managed object type affected by the
change using the provided context.

Type Method

# entityDescription(with:)

Requests an entity description for the managed object type affected by the
change using the provided context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class func entityDescription(with context: NSManagedObjectContext) -> NSEntityDescription?

##  Parameters

`context`

    

The managed object context for this request.

## Return Value

The entity description (`NSEntityDescription`) of the persistent history
transaction entity.

## See Also

### Inspecting Change Metadata

`class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?`

A fetch request that has the persistent history change as the entity.

`class var entityDescription: NSEntityDescription?`

The entity description of the persistent history change entity.

Instance Property

# changeID

The change’s numeric identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var changeID: Int64 { get }

## See Also

### Inspecting Change Details

`var changeType: NSPersistentHistoryChangeType`

The type of change to the managed object in the persistent store.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var changedObjectID: NSManagedObjectID`

The identifier of the managed object that changed.

`var tombstone: [AnyHashable : Any]?`

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

`var transaction: NSPersistentHistoryTransaction?`

The persistent history transaction containing this change.

`var updatedProperties: Set<NSPropertyDescription>?`

The set of properties that were updated on the managed object.

Instance Property

# changeType

The type of change to the managed object in the persistent store.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var changeType: NSPersistentHistoryChangeType { get }

## See Also

### Inspecting Change Details

`var changeID: Int64`

The change’s numeric identifier.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var changedObjectID: NSManagedObjectID`

The identifier of the managed object that changed.

`var tombstone: [AnyHashable : Any]?`

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

`var transaction: NSPersistentHistoryTransaction?`

The persistent history transaction containing this change.

`var updatedProperties: Set<NSPropertyDescription>?`

The set of properties that were updated on the managed object.

Instance Property

# changedObjectID

The identifier of the managed object that changed.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    @NSCopying
    var changedObjectID: NSManagedObjectID { get }

## See Also

### Inspecting Change Details

`var changeID: Int64`

The change’s numeric identifier.

`var changeType: NSPersistentHistoryChangeType`

The type of change to the managed object in the persistent store.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var tombstone: [AnyHashable : Any]?`

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

`var transaction: NSPersistentHistoryTransaction?`

The persistent history transaction containing this change.

`var updatedProperties: Set<NSPropertyDescription>?`

The set of properties that were updated on the managed object.

Instance Property

# tombstone

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var tombstone: [AnyHashable : Any]? { get }

## Discussion

This value is expected on changes of type
`NSPersistentHistoryChangeType.delete`.

## See Also

### Inspecting Change Details

`var changeID: Int64`

The change’s numeric identifier.

`var changeType: NSPersistentHistoryChangeType`

The type of change to the managed object in the persistent store.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var changedObjectID: NSManagedObjectID`

The identifier of the managed object that changed.

`var transaction: NSPersistentHistoryTransaction?`

The persistent history transaction containing this change.

`var updatedProperties: Set<NSPropertyDescription>?`

The set of properties that were updated on the managed object.

Instance Property

# transaction

The persistent history transaction containing this change.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var transaction: NSPersistentHistoryTransaction? { get }

## See Also

### Inspecting Change Details

`var changeID: Int64`

The change’s numeric identifier.

`var changeType: NSPersistentHistoryChangeType`

The type of change to the managed object in the persistent store.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var changedObjectID: NSManagedObjectID`

The identifier of the managed object that changed.

`var tombstone: [AnyHashable : Any]?`

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

`var updatedProperties: Set<NSPropertyDescription>?`

The set of properties that were updated on the managed object.

Instance Property

# updatedProperties

The set of properties that were updated on the managed object.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var updatedProperties: Set<NSPropertyDescription>? { get }

## Discussion

This value is expected on changes of type
`NSPersistentHistoryChangeType.update`.

## See Also

### Inspecting Change Details

`var changeID: Int64`

The change’s numeric identifier.

`var changeType: NSPersistentHistoryChangeType`

The type of change to the managed object in the persistent store.

`enum NSPersistentHistoryChangeType`

The types of changes to managed objects reflected in persistent history.

`var changedObjectID: NSManagedObjectID`

The identifier of the managed object that changed.

`var tombstone: [AnyHashable : Any]?`

A dictionary of attributes marked for preservation after deletion, and their
values when deleted.

`var transaction: NSPersistentHistoryTransaction?`

The persistent history transaction containing this change.

