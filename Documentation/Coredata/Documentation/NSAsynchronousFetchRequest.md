Initializer

# init(fetchRequest:completionBlock:)

Initializes a new asynchronous fetch request configured with the provided
fetch request and completion block.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        fetchRequest request: NSFetchRequest<ResultType>,
        completionBlock blk: ((NSAsynchronousFetchResult<ResultType>) -> Void)? = nil
    )

Instance Property

# completionBlock

The block that is executed when the fetch request has completed.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get }

## See Also

### Preparing a Request

`var estimatedResultCount: Int`

A configuration parameter that assists Core Data with scheduling the
asynchronous fetch request.

`var fetchRequest: NSFetchRequest<ResultType>`

The underlying fetch request that is executed asynchronously.

Instance Property

# estimatedResultCount

A configuration parameter that assists Core Data with scheduling the
asynchronous fetch request.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var estimatedResultCount: Int { get set }

## See Also

### Preparing a Request

`var completionBlock:
NSPersistentStoreAsynchronousFetchResultCompletionBlock?`

The block that is executed when the fetch request has completed.

`var fetchRequest: NSFetchRequest<ResultType>`

The underlying fetch request that is executed asynchronously.

Instance Property

# fetchRequest

The underlying fetch request that is executed asynchronously.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchRequest: NSFetchRequest<ResultType> { get }

## See Also

### Preparing a Request

`var completionBlock:
NSPersistentStoreAsynchronousFetchResultCompletionBlock?`

The block that is executed when the fetch request has completed.

`var estimatedResultCount: Int`

A configuration parameter that assists Core Data with scheduling the
asynchronous fetch request.

