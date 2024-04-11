Instance Property

# document

The current document model.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @Binding
    var document: Document { get nonmutating set }

## Discussion

Setting a new value marks the document as having changes for later saving and
registers an undo action to restore the model to its previous value.

If `isEditable` is `false`, setting a new value has no effect because the
document is in viewing mode.

## See Also

### Getting and setting the document

`var $document: Binding<Document>`

Instance Property

# $document

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var $document: Binding<Document> { get }

## See Also

### Getting and setting the document

`var document: Document`

The current document model.

Instance Property

# fileURL

The URL of the open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var fileURL: URL?

## See Also

### Getting document properties

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean that indicates whether you can edit the document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var isEditable: Bool

## Discussion

This value is `false` if the document is in viewing mode, or if the file is
not writable.

## See Also

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

