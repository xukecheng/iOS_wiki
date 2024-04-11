Article

# Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

## Overview

Displaying a collection of data in a vertical list is a common requirement in
many apps. Whether it’s a list of contacts, a schedule of events, an index of
categories, or a shopping list, you’ll often find a use for a `List`.

List views display collections of items vertically, load rows as needed, and
add scrolling when the rows don’t fit on the screen, making them suitable for
displaying large collections of data.

By default, list views also apply platform-appropriate styling to their
elements. For example, on iOS, the default configuration of a list displays a
separator line between each row, and adds disclosure indicators next to items
that initiate navigation actions.

Note

If you want to remove the platform-appropriate styling — such as row
separators or automatic disclosure indicators — from your list, consider using
`LazyVStack` instead. For more information on working with lazy stacks, see
Creating performant scrollable stacks

The code in this article shows the use of list views to display a company’s
staff directory. Each section enhances the usefulness of the list, by adding
custom cells, splitting the list into sections, and using the list selection
to navigate to a detail view.

### Prepare your data for iteration

The most common use of `List` is for representing collections of information
in your data model. The following example defines a `Person` as an
`Identifiable` type with the properties `name` and `phoneNumber`. An array
called `staff` contains two instances of this type.

To present the contents of the array as a list, the example creates a `List`
instance. The list’s content builder uses a `ForEach` to iterate over the
`staff` array. For each member of the array, the listing creates a row view by
instantiating a new `Text` that contains the name of the `Person`.

Members of a list must be uniquely identifiable from one another. Unique
identifiers allow SwiftUI to automatically generate animations for changes in
the underlying data, like inserts, deletions, and moves. Identify list members
either by using a type that conforms to `Identifiable`, as `Person` does, or
by providing an `id` parameter with the key path to a unique property of the
type. The `ForEach` that populates the list above depends on this behavior, as
do the `List` initializers that take a `RandomAccessCollection` of members to
iterate over.

Important

The values you use for `Identifiable` data must be unique. Using a `UUID` or a
database row identifier are both good choices, whereas using data like a
person’s name or phone number could potentially contain duplicates.

### Display data inside a row

Each row inside a `List` must be a SwiftUI `View`. You may be able to
represent your data with a single view such as an `Image` or `Text` view, or
you may need to define a custom view to compose several views into something
more complex.

As your row views get more sophisticated, refactor the views into separate
view structures, passing in the data that the row needs to render. The
following example defines a `PersonRowView` to create a two-line view for a
`Person`, using fonts, colors, and the system “phone” icon image to visually
style the data.

For more information on composing the types of views commonly used inside list
rows, see Building layouts with stack views.

### Represent data hierarchy with sections

`List` views can also display data with a level of hierarchy, grouping
associated data into sections.

Consider an expanded data model that represents an entire company, including
multiple departments. Each `Department` has a name and an array of `Person`
instances, and the company has an array of the `Department` type.

Use `Section` views to give the data inside a `List` a level of hierarchy.
Start by creating the `List`, using a `ForEach` to iterate over the
`company.departments` array, and then create `Section` views for each
department. Within the section’s view builder, use a `ForEach` to iterate over
the department’s `staff`, and return a customized view for each `Person`.

Note

If your data hierarchy is too deep to represent with a single level of
sections and rows, `OutlineGroup` and `DisclosureGroup` might be a better fit.
These views use a disclosure metaphor to allow the user to drill down to an
arbitrary depth in the hierarchy.

## Use Lists for Navigation

Using a `NavigationLink` within a `List` contained inside a `NavigationView`
adds platform-appropriate visual styling, and in some cases, additional
container views that provide the structure for navigation. SwiftUI uses one of
two visual presentations, based on the runtime environment:

  * A list with disclosure indicators, which performs an animated navigation to a destination scene when the user chooses a list item. SwiftUI uses this presentation on watchOS, tvOS, and on most iOS devices except as described below.

  * A two-panel split view, with the top-level data as a list on the left side and the detail on the right. To get this presentation, you also need to provide a placeholder view after the list; this placeholder fills the detail pane until the user makes a selection. SwiftUI uses this two-panel approach on macOS, iPadOS, and on iOS devices with sufficient horizontal space, as indicated by the `horizontalSizeClass` environment value.

The following example sets up a navigation-based UI by wrapping the list with
a navigation view. Instances of `NavigationLink` wrap the list’s rows to
provide a `destination` view to navigate to when the user taps the row. If a
split view navigation is appropriate for the platform, the right panel
initially contains the “No Selection” placeholder view, which the navigation
view replaces with the destination view when the user makes a selection.

