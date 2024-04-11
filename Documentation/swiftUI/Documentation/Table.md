Initializer

# init(_:columns:)

Creates a table that computes its rows based on a collection of identifiable
data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`columns`

    

The columns to display in the table.

## See Also

### Creating a table from columns

`init<Data>(Data, selection: Binding<Value.ID?>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:columns:)

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting zero or one row.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        selection: Binding<Value.ID?>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to the optional selected row ID.

`columns`

    

The columns to display in the table.

## See Also

### Creating a table from columns

`init<Data>(Data, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:columns:)

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        selection: Binding<Set<Value.ID>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to a set that identifies selected rows IDs.

`columns`

    

The columns to display in the table.

## See Also

### Creating a table from columns

`init<Data>(Data, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Value.ID?>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:sortOrder:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

## See Also

### Creating a sortable table from columns

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:sortOrder:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting zero or one row.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

## See Also

### Creating a sortable table from columns

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:sortOrder:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to a set that identifies selected rows IDs.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

## See Also

### Creating a sortable table from columns

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:columns:rows:)

Creates a table with the given columns and rows that generates its contents
using values of the given type.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a table from columns and rows

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columns: () ->
Columns, rows: () -> Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columns: () -> Columns,
rows: () -> Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:columns:rows:)

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        selection: Binding<Set<Value.ID>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to a set that identifies the selected rows IDs.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a table from columns and rows

`init(of: Value.Type, columns: () -> Columns, rows: () -> Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columns: () -> Columns,
rows: () -> Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:columns:rows:)

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        selection: Binding<Value.ID?>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to the optional selected row ID.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a table from columns and rows

`init(of: Value.Type, columns: () -> Columns, rows: () -> Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columns: () ->
Columns, rows: () -> Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type,
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () ->
Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type,
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to a set that identifies selected rows ids.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () ->
Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () ->
Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(selection:sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () ->
Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(selection:sortOrder:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<Sort>(
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`selection`

    

A binding to a set that identifies selected rows ids.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () ->
Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:columnCustomization:columns:)

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:columnCustomization:columns:)

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        selection: Binding<Value.ID?>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to the optional selected row ID.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:columnCustomization:columns:)

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        selection: Binding<Set<Value.ID>>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to a set that identifies selected rows IDs.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:sortOrder:columnCustomization:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to a set that identifies selected rows IDs.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:selection:sortOrder:columnCustomization:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:sortOrder:columnCustomization:columns:)

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with customizable columns

`init<Data>(Data, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting zero or one row, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, that supports selecting multiple rows, and that has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting multiple rows, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, supports selecting zero or one row, and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:columnCustomization:columns:rows:)

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:columnCustomization:columns:rows:)

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        selection: Binding<Set<Value.ID>>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to a set that identifies the selected rows IDs.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:columnCustomization:columns:rows:)

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init(
        of valueType: Value.Type,
        selection: Binding<Value.ID?>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Never> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    )

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to the optional selected row ID.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:sortOrder:columnCustomization:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type = Value.self,
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to a set that identifies selected rows ids.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:selection:sortOrder:columnCustomization:columns:rows:)

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type = Value.self,
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(of:sortOrder:columnCustomization:columns:rows:)

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Sort>(
        of valueType: Value.Type = Value.self,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns,
        @TableRowBuilder<Value> rows: () -> Rows
    ) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`valueType`

    

The type of value used to derive the table’s contents.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

`rows`

    

The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a table with dynamically customizable columns

`init(of: Value.Type, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that generates its contents
using values of the given type and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting
multiple rows that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init(of: Value.Type, selection: Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type and has
dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows and dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Sort>(of: Value.Type, selection: Binding<Value.ID?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows that supports
selecting zero or one row and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:columnCustomization:columns:)

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        children: KeyPath<Value, Data?>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:selection:columnCustomization:columns:)

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<Value.ID>>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`selection`

    

A binding to a set that identifies selected rows IDs.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:selection:columnCustomization:columns:)

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Value.ID?>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Never> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`selection`

    

A binding to the optional selected row ID.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:selection:sortOrder:columnCustomization:columns:)

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Value.ID?>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`selection`

    

A binding to the optional selected row ID.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:selection:sortOrder:columnCustomization:columns:)

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<Value.ID>>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`selection`

    

A binding to a set that identifies selected rows IDs.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

Initializer

# init(_:children:sortOrder:columnCustomization:columns:)

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Data, Sort>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        sortOrder: Binding<[Sort]>,
        columnCustomization: Binding<TableColumnCustomization<Value>>? = nil,
        @TableColumnBuilder<Value, Sort> columns: () -> Columns
    ) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

##  Parameters

`data`

    

The identifiable data for computing the table rows.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`,
and whose `nil` value represents a leaf row of the hierarchy, which is not
capable of having children.

`sortOrder`

    

A binding to the ordered sorting of columns.

`columnCustomization`

    

A binding to the state of columns.

`columns`

    

The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required
to have an identifier, specified with `customizationID(_:)`.

## See Also

### Creating a hierarchical table

`init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a hierarchical table that computes its rows based on a collection of
identifiable data and key path to the children of that data, and supports
selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting zero or one row.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, selection:
Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data, and
supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

