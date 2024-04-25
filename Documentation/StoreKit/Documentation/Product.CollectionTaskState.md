Enumeration Case

# Product.CollectionTaskState.loading

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Collection task states

`case success([Product], unavailable: [Product.ID])`

`case failure(any Error)`

Enumeration Case

# Product.CollectionTaskState.success(_:unavailable:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(
        [Product],
        unavailable: [Product.ID]
    )

## See Also

### Collection task states

`case loading`

`case failure(any Error)`

Enumeration Case

# Product.CollectionTaskState.failure(_:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

## See Also

### Collection task states

`case loading`

`case success([Product], unavailable: [Product.ID])`

