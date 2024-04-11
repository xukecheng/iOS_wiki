Initializer

# init(fetchRequest:)

Creates a request that deletes the results of the specified fetch request.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(fetchRequest fetch: NSFetchRequest<any NSFetchRequestResult>)

##  Parameters

`fetch`

    

The fetch request that identifies the managed objects to delete.

## See Also

### Creating a Request

`init(objectIDs: [NSManagedObjectID])`

Creates a request that deletes the managed objects with the specified
identifiers.

Initializer

# init(objectIDs:)

Creates a request that deletes the managed objects with the specified
identifiers.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    convenience init(objectIDs objects: [NSManagedObjectID])

##  Parameters

`objects`

    

The array that contains the identifiers of the managed objects to delete.

## Discussion

Important

The identifiers your provide must be from managed objects of the same entity
type; mixing entity types results in an error when you execute the request.

## See Also

### Creating a Request

`init(fetchRequest: NSFetchRequest<any NSFetchRequestResult>)`

Creates a request that deletes the results of the specified fetch request.

Instance Property

# fetchRequest

The fetch request that identifies the managed objects to delete.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    @NSCopying
    var fetchRequest: NSFetchRequest<any NSFetchRequestResult> { get }

## Discussion

This property contains the fetch request that identifies the managed objects
to delete. If you initialize `NSBatchDeleteRequest` with an array of
`NSManagedObjectID`, Core Data automatically generates a fetch request with a
predicate that matches the identifiers in that array.

Instance Property

# resultType

The type of result the request provides when it executes.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var resultType: NSBatchDeleteRequestResultType { get set }

## Discussion

Set this property before you execute the request if you require a result type
other than the default of
`NSBatchDeleteRequestResultType.resultTypeStatusOnly`.

## See Also

### Configuring the Result Type

`enum NSBatchDeleteRequestResultType`

The types of result a batch delete request can provide when it executes.

