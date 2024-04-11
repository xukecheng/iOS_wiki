Initializer

# init(_:value:)

Creates an unsortable column that displays a string property that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, String>
    ) where Content == Text

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column. The table uses this to
display the property as verbatim text in each row of the table.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`.

## See Also

### Creating an unsortable column

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

Initializer

# init(_:value:)

Creates an unsortable column that displays a string property that generates
its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, String>
    ) where Content == Text, S : StringProtocol

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column. The table uses this to
display the property as verbatim text in each row of the table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For information about localizing strings, see `Text`.

## See Also

### Creating an unsortable column

`init(LocalizedStringKey, value: KeyPath<RowValue, String>)`

Creates an unsortable column that displays a string property that generates
its label from a localized string key.

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

Initializer

# init(_:value:)

Creates an unsortable column that displays a string property with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, String>
    ) where Content == Text

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column. The table uses this to
display the property as verbatim text in each row of the table.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`.

## See Also

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

Initializer

# init(_:content:)

Creates an unsortable column that generates its label from a localized string
key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`.

## See Also

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

`init<S>(S, content: (RowValue) -> Content)`

Creates an unsortable column that generates its label from a string.

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

`init(Text, content: (RowValue) -> Content)`

Creates an unsortable column with a text label

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

Initializer

# init(_:content:)

Creates an unsortable column that generates its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For information about localizing strings, see `Text`.

## See Also

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

`init(Text, content: (RowValue) -> Content)`

Creates an unsortable column with a text label

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

Initializer

# init(_:content:)

Creates an unsortable column with a text label

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`,
`Content` conforms to `View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For information about localizing strings, see `Text`.

## See Also

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

Initializer

# init(_:value:comparator:)

Creates a sortable column that displays a string property, and generates its
label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, to display verbatim as
text in each row of a table, and the key path used to create a sort comparator
when sorting the column.

`comparator`

    

The `SortComparator` used to order the string values.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`.

## See Also

### Creating a column with strings

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

Initializer

# init(_:value:comparator:)

Creates a sortable column that displays a string property, and generates its
label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text, S : StringProtocol

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, to display verbatim as
text in each row of a table, and the key path used to create a sort comparator
when sorting the column.

`comparator`

    

The `SortComparator` used to order the string values.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

### Creating a column with strings

`init(LocalizedStringKey, value: KeyPath<RowValue, String>, comparator:
String.StandardComparator)`

Creates a sortable column that displays a string property, and generates its
label from a localized string key.

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

Initializer

# init(_:value:comparator:)

Creates a sortable column that displays a string property and has a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, to display verbatim as
text in each row of a table, and the key path used to create a sort comparator
when sorting the column.

`comparator`

    

The `SortComparator` used to order the string values.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

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

Initializer

# init(_:value:comparator:)

Creates an unsortable column that displays a string property, and which
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state and to display as verbatim text in each row.

`comparator`

    

The specific comparator to compare string values.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:comparator:)

Creates a sortable column that displays a string property, and which generates
its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text, S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state and to display as verbatim text in each row.

`comparator`

    

The specific comparator to compare string values.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:comparator:)

Creates an unsortable column that displays a string property and has a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard
    ) where Content == Text

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state and to display as verbatim text in each row.

`comparator`

    

The specific comparator to compare string values.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that generates its label from a localized string
key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, String>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that generates its label from a localized string
key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, String?>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, String?>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, String?>, comparator:
String.StandardComparator, content: (RowValue) -> Content)`

Creates a sortable column with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:comparator:content:)

Creates a sortable column with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, String?>,
        comparator: String.StandardComparator = .localizedStandard,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The specific comparator to compare string values.

`content`

    

The view content to display for each row in a table.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for integer values that generates its label from a
localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with integers

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

Initializer

# init(_:value:content:)

Creates a sortable column for integer values that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int>, content: (RowValue)
-> Content)`

