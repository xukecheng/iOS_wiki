Type Property

# appInfo

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appInfo: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * About App

## See Also

### App interactions

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appSettings

Placement for commands that expose app settings and preferences.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appSettings: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Preferences

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appTermination

Placement for commands that result in app termination.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appTermination: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Quit App

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appVisibility

Placement for commands that control the visibility of running apps.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appVisibility: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Hide App

  * Hide Others

  * Show All

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# systemServices

Placement for commands that expose services other apps provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let systemServices: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Services submenu (managed automatically)

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

Type Property

# importExport

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let importExport: CommandGroupPlacement

## Discussion

Empty by default in macOS.

## See Also

### File manipulation

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# newItem

Placement for commands that create and open different kinds of documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let newItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * New

  * Open

  * Open Recent submenu (managed automatically)

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# printItem

Placement for commands related to printing app content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let printItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Page Setup

  * Print

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# saveItem

Placement for commands that save open documents and close windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let saveItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Close

  * Save

  * Save As/Duplicate

  * Revert to Saved

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

Type Property

# pasteboard

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let pasteboard: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Cut

  * Copy

  * Paste

  * Paste and Match Style

  * Delete

  * Select All

## See Also

### Content updates

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# textEditing

Placement for commands that manipulate and transform text selections.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let textEditing: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Find submenu

  * Spelling and Grammar submenu

  * Substitutions submenu

  * Transformations submenu

  * Speech submenu

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# textFormatting

Placement for commands that manipulate and transform the styles applied to
text selections.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let textFormatting: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Font submenu

  * Text submenu

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# undoRedo

Placement for commands that control the Undo Manager.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let undoRedo: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Undo

  * Redo

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

Type Property

# sidebar

Placement for commands that control the app’s sidebar and full-screen modes.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let sidebar: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Show/Hide Sidebar

  * Enter/Exit Full Screen

## See Also

### Bars

`static let toolbar: CommandGroupPlacement`

Placement for commands that manipulate the toolbar.

Type Property

# toolbar

Placement for commands that manipulate the toolbar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let toolbar: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Show/Hide Toolbar

  * Customize Toolbar

## See Also

### Bars

`static let sidebar: CommandGroupPlacement`

Placement for commands that control the app’s sidebar and full-screen modes.

Type Property

# singleWindowList

Placement for commands that describe and reveal any windows that the app
defines.

macOS 13.0+

    
    
    static let singleWindowList: CommandGroupPlacement

## See Also

### Windows

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowArrangement

Placement for commands that arrange all of an app’s windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let windowArrangement: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Bring All to Front

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowList

Placement for commands that describe and reveal the app’s open windows.

macOS 11.0+

    
    
    static let windowList: CommandGroupPlacement

## Discussion

SwiftUI manages this group automatically in macOS.

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowSize

Placement for commands that control the size of the window.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let windowSize: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Minimize

  * Zoom

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

Type Property

# help

Placement for commands that present documentation and helpful information to
people.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let help: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * App Help

