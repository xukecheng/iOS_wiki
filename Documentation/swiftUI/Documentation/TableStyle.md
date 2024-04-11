Type Property

# automatic

The default table style in the current context.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticTableStyle { get }

Available when `Self` is `AutomaticTableStyle`.

## See Also

### Getting built-in table styles

`static var inset: InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

Available when `Self` is `InsetTableStyle`.

`static var bordered: BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Available when `Self` is `BorderedTableStyle`.

Type Property

# inset

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var inset: InsetTableStyle { get }

Available when `Self` is `InsetTableStyle`.

## Discussion

To customize whether the rows of the table should alternate their backgrounds,
use `alternatingRowBackgrounds(_:)`.

## See Also

### Getting built-in table styles

`static var automatic: AutomaticTableStyle`

The default table style in the current context.

Available when `Self` is `AutomaticTableStyle`.

`static var bordered: BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Available when `Self` is `BorderedTableStyle`.

Type Property

# bordered

The table style that describes the behavior and appearance of a table with
standard border.

macOS 12.0+

    
    
    static var bordered: BorderedTableStyle { get }

Available when `Self` is `BorderedTableStyle`.

## Discussion

Bordered tables are expected to be inset from their outer containers, but do
not have inset style rows or selection.

To customize whether the rows of the table should alternate their backgrounds,
use `alternatingRowBackgrounds(_:)`.

## See Also

### Getting built-in table styles

`static var automatic: AutomaticTableStyle`

The default table style in the current context.

Available when `Self` is `AutomaticTableStyle`.

`static var inset: InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

Available when `Self` is `InsetTableStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the table.

## Discussion

The system calls this method for each `Table` instance in a view hierarchy
where this style is the current table style.

## See Also

### Creating custom table styles

`typealias Configuration`

The properties of a table.

`associatedtype Body : View`

A view that represents the body of a table.

**Required**

Type Alias

# TableStyle.Configuration

The properties of a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    typealias Configuration = TableStyleConfiguration

## See Also

### Creating custom table styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a table.

**Required**

` associatedtype Body : View`

A view that represents the body of a table.

**Required**

Associated Type

# Body

A view that represents the body of a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom table styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a table.

**Required**

` typealias Configuration`

The properties of a table.

Type Method

# inset(alternatesRowBackgrounds:)

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

macOS 12.0–14.4  Deprecated

    
    
    static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle

Available when `Self` is `InsetTableStyle`.

Deprecated

Use the `inset` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## See Also

### Deprecated styles

`static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Available when `Self` is `BorderedTableStyle`.

Deprecated

Type Method

# bordered(alternatesRowBackgrounds:)

The table style that describes the behavior and appearance of a table with
standard border.

macOS 12.0–14.4  Deprecated

    
    
    static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle

Available when `Self` is `BorderedTableStyle`.

Deprecated

Use the `bordered` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## Discussion

Bordered tables are expected to be inset from their outer containers, but do
not have inset style rows or selection.

## See Also

### Deprecated styles

`static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

Available when `Self` is `InsetTableStyle`.

Deprecated

Structure

# AutomaticTableStyle

The default table style in the current context.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct AutomaticTableStyle

## Overview

You can also use `automatic` to construct this style.

## Relationships

### Conforms To

  * `TableStyle`

## See Also

### Supporting types

`struct InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

`struct BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Structure

# InsetTableStyle

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct InsetTableStyle

## Overview

You can also use `inset` to construct this style.

## Topics

### Creating the table style

`init()`

Creates a default inset table style, with alternating row backgrounds.

`init(alternatesRowBackgrounds: Bool)`

Creates an inset table style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `TableStyle`

## See Also

### Supporting types

`struct AutomaticTableStyle`

The default table style in the current context.

`struct BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Structure

# BorderedTableStyle

The table style that describes the behavior and appearance of a table with
standard border.

macOS 12.0+

    
    
    struct BorderedTableStyle

## Overview

You can also use `bordered` to construct this style.

## Topics

### Creating the table style

`init()`

Creates a default bordered table style, with alternating row backgrounds.

`init(alternatesRowBackgrounds: Bool)`

Creates an inset table style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `TableStyle`

## See Also

### Supporting types

`struct AutomaticTableStyle`

The default table style in the current context.

`struct InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

