Structure

# Table

A container that presents rows of data arranged in one or more columns,
optionally providing the ability to select one or more members.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct Table<Value, Rows, Columns> where Value == Rows.TableRowValue, Rows : TableRowContent, Columns : TableColumnContent, Rows.TableRowValue == Columns.TableRowValue

## Overview

You commonly create tables from collections of data. The following example
shows how to create a simple, three-column table from an array of `Person`
instances that conform to the `Identifiable` protocol:

If there are more rows than can fit in the available space, `Table` provides
vertical scrolling automatically. On macOS, the table also provides horizontal
scrolling if there are more columns than can fit in the width of the view.
Scroll bars appear as needed on iOS; on macOS, the `Table` shows or hides
scroll bars based on the “Show scroll bars” system preference.

### Supporting selection in tables

To make rows of a table selectable, provide a binding to a selection variable.
Binding to a single instance of the table data’s `id` type creates a single-
selection table. Binding to a `Set` creates a table that supports multiple
selections. The following example shows how to add multi-select to the
previous example. A `Text` view below the table shows the number of items
currently selected.

### Supporting sorting in tables

To make the columns of a table sortable, provide a binding to an array of
`SortComparator` instances. The table reflects the sorted state through its
column headers, allowing sorting for any columns with key paths.

When the table sort descriptors update, re-sort the data collection that
underlies the table; the table itself doesn’t perform a sort operation. You
can watch for changes in the sort descriptors by using a
`onChange(of:perform:)` modifier, and then sort the data in the modifier’s
`perform` closure.

The following example shows how to add sorting capability to the previous
example:

### Building tables with static rows

To create a table from static rows, rather than the contents of a collection
of data, you provide both the columns and the rows.

The following example shows a table that calculates prices from applying
varying gratuities (“tips”) to a fixed set of prices. It creates the table
with the `init(of:columns:rows:)` initializer, with the `rows` parameter
providing the base price that each row uses for its calculations. Each column
receives each price and performs its calculation, producing a `Text` to
display the formatted result.

### Styling tables

Use the `tableStyle(_:)` modifier to set a `TableStyle` for all tables within
a view. SwiftUI provides several table styles, such as `InsetTableStyle` and,
on macOS, `BorderedTableStyle`. The default style is `AutomaticTableStyle`,
which is available on all platforms that support `Table`.

### Using tables on different platforms

You can define a single table for use on macOS, iOS, and iPadOS. However, in a
compact horizontal size class environment — typical on iPhone or on iPad in
certain modes, like Slide Over — the table has limited space to display its
columns. To conserve space, the table automatically hides headers and all
columns after the first when it detects this condition.

To provide a good user experience in a space-constrained environment, you can
customize the first column to show more information when you detect that the
`horizontalSizeClass` environment value becomes
`UserInterfaceSizeClass.compact`. For example, you can modify the sortable
table from above to conditionally show all the information in the first
column:

By making this change, you provide a list-like appearance for narrower
displays, while displaying the full table on wider ones. Because you use the
same table instance in both cases, you get a seamless transition when the size
class changes, like when someone moves your app into or out of Slide Over.

## Topics

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

`init<Data>(Data, selection: Binding<Set<Value.ID>>, columns: () -> Columns)`

Creates a table that computes its rows based on a collection of identifiable
data, and that supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init<Data, Sort>(Data, selection: Binding<Set<Value.ID>>, sortOrder:
Binding<[Sort]>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data, and supports selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init(of: Value.Type, selection: Binding<Value.ID?>, columns: () -> Columns,
rows: () -> Rows)`

Creates a table with the given columns and rows that supports selecting zero
or one row that generates its data using values of the given type.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init<Sort>(selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>,
columns: () -> Columns, rows: () -> Rows)`

Creates a sortable table with the given columns and rows that supports
selecting multiple rows.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns)`

Creates a sortable table that computes its rows based on a collection of
identifiable data and has dynamically customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () ->
Rows)`

Creates a sortable table with the given columns and rows and has dynamically
customizable columns.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

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

`init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder:
Binding<[Sort]>, columnCustomization:
Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)`

