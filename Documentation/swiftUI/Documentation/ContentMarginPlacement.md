Type Property

# automatic

The automatic placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: ContentMarginPlacement { get }

## Discussion

Views that support margin customization can automatically use margins with
this placement. For example, a `ScrollView` will use this placement to
automatically inset both its content and scroll indicators by the specified
amount.

## See Also

### Getting the placement

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

Type Property

# scrollContent

The scroll content placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollContent: ContentMarginPlacement { get }

## Discussion

Scrollable views like `ScrollView` will use this placement to inset their
content, but not their scroll indicators.

## See Also

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

Type Property

# scrollIndicators

The scroll indicators placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollIndicators: ContentMarginPlacement { get }

## Discussion

Scrollable views like `ScrollView` will use this placement to inset their
scroll indicators, but not their content.

## See Also

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.

