Type Property

# automatic

The system places the item automatically, depending on many factors including
the platform, size class, or presence of other items.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let automatic: ToolbarItemPlacement

## Discussion

In macOS and in Mac Catalyst apps, the system places items in the current
toolbar section in order of leading to trailing. On watchOS, only the first
item appears, pinned beneath the navigation bar.

In iPadOS, the system places items in the center of the navigation bar if the
navigation bar supports customization. Otherwise, it places items in the
trailing position of the navigation bar.

In iOS, and tvOS, the system places items in the trailing position of the
navigation bar.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar
when determining how many items to render in the toolbar. If not all items fit
in the available space, an overflow menu may be created and remaining items
placed in that menu.

## See Also

### Getting semantic placement

`static let principal: ToolbarItemPlacement`

The system places the item in the principal item section.

`static let status: ToolbarItemPlacement`

The item represents a change in status for the current context.

Type Property

# principal

The system places the item in the principal item section.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS
1.0+

    
    
    static let principal: ToolbarItemPlacement

## Discussion

Principal actions are key units of functionality that receive prominent
placement. For example, the location field for a web browser is a principal
item.

In macOS and in Mac Catalyst apps, the system places the principal item in the
center of the toolbar.

In iOS, iPadOS, and tvOS, the system places the principal item in the center
of the navigation bar. This item takes precedent over a title specified
through `View/navigationTitle`.

## See Also

### Getting semantic placement

`static let automatic: ToolbarItemPlacement`

The system places the item automatically, depending on many factors including
the platform, size class, or presence of other items.

`static let status: ToolbarItemPlacement`

The item represents a change in status for the current context.

Type Property

# status

The item represents a change in status for the current context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let status: ToolbarItemPlacement

## Discussion

Status items are informational in nature, and don’t represent an action that
can be taken by the user. For example, a message that indicates the time of
the last communication with the server to check for new messages.

In macOS and in Mac Catalyst apps, the system places status items in the
center of the toolbar.

In iOS and iPadOS, the system places status items in the center of the bottom
toolbar.

## See Also

### Getting semantic placement

`static let automatic: ToolbarItemPlacement`

The system places the item automatically, depending on many factors including
the platform, size class, or presence of other items.

`static let principal: ToolbarItemPlacement`

The system places the item in the principal item section.

Type Property

# primaryAction

The item represents a primary action.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let primaryAction: ToolbarItemPlacement

## Discussion

A primary action is a more frequently used action for the current context. For
example, a button the user clicks or taps to compose a new message in a chat
app.

In macOS and in Mac Catalyst apps, the location for the primary action is the
leading edge of the toolbar.

In iOS, iPadOS, and tvOS, the location for the primary action is the trailing
edge of the navigation bar.

In watchOS the system places the primary action beneath the navigation bar;
the user reveals the action by scrolling.

## See Also

### Getting placement for specific actions

`static let secondaryAction: ToolbarItemPlacement`

The item represents a secondary action.

`static let confirmationAction: ToolbarItemPlacement`

The item represents a confirmation action for a modal interface.

`static let cancellationAction: ToolbarItemPlacement`

The item represents a cancellation action for a modal interface.

`static let destructiveAction: ToolbarItemPlacement`

The item represents a destructive action for a modal interface.

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

Type Property

# secondaryAction

The item represents a secondary action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static let secondaryAction: ToolbarItemPlacement

## Discussion

A secondary action is a frequently used action for the current context but is
not a requirement for the current context to function.

## See Also

### Getting placement for specific actions

`static let primaryAction: ToolbarItemPlacement`

The item represents a primary action.

`static let confirmationAction: ToolbarItemPlacement`

The item represents a confirmation action for a modal interface.

`static let cancellationAction: ToolbarItemPlacement`

The item represents a cancellation action for a modal interface.

`static let destructiveAction: ToolbarItemPlacement`

The item represents a destructive action for a modal interface.

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

Type Property

# confirmationAction

The item represents a confirmation action for a modal interface.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let confirmationAction: ToolbarItemPlacement

## Discussion

Use confirmation actions to receive user confirmation of a particular action.
An example of a confirmation action would be an action with the label “Add” to
add a new event to the calendar.

In macOS and in Mac Catalyst apps, the system places `confirmationAction`
items on the trailing edge in the trailing-most position of the sheet and gain
the apps accent color as a background color.

