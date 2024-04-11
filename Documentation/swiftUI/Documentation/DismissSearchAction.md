Instance Method

# callAsFunction()

Dismisses the current search operation, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the
`DismissSearchAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

