Instance Property

# label

A view that describes the effect of calling the button’s action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let label: PrimitiveButtonStyleConfiguration.Label

## See Also

### Configuring a button’s label

`struct Label`

A type-erased label of a button.

Structure

# PrimitiveButtonStyleConfiguration.Label

A type-erased label of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring a button’s label

`let label: PrimitiveButtonStyleConfiguration.Label`

A view that describes the effect of calling the button’s action.

Instance Method

# trigger()

Performs the button’s action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func trigger()

Instance Property

# role

An optional semantic role describing the button’s purpose.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let role: ButtonRole?

## Discussion

A value of `nil` means that the Button has no assigned role. If the button
does have a role, use it to make adjustments to the button’s appearance. The
following example shows a custom style that uses bold text when the role is
`cancel`, `red` text when the role is `destructive`, and adds no special
styling otherwise:

You can create one of each button using this style to see the effect:

