Instance Method

# controller(_:didChangeContentWith:)

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    optional func controller(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>,
        didChangeContentWith snapshot: NSDiffableDataSourceSnapshot
    )

## Discussion

To apply the changes, call `applySnapshot(_:animatingDifferences:)` on the
collection or table view’s data source.

If this method is implemented, no other delegate methods are invoked.

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: CollectionDifference<NSManagedObjectID>)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

`func controllerWillChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath:
IndexPath?)`

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for:
NSFetchedResultsChangeType)`

Notifies the receiver of the addition or removal of a section.

`func controllerDidChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

Instance Method

# controller(_:didChangeContentWith:)

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    optional func controller(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>,
        didChangeContentWith diff: CollectionDifference<NSManagedObjectID>
    )

## Discussion

This method is only invoked if the controller’s `sectionNameKeyPath` property
is `nil` and `controller(_:didChangeContentWith:)` is not implemented.

If this method is implemented, no other delegate methods are invoked.

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: NSDiffableDataSourceSnapshot)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

`func controllerWillChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath:
IndexPath?)`

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for:
NSFetchedResultsChangeType)`

Notifies the receiver of the addition or removal of a section.

`func controllerDidChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

Instance Method

# controllerWillChangeContent(_:)

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

iOS 4.0+  iPadOS 4.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    optional func controllerWillChangeContent(_ controller: NSFetchedResultsController<any NSFetchRequestResult>)

##  Parameters

`controller`

    

The fetched results controller that sent the message.

## Discussion

This method is invoked before all invocations of
`controller(_:didChange:at:for:newIndexPath:)` and
`controller(_:didChange:atSectionIndex:for:)` have been sent for a given
change event (such as the controller receiving a
`NSManagedObjectContextDidSave` notification).

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: NSDiffableDataSourceSnapshot)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: CollectionDifference<NSManagedObjectID>)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath:
IndexPath?)`

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for:
NSFetchedResultsChangeType)`

Notifies the receiver of the addition or removal of a section.

`func controllerDidChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

### Related Documentation

Core Data Programming Guide

Instance Method

# controller(_:didChange:at:for:newIndexPath:)

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

iOS 4.0+  iPadOS 4.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    optional func controller(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>,
        didChange anObject: Any,
        at indexPath: IndexPath?,
        for type: NSFetchedResultsChangeType,
        newIndexPath: IndexPath?
    )

##  Parameters

`controller`

    

The fetched results controller that sent the message.

`anObject`

    

The object in controller’s fetched results that changed.

`indexPath`

    

The index path of the changed object (this value is `nil` for insertions).

`type`

    

The type of change. For valid values see `NSFetchedResultsChangeType`.

`newIndexPath`

    

The destination path for the object for insertions or moves (this value is
`nil` for a deletion).

## Discussion

The fetched results controller reports changes to its section before changes
to the fetch result objects.

Changes are reported with the following heuristics:

  * On add and remove operations, only the added/removed object is reported.

It’s assumed that all objects that come after the affected object are also
moved, but these moves are not reported.

  * A move is reported when the changed attribute on the object is one of the sort descriptors used in the fetch request.

An update of the object is assumed in this case, but no separate update
message is sent to the delegate.

  * An update is reported when an object’s state changes, but the changed attributes aren’t part of the sort keys. 

### Special Considerations

This method may be invoked many times during an update event (for example, if
you are importing data on a background thread and adding them to the context
in a batch). You should consider carefully whether you want to update the
table view on receipt of each message.

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: NSDiffableDataSourceSnapshot)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: CollectionDifference<NSManagedObjectID>)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

`func controllerWillChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for:
NSFetchedResultsChangeType)`

Notifies the receiver of the addition or removal of a section.

`func controllerDidChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

Instance Method

# controller(_:didChange:atSectionIndex:for:)

Notifies the receiver of the addition or removal of a section.

iOS 4.0+  iPadOS 4.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    optional func controller(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>,
        didChange sectionInfo: any NSFetchedResultsSectionInfo,
        atSectionIndex sectionIndex: Int,
        for type: NSFetchedResultsChangeType
    )

##  Parameters

`controller`

    

The fetched results controller that sent the message.

`sectionInfo`

    

The section that changed.

`sectionIndex`

    

The index of the changed section.

`type`

    

The type of change (insert or delete). Valid values are
`NSFetchedResultsChangeType.insert` and `NSFetchedResultsChangeType.delete`.

## Discussion

The fetched results controller reports changes to its section before changes
to the fetched result objects.

### Special Considerations

This method may be invoked many times during an update event (for example, if
you are importing data on a background thread and adding them to the context
in a batch). You should consider carefully whether you want to update the
table view on receipt of each message.

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: NSDiffableDataSourceSnapshot)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: CollectionDifference<NSManagedObjectID>)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

`func controllerWillChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath:
IndexPath?)`

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

`func controllerDidChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

Instance Method

# controllerDidChangeContent(_:)

Notifies the receiver that the fetched results controller has completed
processing of one or more changes due to an add, remove, move, or update.

iOS 4.0+  iPadOS 4.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    optional func controllerDidChangeContent(_ controller: NSFetchedResultsController<any NSFetchRequestResult>)

##  Parameters

`controller`

    

The fetched results controller that sent the message.

## Discussion

This method is invoked after all invocations of
`controller(_:didChange:at:for:newIndexPath:)` and
`controller(_:didChange:atSectionIndex:for:)` have been sent for a given
change event (such as the controller receiving a
`NSManagedObjectContextDidSave` notification).

## See Also

### Responding to Changes

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: NSDiffableDataSourceSnapshot)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a diffable data source snapshot.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChangeContentWith: CollectionDifference<NSManagedObjectID>)`

Notifies the receiver about changes to the content in the fetched results
controller, by using a collection difference.

`func controllerWillChangeContent(NSFetchedResultsController<any
NSFetchRequestResult>)`

Notifies the receiver that the fetched results controller is about to start
processing of one or more changes due to an add, remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath:
IndexPath?)`

Notifies the receiver that a fetched object has been changed due to an add,
remove, move, or update.

`func controller(NSFetchedResultsController<any NSFetchRequestResult>,
didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for:
NSFetchedResultsChangeType)`

Notifies the receiver of the addition or removal of a section.

Instance Method

# controller(_:sectionIndexTitleForSectionName:)

Returns the name for a given section.

iOS 4.0+  iPadOS 4.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    optional func controller(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>,
        sectionIndexTitleForSectionName sectionName: String
    ) -> String?

##  Parameters

`controller`

    

The fetched results controller that sent the message.

`sectionName`

    

The default name of the section.

## Return Value

The string to use as the name for the specified section.

## Discussion

This method does not enable change tracking. It is only needed if a section
index is used.

If the delegate doesn’t implement this method, the default implementation
returns the capitalized first letter of the section name (see
`sectionIndexTitle(forSectionName:)` in `NSFetchedResultsController`).

