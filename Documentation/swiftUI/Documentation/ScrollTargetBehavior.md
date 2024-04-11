Type Property

# paging

The scroll behavior that aligns scroll targets to container-based geometry.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var paging: PagingScrollTargetBehavior { get }

Available when `Self` is `PagingScrollTargetBehavior`.

## Discussion

In the following example, every view in the lazy stack is flexible in both
directions and the scroll view settles to container-aligned boundaries.

## See Also

### Getting the scroll target behavior

`static var viewAligned: ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

`static func viewAligned(limitBehavior:
ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

Type Property

# viewAligned

The scroll behavior that aligns scroll targets to view-based geometry.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var viewAligned: ViewAlignedScrollTargetBehavior { get }

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

## Discussion

You use this behavior when a scroll view should always align its scroll
targets to a rectangle that’s aligned to the geometry of a view. In the
following example, the scroll view always picks an item view to settle on.

You configure which views should be used for settling using the
`View/scrollTargetLayout()` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views
that can be scrolled at a time by using the
`ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of
`ViewAlignedScrollTargetBehavior.LimitBehavior/always` to always have the
behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior limits the number of views it scrolls
when in a compact horizontal size class when scrollable in the horizontal
axis, when in a compact vertical size class when scrollable in the vertical
axis, and otherwise doesn’t impose any limit on the number of views that can
be scrolled.

## See Also

### Getting the scroll target behavior

`static var paging: PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

Available when `Self` is `PagingScrollTargetBehavior`.

`static func viewAligned(limitBehavior:
ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

Type Method

# viewAligned(limitBehavior:)

The scroll behavior that aligns scroll targets to view-based geometry.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func viewAligned(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

## Discussion

You use this behavior when a scroll view should always align its scroll
targets to a rectangle that’s aligned to the geometry of a view. In the
following example, the scroll view always picks an item view to settle on.

You configure which views should be used for settling using the
`View/scrollTargetLayout()` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views
that can be scrolled at a time by using the
`ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of
`ViewAlignedScrollTargetBehavior.LimitBehavior/always` to always have the
behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior limits the number of views it scrolls
when in a compact horizontal size class when scrollable in the horizontal
axis, when in a compact vertical size class when scrollable in the vertical
axis, and otherwise doesn’t impose any limit on the number of views that can
be scrolled.

## See Also

### Getting the scroll target behavior

`static var paging: PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

Available when `Self` is `PagingScrollTargetBehavior`.

`static var viewAligned: ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

Instance Method

# updateTarget(_:context:)

Updates the proposed target that a scrollable view should scroll to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func updateTarget(
        _ target: inout ScrollTarget,
        context: Self.TargetContext
    )

**Required**

## Discussion

The system calls this method in two main cases:

  * When a scroll gesture ends, it calculates where it would naturally scroll to using its deceleration rate. The system provides this calculated value as the target of this method.

  * When a scrollable view’s size changes, it calculates where it should be scrolled given the new size and provides this calculates value as the target of this method.

You can implement this method to override the calculated target which will
have the scrollable view scroll to a different position than it would
otherwise.

## See Also

### Updating the proposed target

`typealias TargetContext`

The context in which a scroll behavior updates the scroll target.

Type Alias

# ScrollTargetBehavior.TargetContext

The context in which a scroll behavior updates the scroll target.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    typealias TargetContext = ScrollTargetBehaviorContext

## See Also

### Updating the proposed target

`func updateTarget(inout ScrollTarget, context: Self.TargetContext)`

Updates the proposed target that a scrollable view should scroll to.

**Required**

