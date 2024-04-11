Instance Method

# objectIDNotification()

Obtains a notification for use in merging the transaction’s changes into a
managed object context.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    func objectIDNotification() -> Notification

## Return Value

An `NSManagedObjectContextDidSaveObjectIDsNotification` notification.

## Discussion

To merge the relevant changes into your view context, first obtain a
notification by calling `objectIDNotification()` on the transaction. Then,
pass the notification to `mergeChanges(fromContextDidSave:)`.

Type Property

# fetchRequest

A fetch request that has the persistent history transaction as the entity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get }

## See Also

### Customizing History Fetch Requests

`class var entityDescription: NSEntityDescription?`

The entity description of the persistent history transaction entity.

`class func entityDescription(with: NSManagedObjectContext) ->
NSEntityDescription?`

Requests an entity description using the provided context for the managed
object type affected by the transaction.

Type Property

# entityDescription

The entity description of the persistent history transaction entity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    class var entityDescription: NSEntityDescription? { get }

## Discussion

The entity description of `NSPersistentHistoryTransaction` lists the
properties of the persistent history change. This can be useful for filtering
your request.

## See Also

### Customizing History Fetch Requests

`class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?`

A fetch request that has the persistent history transaction as the entity.

`class func entityDescription(with: NSManagedObjectContext) ->
NSEntityDescription?`

Requests an entity description using the provided context for the managed
object type affected by the transaction.

Type Method

# entityDescription(with:)

Requests an entity description using the provided context for the managed
object type affected by the transaction.

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

### Customizing History Fetch Requests

`class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?`

A fetch request that has the persistent history transaction as the entity.

`class var entityDescription: NSEntityDescription?`

The entity description of the persistent history transaction entity.

Instance Property

# author

A granular description of the context that made the persistent history change,
if available.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var author: String? { get }

## Discussion

This property has a value if the managed object context set a
`transactionAuthor` before the save.

## See Also

### Inspecting Transaction Details

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# bundleID

The originating bundle’s identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var bundleID: String { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# changes

The array of persistent history changes.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var changes: [NSPersistentHistoryChange]? { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# contextName

The originating context’s name.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var contextName: String? { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# processID

The originating process’s identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var processID: String { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# storeID

The originating store’s identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var storeID: String { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# timestamp

The date of the persistent history change.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var timestamp: Date { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# token

The token that represents this transaction in the persistent history.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var token: NSPersistentHistoryToken { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var transactionNumber: Int64`

The transaction’s numeric identifier.

Instance Property

# transactionNumber

The transaction’s numeric identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var transactionNumber: Int64 { get }

## See Also

### Inspecting Transaction Details

`var author: String?`

A granular description of the context that made the persistent history change,
if available.

`var bundleID: String`

The originating bundle’s identifier.

`var changes: [NSPersistentHistoryChange]?`

The array of persistent history changes.

`var contextName: String?`

The originating context’s name.

`var processID: String`

The originating process’s identifier.

`var storeID: String`

The originating store’s identifier.

`var timestamp: Date`

The date of the persistent history change.

`var token: NSPersistentHistoryToken`

The token that represents this transaction in the persistent history.

