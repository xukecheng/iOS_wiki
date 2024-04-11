Type Property

# browser

The browser role.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var browser: ToolbarRole { get }

## Discussion

Use this role for content that can be navigated forwards and backwards. In
iPadOS, this will leading align the navigation title and allow for toolbar
items to occupy the center of the navigation bar.

## See Also

### Behavior-specific roles

`static var editor: ToolbarRole`

The editor role.

`static var navigationStack: ToolbarRole`

The navigationStack role.

Type Property

# editor

The editor role.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var editor: ToolbarRole { get }

## Discussion

Use this role for a toolbar that primarily displays controls geared towards
editing document-like content. In iPadOS, this will leading align the
navigation title, allow for toolbar items to occupy the center of the
navigation bar, and provide a custom appearance for any back button present in
the toolbar.

## See Also

### Behavior-specific roles

`static var browser: ToolbarRole`

The browser role.

`static var navigationStack: ToolbarRole`

The navigationStack role.

Type Property

# navigationStack

The navigationStack role.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var navigationStack: ToolbarRole { get }

## Discussion

Use this role for content that can be pushed and popped.

## See Also

### Behavior-specific roles

`static var browser: ToolbarRole`

The browser role.

`static var editor: ToolbarRole`

The editor role.

Type Property

# automatic

The automatic role.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: ToolbarRole { get }

## Discussion

In iOS, tvOS, and watchOS this resolves to the `navigationStack` role. In
macOS, this resolves to the `editor` role.

