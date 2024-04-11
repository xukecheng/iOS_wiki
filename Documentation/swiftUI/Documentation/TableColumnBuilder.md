Type Method

# buildBlock(_:)

Creates a single, unsortable column result.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never

## See Also

### Building an unsortable column

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:)

Creates an unsortable column result from two sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:)

Creates an unsortable column result from three sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:)

Creates an unsortable column result from four sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:)

Creates an unsortable column result from five sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:_:)

Creates an unsortable column result from six sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

Creates an unsortable column result from seven sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

Creates an unsortable column result from eight sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6, C7)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never, C6.TableRowValue == C7.TableRowValue, C7.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

Creates an unsortable column result from nine sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6, C7, C8)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C8 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never, C6.TableRowValue == C7.TableRowValue, C7.TableColumnSortComparator == Never, C7.TableRowValue == C8.TableRowValue, C8.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

Creates an unsortable column result from ten sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C8 : TableColumnContent, C9 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never, C6.TableRowValue == C7.TableRowValue, C7.TableColumnSortComparator == Never, C7.TableRowValue == C8.TableRowValue, C8.TableColumnSortComparator == Never, C8.TableRowValue == C9.TableRowValue, C9.TableColumnSortComparator == Never

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildExpression(_:)

Creates a generic, unsortable single column expression.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

Type Method

# buildExpression(_:)

Creates a sortable table column expression whose value type matches that of
the builder.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Never, Content, Label>) -> TableColumn<RowValue, Never, Content, Label> where Content : View, Label : View

## See Also

### Building an unsortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, unsortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Never, (C0, C1)>`

Creates an unsortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2)>`

Creates an unsortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3)>`

Creates an unsortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4)>`

Creates an unsortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)>`

Creates an unsortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)>`

Creates an unsortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates an unsortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates an unsortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Never, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates an unsortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, unsortable single column expression.

Type Method

# buildBlock(_:)

Creates a single, sortable column result.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Sort == Column.TableColumnSortComparator, Column : TableColumnContent

## See Also

### Building a sortable column

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:)

Creates a sortable column result from two sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableRowValue == C1.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:)

Creates a sortable column result from three sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:)

Creates a sortable column result from four sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:)

Creates a sortable column result from five sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:_:)

Creates a sortable column result from six sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

Creates a sortable column result from seven sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

Creates a sortable column result from eight sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6, C7)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

Creates a sortable column result from nine sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6, C7, C8)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C8 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue, C7.TableRowValue == C8.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

Creates a sortable column result from ten sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C8 : TableColumnContent, C9 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue, C7.TableRowValue == C8.TableRowValue, C8.TableRowValue == C9.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildExpression(_:)

Creates a generic, sortable single column expression.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Sort == Column.TableColumnSortComparator, Column : TableColumnContent

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

Type Method

# buildExpression(_:)

Creates a sortable table column expression whose value and sort types match
those of the builder.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Sort, Content, Label>) -> TableColumn<RowValue, Sort, Content, Label> where Content : View, Label : View

## See Also

### Building a sortable column

`static func buildBlock<Column>(Column) -> Column`

Creates a single, sortable column result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableColumnContent<RowValue,
Sort, (C0, C1)>`

Creates a sortable column result from two sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)>`

Creates a sortable column result from three sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3)>`

Creates a sortable column result from four sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4)>`

Creates a sortable column result from five sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)>`

Creates a sortable column result from six sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a sortable column result from seven sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4,
C5, C6, C7)>`

Creates a sortable column result from eight sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2,
C3, C4, C5, C6, C7, C8)>`

Creates a sortable column result from nine sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableColumnContent<RowValue, Sort, (C0,
C1, C2, C3, C4, C5, C6, C7, C8, C9)>`

Creates a sortable column result from ten sources.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildExpression<Column>(Column) -> Column`

Creates a generic, sortable single column expression.

Structure

# TupleTableColumnContent

A type of table column content that creates table columns created from a Swift
tuple of table columns.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @frozen
    struct TupleTableColumnContent<RowValue, Sort, T> where RowValue : Identifiable, Sort : SortComparator

## Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return
value from the various `buildBlock` methods in `TableColumnBuilder`. The size
of the tuple corresponds to how many columns you create in the `columns`
closure you provide to the `Table` initializer.

## Topics

### Accessing the value

`var value: T`

The value of a row presented by this column content.

## Relationships

### Conforms To

  * `TableColumnContent`

Type Method

# buildEither(first:)

Creates a column result for the first of two column content alternatives.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, Sort == T.TableColumnSortComparator, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == F.TableColumnSortComparator, T.TableRowValue == F.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing conditional content for the “then” branch.

Type Method

# buildEither(second:)

Creates a row result for the second of two row content alternatives.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, Sort == T.TableColumnSortComparator, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == F.TableColumnSortComparator, T.TableRowValue == F.TableRowValue

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing conditional content for the “else” branch.

Type Method

# buildIf(_:)

Creates a column result for conditional statements.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    static func buildIf<C>(_ content: C?) -> C? where RowValue == C.TableRowValue, Sort == C.TableColumnSortComparator, C : TableColumnContent

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing an optional value that is visible only when the condition evaluates
to `true`.

