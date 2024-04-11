Instance Method

# update()

Updates the fetched results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    mutating func update()

Available when `Result` conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

Instance Method

# update()

Updates the fetched results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    func update()

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>`

The fetched results of the fetch request.

