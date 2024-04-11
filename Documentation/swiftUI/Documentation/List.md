Initializer

# init(content:)

Creates a list with the given content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(@ViewBuilder content: () -> Content)

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

macOS 13.0+

    
    
    @MainActor
    init(
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a selected row.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        selection: Binding<SelectionValue?>?,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a selected row.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init(
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a set that identifies selected rows.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

Initializer

# init(_:rowContent:)

Creates a list that computes its views on demand over a constant range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single element.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select
multiple elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select
multiple elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and selects
a single row.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Instance Property

# body

The content of the list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var body: some View { get }

