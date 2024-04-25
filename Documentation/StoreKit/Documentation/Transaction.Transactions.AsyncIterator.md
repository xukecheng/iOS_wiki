Instance Method

# next()

Advances to the next element and returns either the element or `nil` if there
isn’t a next element.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    mutating func next() async -> VerificationResult<Transaction>?

## Return Value

The next element in the underlying sequence, if a next element exists;
otherwise, `nil`.

## Relationships

### From Protocol

  * `AsyncIteratorProtocol`

## See Also

### Getting the Next Element

`typealias Transaction.Transactions.AsyncIterator.Element`

The type of element produced by this iterator.

Type Alias

# Transaction.Transactions.AsyncIterator.Element

The type of element produced by this iterator.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.Transactions.AsyncIterator.Element = VerificationResult<Transaction>

## See Also

### Getting the Next Element

`func next() -> VerificationResult<Transaction>?`

Advances to the next element and returns either the element or `nil` if there
isn’t a next element.