Creates a sortable column for integer values that generates its label from a
localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UInt?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned integer values with a text
label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for 64-bit integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with 64-bit integers

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

Initializer

# init(_:value:content:)

Creates a sortable column for 64-bit integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with 64-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int64>, content: (RowValue)
-> Content)`

Creates a sortable column for 64-bit integer values that generates its label
from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for 64-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 64-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 64-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 64-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 64-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 64-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 64-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt64>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 64-bit integer values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 64-bit integer values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UInt64?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 64-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 64-bit integer values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt64?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for 32-bit integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with 32-bit integers

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

Initializer

# init(_:value:content:)

Creates a sortable column for 32-bit integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with 32-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int32>, content: (RowValue)
-> Content)`

Creates a sortable column for 32-bit integer values that generates its label
from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for 32-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 32-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 32-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 32-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 32-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 32-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 32-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt32>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 32-bit integer values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 32-bit integer values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UInt32?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 32-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 32-bit integer values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt32?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for 16-bit integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with 16-bit integers

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

Initializer

# init(_:value:content:)

Creates a sortable column for 16-bit integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with 16-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int16>, content: (RowValue)
-> Content)`

Creates a sortable column for 16-bit integer values that generates its label
from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for 16-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 16-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 16-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 16-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 16-bit integer values that generates
its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 16-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 16-bit integer values with a text
label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt16>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 16-bit integer values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 16-bit integer values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UInt16?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional unsigned 16-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 16-bit integer values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt16?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for 8-bit integer values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with 8-bit integers

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

Initializer

# init(_:value:content:)

Creates a sortable column for 8-bit integer values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with 8-bit integers

`init(LocalizedStringKey, value: KeyPath<RowValue, Int8>, content: (RowValue)
-> Content)`

Creates a sortable column for 8-bit integer values that generates its label
from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for 8-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 8-bit integer values that generates its
label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Int8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 8-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Int8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional 8-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Int8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 8-bit integer values that generates its
label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 8-bit integer values that displays a
string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for unsigned 8-bit integer values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt8>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 8-bit integer values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UInt8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 8-bit integer values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UInt8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UInt8?>, content: (RowValue) -> Content)`

Creates a sortable column for optional unsigned 8-bit integer values with a
text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional unsigned 8-bit integer values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UInt8?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for Boolean values that generates its label from a
localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Bool>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with Booleans

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

Initializer

# init(_:value:content:)

Creates a sortable column for Boolean values that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Bool>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with Booleans

`init(LocalizedStringKey, value: KeyPath<RowValue, Bool>, content: (RowValue)
-> Content)`

Creates a sortable column for Boolean values that generates its label from a
localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for Boolean values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Bool>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional Boolean values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Bool?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional Boolean values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Bool?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, Bool?>, content: (RowValue) -> Content)`

Creates a sortable column for optional Boolean values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional Boolean values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Bool?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for single-precision floating-point values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Float>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with floats

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

Initializer

# init(_:value:content:)

Creates a sortable column for single-precision floating-point values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Float>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with floats

`init(LocalizedStringKey, value: KeyPath<RowValue, Float>, content: (RowValue)
-> Content)`

Creates a sortable column for single-precision floating-point values that
generates its label from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for single-precision floating-point values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Float>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional single-precision floating-point values
that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Float?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional single-precision floating-point values
that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Float?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, Float?>, content: (RowValue) -> Content)`

Creates a sortable column for optional single-precision floating-point values
with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional single-precision floating-point values
with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Float?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for double-precision floating-point values that
generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Double>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with doubles

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

Initializer

# init(_:value:content:)

Creates a sortable column for double-precision floating-point values that
displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Double>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with doubles

`init(LocalizedStringKey, value: KeyPath<RowValue, Double>, content:
(RowValue) -> Content)`

