Instance Method

# toolbar(content:)

Populates the toolbar or navigation bar with the views you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The views representing the content of the toolbar.

## Discussion

Use this modifier to add content to the toolbar. The toolbar modifier expects
a collection of toolbar items that you can provide either by supplying a
collection of views with each view wrapped in a `ToolbarItem`, or by providing
a collection of views as a `ToolbarItemGroup`. The example below adds views to
using a toolbar item group to support text editing features:

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Instance Method

# toolbar(content:)

Populates the toolbar or navigation bar with the specified items.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
    

##  Parameters

`content`

    

The items representing the content of the toolbar.

## Discussion

Use this method to populate a toolbar with a collection of views that you
provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can
provide either by supplying a collection of views with each view wrapped in a
`ToolbarItem`, or by providing a collection of views as a `ToolbarItemGroup`.
The example below uses a collection of `ToolbarItem` views to create a macOS
toolbar that supports text editing features:

Although it’s not mandatory, wrapping a related group of toolbar items
together in a `ToolbarItemGroup` provides a one-to-one mapping between
controls and toolbar items which results in the correct layout and spacing on
each platform. For design guidance on toolbars, see Toolbars in the Human
Interface Guidelines.

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Structure

# ToolbarItem

A model that represents an item which can be placed in the toolbar or
navigation bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ToolbarItem<ID, Content> where Content : View

## Topics

### Creating a toolbar item

