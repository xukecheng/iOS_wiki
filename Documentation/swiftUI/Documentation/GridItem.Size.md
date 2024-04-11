Case

# GridItem.Size.adaptive(minimum:maximum:)

Multiple items in the space of a single flexible item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case adaptive(
        minimum: CGFloat,
        maximum: CGFloat = .infinity
    )

## Discussion

This size case places one or more items into the space assigned to a single
`flexible` item, using the provided bounds and spacing to decide exactly how
many items fit. This approach prefers to insert as many items of the `minimum`
size as possible but lets them increase to the `maximum` size.

## See Also

### Getting the sizes

`case fixed(CGFloat)`

A single item with the specified fixed size.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

Case

# GridItem.Size.fixed(_:)

A single item with the specified fixed size.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case fixed(CGFloat)

## See Also

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

Case

# GridItem.Size.flexible(minimum:maximum:)

A single flexible item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case flexible(
        minimum: CGFloat = 10,
        maximum: CGFloat = .infinity
    )

## Discussion

The size of this item is the size of the grid with spacing and inflexible
items removed, divided by the number of flexible items, clamped to the
provided bounds.

## See Also

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case fixed(CGFloat)`

A single item with the specified fixed size.