Creates a sortable column for double-precision floating-point values that
generates its label from a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for double-precision floating-point values with a
text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Double>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional double-precision floating-point values
that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Double?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional double-precision floating-point values
that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Double?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, Double?>, content: (RowValue) ->
Content)`

Creates a sortable column for optional double-precision floating-point values
with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional double-precision floating-point values
with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Double?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for date values that generates its label from a
localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Date>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with dates

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

Initializer

# init(_:value:content:)

Creates a sortable column for date values that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Date>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with dates

`init(LocalizedStringKey, value: KeyPath<RowValue, Date>, content: (RowValue)
-> Content)`

Creates a sortable column for date values that generates its label from a
localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for date values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Date>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional date values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, Date?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional date values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, Date?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, Date?>, content: (RowValue) -> Content)`

Creates a sortable column for optional date values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional date values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, Date?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for UUID values that generates its label from a
localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UUID>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a column with UUIDs

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

Initializer

# init(_:value:content:)

Creates a sortable column for UUID values that displays a string property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UUID>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

### Creating a column with UUIDs

`init(LocalizedStringKey, value: KeyPath<RowValue, UUID>, content: (RowValue)
-> Content)`

Creates a sortable column for UUID values that generates its label from a
localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for UUID values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UUID>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, which will be used to
update and reflect the sorting state in a table.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional UUID values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, UUID?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for optional UUID values that displays a string
property.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        value: KeyPath<RowValue, UUID?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. For more information about localizing strings, see
`Text`.

## See Also

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

`init(Text, value: KeyPath<RowValue, UUID?>, content: (RowValue) -> Content)`

Creates a sortable column for optional UUID values with a text label.

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:value:content:)

Creates a sortable column for optional UUID values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        value: KeyPath<RowValue, UUID?>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to
`Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

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

Initializer

# init(_:value:content:)

Creates a sortable column for comparable values that generates its label from
a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, V>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where V : Comparable

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`.

## See Also

### Creating a column with comparable values

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

Initializer

# init(_:value:content:)

Creates a sortable column for comparable values that generates its label from
a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: KeyPath<RowValue, V>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol, V : Comparable

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

### Creating a column with comparable values

`init<V>(LocalizedStringKey, value: KeyPath<RowValue, V>, content: (RowValue)
-> Content)`

Creates a sortable column for comparable values that generates its label from
a localized string key.

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

Initializer

# init(_:value:content:)

