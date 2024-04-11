Instance Method

# callAsFunction()

Initiates a refresh action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction() async

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`RefreshAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_. For information about asynchronous operations in Swift, see
Concurrency.

