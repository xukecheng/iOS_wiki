Initializer

# init()

Creates an empty table column customization.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()

## Discussion

With an empty customization, columns will be ordered as described by the
table’s column builder.

Instance Method

# resetOrder()

Resets the column order back to the default, preserving the customized
visibility and size.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    mutating func resetOrder()

## Discussion

Tables that are bound to this state will order their columns as described by
their column builder.

## See Also

### Managing the customization

`subscript(visibility _: String) -> Visibility`

The visibility of the column identified by its identifier.

Instance Subscript

# subscript(visibility:)

The visibility of the column identified by its identifier.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    subscript(visibility id: String) -> Visibility { get set }

## Overview

Explicit identifiers can be associated with a `TableColumn` using the
`customizationID(_:)` modifier.

If the ID isn’t associated with the state, a default value of `.automatic` is
returned.

## See Also

### Managing the customization

`func resetOrder()`

Resets the column order back to the default, preserving the customized
visibility and size.

