Structure

# DocumentGroup

A scene that enables support for opening, creating, and saving documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DocumentGroup<Document, Content> where Content : View

## Overview

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app
can open when you declare your app using the `App` protocol.

Initialize a document group scene by passing in the document model and a view
capable of displaying the document type. The document types you supply to
`DocumentGroup` must conform to `FileDocument` or `ReferenceFileDocument`.
SwiftUI uses the model to add document support to your app. In macOS this
includes document-based menu support, including the ability to open multiple
documents. On iOS this includes a document browser that can navigate to the
documents stored on the file system and multiwindow support:

Any time the configuration changes, SwiftUI updates the contents with that new
configuration, similar to other parameterized builders.

### Viewing documents

If your app only needs to display but not modify a specific document type, you
can use the file viewer document group scene. You supply the file type of the
document, and a view that displays the document type that you provide:

### Supporting multiple document types

Your app can support multiple document types by adding additional document
group scenes:

### Accessing the document’s URL

If your app needs to know the document’s URL, you can read it from the
`editor` closure’s `configuration` parameter, along with the binding to the
document. When you create a new document, the configuration’s `fileURL`
property is `nil`. Every time it changes, it is passed over to the
`DocumentGroup` builder in the updated `configuration`. This ensures that the
view you define in the closure always knows the URL of the document it hosts.

The URL can be used, for example, to present the file path of the file name in
the user interface. Don’t access the document’s contents or metadata using the
URL because that can conflict with the management of the file that SwiftUI
performs. Instead, use the methods that `FileDocument` and
`ReferenceFileDocument` provide to perform read and write operations.

## Topics

### Creating a document group

`init(newDocument: () -> Document, editor:
(FileDocumentConfiguration<Document>) -> Content)`

Creates a document group for creating and editing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

`init(viewing: Document.Type, viewer: (FileDocumentConfiguration<Document>) ->
Content)`

Creates a document group capable of viewing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

### Creating a reference file document group

