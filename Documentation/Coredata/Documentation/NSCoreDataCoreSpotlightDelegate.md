Initializer

# init(forStoreWith:coordinator:)

Creates a Core Spotlight delegate with the specified store description and
coordinator.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    init(
        forStoreWith description: NSPersistentStoreDescription,
        coordinator psc: NSPersistentStoreCoordinator
    )

##  Parameters

`description`

    

An object that describes the persistent store that contains the entities to
index.

`psc`

    

The persistent store coordinator, which you initialize with the managed object
model that contains the definitions of the entities to index.

## Discussion

After you initialize a Core Spotlight delegate, call the
`startSpotlightIndexing()` to begin indexing your store’s contents.

Note

If you initialize your Core Spotlight delegate using this method, you don’t
need to set the `NSCoreDataCoreSpotlightExporter` option on the specified
store description.

## See Also

### Creating a Core Spotlight Delegate

`init(forStoreWith: NSPersistentStoreDescription, model:
NSManagedObjectModel)`

Creates a Core Spotlight delegate with the specified store description and
managed object model.

Deprecated

Initializer

# init(forStoreWith:model:)

Creates a Core Spotlight delegate with the specified store description and
managed object model.

iOS 11.0–15.0  Deprecated  iPadOS 11.0–15.0  Deprecated  macOS 10.13–12.0
Deprecated  Mac Catalyst 13.1–15.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    convenience init(
        forStoreWith description: NSPersistentStoreDescription,
        model: NSManagedObjectModel
    )

Deprecated

Use `init(forStoreWith:coordinator:)` instead.

##  Parameters

`description`

    

An object that describes the persistent store that contains the entities to
index.

`model`

    

The managed object model that contains the definitions of the entities to
index.

## See Also

### Creating a Core Spotlight Delegate

`init(forStoreWith: NSPersistentStoreDescription, coordinator:
NSPersistentStoreCoordinator)`

Creates a Core Spotlight delegate with the specified store description and
coordinator.

Instance Property

# isIndexingEnabled

A Boolean value that indicates whether Core Data is currently updating the
Core Spotlight index with the persistent store’s entities.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var isIndexingEnabled: Bool { get }

## See Also

### Configuring the Index

`func domainIdentifier() -> String`

Returns the domain identifier.

`func indexName() -> String?`

Returns the index’s name.

Instance Method

# domainIdentifier()

Returns the domain identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func domainIdentifier() -> String

## Discussion

The default value is the persistent store’s identifier.

## See Also

### Configuring the Index

`var isIndexingEnabled: Bool`

A Boolean value that indicates whether Core Data is currently updating the
Core Spotlight index with the persistent store’s entities.

`func indexName() -> String?`

Returns the index’s name.

Instance Method

# indexName()

Returns the index’s name.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func indexName() -> String?

## Discussion

The default value is `nil`.

## See Also

### Configuring the Index

`var isIndexingEnabled: Bool`

A Boolean value that indicates whether Core Data is currently updating the
Core Spotlight index with the persistent store’s entities.

`func domainIdentifier() -> String`

Returns the domain identifier.

Instance Method

# attributeSet(for:)

Returns the searchable attributes for the specified managed object.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func attributeSet(for object: NSManagedObject) -> CSSearchableItemAttributeSet?

##  Parameters

`object`

    

The managed object to index.

## Return Value

An instance of `CSSearchableItemAttributeSet` that provides the searchable
item’s attributes.

## Discussion

Important

If you enable `isIndexedBySpotlight` on a property description that describes
a relationship, override this method and return the necessary set of
attributes. Core Data doesn’t automatically infer indexable information for
relationships.

To prevent Core Spotlight from indexing a specific managed object, override
this method and return `nil` for that object.

## See Also

### Managing the Index

`func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)`

Deletes all searchable items from the configured index.

`func startSpotlightIndexing()`

Starts the indexing of the store’s entities.

`func stopSpotlightIndexing()`

Stops the indexing of the store’s entities.

Instance Method

