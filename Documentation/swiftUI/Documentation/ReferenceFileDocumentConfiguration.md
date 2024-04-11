Instance Property

# document

The current document model.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @ObservedObject @MainActor
    var document: Document { get set }

## Discussion

Changes to the document dirty the document state, indicating that it needs to
be saved. SwiftUI doesn’t automatically register undo actions. You have to
manage undo operations yourself, as demonstrated in Building a Document-Based
App with SwiftUI.

## See Also

### Getting and setting the document

`var $document: ObservedObject<Document>.Wrapper`

Instance Property

# $document

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var $document: ObservedObject<Document>.Wrapper { get }

## See Also

### Getting and setting the document

`var document: Document`

The current document model.

Instance Property

# fileURL

The URL of the open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var fileURL: URL?

## See Also

### Getting document properties

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean that indicates whether you can edit the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    var isEditable: Bool

## Discussion

The value is `false` if the document is in viewing mode, or if the file is not
writable.

## See Also

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

