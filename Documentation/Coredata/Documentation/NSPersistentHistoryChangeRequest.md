Instance Property

# fetchRequest

The specified fetch request, when retrieving history.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get set }

## See Also

### Configuring the Request

`var resultType: NSPersistentHistoryResultType`

The type of result that this request returns.

Instance Property

# resultType

The type of result that this request returns.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var resultType: NSPersistentHistoryResultType { get set }

## Discussion

This value defaults to `NSPersistentHistoryResultType.transactionsAndChanges`.

## See Also

### Configuring the Request

`var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?`

The specified fetch request, when retrieving history.

Instance Property

# token

The specified token, when retrieving history defined by a token.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var token: NSPersistentHistoryToken? { get }

Type Method

# fetchHistory(after:)

Retrieves history since a given date.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func fetchHistory(after date: Date) -> Self

##  Parameters

`date`

    

The date used to define the start of the fetch history.

## Return Value

A persistent history fetch request (`NSPersistentHistoryChangeRequest`) with
an initial date boundary.

## See Also

### Fetching History

`class func fetchHistory(after: NSPersistentHistoryToken?) -> Self`

Retrieves the request history after a given token.

`class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self`

Retrieves history since a given transaction.

`class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>)
-> Self`

Retrieves history based on a fetch request.

Type Method

# fetchHistory(after:)

Retrieves the request history after a given token.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func fetchHistory(after token: NSPersistentHistoryToken?) -> Self

##  Parameters

`token`

    

The bookmark that defines the start of the request history.

## Return Value

A persistent history fetch request (`NSPersistentHistoryChangeRequest`) with
an initial token bookmark boundary.

## See Also

### Fetching History

`class func fetchHistory(after: Date) -> Self`

Retrieves history since a given date.

`class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self`

Retrieves history since a given transaction.

`class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>)
-> Self`

Retrieves history based on a fetch request.

Type Method

# fetchHistory(after:)

Retrieves history since a given transaction.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func fetchHistory(after transaction: NSPersistentHistoryTransaction?) -> Self

##  Parameters

`transaction`

    

The transaction that marks the beginning of the history request.

## Return Value

A persistent history fetch request (`NSPersistentHistoryChangeRequest`) with
an initial transaction boundary.

## See Also

### Fetching History

`class func fetchHistory(after: Date) -> Self`

Retrieves history since a given date.

`class func fetchHistory(after: NSPersistentHistoryToken?) -> Self`

Retrieves the request history after a given token.

`class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>)
-> Self`

Retrieves history based on a fetch request.

Type Method

# fetchHistory(withFetch:)

Retrieves history based on a fetch request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class func fetchHistory(withFetch fetchRequest: NSFetchRequest<any NSFetchRequestResult>) -> Self

##  Parameters

`fetchRequest`

    

The fetch request that defines the history bounds.

## Return Value

A persistent history fetch request (`NSPersistentHistoryChangeRequest`) built
using an existing fetch request.

## See Also

### Fetching History

`class func fetchHistory(after: Date) -> Self`

Retrieves history since a given date.

`class func fetchHistory(after: NSPersistentHistoryToken?) -> Self`

Retrieves the request history after a given token.

`class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self`

Retrieves history since a given transaction.

Type Method

# deleteHistory(before:)

Purges history older than a given date.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func deleteHistory(before date: Date) -> Self

##  Parameters

`date`

    

The date used to define the end of the delete history request.

## Return Value

A delete history change request (`NSPersistentHistoryChangeRequest`) using an
end date boundary.

## See Also

### Purging History

`class func deleteHistory(before: NSPersistentHistoryToken?) -> Self`

Purges history older than that defined by a given token.

`class func deleteHistory(before: NSPersistentHistoryTransaction?) -> Self`

Purges history older than a given transaction.

Type Method

# deleteHistory(before:)

Purges history older than that defined by a given token.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func deleteHistory(before token: NSPersistentHistoryToken?) -> Self

##  Parameters

`token`

    

The bookmark that marks the end of the delete history request.

## Return Value

A delete history change request (`NSPersistentHistoryChangeRequest`) using an
end token bookmark boundary.

## See Also

### Purging History

`class func deleteHistory(before: Date) -> Self`

Purges history older than a given date.

`class func deleteHistory(before: NSPersistentHistoryTransaction?) -> Self`

Purges history older than a given transaction.

Type Method

# deleteHistory(before:)

Purges history older than a given transaction.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    class func deleteHistory(before transaction: NSPersistentHistoryTransaction?) -> Self

##  Parameters

`transaction`

    

The transaction that marks the end of the delete history request.

## Return Value

A delete history change request (`NSPersistentHistoryChangeRequest`) using an
end transaction boundary.

## See Also

### Purging History

`class func deleteHistory(before: Date) -> Self`

Purges history older than a given date.

`class func deleteHistory(before: NSPersistentHistoryToken?) -> Self`

Purges history older than that defined by a given token.