In this example, the view passed in as the `destination` is a
`PersonDetailView`, which repeats the information from the list. In a more
complex app, this detail view could show more information about a `Person`
than would fit inside the list row.

On most iOS devices (those with a compact horizontal size class), the list
appears as a view by itself, and tapping a row performs an animated transition
to the destination view. The following figure shows both the list view and the
destination view that appears when the user makes a selection:

On the other hand, iPadOS and macOS show the list and the detail view together
as a multi-column view. The following figure shows what this example looks
like on macOS prior to making a selection, which means the “No selection”
placeholder view is still in the detail column.

You can use the `navigationViewStyle(_:)` view modifier to change the default
behavior of a `NavigationView`. For example, on iOS, the
`StackNavigationViewStyle` forces single-column mode, even on an iPad in
landscape orientation.

## See Also

### Creating a list

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Structure

# List

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    struct List<SelectionValue, Content> where SelectionValue : Hashable, Content : View

## Overview

In its simplest form, a `List` creates its contents statically, as shown in
the following example:

More commonly, you create lists dynamically from an underlying collection of
data. The following example shows how to create a simple list from an array of
an `Ocean` type which conforms to `Identifiable`:

### Supporting selection in lists

To make members of a list selectable, provide a binding to a selection
variable. Binding to a single instance of the list data’s `Identifiable.ID`
type creates a single-selection list. Binding to a `Set` creates a list that
supports multiple selections. The following example shows how to add
multiselect to the previous example:

When people make a single selection by tapping or clicking, the selected cell
changes its appearance to indicate the selection. To enable multiple
selections with tap gestures, put the list into edit mode by either modifying
the `editMode` value, or adding an `EditButton` to your app’s interface. When
you put the list into edit mode, the list shows a circle next to each list
item. The circle contains a checkmark when the user selects the associated
item. The example above uses an Edit button, which changes its title to Done
while in edit mode:

People can make multiple selections without needing to enter edit mode on
devices that have a keyboard and mouse or trackpad, like Mac and iPad.

### Refreshing the list content

To make the content of the list refreshable using the standard refresh
control, use the `refreshable(action:)` modifier.

The following example shows how to add a standard refresh control to a list.
When the user drags the top of the list downward, SwiftUI reveals the refresh
control and executes the specified action. Use an `await` expression inside
the `action` closure to refresh your data. The refresh indicator remains
visible for the duration of the awaited operation.

### Supporting multidimensional lists

To create two-dimensional lists, group items inside `Section` instances. The
following example creates sections named after the world’s oceans, each of
which has `Text` views named for major seas attached to those oceans. The
example also allows for selection of a single list item, identified by the
`id` of the example’s `Sea` type.

Because this example uses single selection, people can make selections outside
of edit mode on all platforms.

Note

In iOS 15, iPadOS 15, and tvOS 15 and earlier, lists support selection only in
edit mode, even for single selections.

### Creating hierarchical lists

You can also create a hierarchical list of arbitrary depth by providing tree-
structured data and a `children` parameter that provides a key path to get the
child nodes at any level. The following example uses a deeply-nested
collection of a custom `FileItem` type to simulate the contents of a file
system. The list created from this data uses collapsing cells to allow the
user to navigate the tree structure.

### Styling lists

SwiftUI chooses a display style for a list based on the platform and the view
type in which it appears. Use the `listStyle(_:)` modifier to apply a
different `ListStyle` to all lists within a view. For example, adding
`.listStyle(.plain)` to the example shown in the “Creating Multidimensional
Lists” topic applies the `plain` style, the following screenshot shows:

## Topics

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

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

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

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

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Supporting types

`var body: some View`

The content of the list.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Instance Method

# listStyle(_:)

Sets the style for lists within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listStyle<S>(_ style: S) -> some View where S : ListStyle
    

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Structure

# Section

A container view that you can use to add hierarchy within certain views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Section<Parent, Content, Footer>

## Overview

Use `Section` instances in views like `List`, `Picker`, and `Form` to organize
content into separate sections. Each section has custom content that you
provide on a per-instance basis. You can also provide headers and footers for
each section.

### Collapsible sections

Create sections that expand and collapse by using an initializer that accepts
an `isExpanded` binding. A collapsible section in a `List` that uses the
`sidebar` style shows a disclosure indicator next to the section’s header.
Tapping on the disclosure indicator toggles the appearance of the section’s
content.

