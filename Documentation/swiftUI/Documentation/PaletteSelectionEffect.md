Type Property

# automatic

Applies the system’s default effect when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: PaletteSelectionEffect

## Discussion

When using un-tinted SF Symbols or template images, the current tint color is
applied to the selected items’ image. If the provided SF Symbols have custom
tints, a stroke is drawn around selected items.

## See Also

### Getting palette selection effects

`static var custom: PaletteSelectionEffect`

Does not apply any system effect when selected.

`static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect`

Applies the specified symbol variant when selected.

Type Property

# custom

Does not apply any system effect when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var custom: PaletteSelectionEffect

## Discussion

Note

Make sure to manually implement a way to indicate selection when using this
case. For example, you could dynamically resolve the item’s image based on the
selection state.

## See Also

### Getting palette selection effects

`static var automatic: PaletteSelectionEffect`

Applies the system’s default effect when selected.

`static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect`

Applies the specified symbol variant when selected.

Type Method

# symbolVariant(_:)

Applies the specified symbol variant when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static func symbolVariant(_ variant: SymbolVariants) -> PaletteSelectionEffect

## Discussion

Note

This effect only applies to SF Symbols.

## See Also

### Getting palette selection effects

`static var automatic: PaletteSelectionEffect`

Applies the system’s default effect when selected.

`static var custom: PaletteSelectionEffect`

Does not apply any system effect when selected.

