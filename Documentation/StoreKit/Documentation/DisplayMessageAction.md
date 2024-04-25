Instance Method

# callAsFunction(_:)

Tells StoreKit to display the App Store message, if appropriate.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+
Xcode 14.0+

    
    
    @MainActor
    func callAsFunction(_ message: Message) throws

##  Parameters

`message`

    

The App Store message to display.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`DisplayMessageAction` structure using `message` as an argument.

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