In iOS, iPadOS, and tvOS, the system places `confirmationAction` items in the
same location as a `primaryAction` placement.

In watchOS, the system places `confirmationAction` items in the trailing edge
of the navigation bar.

## See Also

### Getting placement for specific actions

`static let primaryAction: ToolbarItemPlacement`

The item represents a primary action.

`static let secondaryAction: ToolbarItemPlacement`

The item represents a secondary action.

`static let cancellationAction: ToolbarItemPlacement`

The item represents a cancellation action for a modal interface.

`static let destructiveAction: ToolbarItemPlacement`

The item represents a destructive action for a modal interface.

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

Type Property

# cancellationAction

The item represents a cancellation action for a modal interface.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let cancellationAction: ToolbarItemPlacement

## Discussion

Cancellation actions dismiss the modal interface without taking any action,
usually by tapping or clicking a Cancel button.

In macOS and in Mac Catalyst apps, the system places `cancellationAction`
items on the trailing edge of the sheet but places them before any
`confirmationAction` items.

In iOS, iPadOS, tvOS, and watchOS, the system places `cancellationAction`
items on the leading edge of the navigation bar.

## See Also

### Getting placement for specific actions

`static let primaryAction: ToolbarItemPlacement`

The item represents a primary action.

`static let secondaryAction: ToolbarItemPlacement`

The item represents a secondary action.

`static let confirmationAction: ToolbarItemPlacement`

The item represents a confirmation action for a modal interface.

`static let destructiveAction: ToolbarItemPlacement`

The item represents a destructive action for a modal interface.

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

Type Property

# destructiveAction

The item represents a destructive action for a modal interface.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let destructiveAction: ToolbarItemPlacement

## Discussion

Destructive actions represent the opposite of a confirmation action. For
example, a button labeled “Don’t Save” that allows the user to discard unsaved
changes to a document before quitting.

In macOS and in Mac Catalyst apps, the system places `destructiveAction` items
in the leading edge of the sheet and gives them a special appearance to
caution against accidental use.

In iOS, tvOS, and watchOS, the system places `destructiveAction` items in the
trailing edge of the navigation bar.

## See Also

### Getting placement for specific actions

`static let primaryAction: ToolbarItemPlacement`

The item represents a primary action.

`static let secondaryAction: ToolbarItemPlacement`

The item represents a secondary action.

`static let confirmationAction: ToolbarItemPlacement`

The item represents a confirmation action for a modal interface.

`static let cancellationAction: ToolbarItemPlacement`

The item represents a cancellation action for a modal interface.

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

Type Property

# navigation

The item represents a navigation action.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS
1.0+

    
    
    static let navigation: ToolbarItemPlacement

## Discussion

Navigation actions allow the user to move between contexts. For example, the
forward and back buttons of a web browser are navigation actions.

In macOS and in Mac Catalyst apps, the system places navigation items in the
leading edge of the toolbar ahead of the inline title if that is present in
the toolbar.

In iOS, iPadOS, and tvOS, navigation items appear in the leading edge of the
navigation bar. If a system navigation item such as a back button is present
in a compact width, it instead appears in the `primaryAction` placement.

## See Also

### Getting placement for specific actions

`static let primaryAction: ToolbarItemPlacement`

The item represents a primary action.

`static let secondaryAction: ToolbarItemPlacement`

The item represents a secondary action.

`static let confirmationAction: ToolbarItemPlacement`

The item represents a confirmation action for a modal interface.

`static let cancellationAction: ToolbarItemPlacement`

The item represents a cancellation action for a modal interface.

`static let destructiveAction: ToolbarItemPlacement`

The item represents a destructive action for a modal interface.

Type Property

# topBarLeading

Places the item in the leading edge of the top bar.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @backDeployed(before: iOS 17.0, tvOS 17.0)
    static var topBarLeading: ToolbarItemPlacement { get }

## Discussion

On watchOS, iOS, and tvOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement

`static var topBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the top bar.

`static let bottomBar: ToolbarItemPlacement`

Places the item in the bottom toolbar.

`static let bottomOrnament: ToolbarItemPlacement`

Places the item in an ornament under the window.

`static let keyboard: ToolbarItemPlacement`

The item is placed in the keyboard section.

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

Type Property

# topBarTrailing

Places the item in the trailing edge of the top bar.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @backDeployed(before: iOS 17.0, tvOS 17.0)
    static var topBarTrailing: ToolbarItemPlacement { get }

## Discussion

On watchOS, iOS, and tvOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement

`static var topBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the top bar.

