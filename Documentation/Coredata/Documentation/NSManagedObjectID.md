Instance Property

# entity

The entity description associated with the object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription { get }

## See Also

### Getting Managed Object ID Information

`var isTemporaryID: Bool`

A Boolean value that indicates whether the object ID is temporary.

`var persistentStore: NSPersistentStore?`

The persistent store that fetched the object for the object ID.

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

### Related Documentation

Core Data Programming Guide

`var entity: NSEntityDescription`

The entity description of the managed object.

Instance Property

# isTemporaryID

A Boolean value that indicates whether the object ID is temporary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isTemporaryID: Bool { get }

## Discussion

`true` if the receiver is temporary, otherwise `false`. Most object IDs return
`false`. New objects inserted into a managed object context are assigned a
temporary ID which is replaced with a permanent one once the object gets saved
to a persistent store.

## See Also

### Getting Managed Object ID Information

`var entity: NSEntityDescription`

The entity description associated with the object ID.

`var persistentStore: NSPersistentStore?`

The persistent store that fetched the object for the object ID.

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

Instance Property

# persistentStore

The persistent store that fetched the object for the object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    weak var persistentStore: NSPersistentStore? { get }

## Discussion

`nil` if the ID is for a newly-inserted object that has not yet been saved to
a persistent store.

## See Also

### Getting Managed Object ID Information

`var entity: NSEntityDescription`

The entity description associated with the object ID.

`var isTemporaryID: Bool`

A Boolean value that indicates whether the object ID is temporary.

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

Instance Method

# uriRepresentation()

Returns a URI that provides an archiveable reference to the object for the
object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func uriRepresentation() -> URL

## Return Value

An `NSURL` object containing a URI that provides an archiveable reference to
the object which the receiver represents.

## Discussion

If the corresponding managed object has not yet been saved, the object ID (and
hence URI) is a temporary value that will change when the corresponding
managed object is saved.

## See Also

### Getting Managed Object ID Information

`var entity: NSEntityDescription`

The entity description associated with the object ID.

`var isTemporaryID: Bool`

A Boolean value that indicates whether the object ID is temporary.

`var persistentStore: NSPersistentStore?`

The persistent store that fetched the object for the object ID.

### Related Documentation

`func managedObjectID(forURIRepresentation: URL) -> NSManagedObjectID?`

Returns the object identifier for the specified URI representation.

`func object(with: NSManagedObjectID) -> NSManagedObject`

Returns either an existing object from the context or a fault that represents
that object.