`init(placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content.

Available when `ID` is `()` and `Content` conforms to `View`.

`init(id: String, placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

`init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool,
content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

## Relationships

### Conforms To

  * `CustomizableToolbarContent`

Conforms when `ID` is `String` and `Content` conforms to `View`.

  * `Identifiable`
  * `ToolbarContent`

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Structure

# ToolbarItemGroup

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ToolbarItemGroup<Content> where Content : View

## Topics

### Creating a toolbar item group

`init(placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item group with a specified placement and content.

`init<C, L>(placement: ToolbarItemPlacement, content: () -> C, label: () ->
L)`

Creates a toolbar item group with the specified placement, content, and a
label describing that content.

Available when `Content` conforms to `View`.

### Supporting types

`struct LabeledToolbarItemGroupContent`

A view that represents the view of a toolbar item group with a specified
label.

## Relationships

### Conforms To

  * `ToolbarContent`

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Structure

# ToolbarItemPlacement

A structure that defines the placement of a toolbar item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ToolbarItemPlacement

## Overview

There are two types of placements:

  * Semantic placements, such as `principal` and `navigation`, denote the intent of the item being added. SwiftUI determines the appropriate placement for the item based on this intent and its surrounding context, like the current platform.

  * Positional placements, such as `navigationBarLeading`, denote a precise placement for the item, usually for a particular platform.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar
when determining how many items to render in the toolbar. If not all items fit
in the available space, an overflow menu may be created and remaining items
placed in that menu.

## Topics

### Getting semantic placement

`static let automatic: ToolbarItemPlacement`

The system places the item automatically, depending on many factors including
the platform, size class, or presence of other items.

`static let principal: ToolbarItemPlacement`

The system places the item in the principal item section.

`static let status: ToolbarItemPlacement`

The item represents a change in status for the current context.

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

`static let navigation: ToolbarItemPlacement`

The item represents a navigation action.

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

`static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement`

Creates a unique accessory bar placement.

### Deprecated symbols

`init<ID>(id: ID)`

Creates a custom accessory bar item placement.

Deprecated

`static let navigationBarLeading: ToolbarItemPlacement`

Places the item in the leading edge of the navigation bar.

Deprecated

`static let navigationBarTrailing: ToolbarItemPlacement`

Places the item in the trailing edge of the navigation bar.

Deprecated

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Protocol

# ToolbarContent

Conforming types represent items that can be placed in various locations in a
toolbar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol ToolbarContent

## Topics

### Implementing toolbar content

`var body: Self.Body`

The composition of content that comprise the toolbar content.

**Required**

` associatedtype Body : ToolbarContent`

The type of content representing the body of this toolbar content.

**Required**

## Relationships

### Inherited By

  * `CustomizableToolbarContent`

### Conforming Types

  * `Group`

Conforms when `Content` conforms to `CustomizableToolbarContent`.

  * `ToolbarItem`
  * `ToolbarItemGroup`
  * `ToolbarTitleMenu`

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Structure

# ToolbarContentBuilder

Constructs a toolbar item set from multi-expression closures.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct ToolbarContentBuilder

## Topics

### Building toolbar content

`static func buildBlock<Content>(Content) -> some ToolbarContent`

`static func buildBlock<C0, C1>(C0, C1) -> some ToolbarContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some ToolbarContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some ToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some ToolbarContent`

### Building customizable toolbar content

`static func buildBlock<Content>(Content) -> some CustomizableToolbarContent`

`static func buildBlock<C0, C1>(C0, C1) -> some CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some CustomizableToolbarContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some CustomizableToolbarContent`

### Building conditional toolbar content

`static func buildIf<Content>(Content?) -> Content?`

`static func buildIf<Content>(Content?) -> Content?`

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability<Content>(Content) -> some
ToolbarContent`

`static func buildLimitedAvailability<Content>(Content) -> some
CustomizableToolbarContent`

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

Instance Method

# toolbar(id:content:)

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(
        id: String,
        @ToolbarContentBuilder content: () -> Content
    ) -> some View where Content : CustomizableToolbarContent
    

##  Parameters

`id`

    

A unique identifier for this toolbar.

`content`

    

The content representing the content of the toolbar.

## Discussion

Use this modifier when you want to allow the user to customize the components
and layout of elements in the toolbar. The toolbar modifier expects a
collection of toolbar items which you can provide either by supplying a
collection of views with each view wrapped in a `ToolbarItem`.

Note

Customizable toolbars will be displayed on both macOS and iOS, but only apps
running on iPadOS 16.0 and later will support user customization.

The example below creates a view that represents each `ToolbarItem` along with
an ID that uniquely identifies the toolbar item to the customization editor:

Note

Only `secondaryAction` items support customization in iPadOS. Other items
follow the normal placement rules and can’t be customized by the user.

In macOS you can enable menu support for toolbar customization by adding a
`ToolbarCommands` instance to a scene using the `commands(content:)` scene
modifier:

When you add the toolbar commands, the system adds a menu item to your app’s
main menu to provide toolbar customization support. This is in addition to the
ability to Control-click on the toolbar to open the toolbar customization
editor.

## See Also

### Populating a customizable toolbar

`protocol CustomizableToolbarContent`

Conforming types represent items that can be placed in various locations in a
customizable toolbar.

`struct ToolbarCustomizationBehavior`

The customization behavior of customizable toolbar content.

`struct ToolbarCustomizationOptions`

Options that influence the default customization behavior of customizable
toolbar content.

Protocol

# CustomizableToolbarContent

Conforming types represent items that can be placed in various locations in a
customizable toolbar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol CustomizableToolbarContent : ToolbarContent where Self.Body : CustomizableToolbarContent

## Topics

### Using default options

`func defaultCustomization() -> some CustomizableToolbarContent`

Configures customizable toolbar content with the default visibility and
options.

`func defaultCustomization(Visibility, options: ToolbarCustomizationOptions)
-> some CustomizableToolbarContent`

Configures the way customizable toolbar items with the default behavior
behave.

### Customizing the behavior

`func customizationBehavior(ToolbarCustomizationBehavior) -> some
CustomizableToolbarContent`

Configures the customization behavior of customizable toolbar content.

## Relationships

### Inherits From

  * `ToolbarContent`

### Conforming Types

  * `Group`

Conforms when `Content` conforms to `CustomizableToolbarContent`.

  * `ToolbarItem`

Conforms when `ID` is `String` and `Content` conforms to `View`.

  * `ToolbarTitleMenu`

## See Also

### Populating a customizable toolbar

`func toolbar<Content>(id: String, content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

`struct ToolbarCustomizationBehavior`

The customization behavior of customizable toolbar content.

`struct ToolbarCustomizationOptions`

Options that influence the default customization behavior of customizable
toolbar content.

Structure

# ToolbarCustomizationBehavior

The customization behavior of customizable toolbar content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ToolbarCustomizationBehavior

## Overview

Customizable toolbar content support different types of customization
behaviors. For example, some customizable content may not be removed by the
user. Some content may be placed in a toolbar that supports customization
overall, but not for that particular content.

Use this type in conjunction with the `customizationBehavior(_:)` modifier.

## Topics

### Getting customization behaviors

`static var `default`: ToolbarCustomizationBehavior`

The default customization behavior.

`static var disabled: ToolbarCustomizationBehavior`

The disabled customization behavior.

`static var reorderable: ToolbarCustomizationBehavior`

The reorderable customization behavior.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Populating a customizable toolbar

`func toolbar<Content>(id: String, content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

`protocol CustomizableToolbarContent`

Conforming types represent items that can be placed in various locations in a
customizable toolbar.

`struct ToolbarCustomizationOptions`

Options that influence the default customization behavior of customizable
toolbar content.

Structure

# ToolbarCustomizationOptions

Options that influence the default customization behavior of customizable
toolbar content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ToolbarCustomizationOptions

## Overview

Use this type in conjunction with the `defaultCustomization(_:options:)`
modifier.

## Topics

### Getting customization options

`static var alwaysAvailable: ToolbarCustomizationOptions`

Configures default customizable toolbar content to always be present in the
toolbar.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Populating a customizable toolbar

`func toolbar<Content>(id: String, content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

`protocol CustomizableToolbarContent`

Conforming types represent items that can be placed in various locations in a
customizable toolbar.

`struct ToolbarCustomizationBehavior`

The customization behavior of customizable toolbar content.

Instance Method

# toolbar(removing:)

Remove a toolbar item present by default

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func toolbar(removing defaultItemKind: ToolbarDefaultItemKind?) -> some View
    

##  Parameters

`defaultItemKind`

    

The kind of default item to remove

## Discussion

Use this modifier to remove toolbar items other `View`s add by default. For
example, to remove the sidebar toggle toolbar item provided by
`NavigationSplitView`:

## See Also

### Removing default items

`struct ToolbarDefaultItemKind`

A kind of toolbar item a `View` adds by default.

Structure

# ToolbarDefaultItemKind

A kind of toolbar item a `View` adds by default.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ToolbarDefaultItemKind

## Overview

`View`s can add toolbar items clients may wish to remove or customize. A
default item kind can be passed to the `toolbar(removing:)` modifier to remove
the item. Documentation on the `View` placing the default item should
reference the `ToolbarDefaultItemKind` used to remove the item.

## Topics

### Getting the default item types

`static let sidebarToggle: ToolbarDefaultItemKind`

The sidebar toggle toolbar item a `NavigationSplitView` adds by default.

## See Also

### Removing default items

`func toolbar(removing: ToolbarDefaultItemKind?) -> some View`

Remove a toolbar item present by default

Instance Method

# toolbar(_:for:)

Specifies the visibility of a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbar(
        _ visibility: Visibility,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the bar.

`bars`

    

The bars to update the visibility of or `automatic` if empty.

## Discussion

The preferred visibility flows up to the nearest container that renders a bar.
This could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS.

This examples shows a view that hides the navigation bar.

You can provide multiple `ToolbarPlacement` instances to hide multiple bars at
once.

Note

In macOS, if you provide `ToolbarCommands` to the scene of your app, this
modifier disables the toolbar visibility command while the value of the
modifier is not `automatic`.

Depending on the specified bars, the requested visibility may not be able to
be fullfilled.

## See Also

### Setting toolbar visibility

`struct ToolbarPlacement`

The placement of a toolbar.

Structure

# ToolbarPlacement

The placement of a toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ToolbarPlacement

## Overview

Use this type in conjunction with modifiers like `toolbarBackground(_:for:)`
and `toolbar(_:for:)` to customize the appearance of different bars managed by
SwiftUI. Not all bars support all types of customizations.

See `ToolbarItemPlacement` to learn about the different regions of these
toolbars that you can place your own controls into.

## Topics

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

`static var windowToolbar: ToolbarPlacement`

The window toolbar of an app.

### Deprecated symbols

`init<ID>(id: ID)`

Creates a custom accessory bar placement.

Deprecated

## See Also

### Setting toolbar visibility

`func toolbar(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the visibility of a bar managed by SwiftUI.

Instance Method

# toolbarRole(_:)

Configures the semantic role for the content populating the toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarRole(_ role: ToolbarRole) -> some View
    

##  Parameters

`role`

    

The role of the toolbar.

## Discussion

Use this modifier to configure the semantic role for content populating your
app’s toolbar. SwiftUI uses this role when rendering the content of your app’s
toolbar.

## See Also

### Specifying the role of toolbar content

`struct ToolbarRole`

The purpose of content that populates the toolbar.

Structure

# ToolbarRole

The purpose of content that populates the toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ToolbarRole

## Overview

A toolbar role provides a description of the purpose of content that populates
the toolbar. The purpose of the content influences how a toolbar renders its
content. For example, a `browser` will automatically leading align the title
of a toolbar in iPadOS.

Provide this type to the `toolbarRole(_:)` modifier:

## Topics

### Behavior-specific roles

`static var browser: ToolbarRole`

The browser role.

`static var editor: ToolbarRole`

The editor role.

`static var navigationStack: ToolbarRole`

The navigationStack role.

### Automatic roles

`static var automatic: ToolbarRole`

The automatic role.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Specifying the role of toolbar content

`func toolbarRole(ToolbarRole) -> some View`

Configures the semantic role for the content populating the toolbar.

Instance Method

# toolbarBackground(_:for:)

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarBackground<S>(
        _ style: S,
        for bars: ToolbarPlacement...
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The style to display as the background of the bar.

`bars`

    

The bars to use the style for or `automatic` if empty.

## Discussion

The preferred style flows up to the nearest container that renders a bar. This
could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS. This example shows a view that renders the navigation
bar with a blue background and dark color scheme.

You can provide multiple `ToolbarPlacement` instances to customize multiple
bars at once.

When used within a `TabView`, the specified style will be preferred while the
tab is currently active. You can use a `Group` to specify the same preferred
background for every tab.

Depending on the specified bars, the requested style may not be able to be
fullfilled.

## See Also

### Styling a toolbar

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# toolbarBackground(_:for:)

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarBackground(
        _ visibility: Visibility,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the background of the bar.

`bars`

    

The bars to update the color scheme of or `automatic` if empty.

## Discussion

The preferred visibility flows up to the nearest container that renders a bar.
This could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS.

In iOS, a value of `automatic` makes the visibility of a tab bar or navigation
bar background depend on where a `List` or `ScrollView` settles. For example,
when aligned to the bottom edge of of a scroll view’s content, the background
of a tab bar becomes transparent.

Specify a value of `Visibility.visible` to ensure that the background of a bar
remains visible regardless of where any scroll view or list stops scrolling.

This example shows a view that prefers to always have the tab bar visible when
the middle tab is selected:

You can provide multiple placements to customize multiple bars at once, as in
the following example:

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# toolbarColorScheme(_:for:)

Specifies the preferred color scheme of a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarColorScheme(
        _ colorScheme: ColorScheme?,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme of the background of the bar.

`bars`

    

The bars to update the color scheme of or `automatic` if empty.

## Discussion

The preferred color scheme flows up to the nearest container that renders a
bar. This could be a `NavigationView` or `TabView` in iOS, or the root view of
a `WindowGroup` in macOS. Pass in a value of nil to match the current system’s
color scheme.

This examples shows a view that renders the navigation bar with a blue
background and dark color scheme:

You can provide multiple `ToolbarPlacement` instances to customize multiple
bars at once.

Note that the provided color scheme is only respected while a background is
visible in the requested bar. As the background becomes visible, the bar
transitions from the color scheme of the app to the requested color scheme.
You can ensure that the color scheme is always respected by specifying that
the background of the bar always be visible.

Depending on the specified bars, the requested color scheme may not be able to
be fullfilled.

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# windowToolbarStyle(_:)

Sets the style for the toolbar defined within this scene.

macOS 11.0+

    
    
    func windowToolbarStyle<S>(_ style: S) -> some Scene where S : WindowToolbarStyle
    

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Protocol

# WindowToolbarStyle

A specification for the appearance and behavior of a window’s toolbar.

macOS 11.0+

    
    
    protocol WindowToolbarStyle

## Topics

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

## Relationships

### Conforming Types

  * `DefaultWindowToolbarStyle`
  * `ExpandedWindowToolbarStyle`
  * `UnifiedCompactWindowToolbarStyle`
  * `UnifiedWindowToolbarStyle`

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

Instance Method

# toolbarTitleDisplayMode(_:)

Configures the toolbar title display mode for this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func toolbarTitleDisplayMode(_ mode: ToolbarTitleDisplayMode) -> some View
    

## Discussion

Use this modifier to override the default toolbar title display mode.

See `ToolbarTitleDisplayMode` for more information on the different kinds of
display modes. This modifier has no effect on macOS.

## See Also

### Configuring the toolbar title display mode

`struct ToolbarTitleDisplayMode`

A type that defines the behavior of title of a toolbar.

Structure

# ToolbarTitleDisplayMode

A type that defines the behavior of title of a toolbar.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ToolbarTitleDisplayMode

## Overview

Use the `toolbarTitleDisplayMode(_:)` modifier to configure the title display
behavior of your toolbar:

## Topics

### Getting display modes

`static var automatic: ToolbarTitleDisplayMode`

The automatic mode.

`static var inline: ToolbarTitleDisplayMode`

The inline mode.

`static var inlineLarge: ToolbarTitleDisplayMode`

The inline large mode.

`static var large: ToolbarTitleDisplayMode`

The large mode.

## See Also

### Configuring the toolbar title display mode

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View`

Configures the toolbar title display mode for this view.

Instance Method

# toolbarTitleMenu(content:)

Configure the title menu of a toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarTitleMenu<C>(@ViewBuilder content: () -> C) -> some View where C : View
    

##  Parameters

`content`

    

The content associated to the toolbar title menu.

## Discussion

A title menu represent common functionality that can be done on the content
represented by your app’s toolbar or navigation title. This menu may be
populated from your app’s commands like `saveItem` or `printItem`.

You can provide your own set of actions to override this behavior.

In iOS and iPadOS, this will construct a menu that can be presented by tapping
the navigation title in the app’s navigation bar.

## See Also

### Setting the toolbar title menu

`struct ToolbarTitleMenu`

The title menu of a toolbar.

Structure

# ToolbarTitleMenu

The title menu of a toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ToolbarTitleMenu<Content> where Content : View

## Overview

A title menu represents common functionality that can be done on the content
represented by your app’s toolbar or navigation title. This menu may be
populated from your app’s commands like `saveItem` or `printItem`.

You can provide your own set of actions to override this behavior.

In iOS and iPadOS, this will construct a menu that can be presented by tapping
the navigation title in the app’s navigation bar.

## Topics

### Creating a toolbar title menu

`init()`

Creates a toolbar title menu where actions are inferred from your apps
commands.

`init(content: () -> Content)`

Creates a toolbar title menu.

## Relationships

### Conforms To

  * `CustomizableToolbarContent`
  * `ToolbarContent`

## See Also

### Setting the toolbar title menu

`func toolbarTitleMenu<C>(content: () -> C) -> some View`

Configure the title menu of a toolbar.

Instance Method

# ornament(visibility:attachmentAnchor:contentAlignment:ornament:)

Presents an ornament.

visionOS 1.0+

    
    
    func ornament<Content>(
        visibility: Visibility = .automatic,
        attachmentAnchor: OrnamentAttachmentAnchor,
        contentAlignment: Alignment = .center,
        @ViewBuilder ornament: () -> Content
    ) -> some View where Content : View
    

##  Parameters

`visibility`

    

The visibility of the ornament.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the ornament.

`contentAlignment`

    

The alignment of the ornament with its attachment anchor.

`content`

    

The content of the ornament.

## Discussion

Use this method to show an ornament at the specified position. The example
below displays an ornament below the window:

## See Also

### Creating an ornament

`struct OrnamentAttachmentAnchor`

Structure

# OrnamentAttachmentAnchor

visionOS 1.0+

    
    
    struct OrnamentAttachmentAnchor

## Topics

### Getting an anchor

`static func scene(UnitPoint) -> OrnamentAttachmentAnchor`

The anchor point for the ornament expressed as a unit point relative to the
scene.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating an ornament

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> some View`

Presents an ornament.

