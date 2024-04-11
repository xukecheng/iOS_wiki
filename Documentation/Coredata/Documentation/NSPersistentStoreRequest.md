Instance Property

# affectedStores

The stores the request should be sent to.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var affectedStores: [NSPersistentStore]? { get set }

## Discussion

The array contains instances of `NSPersistentStore`.

## See Also

### Configuring a Request

`var requestType: NSPersistentStoreRequestType`

The type of the fetch request.

`enum NSPersistentStoreRequestType`

Constants that specify the types of fetch requests.

### Related Documentation

Core Data Programming Guide

Instance Property

# requestType

The type of the fetch request.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var requestType: NSPersistentStoreRequestType { get }

## See Also

### Configuring a Request

`var affectedStores: [NSPersistentStore]?`

The stores the request should be sent to.

`enum NSPersistentStoreRequestType`

Constants that specify the types of fetch requests.