`init(newDocument: () -> Document, editor:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to create and edit reference file
documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

`init(viewing: Document.Type, viewer:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to view reference file documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

### Editing a document backed by a persistent store

`init(editing: [any PersistentModel.Type], contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store
several model types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: any PersistentModel.Type, contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store a
specific model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: ()
-> Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

### Viewing a document backed by a persistent store

`init(viewing: [any PersistentModel.Type], contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store several model
types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: any PersistentModel.Type, contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store a specific
model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: ()
-> Content)`

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating a document

Building a Document-Based App with SwiftUI

Create, save, and open documents in a SwiftUI multiplatform app.

Building a document-based app using SwiftData

Code along with the WWDC presenter to transform an app with SwiftData.

Protocol

# FileDocument

A type that you use to serialize documents to and from file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol FileDocument

## Overview

To store a document as a value type — like a structure — create a type that
conforms to the `FileDocument` protocol and implement the required methods and
properties. Your implementation:

  * Provides a list of the content types that the document can read from and write to by defining `readableContentTypes`. If the list of content types that the document can write to is different from those that it reads from, you can optionally also define `writableContentTypes`.

  * Loads documents from file in the `init(configuration:)` initializer.

  * Stores documents to file by serializing their content in the `fileWrapper(configuration:)` method.

Important

If you store your document as a reference type — like a class — use
`ReferenceFileDocument` instead.

Ensure that types that conform to this protocol are thread-safe. In
particular, SwiftUI calls the protocol’s methods on a background thread. Don’t
use that thread to perform user interface updates. Use it only to serialize
and deserialize the document data.

## Topics

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

### Writing a document

`func fileWrapper(configuration: Self.WriteConfiguration) throws ->
FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

## See Also

### Storing document data in a structure instance

`struct FileDocumentConfiguration`

The properties of an open file document.

Structure

# FileDocumentConfiguration

The properties of an open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentConfiguration<Document> where Document : FileDocument

## Overview

You receive an instance of this structure when you create a `DocumentGroup`
with a value file type. Use it to access the document in your viewer or
editor.

## Topics

### Getting and setting the document

`var document: Document`

The current document model.

`var $document: Binding<Document>`

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a structure instance

`protocol FileDocument`

A type that you use to serialize documents to and from file.

Protocol

# ReferenceFileDocument

A type that you use to serialize reference type documents to and from file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol ReferenceFileDocument : ObservableObject

## Overview

To store a document as a reference type — like a class — create a type that
conforms to the `ReferenceFileDocument` protocol and implement the required
methods and properties. Your implementation:

  * Provides a list of the content types that the document can read from and write to by defining `readableContentTypes`. If the list of content types that the document can write to is different from those that it reads from, you can optionally also define `writableContentTypes`.

  * Loads documents from file in the `init(configuration:)` initializer.

  * Stores documents to file by providing a snapshot of the document’s content in the `snapshot(contentType:)` method, and then serializing that content in the `fileWrapper(snapshot:configuration:)` method.

Important

If you store your document as a value type — like a structure — use
`FileDocument` instead.

Ensure that types that conform to this protocol are thread-safe. In
particular, SwiftUI calls the protocol’s methods on a background thread. Don’t
use that thread to perform user interface updates. Use it only to serialize
and deserialize the document data.

## Topics

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

### Getting a snapshot

`func snapshot(contentType: UTType) throws -> Self.Snapshot`

Creates a snapshot that represents the current state of the document.

**Required**

` associatedtype Snapshot`

A type that represents the document’s stored content.

**Required**

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

## Relationships

### Inherits From

  * `ObservableObject`

## See Also

### Storing document data in a class instance

`struct ReferenceFileDocumentConfiguration`

The properties of an open reference file document.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

Structure

# ReferenceFileDocumentConfiguration

The properties of an open reference file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument

## Overview

You receive an instance of this structure when you create a `DocumentGroup`
with a reference file type. Use it to access the document in your viewer or
editor.

## Topics

### Getting and setting the document

`var document: Document`

The current document model.

`var $document: ObservedObject<Document>.Wrapper`

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a class instance

`protocol ReferenceFileDocument`

A type that you use to serialize reference type documents to and from file.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

Instance Property

# undoManager

The undo manager used to register a view’s undo operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var undoManager: UndoManager? { get }

## Discussion

This value is `nil` when the environment represents a context that doesn’t
support undo and redo operations. You can skip registration of an undo
operation when this value is `nil`.

## See Also

### Storing document data in a class instance

`protocol ReferenceFileDocument`

A type that you use to serialize reference type documents to and from file.

`struct ReferenceFileDocumentConfiguration`

The properties of an open reference file document.

Instance Property

# documentConfiguration

The configuration of a document in a `DocumentGroup`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var documentConfiguration: DocumentConfiguration? { get }

## Discussion

The value is `nil` for views that are not enclosed in a `DocumentGroup`.

For example, if the app shows the document path in the footer of each
document, it can get the URL from the environment:

## See Also

### Accessing document configuration

`struct DocumentConfiguration`

Structure

# DocumentConfiguration

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DocumentConfiguration

## Topics

### Getting configuration values

`var fileURL: URL?`

A URL of an open document.

`var isEditable: Bool`

A Boolean value that indicates whether you can edit the document.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Accessing document configuration

`var documentConfiguration: DocumentConfiguration?`

The configuration of a document in a `DocumentGroup`.

Structure

# FileDocumentReadConfiguration

The configuration for reading file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentReadConfiguration

## Topics

### Reading the content

`let contentType: UTType`

The expected uniform type of the file contents.

`let file: FileWrapper`

The file wrapper containing the document content.

## See Also

### Reading and writing documents

`struct FileDocumentWriteConfiguration`

The configuration for serializing file contents.

Structure

# FileDocumentWriteConfiguration

The configuration for serializing file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentWriteConfiguration

## Topics

### Writing the content

`let contentType: UTType`

The expected uniform type of the file contents.

`let existingFile: FileWrapper?`

The file wrapper containing the current document content. `nil` if the
document is unsaved.

## See Also

### Reading and writing documents

`struct FileDocumentReadConfiguration`

The configuration for reading file contents.

Instance Property

# newDocument

An action in the environment that presents a new document.

macOS 13.0+

    
    
    var newDocument: NewDocumentAction { get }

## Discussion

Use the `newDocument` environment value to get the instance of the
`NewDocumentAction` structure for a given `Environment`. Then call the
instance to present a new document. You call the instance directly because it
defines a `callAsFunction(_:)` method that Swift calls when you call the
instance.

For example, you can define a button that creates a new document from the
selected text:

The above example assumes that you define a `TextDocument` that conforms to
the `FileDocument` or `ReferenceFileDocument` protocol, and a `DocumentGroup`
that handles the associated file type.

## See Also

### Opening a document programmatically

`struct NewDocumentAction`

An action that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`struct OpenDocumentAction`

An action that presents an existing document.

Structure

# NewDocumentAction

An action that presents a new document.

macOS 13.0+

    
    
    struct NewDocumentAction

## Overview

Use the `newDocument` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to present a new document.
You call the instance directly because it defines a `callAsFunction(_:)`
method that Swift calls when you call the instance.

For example, you can define a button that creates a new document from the
selected text:

The above example assumes that you define a `TextDocument` that conforms to
the `FileDocument` or `ReferenceFileDocument` protocol, and a `DocumentGroup`
that handles the associated file type.

## Topics

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`struct OpenDocumentAction`

An action that presents an existing document.

Instance Property

# openDocument

An action in the environment that presents an existing document.

macOS 13.0+

    
    
    var openDocument: OpenDocumentAction { get }

## Discussion

Use the `openDocument` environment value to get the instance of the
`OpenDocumentAction` structure for a given `Environment`. Then call the
instance to present an existing document. You call the instance directly
because it defines a `callAsFunction(at:)` method that Swift calls when you
call the instance.

For example, you can create a button that opens the document at the specified
URL:

The above example uses a `do-catch` statement to handle any errors that the
open document action might throw. It also places the action inside a task and
awaits the result because the action operates asynchronously.

To present an existing document, your app must define a `DocumentGroup` that
handles the content type of the specified file. For a document that’s already
open, the system brings the existing window to the front. Otherwise, the
system opens a new window.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`struct NewDocumentAction`

An action that presents a new document.

`struct OpenDocumentAction`

An action that presents an existing document.

Structure

# OpenDocumentAction

An action that presents an existing document.

macOS 13.0+

    
    
    struct OpenDocumentAction

## Overview

Use the `openDocument` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to present an existing
document. You call the instance directly because it defines a
`callAsFunction(at:)` method that Swift calls when you call the instance.

For example, you can create a button that opens the document at the specified
URL:

The above example uses a `do-catch` statement to handle any errors that the
open document action might throw. It also places the action inside a task and
awaits the result because the action operates asynchronously.

To present an existing document, your app must define a `DocumentGroup` that
handles the content type of the specified file. For a document that’s already
open, the system brings the existing window to the front. Otherwise, the
system opens a new window.

## Topics

### Calling the action

`func callAsFunction(at: URL) async throws`

Opens the document at the specified file URL.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`struct NewDocumentAction`

An action that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

Structure

# RenameButton

A button that triggers a standard rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct RenameButton<Label> where Label : View

## Overview

A rename button receives its action from the environment. Use the
`renameAction(_:)` modifier to set the action. The system disables the button
if you don’t define an action.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation
title modifier automatically configures the environment with the appropriate
rename action.

## Topics

### Creating an rename button

`init()`

Creates a rename button.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating special-purpose buttons

`struct EditButton`

A button that toggles the edit mode environment value.

`struct PasteButton`

A system button that reads items from the pasteboard and delivers it to a
closure.

Instance Method

# renameAction(_:)

Sets the rename action in the environment to update focus state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ isFocused: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`isFocused`

    

The focus binding to update when activating the rename action.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# renameAction(_:)

Sets a closure to run for the rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ action: @escaping () -> Void) -> some View
    

##  Parameters

`action`

    

A closure to run when renaming.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When the user taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Property

# rename

An action that activates the standard rename interaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var rename: RenameAction? { get }

## Discussion

Use the `renameAction(_:)` modifier to configure the rename action in the
environment.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`struct RenameAction`

An action that activates a standard rename interaction.

Structure

# RenameAction

An action that activates a standard rename interaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct RenameAction

## Overview

Use the `renameAction(_:)` modifier to configure the rename action in the
environment.

## Topics

### Calling the action

`func callAsFunction()`

Triggers the standard rename action provided through the environment.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

