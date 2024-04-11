Type Property

# automatic

The ordering of the menu chosen by the system for the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let automatic: MenuOrder

## Discussion

On iOS, this order resolves to `fixed` for menus presented within scrollable
content. Pickers that use the `menu` style also default to `fixed` order. In
all other cases, menus default to `priority` order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to `fixed`
order.

## See Also

### Getting menu orders

`static let fixed: MenuOrder`

Order items from top to bottom.

`static let priority: MenuOrder`

Keep the first items closest to user’s interaction point.

Type Property

# fixed

Order items from top to bottom.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let fixed: MenuOrder

## See Also

### Getting menu orders

`static let automatic: MenuOrder`

The ordering of the menu chosen by the system for the current context.

`static let priority: MenuOrder`

Keep the first items closest to user’s interaction point.

Type Property

# priority

Keep the first items closest to user’s interaction point.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static let priority: MenuOrder

## See Also

### Getting menu orders

`static let automatic: MenuOrder`

The ordering of the menu chosen by the system for the current context.

`static let fixed: MenuOrder`

Order items from top to bottom.

