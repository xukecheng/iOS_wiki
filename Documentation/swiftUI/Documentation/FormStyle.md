Type Property

# automatic

The default form style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticFormStyle { get }

Available when `Self` is `AutomaticFormStyle`.

## See Also

### Getting built-in form styles

`static var columns: ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

Available when `Self` is `ColumnsFormStyle`.

`static var grouped: GroupedFormStyle`

A form style with grouped rows.

Available when `Self` is `GroupedFormStyle`.

Type Property

# columns

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var columns: ColumnsFormStyle { get }

Available when `Self` is `ColumnsFormStyle`.

## See Also

### Getting built-in form styles

`static var automatic: AutomaticFormStyle`

The default form style.

Available when `Self` is `AutomaticFormStyle`.

`static var grouped: GroupedFormStyle`

A form style with grouped rows.

Available when `Self` is `GroupedFormStyle`.

Type Property

# grouped

A form style with grouped rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var grouped: GroupedFormStyle { get }

Available when `Self` is `GroupedFormStyle`.

## Discussion

Rows in a grouped rows form have leading aligned labels and trailing aligned
controls within visually grouped sections.

## See Also

### Getting built-in form styles

`static var automatic: AutomaticFormStyle`

The default form style.

Available when `Self` is `AutomaticFormStyle`.

`static var columns: ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

Available when `Self` is `ColumnsFormStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the form.

## Return Value

A view that has behavior and appearance that enables it to function as a
`Form`.

## See Also

### Creating custom form styles

`typealias Configuration`

The properties of a form instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a form.

**Required**

Type Alias

# FormStyle.Configuration

The properties of a form instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = FormStyleConfiguration

## Discussion

You receive a `configuration` parameter of this type — which is an alias for
the `FormStyleConfiguration` type — when you implement the required
`makeBody(configuration:)` method in a custom form style implementation.

## See Also

### Creating custom form styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a form.

**Required**

` associatedtype Body : View`

A view that represents the appearance and interaction of a form.

**Required**

Associated Type

# Body

A view that represents the appearance and interaction of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom form styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a form.

**Required**

` typealias Configuration`

The properties of a form instance.

Structure

# AutomaticFormStyle

The default form style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticFormStyle

## Overview

Use the `automatic` static variable to create this style:

## Topics

### Creating the form style

`init()`

Creates a default form style.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

`struct GroupedFormStyle`

A form style with grouped rows.

Structure

# ColumnsFormStyle

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ColumnsFormStyle

## Overview

Use the `columns` static variable to create this style:

## Topics

### Creating the form style

`init()`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct AutomaticFormStyle`

The default form style.

`struct GroupedFormStyle`

A form style with grouped rows.

Structure

# GroupedFormStyle

A form style with grouped rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct GroupedFormStyle

## Overview

Rows in this form style have leading aligned labels and trailing aligned
controls within visually grouped sections.

Use the `grouped` static variable to create this style:

## Topics

### Creating the form style

`init()`

Creates a form style with scrolling, grouped rows.

## Relationships

### Conforms To

  * `FormStyle`

## See Also

### Supporting types

`struct AutomaticFormStyle`

The default form style.

`struct ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

