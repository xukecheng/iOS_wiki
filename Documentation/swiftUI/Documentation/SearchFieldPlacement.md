Type Property

# automatic

SwiftUI places the search field automatically.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let automatic: SearchFieldPlacement

## Discussion

Placement of the search field depends on the platform:

  * In iOS, iPadOS, and macOS, the search field appears in the toolbar.

  * In tvOS and watchOS, the search field appears inline with its content.

## See Also

### Getting a search field placement

`static let navigationBarDrawer: SearchFieldPlacement`

The search field appears in the navigation bar.

`static func navigationBarDrawer(displayMode:
SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement`

The search field appears in the navigation bar using the specified display
mode.

`static let sidebar: SearchFieldPlacement`

The search field appears in the sidebar of a navigation view.

`static let toolbar: SearchFieldPlacement`

The search field appears in the toolbar.

Type Property

# navigationBarDrawer

The search field appears in the navigation bar.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  watchOS 8.0+  visionOS 1.0+

    
    
    static let navigationBarDrawer: SearchFieldPlacement

## Discussion

The field appears below any navigation bar title and uses the `automatic`
display mode to configure when to hide the search field. To choose a different
display mode, use `navigationBarDrawer(displayMode:)` instead.

## See Also

### Getting a search field placement

`static let automatic: SearchFieldPlacement`

SwiftUI places the search field automatically.

`static func navigationBarDrawer(displayMode:
SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement`

The search field appears in the navigation bar using the specified display
mode.

`static let sidebar: SearchFieldPlacement`

The search field appears in the sidebar of a navigation view.

`static let toolbar: SearchFieldPlacement`

The search field appears in the toolbar.

Type Method

# navigationBarDrawer(displayMode:)

The search field appears in the navigation bar using the specified display
mode.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement

##  Parameters

`displayMode`

    

A control that indicates whether to hide the search field in response to
scrolling.

## Discussion

The field appears below any navigation bar title. The system can hide the
field in response to scrolling, depending on the `displayMode` that you set.

## See Also

### Getting a search field placement

`static let automatic: SearchFieldPlacement`

SwiftUI places the search field automatically.

`static let navigationBarDrawer: SearchFieldPlacement`

The search field appears in the navigation bar.

`static let sidebar: SearchFieldPlacement`

The search field appears in the sidebar of a navigation view.

`static let toolbar: SearchFieldPlacement`

The search field appears in the toolbar.

Type Property

# sidebar

The search field appears in the sidebar of a navigation view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let sidebar: SearchFieldPlacement

## Discussion

The precise placement depends on the platform:

  * In iOS and iPadOS the search field appears in the section of the navigation bar associated with the sidebar.

  * In macOS, the search field appears inline with the sidebar’s content.

If a sidebar isn’t available, like when you apply the searchable modifier to a
view other than a navigation split view, SwiftUI uses automatic placement
instead.

## See Also

### Getting a search field placement

`static let automatic: SearchFieldPlacement`

SwiftUI places the search field automatically.

`static let navigationBarDrawer: SearchFieldPlacement`

The search field appears in the navigation bar.

`static func navigationBarDrawer(displayMode:
SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement`

The search field appears in the navigation bar using the specified display
mode.

`static let toolbar: SearchFieldPlacement`

The search field appears in the toolbar.

Type Property

# toolbar

The search field appears in the toolbar.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static let toolbar: SearchFieldPlacement

## Discussion

The precise placement depends on the platform:

  * In iOS and watchOS, the search field appears below the navigation bar and is revealed by scrolling.

  * In iPadOS, the search field appears in the trailing navigation bar.

  * In macOS, the search field appears in the trailing toolbar.

## See Also

### Getting a search field placement

`static let automatic: SearchFieldPlacement`

SwiftUI places the search field automatically.

`static let navigationBarDrawer: SearchFieldPlacement`

The search field appears in the navigation bar.

`static func navigationBarDrawer(displayMode:
SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement`

The search field appears in the navigation bar using the specified display
mode.

`static let sidebar: SearchFieldPlacement`

The search field appears in the sidebar of a navigation view.

Structure

# SearchFieldPlacement.NavigationBarDrawerDisplayMode

A mode that determines when to display a search field that appears in a
navigation bar.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct NavigationBarDrawerDisplayMode

## Topics

### Getting display modes

`static let always: SearchFieldPlacement.NavigationBarDrawerDisplayMode`

Always display the search field regardless of the scroll activity.

`static let automatic: SearchFieldPlacement.NavigationBarDrawerDisplayMode`

Enable hiding the search field in response to scrolling.

## Relationships

### Conforms To

  * `Sendable`

