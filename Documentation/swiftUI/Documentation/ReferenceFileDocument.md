Initializer

# init(configuration:)

Creates a document and initializes it with the contents of a file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(configuration: Self.ReadConfiguration) throws

**Required**

##  Parameters

`configuration`

    

Information about the file that you read document data from.

## Discussion

SwiftUI calls this initializer when someone opens a file type that matches one
of those that your document type supports. Use the `file` property of the
`configuration` input to get document’s data. Deserialize the data, and store
it in your document’s data structure:

The above example assumes that you define `Model` to contain the document’s
data, that `Model` conforms to the `Codable` protocol, and that you store a
`model` property of that type inside your document.

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Reading a document

`static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

Type Property

# readableContentTypes

The file and data types that the document reads from.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var readableContentTypes: [UTType] { get }

**Required**

## Discussion

Define this list to indicate the content types that your document can read. By
default, SwiftUI assumes that your document can also write the same set of
content types. If you need to indicate a different set of types for writing
files, define the `writableContentTypes` property in addition to this
property.

## See Also

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

Type Alias

# ReferenceFileDocument.ReadConfiguration

The configuration for reading document contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias ReadConfiguration = FileDocumentReadConfiguration

## Discussion

This type is an alias for `FileDocumentReadConfiguration`, which contains a
content type and a file wrapper that you use to access the contents of a
document file. You get a value of this type as an input to the
`init(configuration:)` initializer. Use it to load a document from a file.

## See Also

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

Instance Method

# snapshot(contentType:)

Creates a snapshot that represents the current state of the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func snapshot(contentType: UTType) throws -> Self.Snapshot

**Required**

##  Parameters

`contentType`

    

The content type that you create the document snapshot for.

## Return Value

A snapshot of the document content that the system provides to the
`fileWrapper(snapshot:configuration:)` method for serialization.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI
begins by calling this method. Return a copy of the document’s content from
your implementation of the method. For example, you might define an
initializer for your document’s model object that copies the contents of the
document’s instance, and return that:

SwiftUI prevents document edits during the snapshot operation to ensure that
the model state remains coherent. After the call completes, SwiftUI reenables
edits, and then calls the `fileWrapper(snapshot:configuration:)` method, where
you serialize the snapshot and store it to a file.

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Getting a snapshot

`associatedtype Snapshot`

A type that represents the document’s stored content.

**Required**

Associated Type

# Snapshot

A type that represents the document’s stored content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Snapshot

**Required**

## Discussion

Define this type to represent all the data that your document stores. When
someone issues a Save command, SwiftUI asks your document for a value of this
type by calling the document’s `snapshot(contentType:)` method. SwiftUI sends
the snapshot that you provide to the document’s
`fileWrapper(snapshot:configuration:)` method, where you serialize the
contents of the snapshot into a file wrapper.

## See Also

### Getting a snapshot

`func snapshot(contentType: UTType) throws -> Self.Snapshot`

Creates a snapshot that represents the current state of the document.

**Required**

Instance Method

# fileWrapper(snapshot:configuration:)

Serializes a document snapshot to a file wrapper.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileWrapper(
        snapshot: Self.Snapshot,
        configuration: Self.WriteConfiguration
    ) throws -> FileWrapper

**Required**

##  Parameters

`snapshot`

    

The document snapshot to save.

`configuration`

    

Information about a file that already exists for the document, if any.

## Return Value

The destination to serialize the document contents to. The value can be a
newly created `FileWrapper` or an update of the one provided in the
`configuration` input.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI
begins by calling the `snapshot(contentType:)` method to get a copy of the
document data in its current state. Then SwiftUI passes that snapshot to this
method, where you serialize it and create or modify a file wrapper with the
serialized data:

SwiftUI disables document edits during the snapshot to ensure that the
document’s data remains coherent, but reenables edits during the serialization
operation.

Note

SwiftUI calls this method on a background thread. Don’t make user interface
changes from that thread.

## See Also

### Writing a document

`static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

Type Property

# writableContentTypes

The file types that the document supports saving or exporting to.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var writableContentTypes: [UTType] { get }

**Required** Default implementation provided.

## Discussion

By default, SwiftUI assumes that your document reads and writes the same set
of content types. Only define this property if you need to indicate a
different set of types for writing files. Otherwise, the default
implementation of this property returns the list that you specify in your
implementation of `readableContentTypes`.

## Default Implementations

### ReferenceFileDocument Implementations

`static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

## See Also

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` typealias WriteConfiguration`

The configuration for writing document contents.

Type Alias

# ReferenceFileDocument.WriteConfiguration

The configuration for writing document contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias WriteConfiguration = FileDocumentWriteConfiguration

## Discussion

This type is an alias for `FileDocumentWriteConfiguration`, which contains a
content type and a file wrapper that you use to access the contents of a
document file, if one already exists. You get a value of this type as an input
to the `fileWrapper(snapshot:configuration:)` method.

## See Also

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

