Type Property

# automatic

The default text editor style, based on the text editor’s context.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticTextEditorStyle { get }

Available when `Self` is `AutomaticTextEditorStyle`.

## Discussion

The default style represents the recommended style based on the current
platform and the text editor’s context within the view hierarchy.

## See Also

### Getting built-in styles

`static var plain: PlainTextEditorStyle`

A text editor style with no decoration.

Available when `Self` is `PlainTextEditorStyle`.

`static var roundedBorder: RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextEditorStyle`.

Type Property

# plain

A text editor style with no decoration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var plain: PlainTextEditorStyle { get }

Available when `Self` is `PlainTextEditorStyle`.

## See Also

### Getting built-in styles

`static var automatic: AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

Available when `Self` is `AutomaticTextEditorStyle`.

`static var roundedBorder: RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextEditorStyle`.

Type Property

# roundedBorder

A text editor style with a system-defined rounded border.

visionOS 1.0+

    
    
    static var roundedBorder: RoundedBorderTextEditorStyle { get }

Available when `Self` is `RoundedBorderTextEditorStyle`.

## See Also

### Getting built-in styles

`static var automatic: AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

Available when `Self` is `AutomaticTextEditorStyle`.

`static var plain: PlainTextEditorStyle`

A text editor style with no decoration.

Available when `Self` is `PlainTextEditorStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a text editor.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the text editor.

## Discussion

The system calls this method for each `TextEditor` instance in a view
hierarchy where this style is the current text editor style.

## See Also

### Creating custom styles

`typealias Configuration`

The properties of a text editor.

`associatedtype Body : View`

A view that represents the body of a text editor.

**Required**

Type Alias

# TextEditorStyle.Configuration

The properties of a text editor.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    typealias Configuration = TextEditorStyleConfiguration

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a text editor.

**Required**

` associatedtype Body : View`

A view that represents the body of a text editor.

**Required**

Associated Type

# Body

A view that represents the body of a text editor.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a text editor.

**Required**

` typealias Configuration`

The properties of a text editor.

Structure

# AutomaticTextEditorStyle

The default text editor style, based on the text editor’s context.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct AutomaticTextEditorStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the text editor style

`init()`

## Relationships

### Conforms To

  * `TextEditorStyle`

## See Also

### Supporting types

`struct PlainTextEditorStyle`

A text editor style with no decoration.

`struct RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

Structure

# PlainTextEditorStyle

A text editor style with no decoration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct PlainTextEditorStyle

## Overview

You can also use `plain` to create this style.

## Topics

### Creating the text editor style

`init()`

## Relationships

### Conforms To

  * `TextEditorStyle`

## See Also

### Supporting types

`struct AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

`struct RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

Structure

# RoundedBorderTextEditorStyle

A text editor style with a system-defined rounded border.

visionOS 1.0+

    
    
    struct RoundedBorderTextEditorStyle

## Overview

You can also use `roundedBorder` to construct this style.

## Topics

### Creating the text editor style

`init()`

## Relationships

### Conforms To

  * `TextEditorStyle`

## See Also

### Supporting types

`struct AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

`struct PlainTextEditorStyle`

A text editor style with no decoration.

