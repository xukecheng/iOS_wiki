Initializer

# init(newDocument:editor:)

Creates a document group for creating and editing file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        newDocument: @autoclosure @escaping () -> Document,
        @ViewBuilder editor: @escaping (FileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

##  Parameters

`newDocument`

    

The initial document to use when a user creates a new document.

`editor`

    

The editing UI for the provided document.

## Discussion

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app
can open when you declare your app using the `App` protocol. You initialize a
document group scene by passing in the document model and a view capable of
displaying the document’s contents. The document types you supply to
`DocumentGroup` must conform to `FileDocument` or `ReferenceFileDocument`.
SwiftUI uses the model to add document support to your app. In macOS this
includes document-based menu support including the ability to open multiple
documents. On iOS this includes a document browser that can navigate to the
documents stored on the file system and multiwindow support:

The document types you supply to `DocumentGroup` must conform to
`FileDocument` or `ReferenceFileDocument`. Your app can support multiple
document types by adding additional `DocumentGroup` scenes.

## See Also

### Creating a document group

`init(viewing: Document.Type, viewer: (FileDocumentConfiguration<Document>) ->
Content)`

Creates a document group capable of viewing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

Initializer

# init(viewing:viewer:)

Creates a document group capable of viewing file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        viewing documentType: Document.Type,
        @ViewBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

##  Parameters

`documentType`

    

The type of document your app can view.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Use this method to create a document group that can view files of a specific
type. The example below creates a new document viewer for
`MyImageFormatDocument` and displays them with `MyImageFormatViewer`:

You tell the system about the app’s role with respect to the document type by
setting the `CFBundleTypeRole` `Info.plist` key with a value of `Viewer`.

## See Also

### Creating a document group

`init(newDocument: () -> Document, editor:
(FileDocumentConfiguration<Document>) -> Content)`

Creates a document group for creating and editing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

Initializer

# init(newDocument:editor:)

Creates a document group that is able to create and edit reference file
documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        newDocument: @escaping () -> Document,
        @ViewBuilder editor: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

##  Parameters

`newDocument`

    

The initial document used when the user creates a new document. The argument
should create a new instance, such that a new document is created on each
invocation of the closure.

`editor`

    

The editing UI for the provided document.

## Discussion

The current document for a given editor instance is also provided as an
environment object for its subhierarchy.

Undo support is not automatically provided for this construction of a
`DocumentGroup`, and any updates to the document by the editor view hierarchy
are expected to register undo operations when appropriate.

## See Also

### Creating a reference file document group

`init(viewing: Document.Type, viewer:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to view reference file documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

Initializer

# init(viewing:viewer:)

Creates a document group that is able to view reference file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        viewing documentType: Document.Type,
        @ViewBuilder viewer: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

##  Parameters

`documentType`

    

The type of document being viewed.

`viewer`

    

The viewing UI for the provided document.

## Discussion

The current document for a given editor instance is also provided as an
environment object for its subhierarchy.

  * See Also: `CFBundleTypeRole` with a value of “Viewer”

## See Also

### Creating a reference file document group

`init(newDocument: () -> Document, editor:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to create and edit reference file
documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

Initializer

# init(editing:contentType:editor:prepareDocument:)

Instantiates a document group for creating and editing documents that store
several model types.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing modelTypes: [any PersistentModel.Type],
        contentType: UTType,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelTypes`

    

The array of model types defining the schema used for each document.

`contentType`

    

The content type of the document. It should conform to `UTType.package`.

`editor`

    

The editing UI for the provided document.

`prepareDocument`

    

The optional closure that accepts `ModelContext` associated with the new
document. Use this closure to set the document’s initial contents before it is
displayed: insert preconfigured models in the provided `ModelContext`.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the Info.plist as well.

## See Also

### Editing a document backed by a persistent store

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

Initializer

# init(editing:contentType:editor:prepareDocument:)

Instantiates a document group for creating and editing documents that store a
specific model type.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing modelType: any PersistentModel.Type,
        contentType: UTType,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelType`

    

The model type defining the schema used for each document.

`contentType`

    

The content type of the document. It should conform to `UTType.package`.

`editor`

    

The editing UI for the provided document.

`prepareDocument`

    

The optional closure that accepts `ModelContext` associated with the new
document. Use this closure to set the document’s initial contents before it is
displayed: insert preconfigured models in the provided `ModelContext`.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the Info.plist as well.

## See Also

### Editing a document backed by a persistent store

`init(editing: [any PersistentModel.Type], contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store
several model types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: ()
-> Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(editing:migrationPlan:editor:prepareDocument:)

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing contentType: UTType,
        migrationPlan: any SchemaMigrationPlan.Type,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`editing`

    

The content type of the document. It should conform to `UTType.package`.

`migrationPlan`

    

The description of steps required to migrate older document versions so that
they can be opened and edited. The last `VersionedSchema` in the plan is
considered to be the current application schema.

`editor`

    

The editing UI for the provided document.

## See Also

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

Initializer

# init(viewing:contentType:viewer:)

Instantiates a document group for viewing documents that store several model
types.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing modelTypes: [any PersistentModel.Type],
        contentType: UTType,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelTypes`

    

The model types defining the schema used for each document.

`contentType`

    

The content type of document your app can view. It should conform to
`UTType.package`.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the `Info.plist` as well.

## See Also

### Viewing a document backed by a persistent store

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

Initializer

# init(viewing:contentType:viewer:)

Instantiates a document group for viewing documents that store a specific
model type.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing modelType: any PersistentModel.Type,
        contentType: UTType,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelType`

    

The model type defining the schema used for each document.

`contentType`

    

The content type of document your app can view. It should conform to
`UTType.package`.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the `Info.plist` as well.

## See Also

### Viewing a document backed by a persistent store

`init(viewing: [any PersistentModel.Type], contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store several model
types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: ()
-> Content)`

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(viewing:migrationPlan:viewer:)

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing contentType: UTType,
        migrationPlan: any SchemaMigrationPlan.Type,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`viewing`

    

The content type of the document. It should conform to `UTType.package`.

`migrationPlan`

    

The description of steps required to migrate older document versions so that
they can be opened. The last `VersionedSchema` in the plan is considered to be
the current application schema.

`viewer`

    

The viewing UI for the provided document.

## See Also

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

