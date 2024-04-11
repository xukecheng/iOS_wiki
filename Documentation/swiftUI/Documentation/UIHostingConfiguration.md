Initializer

# init(content:)

Creates a hosting configuration with the given contents.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Content` conforms to `View` and `Background` is `EmptyView`.

##  Parameters

`content`

    

The contents of the SwiftUI hierarchy to be shown inside the cell.

Instance Method

# background(_:)

Sets the background contents for the hosting configuration’s enclosing cell.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func background<S>(_ style: S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>> where S : ShapeStyle

##  Parameters

`style`

    

The shape style to be used as the background of the cell.

## Discussion

The following example sets a custom view to the background of the cell:

## See Also

### Setting the background

`func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>`

Sets the background contents for the hosting configuration’s enclosing cell.

Instance Method

# background(content:)

Sets the background contents for the hosting configuration’s enclosing cell.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func background<B>(@ViewBuilder content: () -> B) -> UIHostingConfiguration<Content, B> where B : View

##  Parameters

`background`

    

The contents of the SwiftUI hierarchy to be shown inside the background of the
cell.

## Discussion

The following example sets a custom view to the background of the cell:

## See Also

### Setting the background

`func background<S>(S) -> UIHostingConfiguration<Content,
_UIHostingConfigurationBackgroundView<S>>`

Sets the background contents for the hosting configuration’s enclosing cell.

Instance Method

# margins(_:_:)

Sets the margins around the content of the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func margins(
        _ edges: Edge.Set = .all,
        _ insets: EdgeInsets
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`edges`

    

The edges to apply the insets. Any edges not specified will use the system
default values. The default value is `all`.

`insets`

    

The insets to apply.

## Discussion

Use this modifier to replace the default margins applied to the root of the
configuration. The following example creates 10 points of space between the
content and the background on the leading edge and 20 points of space on the
trailing edge:

## See Also

### Setting margins

`func margins(Edge.Set, CGFloat) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

Instance Method

# margins(_:_:)

Sets the margins around the content of the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func margins(
        _ edges: Edge.Set = .all,
        _ length: CGFloat
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`edges`

    

The edges to apply the insets. Any edges not specified will use the system
default values. The default value is `all`.

`length`

    

The amount to apply.

## Discussion

Use this modifier to replace the default margins applied to the root of the
configuration. The following example creates 20 points of space between the
content and the background on the horizontal edges.

## See Also

### Setting margins

`func margins(Edge.Set, EdgeInsets) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

Instance Method

# minSize(width:height:)

Sets the minimum size for the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func minSize(
        width: CGFloat? = nil,
        height: CGFloat? = nil
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`width`

    

The value to use for the width dimension. A value of `nil` indicates that the
system default should be used.

`height`

    

The value to use for the height dimension. A value of `nil` indicates that the
system default should be used.

## Discussion

Use this modifier to indicate that a configuration’s associated cell can be
resized to a specific minimum. The following example allows the cell to be
compressed to zero size:

## See Also

### Setting a size

`func minSize() -> UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

Deprecated

Instance Method

# minSize()

Sets the minimum size for the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func minSize() -> UIHostingConfiguration<Content, Background>

Deprecated

Use `minSize(width:height:)` instead.

## See Also

### Setting a size

`func minSize(width: CGFloat?, height: CGFloat?) ->
UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

