Type Property

# none

No variant for a symbol.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let none: SymbolVariants

## Discussion

Using this variant with the `symbolVariant(_:)` modifier doesn’t have any
effect. Instead, to show a symbol that ignores the current variant, directly
set the `symbolVariants` environment value to `none` using the
`environment(_:_:)` modifer:

## See Also

### Getting symbol variants

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let fill: SymbolVariants`

A variant that fills the symbol.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

Type Property

# circle

A variant that encapsulates the symbol in a circle.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let circle: SymbolVariants

## Discussion

Use this variant with a call to the `symbolVariant(_:)` modifier to draw
symbols in a circle, for those symbols that have a circle variant:

## See Also

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let fill: SymbolVariants`

A variant that fills the symbol.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

Type Property

# square

A variant that encapsulates the symbol in a square.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let square: SymbolVariants

## Discussion

Use this variant with a call to the `symbolVariant(_:)` modifier to draw
symbols in a square, for those symbols that have a square variant:

## See Also

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let fill: SymbolVariants`

A variant that fills the symbol.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

Type Property

# rectangle

A variant that encapsulates the symbol in a rectangle.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let rectangle: SymbolVariants

## Discussion

Use this variant with a call to the `symbolVariant(_:)` modifier to draw
symbols in a rectangle, for those symbols that have a rectangle variant:

## See Also

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let fill: SymbolVariants`

A variant that fills the symbol.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

Type Property

# fill

A variant that fills the symbol.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let fill: SymbolVariants

## Discussion

Use this variant with a call to the `symbolVariant(_:)` modifier to draw
filled symbols, for those symbols that have a filled variant:

## See Also

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

Type Property

# slash

A variant that draws a slash through the symbol.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let slash: SymbolVariants

## Discussion

Use this variant with a call to the `symbolVariant(_:)` modifier to draw
symbols with a slash, for those symbols that have such a variant:

## See Also

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let fill: SymbolVariants`

A variant that fills the symbol.

Instance Property

# circle

A version of the variant that’s encapsulated in a circle.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var circle: SymbolVariants { get }

## Discussion

Use this property to modify a variant like `fill` so that it’s also contained
in a circle:

## See Also

### Modifying a variant

`var square: SymbolVariants`

A version of the variant that’s encapsulated in a square.

`var rectangle: SymbolVariants`

A version of the variant that’s encapsulated in a rectangle.

`var fill: SymbolVariants`

A filled version of the variant.

`var slash: SymbolVariants`

A slashed version of the variant.

Instance Property

# square

A version of the variant that’s encapsulated in a square.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var square: SymbolVariants { get }

## Discussion

Use this property to modify a variant like `fill` so that it’s also contained
in a square:

## See Also

### Modifying a variant

`var circle: SymbolVariants`

A version of the variant that’s encapsulated in a circle.

`var rectangle: SymbolVariants`

A version of the variant that’s encapsulated in a rectangle.

`var fill: SymbolVariants`

A filled version of the variant.

`var slash: SymbolVariants`

A slashed version of the variant.

Instance Property

# rectangle

A version of the variant that’s encapsulated in a rectangle.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var rectangle: SymbolVariants { get }

## Discussion

Use this property to modify a variant like `fill` so that it’s also contained
in a rectangle:

## See Also

### Modifying a variant

`var circle: SymbolVariants`

A version of the variant that’s encapsulated in a circle.

`var square: SymbolVariants`

A version of the variant that’s encapsulated in a square.

`var fill: SymbolVariants`

A filled version of the variant.

`var slash: SymbolVariants`

A slashed version of the variant.

Instance Property

# fill

A filled version of the variant.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var fill: SymbolVariants { get }

## Discussion

Use this property to modify a shape variant like `circle` so that it’s also
filled:

## See Also

### Modifying a variant

`var circle: SymbolVariants`

A version of the variant that’s encapsulated in a circle.

`var square: SymbolVariants`

A version of the variant that’s encapsulated in a square.

`var rectangle: SymbolVariants`

A version of the variant that’s encapsulated in a rectangle.

`var slash: SymbolVariants`

A slashed version of the variant.

Instance Property

# slash

A slashed version of the variant.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var slash: SymbolVariants { get }

## Discussion

Use this property to modify a shape variant like `circle` so that it’s also
covered by a slash:

## See Also

### Modifying a variant

`var circle: SymbolVariants`

A version of the variant that’s encapsulated in a circle.

`var square: SymbolVariants`

A version of the variant that’s encapsulated in a square.

`var rectangle: SymbolVariants`

A version of the variant that’s encapsulated in a rectangle.

`var fill: SymbolVariants`

A filled version of the variant.

Instance Method

# contains(_:)

Returns a Boolean value that indicates whether the current variant contains
the specified variant.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func contains(_ other: SymbolVariants) -> Bool

##  Parameters

`other`

    

A variant to look for in this variant.

## Return Value

`true` if this variant contains `other`; otherwise, `false`.

