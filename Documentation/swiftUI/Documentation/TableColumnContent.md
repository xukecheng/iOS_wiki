Instance Property

# tableColumnBody

The composition of content that comprise the table column content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var tableColumnBody: Self.TableColumnBody { get }

**Required**

## See Also

### Getting the column body

`associatedtype TableColumnBody : TableColumnContent`

The type of content representing the body of this table column content.

**Required**

Associated Type

# TableColumnBody

The type of content representing the body of this table column content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype TableColumnBody : TableColumnContent

**Required**

## See Also

### Getting the column body

`var tableColumnBody: Self.TableColumnBody`

The composition of content that comprise the table column content.

**Required**

Associated Type

# TableRowValue

The type of value of rows presented by this column content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype TableRowValue : Identifiable = Self.TableColumnBody.TableRowValue

**Required**

Associated Type

# TableColumnSortComparator

The type of sort comparator associated with this table column content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype TableColumnSortComparator : SortComparator = Self.TableColumnBody.TableColumnSortComparator

**Required**

Instance Method

# alignment(_:)

Sets the alignment of the column, applying to both its column header label and
the row view content for that column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func alignment(_ alignment: TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
    

##  Parameters

`alignment`

    

The alignment to apply to the column.

## See Also

### Configuring the content

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

Instance Method

# customizationID(_:)

Sets the identifier to be associated with a column when persisting its state
with `TableColumnCustomization`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func customizationID(_ id: String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
    

##  Parameters

`id`

    

The identifier to associate with a column.

## Discussion

This is required to allow user customization of a specific table column, in
addition to the table as a whole being provided a binding to a
`TableColumnCustomization`.

The identifier needs to to be stable, including across app version updates,
since it is used to persist the user customization.

## See Also

### Configuring the content

`func alignment(TableColumnAlignment) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the alignment of the column, applying to both its column header label and
the row view content for that column.

`func defaultVisibility(Visibility) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the default visibility of a table column.

`func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the disabled customization behavior for a table column.

Instance Method

# defaultVisibility(_:)

Sets the default visibility of a table column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func defaultVisibility(_ visibility: Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
    

##  Parameters

`visibility`

    

The default visibility to apply to columns.

## Discussion

A `hidden` column will not be visible, unless the `Table` is also bound to
`TableColumnCustomization` and either modified programmatically or by the
user.

## See Also

### Configuring the content

`func alignment(TableColumnAlignment) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the alignment of the column, applying to both its column header label and
the row view content for that column.

`func customizationID(String) -> some TableColumnContent<Self.TableRowValue,
Self.TableColumnSortComparator> `

Sets the identifier to be associated with a column when persisting its state
with `TableColumnCustomization`.

`func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some
TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator> `

Sets the disabled customization behavior for a table column.

Instance Method

# disabledCustomizationBehavior(_:)

Sets the disabled customization behavior for a table column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func disabledCustomizationBehavior(_ behavior: TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
    

##  Parameters

`behavior`

    

The behavior to disable, or `.all` to not allow any customization.

## Discussion

When the containing `Table` is bound to some `TableColumnCustomization`, all
columns will be able to be customized by the user on macOS by default (i.e.
`TableColumnCustomizationBehavior.all`). This modifier allows disabling
specific behavior.

This modifier has no effect on iOS since `Table` does not support any built-in
user customization features.

This does not prevent programmatic changes to a table column customization.

## See Also

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

