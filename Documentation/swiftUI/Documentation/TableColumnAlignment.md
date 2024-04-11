Type Property

# automatic

The default column alignment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: TableColumnAlignment { get }

## Discussion

This is equivalent to `leading`.

## See Also

### Getting the alignment

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

Type Property

# leading

Leading column alignment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var leading: TableColumnAlignment { get }

## Discussion

With a `layoutDirection` of `leftToRight`, this is equivalent to left; and
with a `layoutDirection` of `rightToLeft`, this is equivalent to right.

## See Also

### Getting the alignment

`static var automatic: TableColumnAlignment`

The default column alignment.

`static var center: TableColumnAlignment`

Center column alignment.

`static var trailing: TableColumnAlignment`

Trailing column alignment.

`static var numeric: TableColumnAlignment`

Column alignment appropriate for numeric content.

`static func numeric(Locale.NumberingSystem) -> TableColumnAlignment`

Column alignment appropriate for numeric content.

Type Property

# center

Center column alignment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var center: TableColumnAlignment { get }

## See Also

### Getting the alignment

`static var automatic: TableColumnAlignment`

The default column alignment.

`static var leading: TableColumnAlignment`

Leading column alignment.

`static var trailing: TableColumnAlignment`

Trailing column alignment.

`static var numeric: TableColumnAlignment`

Column alignment appropriate for numeric content.

`static func numeric(Locale.NumberingSystem) -> TableColumnAlignment`

Column alignment appropriate for numeric content.

Type Property

# trailing

Trailing column alignment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var trailing: TableColumnAlignment { get }

## Discussion

With a `layoutDirection` of `leftToRight`, this is equivalent to right; and
with a `layoutDirection` of `rightToLeft`, this is equivalent to left.

## See Also

### Getting the alignment

`static var automatic: TableColumnAlignment`

The default column alignment.

`static var leading: TableColumnAlignment`

Leading column alignment.

`static var center: TableColumnAlignment`

Center column alignment.

`static var numeric: TableColumnAlignment`

Column alignment appropriate for numeric content.

`static func numeric(Locale.NumberingSystem) -> TableColumnAlignment`

Column alignment appropriate for numeric content.

Type Property

# numeric

Column alignment appropriate for numeric content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var numeric: TableColumnAlignment { get }

## Discussion

Use this alignment when a table column is primarily displaying numeric
content, so that the values are easy to visually scan and compare.

This uses the current locale’s numbering system to determine the alignment:

  * For left to right numbering systems, this is equivalent to right.

  * For right to left numbering systems, this is equivalent to left.

## See Also

### Getting the alignment

`static var automatic: TableColumnAlignment`

The default column alignment.

`static var leading: TableColumnAlignment`

Leading column alignment.

`static var center: TableColumnAlignment`

Center column alignment.

`static var trailing: TableColumnAlignment`

Trailing column alignment.

`static func numeric(Locale.NumberingSystem) -> TableColumnAlignment`

Column alignment appropriate for numeric content.

Type Method

# numeric(_:)

Column alignment appropriate for numeric content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static func numeric(_ numberingSystem: Locale.NumberingSystem) -> TableColumnAlignment

## Discussion

Use this alignment when a table column is primarily displaying numeric
content, so that the values are easy to visually scan and compare.

This uses the provided numbering system to determine the alignment:

  * For left to right numbering systems, this is equivalent to right.

  * For right to left numbering systems, this is equivalent to left.

## See Also

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

