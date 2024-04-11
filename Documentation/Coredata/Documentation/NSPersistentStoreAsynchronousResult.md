Instance Property

# managedObjectContext

The managed object context for the result.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var managedObjectContext: NSManagedObjectContext { get }

## See Also

### Inspecting the Result

`var operationError: (any Error)?`

An error that contains details if the asynchronous fetch request fails.

`var progress: Progress?`

An object that reports progress for the asynchronous fetch request.

Instance Property

# operationError

An error that contains details if the asynchronous fetch request fails.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var operationError: (any Error)? { get }

## See Also

### Inspecting the Result

`var managedObjectContext: NSManagedObjectContext`

The managed object context for the result.

`var progress: Progress?`

An object that reports progress for the asynchronous fetch request.

Instance Property

# progress

An object that reports progress for the asynchronous fetch request.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var progress: Progress? { get }

## See Also

### Inspecting the Result

`var managedObjectContext: NSManagedObjectContext`

The managed object context for the result.

`var operationError: (any Error)?`

An error that contains details if the asynchronous fetch request fails.

Instance Method

# cancel()

Cancels the asynchronous fetch request.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func cancel()

Type Alias

# NSPersistentStoreAsynchronousFetchResultCompletionBlock

A completion block that an asynchronous fetch request calls with a result.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult<any NSFetchRequestResult>) -> Void

##  Parameters

`result`

    

The result of the fetch request.

