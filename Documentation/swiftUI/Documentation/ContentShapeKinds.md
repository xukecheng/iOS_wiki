Type Property

# interaction

The kind for hit-testing and accessibility.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let interaction: ContentShapeKinds

## Discussion

Setting a content shape with this kind causes the view to hit-test using the
specified shape.

## See Also

### Getting shape kinds

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# dragPreview

The kind for drag and drop previews.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let dragPreview: ContentShapeKinds

## Discussion

When using this kind, only the preview shape is affected. To control the shape
used to hit-test and start the drag preview, use the `interaction` kind.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# contextMenuPreview

The kind for context menu previews.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static let contextMenuPreview: ContentShapeKinds

## Discussion

When using this kind, only the preview shape will be affected. To control the
shape used to hit-test and start the context menu presentation, use the
`.interaction` kind.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# focusEffect

The kind for the focus effect.

macOS 12.0+  watchOS 8.0+

    
    
    static let focusEffect: ContentShapeKinds

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# hoverEffect

The kind for hover effects.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let hoverEffect: ContentShapeKinds

## Discussion

When using this kind, only the preview shape is affected. To control the shape
used to hit-test and start the effect, use the `interaction` kind.

This kind does not affect the `onHover` modifier.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Initializer

# init(rawValue:)

Creates a content shape kind.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(rawValue: Int)

