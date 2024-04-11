Type Property

# automatic

The primary toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: ToolbarPlacement { get }

## Discussion

Depending on the context, this may refer to the navigation bar of an app on
iOS, or watchOS, the tab bar of an app on tvOS, or the window toolbar of an
app on macOS.

## See Also

### Getting placements

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Method

# accessoryBar(id:)

Creates a unique accessory bar placement.

macOS 13.0+

    
    
    @backDeployed(before: macOS 14.0)
    static func accessoryBar<ID>(id: ID) -> ToolbarPlacement where ID : Hashable

##  Parameters

`id`

    

A unique identifier for this placement.

## Discussion

On macOS, accessory bars are in a section below the title bar and toolbar area
of the window. Each separate identifier will correspond to a separate
accessory bar that is added to this area.

Use a custom placement to control the appearance of the containing bar for
items using a custom `ToolbarItemPlacement` with the same identifier.

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Property

# bottomBar

The bottom toolbar of an app.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static var bottomBar: ToolbarPlacement { get }

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Property

# bottomOrnament

The bottom ornament of an app.

visionOS 1.0+

    
    
    static var bottomOrnament: ToolbarPlacement { get }

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Property

# navigationBar

The navigation bar of an app.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var navigationBar: ToolbarPlacement { get }

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Property

# tabBar

The tab bar of an app.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    static var tabBar: ToolbarPlacement { get }

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

Type Property

# windowToolbar

The window toolbar of an app.

macOS 13.0+

    
    
    static var windowToolbar: ToolbarPlacement { get }

## See Also

### Getting placements

`static var automatic: ToolbarPlacement`

The primary toolbar.

`static func accessoryBar<ID>(id: ID) -> ToolbarPlacement`

Creates a unique accessory bar placement.

`static var bottomBar: ToolbarPlacement`

The bottom toolbar of an app.

`static var bottomOrnament: ToolbarPlacement`

The bottom ornament of an app.

`static var navigationBar: ToolbarPlacement`

The navigation bar of an app.

`static var tabBar: ToolbarPlacement`

The tab bar of an app.

Initializer

# init(id:)

Creates a custom accessory bar placement.

macOS 13.0–14.0  Deprecated

    
    
    init<ID>(id: ID) where ID : Hashable

Deprecated

Use `init(id:)` instead.

