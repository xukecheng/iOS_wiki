Type Property

# automatic

The default text field style, based on the text field’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultTextFieldStyle { get }

Available when `Self` is `DefaultTextFieldStyle`.

## Discussion

The default style represents the recommended style based on the current
platform and the text field’s context within the view hierarchy.

## See Also

### Getting built-in text field styles

`static var plain: PlainTextFieldStyle`

A text field style with no decoration.

Available when `Self` is `PlainTextFieldStyle`.

`static var roundedBorder: RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextFieldStyle`.

`static var squareBorder: SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Available when `Self` is `SquareBorderTextFieldStyle`.

Type Property

# plain

A text field style with no decoration.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var plain: PlainTextFieldStyle { get }

Available when `Self` is `PlainTextFieldStyle`.

## See Also

### Getting built-in text field styles

`static var automatic: DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

Available when `Self` is `DefaultTextFieldStyle`.

`static var roundedBorder: RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextFieldStyle`.

`static var squareBorder: SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Available when `Self` is `SquareBorderTextFieldStyle`.

Type Property

# roundedBorder

A text field style with a system-defined rounded border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    static var roundedBorder: RoundedBorderTextFieldStyle { get }

Available when `Self` is `RoundedBorderTextFieldStyle`.

## See Also

### Getting built-in text field styles

`static var automatic: DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

Available when `Self` is `DefaultTextFieldStyle`.

`static var plain: PlainTextFieldStyle`

A text field style with no decoration.

Available when `Self` is `PlainTextFieldStyle`.

`static var squareBorder: SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Available when `Self` is `SquareBorderTextFieldStyle`.

Type Property

# squareBorder

A text field style with a system-defined square border.

macOS 10.15+

    
    
    static var squareBorder: SquareBorderTextFieldStyle { get }

Available when `Self` is `SquareBorderTextFieldStyle`.

## See Also

### Getting built-in text field styles

`static var automatic: DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

Available when `Self` is `DefaultTextFieldStyle`.

`static var plain: PlainTextFieldStyle`

A text field style with no decoration.

Available when `Self` is `PlainTextFieldStyle`.

`static var roundedBorder: RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextFieldStyle`.

Structure

# DefaultTextFieldStyle

The default text field style, based on the text field’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultTextFieldStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the text field style

`init()`

## Relationships

### Conforms To

  * `TextFieldStyle`

## See Also

### Supporting types

`struct PlainTextFieldStyle`

A text field style with no decoration.

`struct RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

`struct SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Structure

# PlainTextFieldStyle

A text field style with no decoration.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PlainTextFieldStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the text field style

`init()`

## Relationships

### Conforms To

  * `TextFieldStyle`

## See Also

### Supporting types

`struct DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

`struct RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

`struct SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Structure

# RoundedBorderTextFieldStyle

A text field style with a system-defined rounded border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    struct RoundedBorderTextFieldStyle

## Overview

You can also use `roundedBorder` to construct this style.

## Topics

### Creating the text field style

`init()`

## Relationships

### Conforms To

  * `TextFieldStyle`

## See Also

### Supporting types

`struct DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

`struct PlainTextFieldStyle`

A text field style with no decoration.

`struct SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Structure

# SquareBorderTextFieldStyle

A text field style with a system-defined square border.

macOS 10.15+

    
    
    struct SquareBorderTextFieldStyle

## Overview

You can also use `squareBorder` to construct this style.

## Topics

### Creating the text field style

`init()`

## Relationships

### Conforms To

  * `TextFieldStyle`

## See Also

### Supporting types

`struct DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

`struct PlainTextFieldStyle`

A text field style with no decoration.

`struct RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

