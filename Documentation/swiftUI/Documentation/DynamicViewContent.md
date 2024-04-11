Instance Property

# data

The collection of underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var data: Self.Data { get }

**Required**

## See Also

### Managing the data

`associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

Associated Type

# Data

The type of the underlying collection of data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Data : Collection

**Required**

## See Also

### Managing the data

`var data: Self.Data`

The collection of underlying data.

**Required**

Instance Method

# onDelete(perform:)

Sets the deletion action for the dynamic view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDelete(perform action: Optional<(IndexSet) -> Void>) -> some DynamicViewContent
    

##  Parameters

`action`

    

The action that you want SwiftUI to perform when elements in the view are
deleted. SwiftUI passes a set of indices to the closure that’s relative to the
dynamic view’s underlying collection of data.

## Return Value

A view that calls `action` when elements are deleted from the original view.

## See Also

### Responding to updates

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onInsert(
        of supportedContentTypes: [UTType],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> some DynamicViewContent
    

##  Parameters

`supportedContentTypes`

    

An array of UTI types that the dynamic view supports.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `NSItemProvider` items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# onMove(perform:)

Sets the move action for the dynamic view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onMove(perform action: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent
    

##  Parameters

`action`

    

A closure that SwiftUI invokes when elements in the dynamic view are moved.
The closure takes two arguments that represent the offset relative to the
dynamic view’s underlying collection of data. Pass `nil` to disable the
ability to move items.

## Return Value

A view that calls `action` when elements are moved within the original view.

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# dropDestination(for:action:)

Sets the insert action for the dynamic view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], Int) -> Void
    ) -> some DynamicViewContent where T : Transferable
    

##  Parameters

`payloadType`

    

Type of the models that are dropped.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `Transferable` items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Discussion

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func onInsert(
        of acceptedTypeIdentifiers: [String],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> some DynamicViewContent
    

Deprecated

Use `onInsert(of:perform:)` instead.

##  Parameters

`acceptedTypeIdentifiers`

    

An array of UTI types that the dynamic view supports.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `NSItemProvider` that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

