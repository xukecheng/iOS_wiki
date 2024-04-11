Instance Method

# callAsFunction()

Dismisses the currently opened immersive space.

visionOS 1.0+

    
    
    @MainActor
    func callAsFunction() async

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissImmersiveSpace` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

