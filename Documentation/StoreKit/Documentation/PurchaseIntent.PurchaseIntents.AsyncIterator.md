Instance Method

# next()

Advances to and returns the next element, if it exists.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    mutating func next() async -> PurchaseIntent.PurchaseIntents.Element?

## Return Value

The next element in the underlying sequence, if a next element exists;
otherwise, `nil`.

## Relationships

### From Protocol

  * `AsyncIteratorProtocol`

## See Also

### Getting the next element

`typealias PurchaseIntent.PurchaseIntents.AsyncIterator.Element`

The type of element the iterator produces.

Type Alias

# PurchaseIntent.PurchaseIntents.AsyncIterator.Element

The type of element the iterator produces.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    typealias PurchaseIntent.PurchaseIntents.AsyncIterator.Element = PurchaseIntent.PurchaseIntents.Element

## See Also

### Getting the next element

`func next() -> PurchaseIntent.PurchaseIntents.Element?`

Advances to and returns the next element, if it exists.

