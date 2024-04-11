Instance Property

# data

The collection of underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var data: Self.Data { get }

**Required**

## See Also

### Getting row data

`associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

Associated Type

# Data

The type of the underlying collection of data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype Data : Collection

**Required**

## See Also

### Getting row data

`var data: Self.Data`

The collection of underlying data.

**Required**

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func onInsert(
        of supportedContentTypes: [UTType],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> ModifiedContent<Self, OnInsertTableRowModifier>

##  Parameters

`supportedContentTypes`

    

An array of universal type identifiers types that the rows supports.

`action`

    

A closure that SwiftUI invokes when adding elements to the collection of rows.
The closure takes two arguments. The first argument is the offset relative to
the dynamic view’s underlying collection of data. The second argument is an
array of `NSItemProvider` items that represents the data that you want to
insert.

## Return Value

A view that calls `action` when inserting elements into the original view.

## See Also

### Inserting rows

`struct OnInsertTableRowModifier`

A table row modifier that adds the ability to insert data in some base row
content.

Structure

# OnInsertTableRowModifier

A table row modifier that adds the ability to insert data in some base row
content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct OnInsertTableRowModifier

## See Also

### Inserting rows

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) ->
ModifiedContent<Self, OnInsertTableRowModifier>`

Sets the insert action for the dynamic table rows.

Instance Method

# dropDestination(for:action:)

Sets the insert action for the dynamic table rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping (Int, [T]) -> Void
    ) -> ModifiedContent<Self, OnInsertTableRowModifier> where T : Transferable

##  Parameters

`payloadType`

    

Type of the models that are dropped.

`action`

    

A closure that SwiftUI invokes when elements are added to the collection of
rows. The closure takes two arguments: The first argument is the offset
relative to the dynamic view’s underlying collection of data. The second
argument is an array of `Transferable` items that represents the data that you
want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Discussion

