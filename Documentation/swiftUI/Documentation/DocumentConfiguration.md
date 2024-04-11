Instance Property

# fileURL

A URL of an open document.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var fileURL: URL? { get }

## Discussion

If the document has never been saved, returns `nil`.

## See Also

### Getting configuration values

`var isEditable: Bool`

A Boolean value that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean value that indicates whether you can edit the document.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var isEditable: Bool { get }

## Discussion

On macOS, the document could be non-editable if the user lacks write
permissions, the parent directory or volume is read-only, or the document
couldn’t be autosaved.

On iOS, the document is not editable if there was an error reading or saving
it, there’s an unresolved conflict, the document is being uploaded or
downloaded, or otherwise, it is currently busy and unsafe for user edits.

## See Also

### Getting configuration values

`var fileURL: URL?`

A URL of an open document.