# deleteSpotlightIndex(completionHandler:)

Deletes all searchable items from the configured index.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func deleteSpotlightIndex(completionHandler: @escaping ((any Error)?) -> Void)

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

The closure returns no value and takes only a single parameter, which is an
error object that contains information about issues preventing the deletion of
searchable items, or `nil` if Core Spotlight successfully deletes all
searchable items.

Depending on the cause of the issue, an error can originate from Core Data or
from Core Spotlight. Make sure your app can handle both scenarios.

Note

You must call `stopSpotlightIndexing()` before you call this method;
otherwise, Core Data immediately recreates the index.

## See Also

### Managing the Index

`func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?`

Returns the searchable attributes for the specified managed object.

`func startSpotlightIndexing()`

Starts the indexing of the store’s entities.

`func stopSpotlightIndexing()`

Stops the indexing of the store’s entities.

Instance Method

# startSpotlightIndexing()

Starts the indexing of the store’s entities.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func startSpotlightIndexing()

## Discussion

After you call this method, the delegate posts a notification whenever the
index changes. The type of notification is `indexDidUpdateNotification`, and
its `userInfo` dictionary contains the keys `NSStoreUUIDKey` and
`NSPersistentHistoryTokenKey`.

## See Also

### Managing the Index

`func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?`

Returns the searchable attributes for the specified managed object.

`func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)`

Deletes all searchable items from the configured index.

`func stopSpotlightIndexing()`

Stops the indexing of the store’s entities.

Instance Method

# stopSpotlightIndexing()

Stops the indexing of the store’s entities.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func stopSpotlightIndexing()

## Discussion

After you call this method, the delegate no longer posts notifications about
index changes.

## See Also

### Managing the Index

`func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?`

Returns the searchable attributes for the specified managed object.

`func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)`

Deletes all searchable items from the configured index.

`func startSpotlightIndexing()`

Starts the indexing of the store’s entities.

Type Property

# indexDidUpdateNotification

The notification the delegate posts after Spotlight updates the index.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+  Xcode
13.0+

    
    
    static let indexDidUpdateNotification: Notification.Name

## Discussion

The notification’s `userInfo` dictionary contains the keys `NSStoreUUIDKey`
and `NSPersistentHistoryTokenKey`.

## See Also

### Updating the Index

`func searchableIndex(CSSearchableIndex,
reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)`

Reindexes all searchable items and clears any local state.

`func searchableIndex(CSSearchableIndex,
reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () ->
Void)`

Reindexes the searchable items for the specified identifiers.

Instance Method

# searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)

Reindexes all searchable items and clears any local state.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func searchableIndex(
        _ searchableIndex: CSSearchableIndex,
        reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Void
    )

##  Parameters

`searchableIndex`

    

The index that requires reindexing.

`acknowledgementHandler`

    

The handler to call when you finish saving client state information.

## Discussion

For more information, see
`searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)`.

## See Also

### Updating the Index

`static let indexDidUpdateNotification: Notification.Name`

The notification the delegate posts after Spotlight updates the index.

`func searchableIndex(CSSearchableIndex,
reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () ->
Void)`

Reindexes the searchable items for the specified identifiers.

Instance Method

#
searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)

Reindexes the searchable items for the specified identifiers.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  visionOS 1.0+

    
    
    func searchableIndex(
        _ searchableIndex: CSSearchableIndex,
        reindexSearchableItemsWithIdentifiers identifiers: [String],
        acknowledgementHandler: @escaping () -> Void
    )

##  Parameters

`searchableIndex`

    

The index that contains the items that require reindexing.

`identifiers`

    

An array of strings that identify the searchable items.

`acknowledgementHandler`

    

The handler to call when you finish saving client state information.

## Discussion

For more information, see
`searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)`.

## See Also

### Updating the Index

`static let indexDidUpdateNotification: Notification.Name`

The notification the delegate posts after Spotlight updates the index.

`func searchableIndex(CSSearchableIndex,
reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)`

Reindexes all searchable items and clears any local state.

