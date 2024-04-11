Type Property

# default

The default customization behavior.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var `default`: ToolbarCustomizationBehavior { get }

## Discussion

Items with this behavior start in the toolbar and can be moved or removed from
the toolbar by the user.

## See Also

### Getting customization behaviors

`static var disabled: ToolbarCustomizationBehavior`

The disabled customization behavior.

`static var reorderable: ToolbarCustomizationBehavior`

The reorderable customization behavior.

Type Property

# disabled

The disabled customization behavior.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var disabled: ToolbarCustomizationBehavior { get }

## Discussion

Items with this behavior may not be removed or moved by the user. They will be
placed before other customizatable items. Use this behavior for the most
important items that users need for the app to do common functionality.

## See Also

### Getting customization behaviors

`static var `default`: ToolbarCustomizationBehavior`

The default customization behavior.

`static var reorderable: ToolbarCustomizationBehavior`

The reorderable customization behavior.

Type Property

# reorderable

The reorderable customization behavior.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var reorderable: ToolbarCustomizationBehavior { get }

## Discussion

Items with this behavior start in the toolbar and can be moved within the
toolbar by the user, but can not be removed from the toolbar.

## See Also

### Getting customization behaviors

`static var `default`: ToolbarCustomizationBehavior`

The default customization behavior.

`static var disabled: ToolbarCustomizationBehavior`

The disabled customization behavior.