Creates a sortable, hierarchical table that computes its rows based on a
collection of identifiable data and key path to the children of that data.

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to
`TableRowContent`, `Columns` conforms to `TableColumnContent`, and
`Rows.TableRowValue` is `Columns.TableRowValue`.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a table

Building a Great Mac App with SwiftUI

Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars,
and several other popular user interface elements.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

Instance Method

# tableStyle(_:)

Sets the style for tables within this view.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func tableStyle<S>(_ style: S) -> some View where S : TableStyle
    

## See Also

### Creating a table

Building a Great Mac App with SwiftUI

Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars,
and several other popular user interface elements.

`struct Table`

A container that presents rows of data arranged in one or more columns,
optionally providing the ability to select one or more members.

Structure

# TableColumn

A column that displays a view for each row in a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct TableColumn<RowValue, Sort, Content, Label> where RowValue : Identifiable, Sort : SortComparator, Content : View, Label : View

## Overview

You create a column with a label, content view, and optional key path. The
table calls the content view builder with the value for each row in the table.
The column uses a key path to map to a property of each row value, which
sortable tables use to reflect the current sort order.

The following example creates a sortable column for a table with `Person`
rows, displaying each person’s given name:

For the common case of `String` properties, you can use the convenience
initializer that doesn’t require an explicit content closure and displays that
string verbatim as a `Text` view. This means you can write the previous
example as:

## Topics

### Creating an unsortable column

`init(LocalizedStringKey, value: KeyPath<RowValue, String>)`

Creates an unsortable column that displays a string property that generates
its label from a localized string key.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, String>)`

Creates an unsortable column that displays a string property that generates
its label from a string.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, String>)`

Creates an unsortable column that displays a string property with a text
label.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init(LocalizedStringKey, content: (RowValue) -> Content)`

Creates an unsortable column that generates its label from a localized string
key.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init<S>(S, content: (RowValue) -> Content)`

Creates an unsortable column that generates its label from a string.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init(Text, content: (RowValue) -> Content)`

Creates an unsortable column with a text label

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

### Creating a column with strings

`init(LocalizedStringKey, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates a sortable column that displays a string property, and generates its
label from a localized string key.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<S>(S, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates a sortable column that displays a string property, and generates its
label from a string.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init(Text, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates a sortable column that displays a string property and has a text
label.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates an unsortable column that displays a string property, and which
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates a sortable column that displays a string property, and which generates
its label from a string.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates an unsortable column that displays a string property and has a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a localized string
key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, String?>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a localized string
key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, String?>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, String?>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int>, content: (RowValue)
-> Content)`

Creates a sortable column for integer values that generates its label from a
localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int>, content: (RowValue) -> Content)`

Creates a sortable column for integer values that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int>, content: (RowValue) -> Content)`

Creates a sortable column for integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Int?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int?>, content: (RowValue) -> Content)`

Creates a sortable column for optional integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int?>, content: (RowValue) -> Content)`

Creates a sortable column for optional integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt>, content: (RowValue)
-> Content)`

Creates a sortable column for unsigned integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional unsigned integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with 64-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int64>, content: (RowValue)
-> Content)`

Creates a sortable column for 64-bit integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int64>, content: (RowValue) -> Content)`

Creates a sortable column for 64-bit integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int64>, content: (RowValue) -> Content)`

Creates a sortable column for 64-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Int64?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional 64-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int64?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 64-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int64?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 64-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt64>, content:
(RowValue) -> Content)`

Creates a sortable column for unsigned 64-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt64>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 64-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt64>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 64-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt64?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional unsigned 64-bit integer values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt64?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 64-bit integer values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt64?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 64-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with 32-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int32>, content: (RowValue)
-> Content)`

Creates a sortable column for 32-bit integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int32>, content: (RowValue) -> Content)`

Creates a sortable column for 32-bit integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int32>, content: (RowValue) -> Content)`

Creates a sortable column for 32-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Int32?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional 32-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int32?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 32-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int32?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 32-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt32>, content:
(RowValue) -> Content)`

