Instance Method

# callAsFunction(at:)

Opens the document at the specified file URL.

macOS 13.0+

    
    
    func callAsFunction(at url: URL) async throws

##  Parameters

`url`

    

A file URL that points at an existing document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

