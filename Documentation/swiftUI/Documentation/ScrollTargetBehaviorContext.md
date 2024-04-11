Instance Property

# axes

The axes in which the scrollable view is scrollable.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var axes: Axis.Set { get }

## See Also

### Getting the scroll target behavior context

`var containerSize: CGSize`

The size of the container of the scrollable view.

`var contentSize: CGSize`

The size of the content of the scrollable view.

`var originalTarget: ScrollTarget`

The original target when the scroll gesture began.

`var velocity: CGVector`

The current velocity of the scrollable view’s scroll gesture.

Instance Property

# containerSize

The size of the container of the scrollable view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var containerSize: CGSize { get }

## Discussion

This is the size of the bounds of the scroll view subtracting any insets
applied to the scroll view (like the safe area).

## See Also

### Getting the scroll target behavior context

`var axes: Axis.Set`

The axes in which the scrollable view is scrollable.

`var contentSize: CGSize`

The size of the content of the scrollable view.

`var originalTarget: ScrollTarget`

The original target when the scroll gesture began.

`var velocity: CGVector`

The current velocity of the scrollable view’s scroll gesture.

Instance Property

# contentSize

The size of the content of the scrollable view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var contentSize: CGSize { get }

## See Also

### Getting the scroll target behavior context

`var axes: Axis.Set`

The axes in which the scrollable view is scrollable.

`var containerSize: CGSize`

The size of the container of the scrollable view.

`var originalTarget: ScrollTarget`

The original target when the scroll gesture began.

`var velocity: CGVector`

The current velocity of the scrollable view’s scroll gesture.

Instance Property

# originalTarget

The original target when the scroll gesture began.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var originalTarget: ScrollTarget { get }

## See Also

### Getting the scroll target behavior context

`var axes: Axis.Set`

The axes in which the scrollable view is scrollable.

`var containerSize: CGSize`

The size of the container of the scrollable view.

`var contentSize: CGSize`

The size of the content of the scrollable view.

`var velocity: CGVector`

The current velocity of the scrollable view’s scroll gesture.

Instance Property

# velocity

The current velocity of the scrollable view’s scroll gesture.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var velocity: CGVector { get }

## See Also

### Getting the scroll target behavior context

`var axes: Axis.Set`

The axes in which the scrollable view is scrollable.

`var containerSize: CGSize`

The size of the container of the scrollable view.

`var contentSize: CGSize`

The size of the content of the scrollable view.

`var originalTarget: ScrollTarget`

The original target when the scroll gesture began.

Instance Subscript

# subscript(dynamicMember:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<T>(dynamicMember keyPath: KeyPath<EnvironmentValues, T>) -> T { get }