Creates a sortable column for unsigned 32-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt32>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 32-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt32>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 32-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt32?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional unsigned 32-bit integer values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt32?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 32-bit integer values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt32?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 32-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with 16-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int16>, content: (RowValue)
-> Content)`

Creates a sortable column for 16-bit integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int16>, content: (RowValue) -> Content)`

Creates a sortable column for 16-bit integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int16>, content: (RowValue) -> Content)`

Creates a sortable column for 16-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Int16?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional 16-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int16?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 16-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int16?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 16-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt16>, content:
(RowValue) -> Content)`

Creates a sortable column for unsigned 16-bit integer values that generates
its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt16>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 16-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt16>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 16-bit integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt16?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional unsigned 16-bit integer values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt16?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 16-bit integer values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt16?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 16-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with 8-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int8>, content: (RowValue)
-> Content)`

Creates a sortable column for 8-bit integer values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int8>, content: (RowValue) -> Content)`

Creates a sortable column for 8-bit integer values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int8>, content: (RowValue) -> Content)`

Creates a sortable column for 8-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Int8?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional 8-bit integer values that generates its
label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Int8?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 8-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Int8?>, content: (RowValue) -> Content)`

Creates a sortable column for optional 8-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt8>, content: (RowValue)
-> Content)`

Creates a sortable column for unsigned 8-bit integer values that generates its
label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt8>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 8-bit integer values that displays a
string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt8>, content: (RowValue) -> Content)`

Creates a sortable column for unsigned 8-bit integer values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UInt8?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional unsigned 8-bit integer values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UInt8?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned 8-bit integer values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UInt8?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned 8-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with Booleans

`init(LocalizedStringKey, value: KeyPath<RowValue, Bool>, content: (RowValue)
-> Content)`

Creates a sortable column for Boolean values that generates its label from a
localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Bool>, content: (RowValue) -> Content)`

Creates a sortable column for Boolean values that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Bool>, content: (RowValue) -> Content)`

Creates a sortable column for Boolean values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Bool?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional Boolean values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Bool?>, content: (RowValue) -> Content)`

Creates a sortable column for optional Boolean values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Bool?>, content: (RowValue) -> Content)`

Creates a sortable column for optional Boolean values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with floats

`init(LocalizedStringKey, value: KeyPath<RowValue, Float>, content: (RowValue)
-> Content)`

Creates a sortable column for single-precision floating-point values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Float>, content: (RowValue) -> Content)`

Creates a sortable column for single-precision floating-point values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Float>, content: (RowValue) -> Content)`

Creates a sortable column for single-precision floating-point values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Float?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional single-precision floating-point values
that generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Float?>, content: (RowValue) -> Content)`

Creates a sortable column for optional single-precision floating-point values
that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Float?>, content: (RowValue) -> Content)`

Creates a sortable column for optional single-precision floating-point values
with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with doubles

`init(LocalizedStringKey, value: KeyPath<RowValue, Double>, content:
(RowValue) -> Content)`

Creates a sortable column for double-precision floating-point values that
generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Double>, content: (RowValue) -> Content)`

Creates a sortable column for double-precision floating-point values that
displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Double>, content: (RowValue) -> Content)`

Creates a sortable column for double-precision floating-point values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Double?>, content:
(RowValue) -> Content)`

Creates a sortable column for optional double-precision floating-point values
that generates its label from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Double?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional double-precision floating-point values
that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Double?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional double-precision floating-point values
with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with dates

`init(LocalizedStringKey, value: KeyPath<RowValue, Date>, content: (RowValue)
-> Content)`

Creates a sortable column for date values that generates its label from a
localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Date>, content: (RowValue) -> Content)`

Creates a sortable column for date values that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Date>, content: (RowValue) -> Content)`

Creates a sortable column for date values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, Date?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional date values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, Date?>, content: (RowValue) -> Content)`

Creates a sortable column for optional date values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, Date?>, content: (RowValue) -> Content)`

Creates a sortable column for optional date values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with UUIDs

`init(LocalizedStringKey, value: KeyPath<RowValue, UUID>, content: (RowValue)
-> Content)`

Creates a sortable column for UUID values that generates its label from a
localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UUID>, content: (RowValue) -> Content)`

