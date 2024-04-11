Initializer

# init(_:content:)

Creates an instance that uniquely identifies and creates table columns across
updates based on the identity of the underlying data.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    init(
        _ data: Data,
        @TableColumnBuilder<TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Data.Element) -> Content
    ) where ID == Data.Element.ID, Data.Element : Identifiable

##  Parameters

`data`

    

The identified data that the `TableColumnForEach` instance uses to create
table columns dynamically.

`content`

    

The table column builder that creates columns dynamically for each element.

## See Also

### Creating the collection

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table columns on demand over a given
constant range.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the provided key path to the underlying data’s identifier.

Initializer

# init(_:content:)

Creates an instance that computes table columns on demand over a given
constant range.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    init(
        _ data: Range<Int>,
        @TableColumnBuilder<TableColumnForEach<Range<Int>, Int, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Range<Int>, Int, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Int) -> Content
    ) where Data == Range<Int>, ID == Int

##  Parameters

`data`

    

A constant range.

`content`

    

The table column builder that creates columns based on the range index.

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t
need to identify columns across updates. To compute columns on demand over a
dynamic range, use `init(_:id:content:)`.

## See Also

### Creating the collection

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the identity of the underlying data.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the provided key path to the underlying data’s identifier.

Initializer

# init(_:id:content:)

Creates an instance that uniquely identifies and creates table columns across
updates based on the provided key path to the underlying data’s identifier.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    init(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @TableColumnBuilder<TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Data.Element) -> Content
    )

##  Parameters

`data`

    

The data that the `TableColumnForEach` instance uses to create table columns
dynamically.

`id`

    

The key path to the provided data’s identifier.

`content`

    

The table column builder that creates columns dynamically for each element.

## See Also

### Creating the collection

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the identity of the underlying data.

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table columns on demand over a given
constant range.

Instance Property

# content

A function to create content on demand using the underlying data.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    var content: (Data.Element) -> Content

## See Also

### Accessing collection content

`var data: Data`

The collection of underlying identified data that SwiftUI uses to create
columns dynamically.

Instance Property

# data

The collection of underlying identified data that SwiftUI uses to create
columns dynamically.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    var data: Data

## See Also

### Accessing collection content

`var content: (Data.Element) -> Content`

A function to create content on demand using the underlying data.

