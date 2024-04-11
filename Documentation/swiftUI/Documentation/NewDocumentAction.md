Instance Method

# callAsFunction(_:)

Presents a new reference type document window.

macOS 13.0+

    
    
    func callAsFunction<D>(_ newDocument: @escaping () -> D) where D : ReferenceFileDocument

##  Parameters

`newDocument`

    

The new reference type file document to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(_:)

Presents a new document window.

macOS 13.0+

    
    
    func callAsFunction<D>(_ newDocument: @autoclosure @escaping () -> D) where D : FileDocument

##  Parameters

`newDocument`

    

The new file document to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(contentType:)

Presents a new document window.

macOS 14.0+

    
    
    func callAsFunction(contentType: UTType)

##  Parameters

`contentType`

    

The content type of the document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist` file. For more information, see Defining
file and data types for your app. Also, remember to specify the supported
Document types in the `Info.plist` file as well.

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(contentType:prepareDocument:)

Presents a new document window with preset contents.

SwiftData  SwiftUI  macOS 14.0+

    
    
    func callAsFunction(
        contentType: UTType,
        prepareDocument: @escaping (ModelContext) -> Void
    )

##  Parameters

`contentType`

    

The content type of the document.

`prepareDocument`

    

The closure that accepts `ModelContext` associated with the new document. Use
this closure to set the document’s initial contents before it is displayed:
insert preconfigured models in the provided `ModelContext`.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action.

For example, a Todo app might have a way to create a sample prepopulated Todo
list as a part of onboarding experience:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

