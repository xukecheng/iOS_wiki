Type Property

# alwaysAvailable

Configures default customizable toolbar content to always be present in the
toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var alwaysAvailable: ToolbarCustomizationOptions { get }

## Discussion

In iOS, default customizable toolbar content have the option of always being
available in the toolbar regardless of the customization status of the user.
These items will always be in the overflow menu of the toolbar. Users can
customize whether the items are present as controls in the toolbar itself but
will still always be able to access the item if they remove it from the
toolbar itself.

Consider using this for items that users should always be able to access, but
may not be important enough to always occupy space in the toolbar itself.

