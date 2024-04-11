Type Property

# enabled

A selectability value that enables text selection by a person using your app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static var enabled: EnabledTextSelectability { get }

Available when `Self` is `EnabledTextSelectability`.

## Discussion

Enabling text selection allows people to perform actions on the text content,
such as copying and sharing. Enable text selection in views where those
operations are useful, such as copying unique IDs or error messages. This
allows people to paste the data into emails or documents.

The following example enables text selection on the second of two `Text` views
in a `VStack`.

## See Also

### Getting selectability options

`static var disabled: DisabledTextSelectability`

A selectability value that disables text selection by the person using your
app.

Available when `Self` is `DisabledTextSelectability`.

Type Property

# disabled

A selectability value that disables text selection by the person using your
app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static var disabled: DisabledTextSelectability { get }

Available when `Self` is `DisabledTextSelectability`.

## Discussion

Use this property to disable text selection of views that you don’t want
people to select and copy, even if contained within an overall context that
allows text selection.

## See Also

### Getting selectability options

`static var enabled: EnabledTextSelectability`

A selectability value that enables text selection by a person using your app.

Available when `Self` is `EnabledTextSelectability`.

Type Property

# allowsSelection

A Boolean value that indicates whether the selectability type allows
selection.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static var allowsSelection: Bool { get }

**Required**

## Discussion

Conforming types, such as `EnabledTextSelectability` and
`DisabledTextSelectability`, return `true` or `false` for this property as
appropriate. SwiftUI expects this value for a given selectability type to be
constant, unaffected by global state.

Structure

# EnabledTextSelectability

A selectability type that enables text selection by the person using your app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct EnabledTextSelectability

## Overview

Don’t use this type directly. Instead, use `enabled`.

## Relationships

### Conforms To

  * `TextSelectability`

## See Also

### Supporting types

`struct DisabledTextSelectability`

A selectability type that disables text selection by the person using your
app.

Structure

# DisabledTextSelectability

A selectability type that disables text selection by the person using your
app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct DisabledTextSelectability

## Overview

Don’t use this type directly. Instead, use `disabled`.

## Relationships

### Conforms To

  * `TextSelectability`

## See Also

### Supporting types

`struct EnabledTextSelectability`

A selectability type that enables text selection by the person using your app.