Note

Not all contexts provide a default control to trigger collapse or expansion.

## Topics

### Creating a section

`init<V>(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<S>(S, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<V, S>(S, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init<V>(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

### Adding headers and footers

`init(content: () -> Content, header: () -> Parent)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init<V, H>(content: () -> Content, header: () -> H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content, footer: () -> Footer)`

Creates a section with a footer and the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

`init(content: () -> Content, header: () -> Parent, footer: () -> Footer)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

### Controlling collapsibility

`init<V, S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<V>(LocalizedStringKey, isExpanded: Binding<Bool>, content: () ->
Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init(isExpanded: Binding<Bool>, content: () -> Content, header: () ->
Parent)`

Creates a section with a header, the provided section content, and a binding
representing the section’s expansion state.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init<V, H>(isExpanded: Binding<Bool>, content: () -> Content, header: () ->
H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

### Deprecated symbols

`init(header: Parent, content: () -> Content)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

Deprecated

`init(footer: Footer, content: () -> Content)`

Creates a section with a footer and the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

`init(header: Parent, footer: Footer, content: () -> Content)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

`func collapsible(Bool) -> some View`

Sets whether a section can be collapsed by the user.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `TableRowContent`

Conforms when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

  * `View`

Conforms when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

Structure

# ForEach

A structure that computes views on demand from an underlying collection of
identified data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable

## Overview

Use `ForEach` to provide views based on a `RandomAccessCollection` of some
data type. Either the collection’s elements must conform to `Identifiable` or
you need to provide an `id` parameter to the `ForEach` initializer.

The following example creates a `NamedFont` type that conforms to
`Identifiable`, and an array of this type called `namedFonts`. A `ForEach`
instance iterates over the array, producing new `Text` instances that display
examples of each SwiftUI `Font` style provided in the array.

## Topics

### Creating a collection from a range

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes views on demand over a given constant range.

Available when `Data` is `Range<Int>`, `ID` is `Int`, and `Content` conforms
to `View`.

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

### Generating rotor content

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AccessibilityRotorContent`, and
`Data.Element` conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

### Creating a collection of table rows

`init<V>(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table rows on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

### Creating chart content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `ChartContent`, and `Data.Element`
conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `ChartContent`.

### Creating editable content

`init<C, R>(Binding<C>, editActions: EditActions<C>, content:
(Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

`init<C, R>(Binding<C>, id: KeyPath<C.Element, ID>, editActions:
EditActions<C>, content: (Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

### Creating attachment content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AttachmentContent`, and
`Data.Element` conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

### Accessing content

`var content: (Data.Element) -> Content`

A function to create content on demand using the underlying data.

`var data: Data`

The collection of underlying identified data that SwiftUI uses to create views
dynamically.

### Initializers

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes map content on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates map content across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates map content across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

### Type Aliases

`typealias Body`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

### Default Implementations

API Reference

AttachmentContent Implementations

API Reference

MapContent Implementations

## Relationships

### Conforms To

  * `AccessibilityRotorContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

  * `AttachmentContent`
  * `ChartContent`
  * `DynamicMapContent`
  * `DynamicTableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `DynamicViewContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `MapContent`
  * `TableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `View`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

## See Also

### Iterating over list content

`protocol DynamicViewContent`

A type of view that generates views from an underlying collection of data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Protocol

# DynamicViewContent

A type of view that generates views from an underlying collection of data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol DynamicViewContent : View

## Topics

### Managing the data

`var data: Self.Data`

The collection of underlying data.

**Required**

` associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

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

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

### Deprecated symbols

`func onInsert(of: [String], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Deprecated

## Relationships

### Inherits From

  * `View`

### Conforming Types

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

## See Also

### Iterating over list content

`struct ForEach`

A structure that computes views on demand from an underlying collection of
identified data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Structure

# OutlineGroup

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable

## Overview

Use an outline group when you need a view that can represent a hierarchy of
data by using disclosure views. This allows the user to navigate the tree
structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a
simplified view of a file system. Passing the root of this tree and the key
path of its children allows you to quickly create a visual representation of
the file system.

### Type parameters

Five generic type constraints define a specific `OutlineGroup` instance:

  * `Data`: The type of a collection containing the children of an element in the tree-shaped data.

  * `ID`: The type of the identifier for an element.

  * `Parent`: The type of the visual representation of an element whose children property is non-`nil`

  * `Leaf`: The type of the visual representation of an element whose children property is `nil`.

  * `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

## Topics

### Creating an outline group

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

### Creating an outline group from a binding

`init<C, E>(Binding<E>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element and a key path
to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<C>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<C, E>(Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

### Supporting types

`struct OutlineSubgroupChildren`

A type-erased view representing the children in an outline subgroup.

### Initializers

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, a key path
to the element’s identifier, as well as a key path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

## Relationships

### Conforms To

  * `TableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

  * `View`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Leaf` conforms to `View`, and
`Subgroup` conforms to `View`.

## See Also

### Disclosing information progressively

`struct DisclosureGroup`

A view that shows or hides another content view, based on the state of a
disclosure control.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

Structure

# DisclosureGroup

A view that shows or hides another content view, based on the state of a
disclosure control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DisclosureGroup<Label, Content> where Label : View, Content : View

## Overview

A disclosure group view consists of a label to identify the contents, and a
control to show and hide the contents. Showing the contents puts the
disclosure group into the “expanded” state, and hiding them makes the
disclosure group “collapsed”.

In the following example, a disclosure group contains two toggles and an
embedded disclosure group. The top level disclosure group exposes its expanded
state with the bound property, `topLevelExpanded`. By expanding the disclosure
group, the user can use the toggles to update the state of the `toggleStates`
structure.

## Topics

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

### Creating a group with a label view

`init(content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views.

`init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

## Relationships

### Conforms To

  * `View`

## See Also

### Disclosing information progressively

`struct OutlineGroup`

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

Instance Method

# disclosureGroupStyle(_:)

Sets the style for disclosure groups within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func disclosureGroupStyle<S>(_ style: S) -> some View where S : DisclosureGroupStyle
    

## See Also

### Disclosing information progressively

`struct OutlineGroup`

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

`struct DisclosureGroup`

A view that shows or hides another content view, based on the state of a
disclosure control.

Instance Method

# listRowInsets(_:)

Applies an inset to the rows in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowInsets(_ insets: EdgeInsets?) -> some View
    

##  Parameters

`insets`

    

The `EdgeInsets` to apply to the edges of the view.

## Return Value

A view that uses the given edge insets when used as a list cell.

## Discussion

Use `listRowInsets(_:)` to change the default padding of the content of list
items.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowInsets(_:)`
modifier then changes the edge insets of each row of the list according to the
`EdgeInsets` provided:

## See Also

### Configuring rows

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listRowHoverEffect(_:)

Requests that the containing list row use the provided hover effect.

visionOS 1.0+

    
    
    func listRowHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The hover effect applied to the entire list row.

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list
row’s default effect be replaced by the provided effect. If the view is not
contained within a `List` or if the view does not support hover effects in
this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should
not be modified.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listRowHoverEffectDisabled(_:)

Requests that the containing list row have its hover effect disabled.

visionOS 1.0+

    
    
    func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether the containing list row should display
its default hover effect.

## Return Value

A view that requests the default hover effect on its containing list row to
conditionally be disabled.

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to disable the default hover effect.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets a fixed tint color for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The color to use to tint the content. Use `nil` to avoid overriding the
inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

Note

This modifier is equivalent to using the version of the modifier that takes a
`ListItemTint` value and specifying the `tint` color in the corresponding
`fixed(_:)` input.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets the tint effect for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: ListItemTint?) -> some View
    

##  Parameters

`tint`

    

The tint effect to use. Use `nil` to avoid overriding the inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Structure

# ListItemTint

A tint effect configuration that you can apply to content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ListItemTint

## Overview

Use one of these tint values with the `listItemTint(_:)` view modifier. The
containing list applies the tint in a platform-specific way.

## Topics

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func fixed(Color) -> ListItemTint`

An explicit tint color.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Property

# defaultMinListRowHeight

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListRowHeight: CGFloat { get set }

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

Instance Method

# listRowSeparatorTint(_:edges:)

Sets the tint color associated with a row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the row separators, or `nil` to use the default color
for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose row separators are
tinted based on row-specific data:

To hide a row separators, use `listRowSeparator(_:edges:)`. To hide or change
the tint color for a section separator, use `listSectionSeparator(_:edges:)`
and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparatorTint(_:edges:)

Sets the tint color associated with a section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the section separators, or `nil` to use the default
color for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are
tinted based on section-specific data:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To hide a
section separator, use `listSectionSeparator(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listRowSeparator(_:edges:)

Sets the display mode for the separator associated with this specific row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this row’s separators.

`edges`

    

The set of row edges for which this preference applies. The list style might
already decide to not display separators for some edges, typically the top
edge. The default is `all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are
hidden:

To change the color of a row separators, use `listRowSeparatorTint(_:edges:)`.
To hide or change the tint color for a section separators, use
`listSectionSeparator(_:edges:)` and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparator(_:edges:)

Sets whether to hide the separator associated with a list section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this section’s separators.

`edges`

    

The set of row edges for which the preference applies. The list style might
already decide to not display separators for some edges. The default is `all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections
separator are hidden:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To set the
tint color for a section separator, use `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

Instance Method

# headerProminence(_:)

Sets the header prominence for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func headerProminence(_ prominence: Prominence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply.

## Discussion

In the following example, the section header appears with increased
prominence:

## See Also

### Configuring headers

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Property

# headerProminence

The prominence to apply to section headers within a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var headerProminence: Prominence { get set }

## Discussion

The default is `Prominence.standard`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Enumeration

# Prominence

A type indicating the prominence of a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum Prominence

## Topics

### Getting prominence options

`case standard`

The standard prominence.

`case increased`

An increased prominence.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Property

# defaultMinListHeaderHeight

The default minimum height of a header in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListHeaderHeight: CGFloat? { get set }

## Discussion

When this value is `nil`, the system chooses the appropriate height. The
default is `nil`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

Instance Method

# listRowSpacing(_:)

Sets the vertical spacing between two adjacent rows in a List.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSpacing(_ spacing: CGFloat?) -> some View
    

##  Parameters

`spacing`

    

The spacing value to use. A value of `nil` uses the default spacing.

## Discussion

The following example creates a List with 10 pts of spacing between each row:

## See Also

### Configuring spacing

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing to a custom value between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: CGFloat) -> some View
    

##  Parameters

`spacing`

    

the amount of spacing to apply.

## Discussion

The following example creates a List with 5 pts of spacing between sections:

Spacing can also be specified on a per-section basis. The following example
creates a List with compact spacing for its second section:

If adjacent sections have different spacing value, the smaller value on the
shared edge is used. Spacing specified inside the List is preferred over any
List-wide value.

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
    

## Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact
appearance between sections.

The following example creates a List with compact spacing between sections:

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Structure

# ListSectionSpacing

The spacing options between two adjacent sections in a list.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    struct ListSectionSpacing

## Topics

### Getting section spacing

`static let `default`: ListSectionSpacing`

The default spacing between sections

`static let compact: ListSectionSpacing`

Compact spacing between sections

`static func custom(CGFloat) -> ListSectionSpacing`

Creates a custom spacing value.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

Instance Method

# listRowBackground(_:)

Places a custom background view behind a list row item.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowBackground<V>(_ view: V?) -> some View where V : View
    

##  Parameters

`view`

    

The `View` to use as the background behind the list row view.

## Return Value

A list row view with `view` as its background view.

## Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list
row item.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowBackground(_:)`
modifier then places the view you supply behind each of the list row items:

## See Also

### Configuring backgrounds

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# alternatingRowBackgrounds(_:)

Overrides whether lists and tables in this view have alternating row
backgrounds.

macOS 14.0+

    
    
    func alternatingRowBackgrounds(_ behavior: AlternatingRowBackgroundBehavior = .enabled) -> some View
    

##  Parameters

`behavior`

    

Whether alternating row backgrounds are enabled or not.

## Discussion

This can be used in conjunction with an explicit list or table style or used
by itself to customize the row backgrounds of the automatic style. The only
list style this has no effect on is `.sidebar.`

This is able to be combined with `scrollContentBackground(_:)` and applies an
alternating row background on top of the overall list or table background.

This can also be combined with `listRowBackground`, which overrides the
background for a specific list row, replacing the automatic alternating
background for that row.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Structure

# AlternatingRowBackgroundBehavior

The styling of views with respect to alternating row backgrounds.

macOS 14.0+

    
    
    struct AlternatingRowBackgroundBehavior

## Overview

Use values of this type with the `alternatingRowBackgrounds(_:)` modifier.

## Topics

### Getting alternating row background behavior

`static let automatic: AlternatingRowBackgroundBehavior`

The automatic alternating row background behavior.

`static let enabled: AlternatingRowBackgroundBehavior`

Alternating rows will be enabled for applicable views.

`static let disabled: AlternatingRowBackgroundBehavior`

Alternating rows will be disabled for applicable views.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Property

# backgroundProminence

The prominence of the background underneath views associated with this
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var backgroundProminence: BackgroundProminence { get set }

## Discussion

Foreground elements above an increased prominence background are typically
adjusted to have higher contrast against a potentially vivid color, such as
taking on a higher opacity monochrome appearance according to the
`colorScheme`. System styles like `primary`, `secondary`, etc will
automatically resolve to an appropriate style in this context. The property
can be read and used for custom styled elements.

In the example below, a custom star rating element is in a list row alongside
some text. When the row is selected and has an increased prominence
appearance, the text and star rating will update their appearance, the star
rating replacing its use of yellow with the standard `secondary` style.

Note that the use of `backgroundProminence` was used by a view that was nested
in additional stack containers within the row. This ensured that the value
correctly reflected the environment within the list row itself, as opposed to
the environment of the list as a whole. One way to ensure correct resolution
would be to prefer using this in a custom ShapeStyle instead, for example:

Views like `List` and `Table` as well as standard shape styles like
`ShapeStyle.selection` will automatically update the background prominence of
foreground views. For custom backgrounds, this environment property can be
explicitly set on views above custom backgrounds.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Structure

# BackgroundProminence

The prominence of backgrounds underneath other views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct BackgroundProminence

## Overview

Background prominence should influence foreground styling to maintain
sufficient contrast against the background. For example, selected rows in a
`List` and `Table` can have increased prominence backgrounds with accent color
fills when focused; the foreground content above the background should be
adjusted to reflect that level of prominence.

This can be read and written for views with the
`EnvironmentValues.backgroundProminence` property.

## Topics

### Getting background prominence

`static let standard: BackgroundProminence`

The standard prominence of a background

`static let increased: BackgroundProminence`

A more prominent background that likely requires some changes to the views
above it.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

Instance Method

# badge(_:)

Generates a badge for the view from a text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ label: Text?) -> some View
    

##  Parameters

`label`

    

An optional `Text` view to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

Use this initializer when you want to style a `Text` view for use as a badge.
The following example customizes the badge with the `monospacedDigit()`,
`foregroundColor(_:)`, and `bold()` modifiers.

Styling the text view has no effect when the badge appears in a `TabView`.

## See Also

### Displaying a badge on a list item

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge<S>(_ label: S?) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

An optional string to display as a badge. Set the value to `nil` to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:)`. The following example shows a list with a “Default”
badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ key: LocalizedStringKey?) -> some View
    

##  Parameters

`key`

    

An optional string key to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`. The following example shows a list with a
“Default” badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from an integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ count: Int) -> some View
    

##  Parameters

`count`

    

An integer value to display in the badge. Set the value to zero to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count`
represented by a badge on one of the rows:

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badgeProminence(_:)

Specifies the prominence of badges created by this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func badgeProminence(_ prominence: BadgeProminence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply to badges.

## Discussion

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Property

# badgeProminence

The prominence to apply to badges associated with this environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var badgeProminence: BadgeProminence { get set }

## Discussion

The default is `standard`.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`struct BadgeProminence`

The visual prominence of a badge.

Structure

# BadgeProminence

The visual prominence of a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct BadgeProminence

## Overview

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## Topics

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let increased: BadgeProminence`

The highest level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

Instance Method

# swipeActions(edge:allowsFullSwipe:content:)

Adds custom swipe actions to a row in a list.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func swipeActions<T>(
        edge: HorizontalEdge = .trailing,
        allowsFullSwipe: Bool = true,
        @ViewBuilder content: () -> T
    ) -> some View where T : View
    

##  Parameters

`edge`

    

The edge of the view to associate the swipe actions with. The default is
`HorizontalEdge.trailing`.

`allowsFullSwipe`

    

A Boolean value that indicates whether a full swipe automatically performs the
first action. The default is `true`.

`content`

    

The content of the swipe actions.

## Discussion

Use this method to add swipe actions to a view that acts as a row in a list.
Indicate the `HorizontalEdge` where the swipe action originates, and define
individual actions with `Button` instances. For example, if you have a list of
messages, you can add an action to toggle a message as unread on a swipe from
the leading edge, and actions to delete or flag messages on a trailing edge
swipe:

Actions appear in the order you list them, starting from the swipe’s
originating edge. In the example above, the Delete action appears closest to
the screen’s trailing edge:

For labels or images that appear in swipe actions, SwiftUI automatically
applies the `fill` symbol variant, as shown above.

By default, the user can perform the first action for a given swipe direction
with a full swipe. For the example above, the user can perform both the toggle
unread and delete actions with full swipes. You can opt out of this behavior
for an edge by setting the `allowsFullSwipe` parameter to `false`. For
example, you can disable the full swipe on the leading edge:

When you set a role for a button using one of the values from the `ButtonRole`
enumeration, SwiftUI styles the button according to its role. In the example
above, the delete action appears in `red` because it has the `destructive`
role. If you want to set a different color — for example, to match the overall
theme of your app’s UI — add the `View/tint(_:)` modifier to the button:

The modifications in the code above make the toggle unread action `blue` and
the flag action `orange`:

When you add swipe actions, SwiftUI no longer synthesizes the Delete actions
that otherwise appear when using the `ForEach/onDelete(perform:)` method on a
`ForEach` instance. You become responsible for creating a Delete action, if
appropriate, among your swipe actions.

Actions accumulate for a given edge if you call the modifier multiple times on
the same list row view.

## See Also

### Configuring interaction

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

Instance Method

# selectionDisabled(_:)

Adds a condition that controls whether users can select this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func selectionDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that determines whether users can select this view.

## Discussion

Use this modifier to control the selectability of views in selectable
containers like `List` or `Table`. In the example, below, the user can’t
select the first item in the list.

You can also use this modifier to specify the selectability of views within a
`Picker`. The following example represents a flavor picker that disables
selection on flavors that are unavailable.

## See Also

### Configuring interaction

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

Instance Method

# refreshable(action:)

Marks this view as refreshable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func refreshable(action: @escaping () async -> Void) -> some View
    

##  Parameters

`action`

    

An asynchronous handler that SwiftUI executes when the user requests a
refresh. Use this handler to initiate an update of model data displayed in the
modified view. Use `await` in front of any asynchronous calls inside the
handler.

## Return Value

A view with a new refresh action in its environment.

## Discussion

Apply this modifier to a view to set the `refresh` value in the view’s
environment to a `RefreshAction` instance that uses the specified `action` as
its handler. Views that detect the presence of the instance can change their
appearance to provide a way for the user to execute the handler.

For example, when you apply this modifier on iOS and iPadOS to a `List`, the
list enables a standard pull-to-refresh gesture that refreshes the list
contents. When the user drags the top of the scrollable area downward, the
view reveals a progress indicator and executes the specified handler. The
indicator remains visible for the duration of the refresh, which runs
asynchronously:

You can add refresh capability to your own views as well. For information on
how to do that, see `RefreshAction`.

## See Also

### Refreshing a list’s content

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`struct RefreshAction`

An action that initiates a refresh operation.

Instance Property

# refresh

A refresh action stored in a view’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var refresh: RefreshAction? { get }

## Discussion

When this environment value contains an instance of the `RefreshAction`
structure, certain built-in views in the corresponding `Environment` begin
offering a refresh capability. They apply the instance’s handler to any
refresh operation that the user initiates. By default, the environment value
is `nil`, but you can use the `refreshable(action:)` modifier to create and
store a new refresh action that uses the handler that you specify:

On iOS and iPadOS, the `List` in the example above offers a pull to refresh
gesture because it detects the refresh action. When the user drags the list
down and releases, the list calls the action’s handler. Because SwiftUI
declares the handler as asynchronous, it can safely make long-running
asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the `refresh`
environment value to get the `RefreshAction` instance for a given
`Environment`. If you find a non-`nil` value, change your view’s appearance or
behavior to offer the refresh to the user, and call the instance to conduct
the refresh. You can call the refresh instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance:

Be sure to call the handler asynchronously by preceding it with `await`.
Because the call is asynchronous, you can use its lifetime to indicate
progress to the user. For example, you can reveal an indeterminate
`ProgressView` before calling the handler, and hide it when the handler
completes.

If your code isn’t already in an asynchronous context, create a `Task` for the
method to run in. If you do this, consider adding a way for the user to cancel
the task. For more information, see Concurrency in _The Swift Programming
Language_.

## See Also

### Refreshing a list’s content

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`struct RefreshAction`

An action that initiates a refresh operation.

Structure

# RefreshAction

An action that initiates a refresh operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct RefreshAction

## Overview

When the `refresh` environment value contains an instance of this structure,
certain built-in views in the corresponding `Environment` begin offering a
refresh capability. They apply the instance’s handler to any refresh operation
that the user initiates. By default, the environment value is `nil`, but you
can use the `refreshable(action:)` modifier to create and store a new refresh
action that uses the handler that you specify:

On iOS and iPadOS, the `List` in the example above offers a pull to refresh
gesture because it detects the refresh action. When the user drags the list
down and releases, the list calls the action’s handler. Because SwiftUI
declares the handler as asynchronous, it can safely make long-running
asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the `refresh`
environment value to get the `RefreshAction` instance for a given
`Environment`. If you find a non-`nil` value, change your view’s appearance or
behavior to offer the refresh to the user, and call the instance to conduct
the refresh. You can call the refresh instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance:

Be sure to call the handler asynchronously by preceding it with `await`.
Because the call is asynchronous, you can use its lifetime to indicate
progress to the user. For example, you might reveal an indeterminate
`ProgressView` before calling the handler, and hide it when the handler
completes.

If your code isn’t already in an asynchronous context, create a `Task` for the
method to run in. If you do this, consider adding a way for the user to cancel
the task. For more information, see Concurrency in _The Swift Programming
Language_.

## Topics

### Calling the action

`func callAsFunction() async`

Initiates a refresh action.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Refreshing a list’s content

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

Instance Method

# moveDisabled(_:)

Adds a condition for whether the view’s view hierarchy is movable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func moveDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# deleteDisabled(_:)

Adds a condition for whether the view’s view hierarchy is deletable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func deleteDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Property

# editMode

An indication of whether the user can edit the contents of a view associated
with this environment.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    var editMode: Binding<EditMode>? { get set }

## Discussion

Read this environment value to receive a optional binding to the edit mode
state. The binding contains an `EditMode` value that indicates whether edit
mode is active, and that you can use to change the mode. To learn how to read
an environment value, see `EnvironmentValues`.

Certain built-in views automatically alter their appearance and behavior in
edit mode. For example, a `List` with a `ForEach` that’s configured with the
`onDelete(perform:)` or `onMove(perform:)` modifier provides controls to
delete or move list items while in edit mode. On devices without an attached
keyboard and mouse or trackpad, people can make multiple selections in lists
only when edit mode is active.

You can also customize your own views to react to edit mode. The following
example replaces a read-only `Text` view with an editable `TextField`,
checking for edit mode by testing the wrapped value’s `isEditing` property:

You can set the edit mode through the binding, or you can rely on an
`EditButton` to do that for you, as the example above demonstrates. The button
activates edit mode when the user taps the Edit button, and disables editing
mode when the user taps Done.

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Enumeration

# EditMode

A mode that indicates whether the user can edit a view’s content.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    enum EditMode

## Overview

You receive an optional binding to the edit mode state when you read the
`editMode` environment value. The binding contains an `EditMode` value that
indicates whether edit mode is active, and that you can use to change the
mode. To learn how to read an environment value, see `EnvironmentValues`.

Certain built-in views automatically alter their appearance and behavior in
edit mode. For example, a `List` with a `ForEach` that’s configured with the
`onDelete(perform:)` or `onMove(perform:)` modifier provides controls to
delete or move list items while in edit mode. On devices without an attached
keyboard and mouse or trackpad, people can make multiple selections in lists
only when edit mode is active.

You can also customize your own views to react to edit mode. The following
example replaces a read-only `Text` view with an editable `TextField`,
checking for edit mode by testing the wrapped value’s `isEditing` property:

You can set the edit mode through the binding, or you can rely on an
`EditButton` to do that for you, as the example above demonstrates. The button
activates edit mode when the user taps it, and disables the mode when the user
taps again.

## Topics

### Getting edit modes

`case active`

The user can edit the view content.

`case inactive`

The user can’t edit the view content.

`case transient`

The view is in a temporary edit mode.

### Checking for editing mode

`var isEditing: Bool`

Indicates whether a view is being edited.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# EditActions

A set of edit actions on a collection of data that a view can offer to a user.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct EditActions<Data>

## Topics

### Getting edit operations

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `MutableCollection` and
`RangeReplaceableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `MutableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `RangeReplaceableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

`static var delete: EditActions<Data>`

An edit action that allows the user to delete one or more elements of a
collection.

Available when `Data` conforms to `RangeReplaceableCollection`.

`static var move: EditActions<Data>`

An edit action that allows the user to move elements of a collection.

Available when `Data` conforms to `MutableCollection`.

### Creating an edit operation

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# EditableCollectionContent

An opaque wrapper view that adds editing capabilities to a row in a list.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct EditableCollectionContent<Content, Data>

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# IndexedIdentifierCollection

A collection wrapper that iterates over the indices and identifiers of a
collection together.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct IndexedIdentifierCollection<Base, ID> where Base : Collection, ID : Hashable

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

