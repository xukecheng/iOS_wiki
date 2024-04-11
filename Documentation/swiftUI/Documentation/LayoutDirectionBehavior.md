Case

# LayoutDirectionBehavior.fixed

A behavior that doesn’t mirror when the layout direction changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case fixed

## See Also

### Getting behaviors

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

Type Property

# mirrors

A behavior that mirrors when the layout direction is right-to-left.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var mirrors: LayoutDirectionBehavior { get }

## See Also

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

Case

# LayoutDirectionBehavior.mirrors(in:)

A behavior that mirrors when the layout direction has the specified value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case mirrors(in: LayoutDirection)

## Discussion

If you develop your view or shape in an LTR context, you can use `.mirrors(in:
.rightToLeft)` (which is equivalent to `.mirrors`) to mirror your content when
the layout direction is RTL (and keep the original version in LTR). If you
developer in an RTL context, you can use `.mirrors(in: .leftToRight)` to
mirror your content when the layout direction is LTR (and keep the original
version in RTL).

## See Also

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.