Creates a sortable column for UUID values that displays a string property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UUID>, content: (RowValue) -> Content)`

Creates a sortable column for UUID values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(LocalizedStringKey, value: KeyPath<RowValue, UUID?>, content: (RowValue)
-> Content)`

Creates a sortable column for optional UUID values that generates its label
from a localized string key.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, value: KeyPath<RowValue, UUID?>, content: (RowValue) -> Content)`

Creates a sortable column for optional UUID values that displays a string
property.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, value: KeyPath<RowValue, UUID?>, content: (RowValue) -> Content)`

Creates a sortable column for optional UUID values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

### Creating a column with comparable values

`init<V>(LocalizedStringKey, value: KeyPath<RowValue, V>, content: (RowValue)
-> Content)`

Creates a sortable column for comparable values that generates its label from
a localized string key.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<S, V>(S, value: KeyPath<RowValue, V>, content: (RowValue) -> Content)`

Creates a sortable column for comparable values that generates its label from
a string.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<V>(Text, value: KeyPath<RowValue, V>, content: (RowValue) -> Content)`

Creates a sortable column for comparable values with a text label.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<V, C>(LocalizedStringKey, value: KeyPath<RowValue, V>, comparator: C,
content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a localized string
key, and uses an explicit comparator for sorting values.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<S, V, C>(S, value: KeyPath<RowValue, V>, comparator: C, content:
(RowValue) -> Content)`

Creates a sortable column that generates its label from a string, and uses an
explicit comparator for sorting values.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

`init<V, C>(Text, value: KeyPath<RowValue, V>, comparator: C, content:
(RowValue) -> Content)`

Creates a sortable column that has a text label, and uses an explicit
comparator for sorting values.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

### Creating a column with a comparator

`init(LocalizedStringKey, sortUsing: Sort, content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a localized string
key.

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

`init<S>(S, sortUsing: Sort, content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a string.

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, sortUsing: Sort, content: (RowValue) -> Content)`

Creates a sortable column with text label.

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

### Setting the column width

`func width(CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a fixed width table column that isn’t user resizable.

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

`func width(min: CGFloat?, ideal: CGFloat?, max: CGFloat?) ->
TableColumn<RowValue, Sort, Content, Label>`

Creates a resizable table column with the provided constraints.

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

`func width() -> TableColumn<RowValue, Sort, Content, Label>`

Sets the column’s width.

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

Deprecated

## Relationships

### Conforms To

  * `TableColumnContent`

## See Also

### Creating columns

`protocol TableColumnContent`

A type used to represent columns within a table.

`struct TableColumnAlignment`

Describes the alignment of the content of a table column.

`struct TableColumnBuilder`

A result builder that creates table column content from closures.

`struct TableColumnForEach`

A structure that computes columns on demand from an underlying collection of
identified data.

Protocol

# TableColumnContent

A type used to represent columns within a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    protocol TableColumnContent<TableRowValue, TableColumnSortComparator>

## Overview

This type provides the body content of the column, as well as the types of the
column’s row values and the comparator used to sort rows.

You can factor column content out into separate types or properties, or by
creating a custom type conforming to `TableColumnContent`.

The above example factors three table columns into a separate computed
property that has an opaque type. The property’s primary associated type
`TableRowValue` is a `Person` and its associated type
`TableColumnSortComparator` is a key comparator for the `Person` type.

## Topics

### Getting the column body

`var tableColumnBody: Self.TableColumnBody`

The composition of content that comprise the table column content.

**Required**

` associatedtype TableColumnBody : TableColumnContent`

The type of content representing the body of this table column content.

**Required**

### Defining the row value

`associatedtype TableRowValue : Identifiable =
Self.TableColumnBody.TableRowValue`

The type of value of rows presented by this column content.

**Required**

### Defining the comparator

`associatedtype TableColumnSortComparator : SortComparator =
Self.TableColumnBody.TableColumnSortComparator`

The type of sort comparator associated with this table column content.

**Required**

### Configuring the content

`func alignment(TableColumnAlignment) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the alignment of the column, applying to both its column header label and
the row view content for that column.

`func customizationID(String) -> some TableColumnContent<Self.TableRowValue,
Self.TableColumnSortComparator> `

Sets the identifier to be associated with a column when persisting its state
with `TableColumnCustomization`.

`func defaultVisibility(Visibility) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the default visibility of a table column.

`func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the disabled customization behavior for a table column.

## Relationships

### Conforming Types

  * `Group`

Conforms when `Content` conforms to `TableColumnContent`.

  * `TableColumn`
  * `TableColumnForEach`
  * `TupleTableColumnContent`

## See Also

### Creating columns

`struct TableColumn`

A column that displays a view for each row in a table.

`struct TableColumnAlignment`

Describes the alignment of the content of a table column.

`struct TableColumnBuilder`

A result builder that creates table column content from closures.

`struct TableColumnForEach`

A structure that computes columns on demand from an underlying collection of
identified data.

Structure

# TableColumnAlignment

Describes the alignment of the content of a table column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TableColumnAlignment

## Overview

The alignment of a column applies to both its header label as well as the
default alignment of its content view for each row.

## Topics

### Getting the alignment

`static var automatic: TableColumnAlignment`

The default column alignment.

`static var leading: TableColumnAlignment`

Leading column alignment.

`static var center: TableColumnAlignment`

Center column alignment.

`static var trailing: TableColumnAlignment`

Trailing column alignment.

`static var numeric: TableColumnAlignment`

Column alignment appropriate for numeric content.

`static func numeric(Locale.NumberingSystem) -> TableColumnAlignment`

Column alignment appropriate for numeric content.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating columns

`struct TableColumn`

A column that displays a view for each row in a table.

`protocol TableColumnContent`

A type used to represent columns within a table.

`struct TableColumnBuilder`

A result builder that creates table column content from closures.

`struct TableColumnForEach`

A structure that computes columns on demand from an underlying collection of
identified data.

Structure

# TableColumnBuilder

A result builder that creates table column content from closures.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct TableColumnBuilder<RowValue, Sort> where RowValue : Identifiable, Sort : SortComparator

## Overview

The `buildBlock` methods in this type create `TableColumnContent` instances
based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `columns`
parameter of the various `Table` initializers with the `@TableColumnBuilder`
annotation, implicitly calling this builder for you.

## Topics

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

`static func buildExpression<Content, Label>(TableColumn<RowValue, Never,
Content, Label>) -> TableColumn<RowValue, Never, Content, Label>`

Creates a sortable table column expression whose value type matches that of
the builder.

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

`static func buildExpression<Content, Label>(TableColumn<RowValue, Sort,
Content, Label>) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a sortable table column expression whose value and sort types match
those of the builder.

### Supporting types

`struct TupleTableColumnContent`

A type of table column content that creates table columns created from a Swift
tuple of table columns.

### Type Methods

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Creates a column result for the first of two column content alternatives.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Creates a row result for the second of two row content alternatives.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

`static func buildIf<C>(C?) -> C?`

Creates a column result for conditional statements.

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to
`SortComparator`.

## See Also

### Creating columns

`struct TableColumn`

A column that displays a view for each row in a table.

`protocol TableColumnContent`

A type used to represent columns within a table.

`struct TableColumnAlignment`

Describes the alignment of the content of a table column.

`struct TableColumnForEach`

A structure that computes columns on demand from an underlying collection of
identified data.

Structure

# TableColumnForEach

A structure that computes columns on demand from an underlying collection of
identified data.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  visionOS 1.1+

    
    
    struct TableColumnForEach<Data, ID, RowValue, Sort, Content> where Data : RandomAccessCollection, ID : Hashable, RowValue == Content.TableRowValue, Sort == Content.TableColumnSortComparator, Content : TableColumnContent

## Overview

Use `TableColumnForEach` to create columns based on a `RandomAccessCollection`
of some data type. Either the collection’s elements must conform to
`Identifiable` or you need to provide an `id` parameter to the
`TableColumnForEach` initializer.

The following example shows the interface for an `AudioSampleTrack`, which h
as a collection of `AudioSample` across a dynamic number of `AudioChannel`s.
The `Table` is created for displaying rows for each sample. It has one static
column for the sample’s timestamp and uses a `TableColumnForEach` instance to
produce a column for each of the audio channels in the track.

## Topics

### Creating the collection

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the identity of the underlying data.

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table columns on demand over a given
constant range.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table columns across
updates based on the provided key path to the underlying data’s identifier.

### Accessing collection content

`var content: (Data.Element) -> Content`

A function to create content on demand using the underlying data.

`var data: Data`

The collection of underlying identified data that SwiftUI uses to create
columns dynamically.

## Relationships

### Conforms To

  * `TableColumnContent`

## See Also

### Creating columns

`struct TableColumn`

A column that displays a view for each row in a table.

`protocol TableColumnContent`

A type used to represent columns within a table.

`struct TableColumnAlignment`

Describes the alignment of the content of a table column.

`struct TableColumnBuilder`

A result builder that creates table column content from closures.

Instance Method

# tableColumnHeaders(_:)

Controls the visibility of a `Table`’s column header views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func tableColumnHeaders(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value of `visible` will show table columns, `hidden` will remove them, and
`automatic` will defer to default behavior.

## Discussion

By default, `Table` will display a global header view with the labels of each
table column. This area is also where users can sort, resize, and rearrange
the columns. For simple cases that don’t require those features, this header
can be hidden.

This will not affect the header of any `Section`s in a table.

## See Also

### Customizing columns

`struct TableColumnCustomization`

A representation of the state of the columns in a table.

`struct TableColumnCustomizationBehavior`

A set of customization behaviors of a column that a table can offer to a user.

Structure

# TableColumnCustomization

A representation of the state of the columns in a table.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TableColumnCustomization<RowValue> where RowValue : Identifiable

## Overview

`TableColumnCustomization` can be created and provided to a table to enable
column reordering and column visibility. The state can be queried and updated
programmatically, as well as bound to persistent app or scene storage.

The above example creates a table with three columns. On macOS, these columns
can be reordered or hidden and shown by the user of the app. Their
configuration will be saved and restored with the window on relaunches of the
app, using the “BugReportTableConfig” scene storage identifier.

The state of a specific column is stored relative to its customization
identifier, using using the value from the `customizationID(_:)` modifier.
When column customization is encoded and decoded, it relies on stable
identifiers to restore the associate the saved state with a specific column.
If a table column does not have a customization identifier, it will not be
customizable.

These identifiers can also be used to programmatically change column
customizations, such as programmatically hiding a column:

With a binding to the overall customization, a binding to the visibility of a
column can be accessed using the same subscript syntax:

## Topics

### Creating a table column customization

`init()`

Creates an empty table column customization.

### Managing the customization

`func resetOrder()`

Resets the column order back to the default, preserving the customized
visibility and size.

`subscript(visibility _: String) -> Visibility`

The visibility of the column identified by its identifier.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Sendable`

## See Also

### Customizing columns

`func tableColumnHeaders(Visibility) -> some View`

Controls the visibility of a `Table`’s column header views.

`struct TableColumnCustomizationBehavior`

A set of customization behaviors of a column that a table can offer to a user.

Structure

# TableColumnCustomizationBehavior

A set of customization behaviors of a column that a table can offer to a user.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TableColumnCustomizationBehavior

## Overview

This is used as a value provided to `disabledCustomizationBehavior(_:)`.

Setting any of these values as the `disabledCustomizationBehavior(_:)` doesn’t
have any effect on iOS.

## Topics

### Getting the customization behavior

`static var all: TableColumnCustomizationBehavior`

All customization behaviors.

`static let reorder: TableColumnCustomizationBehavior`

A behavior that allows the column to be reordered by the user.

`static let resize: TableColumnCustomizationBehavior`

A behavior that allows the column to be resized by the user.

`static let visibility: TableColumnCustomizationBehavior`

A behavior that allows the column to be hidden or revealed by the user.

### Creating a behavior

`init()`

Creates an empty customization behavior, representing no customization

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Customizing columns

`func tableColumnHeaders(Visibility) -> some View`

Controls the visibility of a `Table`’s column header views.

`struct TableColumnCustomization`

A representation of the state of the columns in a table.

Structure

# TableRow

A row that represents a data value in a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct TableRow<Value> where Value : Identifiable

## Overview

Create instances of `TableRow` in the closure you provide to the `rows`
parameter in `Table` initializers that take columns and rows. The table
provides the value of a row to each column of a table, which produces the
cells for each row in the column.

## Topics

### Creating a row

`init(Value)`

Creates a table row for the given value.

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Creating rows

`protocol TableRowContent`

A type used to represent table rows.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Protocol

# TableRowContent

A type used to represent table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    protocol TableRowContent<TableRowValue>

## Overview

Like with the `View` protocol, you can create custom table row content by
declaring a type that conforms to the `TableRowContent` protocol and
implementing the required `tableRowBody` property.

This example uses an opaque result type and specifies that the primary
associated type `TableRowValue` for the `tableRowBody` property is a `Person`.
From this, SwiftUI can infer `TableRowValue` for the `GroupOfPeopleRows`
structure is also `Person`.

## Topics

### Getting the row body

`var tableRowBody: Self.TableRowBody`

The composition of content that comprise the table row content.

**Required**

` associatedtype TableRowBody : TableRowContent`

The type of content representing the body of this table row content.

**Required**

### Defining the row value

`associatedtype TableRowValue : Identifiable =
Self.TableRowBody.TableRowValue`

The type of value represented by this table row content.

**Required**

### Managing interaction

`func draggable<T>(() -> T) -> some TableRowContent<Self.TableRowValue> `

Activates this row as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

`func onHover(perform: (Bool) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Adds an action to perform when the pointer moves onto or away from the entire
row.

`func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self,
ItemProviderTableRowModifier>`

Provides a closure that vends the drag representation for a particular data
element.

`struct ItemProviderTableRowModifier`

A table row modifier that associates an item provider with some base row
content.

### Adding a context menu to a row

`func contextMenu<M>(menuItems: () -> M) -> ModifiedContent<Self,
_ContextMenuTableRowModifier<M>>`

Adds a context menu to a table row.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) ->
ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>>`

Adds a context menu with a preview to a table row.

### Instance Methods

`func selectionDisabled(Bool) -> some TableRowContent<Self.TableRowValue> `

Adds a condition that controls whether users can select this row.

## Relationships

### Inherited By

  * `DynamicTableRowContent`

### Conforming Types

  * `DisclosureTableRow`
  * `EmptyTableRowContent`

Conforms when `Value` conforms to `Identifiable`.

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `Group`

Conforms when `Content` conforms to `TableRowContent`.

  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicTableRowContent` and `Modifier`
conforms to `_TableRowContentModifier`.

  * `OutlineGroup`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

  * `Section`

Conforms when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

  * `TableForEachContent`
  * `TableHeaderRowContent`
  * `TableOutlineGroupContent`
  * `TableRow`
  * `TupleTableRowContent`

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

Available when `Value` conforms to `Identifiable`.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Structure

# TableHeaderRowContent

A table row that displays a single view instead of columned content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct TableHeaderRowContent<Value, Content> where Value : Identifiable, Content : View

## Overview

You do not create this type directly. The framework creates it on your behalf.

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Structure

# TupleTableRowContent

A type of table column content that creates table rows created from a Swift
tuple of table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @frozen
    struct TupleTableRowContent<Value, T> where Value : Identifiable

## Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return
value from the various `buildBlock` methods in `TableRowBuilder`. The size of
the tuple corresponds to how many columns you create in the `rows` closure you
provide to the `Table` initializer.

## Topics

### Accessing the value

`var value: T`

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Structure

# TableForEachContent

A type of table row content that creates table rows created by iterating over
a collection.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct TableForEachContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable

## Overview

You don’t use this type directly. The various `Table.init(_:,...)`
initializers create this type as the table’s `Rows` generic type.

To explicitly create dynamic collection-based rows, use `ForEach` instead.

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Structure

# EmptyTableRowContent

A table row content that doesn’t produce any rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct EmptyTableRowContent<Value> where Value : Identifiable

## Overview

You will rarely, if ever, need to create an `EmptyTableRowContent` directly.
Instead, `EmptyTableRowContent` represents the absence of a row.

## Relationships

### Conforms To

  * `TableRowContent`

Conforms when `Value` conforms to `Identifiable`.

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

Available when `Value` conforms to `Identifiable`.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Protocol

# DynamicTableRowContent

A type of table row content that generates table rows from an underlying
collection of data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    protocol DynamicTableRowContent : TableRowContent

## Overview

This table row content type provides drag-and-drop support for tables. Use the
`onInsert(of:perform:)` modifier to add an action to call when the table
inserts new contents into its underlying collection.

## Topics

### Getting row data

`var data: Self.Data`

The collection of underlying data.

**Required**

` associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

### Inserting rows

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) ->
ModifiedContent<Self, OnInsertTableRowModifier>`

Sets the insert action for the dynamic table rows.

`struct OnInsertTableRowModifier`

A table row modifier that adds the ability to insert data in some base row
content.

### Supporting drag and drop

`func dropDestination<T>(for: T.Type, action: (Int, [T]) -> Void) ->
ModifiedContent<Self, OnInsertTableRowModifier>`

Sets the insert action for the dynamic table rows.

## Relationships

### Inherits From

  * `TableRowContent`

### Conforming Types

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicTableRowContent` and `Modifier`
conforms to `_TableRowContentModifier`.

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`struct TableRowBuilder`

A result builder that creates table row content from closures.

Structure

# TableRowBuilder

A result builder that creates table row content from closures.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct TableRowBuilder<Value> where Value : Identifiable

## Overview

The `buildBlock` methods in this type create `TableRowContent` instances based
on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `rows` parameter
of the various `Table` initializers with the `@TableRowBuilder` annotation,
implicitly calling this builder for you.

## Topics

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

### Building a row from conditionals

`static func buildIf<C>(C?) -> C?`

Creates a row result for conditional statements.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Creates a row result for the first of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Creates a row result for the second of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

## See Also

### Creating rows

`struct TableRow`

A row that represents a data value in a table.

`protocol TableRowContent`

A type used to represent table rows.

`struct TableHeaderRowContent`

A table row that displays a single view instead of columned content.

`struct TupleTableRowContent`

A type of table column content that creates table rows created from a Swift
tuple of table rows.

`struct TableForEachContent`

A type of table row content that creates table rows created by iterating over
a collection.

`struct EmptyTableRowContent`

A table row content that doesn’t produce any rows.

`protocol DynamicTableRowContent`

A type of table row content that generates table rows from an underlying
collection of data.

Structure

# DisclosureTableRow

A kind of table row that shows or hides additional rows based on the state of
a disclosure control.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DisclosureTableRow<Label, Content> where Label : TableRowContent, Content : TableRowContent, Label.TableRowValue == Content.TableRowValue

## Overview

A disclosure group row consists of a label row that is always visible, and
some content rows that are conditionally visible depending on the state.
Toggling the control will flip the state between “expanded” and “collapsed”.

In the following example, a disclosure group has `allDevices` as the label
row, and exposes its expanded state with the bound property, `expanded`. Upon
toggling the disclosure control, the user can update the expanded state which
will in turn show or hide the three content rows for `iPhone`, `iPad`, and
`Mac`.

## Topics

### Creating a disclosure table row

`init<Value>(Value, isExpanded: Binding<Bool>?, content: () -> Content)`

Creates a disclosure group with the given value and table rows, and a binding
to the expansion state (expanded or collapsed).

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Adding progressive disclosure

`struct TableOutlineGroupContent`

An opaque table row type created by a table’s hierarchical initializers.

Structure

# TableOutlineGroupContent

An opaque table row type created by a table’s hierarchical initializers.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TableOutlineGroupContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable

## Overview

This row content is created by `Table.init(_:,children:,...)` initializers as
the table’s `Rows` generic type.

To explicitly create hierarchical rows, use `OutlineGroup` instead.

## Relationships

### Conforms To

  * `TableRowContent`

## See Also

### Adding progressive disclosure

`struct DisclosureTableRow`

A kind of table row that shows or hides additional rows based on the state of
a disclosure control.