`static let bottomBar: ToolbarItemPlacement`

Places the item in the bottom toolbar.

`static let bottomOrnament: ToolbarItemPlacement`

Places the item in an ornament under the window.

`static let keyboard: ToolbarItemPlacement`

The item is placed in the keyboard section.

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

Type Property

# bottomBar

Places the item in the bottom toolbar.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static let bottomBar: ToolbarItemPlacement

## See Also

### Getting explicit placement

`static var topBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the top bar.

`static var topBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the top bar.

`static let bottomOrnament: ToolbarItemPlacement`

Places the item in an ornament under the window.

`static let keyboard: ToolbarItemPlacement`

The item is placed in the keyboard section.

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

Type Property

# bottomOrnament

Places the item in an ornament under the window.

visionOS 1.0+

    
    
    static let bottomOrnament: ToolbarItemPlacement

## See Also

### Getting explicit placement

`static var topBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the top bar.

`static var topBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the top bar.

`static let bottomBar: ToolbarItemPlacement`

Places the item in the bottom toolbar.

`static let keyboard: ToolbarItemPlacement`

The item is placed in the keyboard section.

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

Type Property

# keyboard

The item is placed in the keyboard section.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+

    
    
    static let keyboard: ToolbarItemPlacement

## Discussion

On iOS, keyboard items are above the software keyboard when present, or at the
bottom of the screen when a hardware keyboard is attached.

On macOS, keyboard items will be placed inside the Touch Bar.

A `FocusedValue`can be used to adjust the content of the keyboard bar based on
the currently focused view. In the example below, the keyboard bar gains
additional buttons only when the appropriate `TextField` is focused.

## See Also

### Getting explicit placement

`static var topBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the top bar.

`static var topBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the top bar.

`static let bottomBar: ToolbarItemPlacement`

Places the item in the bottom toolbar.

`static let bottomOrnament: ToolbarItemPlacement`

Places the item in an ornament under the window.

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

Type Method

# accessoryBar(id:)

Creates a unique accessory bar placement.

macOS 13.0+

    
    
    @backDeployed(before: macOS 14.0)
    static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement where ID : Hashable

##  Parameters

`id`

    

A unique identifier for this placement.

## Discussion

On macOS, items with an accessory bar placement are placed in a section below
the title bar and toolbar area of the window. Each separate identifier will
correspond to a separate accessory bar that is added to this area.

## See Also

### Getting explicit placement

`static var topBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the top bar.

`static var topBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the top bar.

`static let bottomBar: ToolbarItemPlacement`

Places the item in the bottom toolbar.

`static let bottomOrnament: ToolbarItemPlacement`

Places the item in an ornament under the window.

`static let keyboard: ToolbarItemPlacement`

The item is placed in the keyboard section.

Initializer

# init(id:)

Creates a custom accessory bar item placement.

macOS 13.0–14.0  Deprecated

    
    
    init<ID>(id: ID) where ID : Hashable

Deprecated

Use `accessoryBar(id:)` instead.

## See Also

### Deprecated symbols

`static let navigationBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the navigation bar.

Deprecated

`static let navigationBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the navigation bar.

Deprecated

Type Property

# navigationBarLeading

Places the item in the leading edge of the navigation bar.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  Mac Catalyst
14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated  visionOS 1.0+

    
    
    static let navigationBarLeading: ToolbarItemPlacement

Deprecated

Use `topBarLeading` instead.

## See Also

### Deprecated symbols

`init<ID>(id: ID)`

Creates a custom accessory bar item placement.

Deprecated

`static let navigationBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the navigation bar.

Deprecated

Type Property

# navigationBarTrailing

Places the item in the trailing edge of the navigation bar.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  Mac Catalyst
14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated  visionOS 1.0+

    
    
    static let navigationBarTrailing: ToolbarItemPlacement

Deprecated

Use `topBarTrailing` instead.

## See Also

### Deprecated symbols

`init<ID>(id: ID)`

Creates a custom accessory bar item placement.

Deprecated

`static let navigationBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the navigation bar.

Deprecated