Creates a sortable column for comparable values with a text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init<V>(
        _ text: Text,
        value: KeyPath<RowValue, V>,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where V : Comparable

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that generates its label from a localized string
key, and uses an explicit comparator for sorting values.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V, C>(
        _ titleKey: LocalizedStringKey,
        value: KeyPath<RowValue, V>,
        comparator: C,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where V == C.Compared, C : SortComparator

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The `SortComparator` used to order values of the sort value type.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the localized key
similar to `init(_:tableName:bundle:comment:)`. See `Text` for more
information about localizing strings.

## See Also

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

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that generates its label from a string, and uses an
explicit comparator for sorting values.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, V, C>(
        _ title: S,
        value: KeyPath<RowValue, V>,
        comparator: C,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol, V == C.Compared, C : SortComparator

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`title`

    

A string that describes the column.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The `SortComparator` used to order values of the sort value type.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

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

`init<V, C>(Text, value: KeyPath<RowValue, V>, comparator: C, content:
(RowValue) -> Content)`

Creates a sortable column that has a text label, and uses an explicit
comparator for sorting values.

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

Initializer

# init(_:value:comparator:content:)

Creates a sortable column that has a text label, and uses an explicit
comparator for sorting values.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init<V, C>(
        _ text: Text,
        value: KeyPath<RowValue, V>,
        comparator: C,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where V == C.Compared, C : SortComparator

Available when `RowValue` conforms to `Identifiable`, `Sort` is
`KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is
`Text`.

##  Parameters

`text`

    

The column’s label.

`value`

    

The path to the property associated with the column, used to update the
table’s sorting state.

`comparator`

    

The `SortComparator` used to order values of the sort value type.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

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

Initializer

# init(_:sortUsing:content:)

Creates a sortable column that generates its label from a localized string
key.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        sortUsing comparator: Sort,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the column’s localized title.

`comparator`

    

The prototype sort comparator to use when representing this column. When a
person taps or clicks the column header, the containing table’s `sortOrder`
incorporates this value, potentially with a flipped order.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. For more
information about localizing strings, see`Text`.

## See Also

### Creating a column with a comparator

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

Initializer

# init(_:sortUsing:content:)

Creates a sortable column that generates its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        sortUsing comparator: Sort,
        @ViewBuilder content: @escaping (RowValue) -> Content
    ) where S : StringProtocol

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the column.

`comparator`

    

The prototype sort comparator to use when representing this column. When a
person taps or clicks the column header, the containing table’s `sortOrder`
incorporates this value, potentially with a flipped order.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

### Creating a column with a comparator

`init(LocalizedStringKey, sortUsing: Sort, content: (RowValue) -> Content)`

Creates a sortable column that generates its label from a localized string
key.

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

`init(Text, sortUsing: Sort, content: (RowValue) -> Content)`

Creates a sortable column with text label.

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

Initializer

# init(_:sortUsing:content:)

Creates a sortable column with text label.

iOS 16.6+  iPadOS 16.6+  macOS 13.5+  Mac Catalyst 16.6+  visionOS 1.0+

    
    
    init(
        _ text: Text,
        sortUsing comparator: Sort,
        @ViewBuilder content: @escaping (RowValue) -> Content
    )

Available when `RowValue` conforms to `Identifiable`, `RowValue` is
`Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to
`View`, and `Label` is `Text`.

##  Parameters

`text`

    

The column’s label.

`comparator`

    

The prototype sort comparator to use when representing this column. When a
person taps or clicks the column header, the containing table’s `sortOrder`
incorporates this value, potentially with a flipped order.

`content`

    

The view content to display for each row in a table.

## Discussion

This initializer creates a `Text` view for you, and treats the title similar
to `init(_:)`. For more information about localizing strings, see `Text`.

## See Also

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

Instance Method

# width(_:)

Creates a fixed width table column that isn’t user resizable.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func width(_ width: CGFloat? = nil) -> TableColumn<RowValue, Sort, Content, Label>

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

##  Parameters

`width`

    

A fixed width for the resulting column. If `width` is `nil`, the resulting
column has no change in sizing.

## See Also

### Setting the column width

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

Instance Method

# width(min:ideal:max:)

Creates a resizable table column with the provided constraints.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func width(
        min: CGFloat? = nil,
        ideal: CGFloat? = nil,
        max: CGFloat? = nil
    ) -> TableColumn<RowValue, Sort, Content, Label>

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

##  Parameters

`min`

    

The minimum width of a resizable column. If non-`nil`, the value must be
greater than or equal to `0`.

`ideal`

    

The ideal width of the column, used to determine the initial width of the
table column. The column always starts at least as large as the set ideal
size, but may be larger if table was sized larger than the ideal of all of its
columns.

`max`

    

The maximum width of a resizable column. If non-`nil`, the value must be
greater than `0`. Pass `infinity` to indicate unconstrained maximum width.

## Discussion

Always specify at least one width constraint when calling this method. Pass
`nil` or leave out a constraint to indicate no change to the sizing of a
column.

To create a fixed size column use `width(_:)` instead.

## See Also

### Setting the column width

`func width(CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>`

Creates a fixed width table column that isn’t user resizable.

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

`func width() -> TableColumn<RowValue, Sort, Content, Label>`

Sets the column’s width.

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

Deprecated

Instance Method

# width()

Sets the column’s width.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func width() -> TableColumn<RowValue, Sort, Content, Label>

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to
`SortComparator`, `Content` conforms to `View`, and `Label` conforms to
`View`.

Deprecated

Use `width(_:)` or `width(min:ideal:max:)` instead.

## See Also

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

