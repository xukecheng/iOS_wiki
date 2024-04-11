Type Property

# automatic

The automatic mode.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: ToolbarTitleDisplayMode { get }

## Discussion

For root content in a navigation stack in iOS, iPadOS, or tvOS this behavior
will:

  * Default to `large` when a navigation title is configured.

  * Default to `inline` when no navigation title is provided.

In all platforms, content pushed onto a navigation stack will use the behavior
of the content already on the navigation stack. This has no effect in macOS.

## See Also

### Getting display modes

`static var inline: ToolbarTitleDisplayMode`

The inline mode.

`static var inlineLarge: ToolbarTitleDisplayMode`

The inline large mode.

`static var large: ToolbarTitleDisplayMode`

The large mode.

Type Property

# inline

The inline mode.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var inline: ToolbarTitleDisplayMode { get }

## Discussion

In iOS, tvOS, and watchOS this mode displays the title with a smaller size in
the middle of the toolbar. This has no effect in macOS.

## See Also

### Getting display modes

`static var automatic: ToolbarTitleDisplayMode`

The automatic mode.

`static var inlineLarge: ToolbarTitleDisplayMode`

The inline large mode.

`static var large: ToolbarTitleDisplayMode`

The large mode.

Type Property

# inlineLarge

The inline large mode.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var inlineLarge: ToolbarTitleDisplayMode { get }

## Discussion

In iOS, this behavior displays the title as large inside the toolbar and moves
any leading or centered toolbar items into the overflow menu of the toolbar.
This has no effect in macOS.

## See Also

### Getting display modes

`static var automatic: ToolbarTitleDisplayMode`

The automatic mode.

`static var inline: ToolbarTitleDisplayMode`

The inline mode.

`static var large: ToolbarTitleDisplayMode`

The large mode.

Type Property

# large

The large mode.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static var large: ToolbarTitleDisplayMode { get }

## Discussion

In iOS, and watchOS, this displays the toolbar title below the content of the
navigation bar when scrollable content is scrolled to the top and transitions
to the center of the toolbar as content is scrolled.

## See Also

### Getting display modes

`static var automatic: ToolbarTitleDisplayMode`

The automatic mode.

`static var inline: ToolbarTitleDisplayMode`

The inline mode.

`static var inlineLarge: ToolbarTitleDisplayMode`

The inline large mode.

