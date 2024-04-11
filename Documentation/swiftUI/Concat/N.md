# NavigationSplitViewVisibility

Type Property

# automatic

Use the default leading column visibility for the current device.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: NavigationSplitViewVisibility { get }

## Discussion

This computed property returns one of the three concrete cases: `detailOnly`,
`doubleColumn`, or `all`.

## See Also

### Getting visibilities

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# all

Show all the columns of a three-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var all: NavigationSplitViewVisibility { get }

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# doubleColumn

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var doubleColumn: NavigationSplitViewVisibility { get }

## Discussion

For a two-column navigation split view, `doubleColumn` is equivalent to `all`.

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# detailOnly

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var detailOnly: NavigationSplitViewVisibility { get }

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.



# NSViewControllerRepresentable

Instance Method

# makeNSViewController(context:)

Creates the view controller object and configures its initial state.

macOS 10.15+

    
    
    @MainActor
    func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your AppKit view controller configured with the provided information.

## Discussion

You must implement this method and use it to create your view controller
object. Create the view controller using your app’s current data and contents
of the `context` parameter. The system calls this method only once, when it
creates your view controller for the first time. For all subsequent updates,
the system calls the `updateNSViewController(_:context:)` method.

## See Also

### Creating and updating the view controller

`func updateNSViewController(Self.NSViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

`associatedtype NSViewControllerType : NSViewController`

The type of view controller to present.

**Required**

Instance Method

# updateNSViewController(_:context:)

Updates the state of the specified view controller with new information from
SwiftUI.

macOS 10.15+

    
    
    @MainActor
    func updateNSViewController(
        _ nsViewController: Self.NSViewControllerType,
        context: Self.Context
    )

**Required**

##  Parameters

`nsViewController`

    

Your custom view controller object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding AppKit view controller. Use this method to update
the configuration of your view controller to match the new state information
provided in the `context` parameter.

## See Also

### Creating and updating the view controller

`func makeNSViewController(context: Self.Context) ->
Self.NSViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` typealias Context`

`associatedtype NSViewControllerType : NSViewController`

The type of view controller to present.

**Required**

Type Alias

# NSViewControllerRepresentable.Context

macOS 10.15+

    
    
    typealias Context = NSViewControllerRepresentableContext<Self>

## See Also

### Creating and updating the view controller

`func makeNSViewController(context: Self.Context) ->
Self.NSViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateNSViewController(Self.NSViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` associatedtype NSViewControllerType : NSViewController`

The type of view controller to present.

**Required**

Associated Type

# NSViewControllerType

The type of view controller to present.

macOS 10.15+

    
    
    associatedtype NSViewControllerType : NSViewController

**Required**

## See Also

### Creating and updating the view controller

`func makeNSViewController(context: Self.Context) ->
Self.NSViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateNSViewController(Self.NSViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

Instance Method

# sizeThatFits(_:nsViewController:context:)

Given a proposed size, returns the preferred size of the composite view.

macOS 13.0+

    
    
    @MainActor
    func sizeThatFits(
        _ proposal: ProposedViewSize,
        nsViewController: Self.NSViewControllerType,
        context: Self.Context
    ) -> CGSize?

**Required** Default implementation provided.

##  Parameters

`proposal`

    

The proposed size for the view controller.

`nsViewController`

    

Your custom view controller object.

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

The composite size of the represented view controller. Returning a value of
`nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during
the same layout pass. SwiftUI views choose their own size, so one of the
values returned from this function will always be used as the actual size of
the composite view.

## Default Implementations

### NSViewControllerRepresentable Implementations

`func sizeThatFits(ProposedViewSize, nsViewController:
Self.NSViewControllerType, context: Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

Type Method

# dismantleNSViewController(_:coordinator:)

Cleans up the presented view controller (and coordinator) in anticipation of
its removal.

macOS 10.15+

    
    
    @MainActor
    static func dismantleNSViewController(
        _ nsViewController: Self.NSViewControllerType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`nsViewController`

    

Your custom view controller object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
view controller. For example, you might use this method to remove observers or
update other parts of your SwiftUI interface.

## Default Implementations

### NSViewControllerRepresentable Implementations

`static func dismantleNSViewController(Self.NSViewControllerType, coordinator:
Self.Coordinator)`

Cleans up the presented `NSViewController` (and coordinator) in anticipation
of their removal.

Instance Method

# makeCoordinator()

Creates the custom object that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

macOS 10.15+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your view controller might affect other
parts of your app. In your implementation, create a custom Swift instance that
can communicate with other parts of your interface. For example, you might
provide an instance that binds its variables to SwiftUI properties, causing
the two to remain synchronized. If your view controller doesn’t interact with
other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeNSViewController(context:)`
method. The system provides your coordinator instance either directly or as
part of a context structure when calling the other methods of your
representable instance.

## Default Implementations

### NSViewControllerRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates an object to coordinate with the AppKit view controller.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the view controller.

**Required**

Associated Type

# Coordinator

A type to coordinate with the view controller.

macOS 10.15+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom object that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

**Required** Default implementation provided.

Type Alias

# NSViewControllerRepresentable.LayoutOptions

macOS 13.0+

    
    
    typealias LayoutOptions



# NavigationBarItem

Enumeration

# NavigationBarItem.TitleDisplayMode

A style for displaying the title of a navigation bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    enum TitleDisplayMode

## Overview

Use one of these values with the `navigationBarTitleDisplayMode(_:)` view
modifier to configure the title of a navigation bar.

## Topics

### Getting title display modes

`case automatic`

Inherit the display mode from the previous navigation item.

`case inline`

Display the title within the standard bounds of the navigation bar.

`case large`

Display a large title within an expanded navigation bar.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`



# NSHostingSizingOptions

Type Property

# intrinsicContentSize

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

macOS 13.0+

    
    
    static let intrinsicContentSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

## See Also

### Geting sizing options

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# maxSize

The hosting view creates and updates constraints that represent its content’s
maximum size.

macOS 13.0+

    
    
    static let maxSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `width: infinity,
height: infinity`.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# minSize

The hosting view creates and updates constraints that represent its content’s
minimum size.

macOS 13.0+

    
    
    static let minSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `width: 0, height:
0`.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# preferredContentSize

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

macOS 13.0+

    
    
    static let preferredContentSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

Note

this option has no effect when used with an `NSHostingView` directly.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# standardBounds

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

macOS 13.0+

    
    
    static let standardBounds: NSHostingSizingOptions

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

Initializer

# init(rawValue:)

Creates a new options from a raw value.

macOS 13.0+

    
    
    init(rawValue: Int)

## See Also

### Creating a sizing option

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

macOS 13.0+

    
    
    let rawValue: Int

## See Also

### Creating a sizing option

`init(rawValue: Int)`

Creates a new options from a raw value.



# NavigationSplitViewStyle

Type Property

# automatic

A navigation split style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticNavigationSplitViewStyle { get }

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var balanced: BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

Available when `Self` is `BalancedNavigationSplitViewStyle`.

`static var prominentDetail: ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

Type Property

# balanced

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var balanced: BalancedNavigationSplitViewStyle { get }

Available when `Self` is `BalancedNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var automatic: AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

`static var prominentDetail: ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

Type Property

# prominentDetail

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var prominentDetail: ProminentDetailNavigationSplitViewStyle { get }

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var automatic: AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

`static var balanced: BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

Available when `Self` is `BalancedNavigationSplitViewStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the instance to create.

## Discussion

SwiftUI calls this method for each instance of `NavigationSplitView`, where
this style is the current `NavigationSplitViewStyle`.

## See Also

### Creating custom styles

`typealias Configuration`

The properties of a navigation split view instance.

`associatedtype Body : View`

A view that represents the body of a navigation split view.

**Required**

Type Alias

# NavigationSplitViewStyle.Configuration

The properties of a navigation split view instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = NavigationSplitViewStyleConfiguration

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a navigation split view.

**Required**

` associatedtype Body : View`

A view that represents the body of a navigation split view.

**Required**

Associated Type

# Body

A view that represents the body of a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a navigation split view.

**Required**

` typealias Configuration`

The properties of a navigation split view instance.

Structure

# AutomaticNavigationSplitViewStyle

A navigation split style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticNavigationSplitViewStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of the automatic navigation split view style.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# BalancedNavigationSplitViewStyle

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct BalancedNavigationSplitViewStyle

## Overview

Use `balanced` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of `BalancedNavigationSplitViewStyle`.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# ProminentDetailNavigationSplitViewStyle

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ProminentDetailNavigationSplitViewStyle

## Overview

Use `prominentDetail` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of `ProminentDetailNavigationSplitViewStyle`.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# NavigationSplitViewStyleConfiguration

The properties of a navigation split view instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewStyleConfiguration

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.



# NSHostingView

Initializer

# init(rootView:)

Creates a hosting view object that wraps the specified SwiftUI view.

macOS 10.15+

    
    
    @MainActor
    required init(rootView: Content)

##  Parameters

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using this
hosting view.

## See Also

### Creating a hosting view

`init?(coder: NSCoder)`

Creates a hosting view object from the contents of the specified archive.

`func prepareForReuse()`

Initializer

# init(coder:)

Creates a hosting view object from the contents of the specified archive.

macOS 10.15+

    
    
    @MainActor
    required dynamic init?(coder aDecoder: NSCoder)

##  Parameters

`coder`

    

The decoder to use during initialization.

## Discussion

The default implementation of this method throws an exception. Use the
`init(rootView:)` method to create your hosting view instead.

## See Also

### Creating a hosting view

`init(rootView: Content)`

Creates a hosting view object that wraps the specified SwiftUI view.

`func prepareForReuse()`

Instance Method

# prepareForReuse()

macOS 10.15+

    
    
    @MainActor
    override dynamic func prepareForReuse()

## See Also

### Creating a hosting view

`init(rootView: Content)`

Creates a hosting view object that wraps the specified SwiftUI view.

`init?(coder: NSCoder)`

Creates a hosting view object from the contents of the specified archive.

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this view controller.

macOS 10.15+

    
    
    @MainActor
    var rootView: Content { get set }

Type Property

# requiresConstraintBasedLayout

macOS 10.15+

    
    
    @MainActor
    override dynamic class var requiresConstraintBasedLayout: Bool { get }

## See Also

### Configuring the view layout behavior

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# userInterfaceLayoutDirection

macOS 10.15+

    
    
    @MainActor
    override dynamic var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# isFlipped

macOS 10.15+

    
    
    @MainActor
    override final var isFlipped: Bool { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# layerContentsRedrawPolicy

macOS 10.15+

    
    
    @MainActor
    override dynamic var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Method

# updateConstraints()

macOS 10.15+

    
    
    @MainActor
    override dynamic func updateConstraints()

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Method

# layout()

macOS 10.15+

    
    
    @MainActor
    override dynamic func layout()

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# safeAreaRegions

The safe area regions that this view controller adds to its view.

macOS 13.3+

    
    
    @MainActor
    var safeAreaRegions: SafeAreaRegions { get set }

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

Instance Method

# keyDown(with:)

Called when the user presses a key on the keyboard while this view is in the
responder chain.

macOS 10.15+

    
    
    @MainActor
    override dynamic func keyDown(with event: NSEvent)

## See Also

### Managing keyboard interaction

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# keyUp(with:)

Called when the user releases a key on the keyboard while this view is in the
responder chain.

macOS 10.15+

    
    
    @MainActor
    override dynamic func keyUp(with event: NSEvent)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# performKeyEquivalent(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func performKeyEquivalent(with event: NSEvent) -> Bool

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# insertText(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func insertText(_ insertString: Any)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# didChangeValue(forKey:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func didChangeValue(forKey key: String)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# makeTouchBar()

macOS 10.15+

    
    
    @MainActor
    override dynamic func makeTouchBar() -> NSTouchBar?

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

Instance Method

# mouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseEntered(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseEntered(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseExited(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseExited(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseMoved(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseMoved(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# cursorUpdate(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func cursorUpdate(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

Instance Method

# touchesBegan(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesBegan(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesCancelled(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesCancelled(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesCancelled(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesEnded(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesEnded(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesCancelled(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesMoved(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesMoved(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesCancelled(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

Instance Method

# magnify(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func magnify(with event: NSEvent)

## See Also

### Responding to gestures

`func rotate(with: NSEvent)`

`func scrollWheel(with: NSEvent)`

Instance Method

# rotate(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rotate(with event: NSEvent)

## See Also

### Responding to gestures

`func magnify(with: NSEvent)`

`func scrollWheel(with: NSEvent)`

Instance Method

# scrollWheel(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func scrollWheel(with event: NSEvent)

## See Also

### Responding to gestures

`func magnify(with: NSEvent)`

`func rotate(with: NSEvent)`

Instance Method

# validRequestor(forSendType:returnType:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func validRequestor(
        forSendType sendType: NSPasteboard.PasteboardType?,
        returnType: NSPasteboard.PasteboardType?
    ) -> Any?

Instance Method

# menu(for:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func menu(for event: NSEvent) -> NSMenu?

Instance Method

# responds(to:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func responds(to selector: Selector!) -> Bool

## See Also

### Responding to actions

`func forwardingTarget(for: Selector!) -> Any?`

`func doCommand(by: Selector)`

Instance Method

# forwardingTarget(for:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func forwardingTarget(for selector: Selector!) -> Any?

## See Also

### Responding to actions

`func responds(to: Selector!) -> Bool`

`func doCommand(by: Selector)`

Instance Method

# doCommand(by:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func doCommand(by selector: Selector)

## See Also

### Responding to actions

`func responds(to: Selector!) -> Bool`

`func forwardingTarget(for: Selector!) -> Any?`

Instance Property

# acceptsFirstResponder

macOS 10.15+

    
    
    @MainActor
    override dynamic var acceptsFirstResponder: Bool { get }

## See Also

### Configuring the responder behavior

`var needsPanelToBecomeKey: Bool`

Instance Property

# needsPanelToBecomeKey

macOS 10.15+

    
    
    @MainActor
    override dynamic var needsPanelToBecomeKey: Bool { get }

## See Also

### Configuring the responder behavior

`var acceptsFirstResponder: Bool`

Instance Method

# viewWillMove(toWindow:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewWillMove(toWindow newWindow: NSWindow?)

## See Also

### Managing the view hierarchy

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidMoveToWindow()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidMoveToWindow()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidChangeBackingProperties()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidChangeBackingProperties()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidChangeEffectiveAppearance()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidChangeEffectiveAppearance()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func renewGState()`

Instance Method

# renewGState()

macOS 10.15+

    
    
    @MainActor
    override dynamic func renewGState()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

Instance Property

# intrinsicContentSize

macOS 10.15+

    
    
    @MainActor
    override dynamic var intrinsicContentSize: NSSize { get }

## See Also

### Modifying the frame rectangle

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Method

# setFrameSize(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func setFrameSize(_ newSize: NSSize)

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# firstBaselineOffsetFromTop

macOS 10.15+

    
    
    @MainActor
    override dynamic var firstBaselineOffsetFromTop: CGFloat { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# lastBaselineOffsetFromBottom

macOS 10.15+

    
    
    @MainActor
    override dynamic var lastBaselineOffsetFromBottom: CGFloat { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# sizingOptions

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

macOS 13.0+

    
    
    @MainActor
    var sizingOptions: NSHostingSizingOptions { get set }

## Discussion

NSHostingView can create minimum, maximum, and ideal (content size)
constraints that are derived from its SwiftUI view content. These constraints
are only created when Auto Layout constraints are otherwise being used in the
containing window.

If the NSHostingView is set as the `contentView` of an `NSWindow`, it will
also update the window’s `contentMinSize` and `contentMaxSize` based on the
minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`,
`intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to
control this behavior. For instance, setting a value of `.minSize` will only
create the constraints necessary to maintain the minimum size of the SwiftUI
content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingView`
relative to its displayed content, such as the always being displayed in a
fixed frame, setting this to a value with fewer options can improve
performance as it reduces the amount of layout measurements that need to be
performed. If an `NSHostingView` has a `frame` that is smaller or larger than
that required to display its SwiftUI content, the content will be centered
within that frame.

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var firstTextLineCenter: CGFloat?`

Instance Property

# firstTextLineCenter

macOS 10.15+

    
    
    @MainActor
    var firstTextLineCenter: CGFloat? { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

Instance Method

# hitTest(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func hitTest(_ point: NSPoint) -> NSView?

Instance Method

# isAccessibilityElement()

macOS 10.15+

    
    
    @MainActor
    override dynamic func isAccessibilityElement() -> Bool

## See Also

### Managing accessibility behaviors

`var accessibilityFocusedUIElement: Any?`

`func accessibilityChildren() -> [Any]?`

`func accessibilityChildrenInNavigationOrder() -> [any
NSAccessibilityElementProtocol]?`

`func accessibilityHitTest(NSPoint) -> Any?`

`func accessibilityRole() -> NSAccessibility.Role?`

`func accessibilitySubrole() -> NSAccessibility.Subrole?`

Instance Property

# sceneBridgingOptions

The options for which aspects of the window will be managed by this hosting
view.

macOS 14.0+

    
    
    @MainActor
    var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }

## Discussion

`NSHostingView` will populate certain aspects of its associated window,
depending on which options are specified.

For example, a hosting view can manage its window’s toolbar by including the
`.toolbars` option:

When this hosting view is set as the `contentView` for a window, the default
value for this property will be `.all`, which includes the options for
`.toolbars` and `.title`. Otherwise, the default value is `[]`.



# NavigationViewStyle

Type Property

# automatic

The default navigation view style in the current context of the view being
styled.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    static var automatic: DefaultNavigationViewStyle { get }

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Type Property

# columns

A navigation view style represented by a series of views in columns.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  visionOS 1.0+

    
    
    static var columns: ColumnNavigationViewStyle { get }

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Type Property

# stack

A navigation view style represented by a view stack that only shows a single
top view at a time.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 7.0–10.4
Deprecated  visionOS 1.0+

    
    
    static var stack: StackNavigationViewStyle { get }

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

Structure

# DefaultNavigationViewStyle

The default navigation view style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct DefaultNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `automatic` to construct this style.

## Topics

### Creating a default navigation view style

`init()`

Creates the default navigation view style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# ColumnNavigationViewStyle

A navigation view style represented by a series of views in columns.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct ColumnNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `columns` to construct this style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# StackNavigationViewStyle

A navigation view style represented by a view stack that only shows a single
top view at a time.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 7.0–10.4
Deprecated  visionOS 1.0+

    
    
    struct StackNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `stack` to construct this style.

## Topics

### Creating a stack navigation view style

`init()`

Creates a navigation view style represented by a view stack that only shows a
single top view at a time.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# DoubleColumnNavigationViewStyle

A navigation view style represented by a primary view stack that navigates to
a detail view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
visionOS 1.0+

    
    
    struct DoubleColumnNavigationViewStyle

Deprecated

Use `ColumnNavigationViewStyle` instead.

## Topics

### Create a double column view style

`init()`

Creates a double column navigation view style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated



# NavigationView

Initializer

# init(content:)

Creates a destination-based navigation view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Deprecated

Use `NavigationStack` and `NavigationSplitView` instead. For more information,
see Migrating to new navigation types.

##  Parameters

`content`

    

A `ViewBuilder` that produces the content that the navigation view wraps. Any
views after the first act as placeholders for corresponding columns in a
multicolumn display.

## Discussion

Perform navigation by initializing a link with a destination view. For
example, consider a `ColorDetail` view that displays a color sample:

The following `NavigationView` presents three links to color detail views:

When the horizontal size class is `UserInterfaceSizeClass.regular`, like on an
iPad in landscape mode, or on a Mac, the navigation view presents itself as a
multicolumn view, using its second and later content views — a single `Text`
view in the example above — as a placeholder for the corresponding column:

When the user selects one of the navigation links from the list, the linked
destination view replaces the placeholder text in the detail column:

When the size class is `UserInterfaceSizeClass.compact`, like on an iPhone in
portrait orientation, the navigation view presents itself as a single column
that the user navigates as a stack. Tapping one of the links replaces the list
with the detail view, which provides a back button to return to the list:

Instance Method

# navigationViewStyle(_:)

Sets the style for navigation views within this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle
    

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Discussion

Use this modifier to change the appearance and behavior of navigation views.
For example, by default, navigation views appear with multiple columns in
wider environments, like iPad in landscape orientation:

You can apply the `stack` style to force single-column stack navigation in
these environments:

## See Also

### Styling navigation views

`protocol NavigationViewStyle`

A specification for the appearance and interaction of a navigation view.

Deprecated

Protocol

# NavigationViewStyle

A specification for the appearance and interaction of a navigation view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    protocol NavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Topics

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

## Relationships

### Conforming Types

  * `ColumnNavigationViewStyle`
  * `DefaultNavigationViewStyle`
  * `DoubleColumnNavigationViewStyle`
  * `StackNavigationViewStyle`

## See Also

### Styling navigation views

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

Deprecated



# NavigationPath

Initializer

# init()

Creates a new, empty navigation path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a navigation path

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from a serializable version.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ codable: NavigationPath.CodableRepresentation)

##  Parameters

`codable`

    

A value describing the contents of the new path in a serializable format.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from the contents of a sequence that contains
codable elements.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(_ elements: S) where S : Sequence, S.Element : Decodable, S.Element : Encodable, S.Element : Hashable

##  Parameters

`elements`

    

A sequence used to create the navigation path.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from the contents of a sequence.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(_ elements: S) where S : Sequence, S.Element : Hashable

##  Parameters

`elements`

    

A sequence used to create the navigation path.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

Instance Property

# isEmpty

A Boolean that indicates whether this path is empty.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isEmpty: Bool { get }

## See Also

### Managing path contents

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Property

# count

The number of elements in this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var count: Int { get }

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# append(_:)

Appends a new codable value to the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func append<V>(_ value: V) where V : Decodable, V : Encodable, V : Hashable

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# append(_:)

Appends a new value to the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func append<V>(_ value: V) where V : Hashable

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# removeLast(_:)

Removes values from the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func removeLast(_ k: Int = 1)

##  Parameters

`k`

    

The number of values to remove. The default value is `1`.

## Discussion

Precondition

The input parameter `k` must be greater than or equal to zero, and must be
less than or equal to the number of elements in the path.

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

Instance Property

# codable

A value that describes the contents of this path in a serializable format.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var codable: NavigationPath.CodableRepresentation? { get }

## Discussion

This value is `nil` if any of the type-erased elements of the path don’t
conform to the `Codable` protocol.

## See Also

### Encoding a path

`struct CodableRepresentation`

A serializable representation of a navigation path.

Structure

# NavigationPath.CodableRepresentation

A serializable representation of a navigation path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct CodableRepresentation

## Overview

When a navigation path contains elements the conform to the `Codable`
protocol, you can use the path’s `CodableRepresentation` to convert the path
to an external representation and to convert an external representation back
into a navigation path.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`

## See Also

### Encoding a path

`var codable: NavigationPath.CodableRepresentation?`

A value that describes the contents of this path in a serializable format.



# NewDocumentAction

Instance Method

# callAsFunction(_:)

Presents a new reference type document window.

macOS 13.0+

    
    
    func callAsFunction<D>(_ newDocument: @escaping () -> D) where D : ReferenceFileDocument

##  Parameters

`newDocument`

    

The new reference type file document to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(_:)

Presents a new document window.

macOS 13.0+

    
    
    func callAsFunction<D>(_ newDocument: @autoclosure @escaping () -> D) where D : FileDocument

##  Parameters

`newDocument`

    

The new file document to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(contentType:)

Presents a new document window.

macOS 14.0+

    
    
    func callAsFunction(contentType: UTType)

##  Parameters

`contentType`

    

The content type of the document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action:

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist` file. For more information, see Defining
file and data types for your app. Also, remember to specify the supported
Document types in the `Info.plist` file as well.

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

Instance Method

# callAsFunction(contentType:prepareDocument:)

Presents a new document window with preset contents.

SwiftData  SwiftUI  macOS 14.0+

    
    
    func callAsFunction(
        contentType: UTType,
        prepareDocument: @escaping (ModelContext) -> Void
    )

##  Parameters

`contentType`

    

The content type of the document.

`prepareDocument`

    

The closure that accepts `ModelContext` associated with the new document. Use
this closure to set the document’s initial contents before it is displayed:
insert preconfigured models in the provided `ModelContext`.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`newDocument` action.

For example, a Todo app might have a way to create a sample prepopulated Todo
list as a part of onboarding experience:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.



# NavigationLinkPickerStyle

Initializer

# init()

Creates a navigation link picker style.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# NSApplicationDelegateAdaptor

Initializer

# init(_:)

Creates an AppKit app delegate adaptor using a delegate that’s an observable
object.

macOS 11.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `NSApplicationDelegate` and `ObservableObject` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`NSApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`ObservableObject` protocol. In this case, SwiftUI automatically places the
delegate in the `Environment`. You can access such a delegate from any scene
or view in your app using the `EnvironmentObject` property wrapper:

If your delegate isn’t an observable object, SwiftUI invokes the `init(_:)`
initializer rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `Observable`.

Initializer

# init(_:)

Creates an AppKit app delegate adaptor.

macOS 11.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `NSApplicationDelegate` protocol.

## Discussion

Call this initializer indirectly by creating a property with the
`NSApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling upon it to
handle application delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the `Environment`,
make sure the delegate class also conforms to the `ObservableObject` protocol.
That causes SwiftUI to invoke the `init(_:)` initializer rather than this one.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `Observable`.

Initializer

# init(_:)

Creates an AppKit app delegate adaptor using an observable delegate.

macOS 14.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `Observable`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `NSApplicationDelegate` and `Observable` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`NSApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`Observable` protocol. In this case, SwiftUI automatically places the delegate
in the `Environment`. You can access such a delegate from any scene or view in
your app using the `Environment` property wrapper:

If your delegate isn’t observable, SwiftUI invokes the `init(_:)` initializer
rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor.

Instance Property

# projectedValue

A projection of the observed object that provides bindings to its properties.

macOS 11.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

## Discussion

Use the projected value to get a binding to a value that the delegate
publishes. Access the projected value by prefixing the name of the delegate
instance with a dollar sign (`$`). For example, you might publish a Boolean
value in your application delegate:

If you declare the delegate in your `App` using the
`NSApplicationDelegateAdaptor` property wrapper, you can get the delegate that
SwiftUI instantiates from the environment and access a binding to its
published values from any view in your app:

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying delegate.

Instance Property

# wrappedValue

The underlying delegate.

macOS 11.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.



# Navigation

Article

# Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

## Overview

If your app has a minimum deployment target of iOS 16, iPadOS 16, macOS 13,
tvOS 16, watchOS 9, or visionOS 1, or later, transition away from using
`NavigationView`. In its place, use `NavigationStack` and
`NavigationSplitView` instances. How you use these depends on whether you
perform navigation in one column or across multiple columns. With these newer
containers, you get better control over view presentation, container
configuration, and programmatic navigation.

### Update single column navigation

If your app uses a `NavigationView` that you style using the `stack`
navigation view style, where people navigate by pushing a new view onto a
stack, switch to `NavigationStack`.

In particular, stop doing this:

Instead, create a navigation stack:

### Update multicolumn navigation

If your app uses a two- or three-column `NavigationView`, or for apps that
have multiple columns in some cases and a single column in others — which is
typical for apps that run on iPhone and iPad — switch to
`NavigationSplitView`.

Instead of using a two-column navigation view:

Create a navigation split view that has explicit sidebar and detail content
using the `init(sidebar:detail:)` initializer:

Similarly, instead of using a three-column navigation view:

Create a navigation split view that has explicit sidebar, content, and detail
components using the `init(sidebar:content:detail:)` initializer:

If you need navigation within a column, embed a navigation stack in that
column. This arrangement provides finer control over what each column
displays. `NavigationSplitView` also enables you to customize column
visibility and width.

### Update programmatic navigation

If you perform programmatic navigation using one of the `NavigationLink`
initializers that has an `isActive` input parameter, move the automation to
the enclosing stack. Do this by changing your navigation links to use the
`init(value:label:)` initializer, then use one of the navigation stack
initializers that takes a path input, like `init(path:root:)`.

For example, if you have a navigation view with links that activate in
response to individual state variables:

When some other part of your code sets one of the state variables to true, the
navigation link that has the matching tag activates in response.

Rewrite this as a navigation stack that takes a path input:

This version uses the `navigationDestination(for:destination:)` view modifier
to detach the presented data from the corresponding view. That makes it
possible for the `path` array to represent every view on the stack. Changes
that you make to the array affect what the container displays right now, as
well as what people encounter as they navigate through the stack. You can
support even more sophisticated programmatic navigation if you use a
`NavigationPath` to store the path information, rather than a plain collection
of data. For more information, see `NavigationStack`.

### Update selection-based navigation

If you perform programmatic navigation on `List` elements that use one of the
`NavigationLink` initializers with a `selection` input parameter, you can move
the selection to the list. For example, suppose you have a navigation view
with links that activate in response to a `selection` state variable:

Using the same properties, you can rewrite the body as:

The list coordinates with the navigation logic so that changing the selection
state variable in another part of your code activates the navigation link with
the corresponding color. Similarly, if someone chooses the navigation link
associated with a particular color, the list updates the selection value that
other parts of your code can read.

### Provide backward compatibility with an availability check

If your app needs to run on platform versions earlier than iOS 16, iPadOS 16,
macOS 13, tvOS 16, watchOS 9, or visionOS 1, you can start migration while
continuing to support older clients by using an availability condition. For
example, you can create a custom wrapper view that conditionally uses either
`NavigationSplitView` or `NavigationView`:

Customize the wrapper to meet your app’s needs. For example, you can add a
navigation split view style modifier like `navigationSplitViewStyle(_:)` to
the `NavigationSplitView` in the appropriate branch of the availability check.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationSplitView

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitView<Sidebar, Content, Detail> where Sidebar : View, Content : View, Detail : View

## Overview

You create a navigation split view with two or three columns, and typically
use it as the root view in a `Scene`. People choose one or more items in a
leading column to display details about those items in subsequent columns.

To create a two-column navigation split view, use the `init(sidebar:detail:)`
initializer:

In the above example, the navigation split view coordinates with the `List` in
its first column, so that when people make a selection, the detail view
updates accordingly. Programmatic changes that you make to the selection
property also affect both the list appearance and the presented detail view.

To create a three-column view, use the `init(sidebar:content:detail:)`
initializer. The selection in the first column affects the second, and the
selection in the second column affects the third. For example, you can show a
list of departments, the list of employees in the selected department, and the
details about all of the selected employees:

You can also embed a `NavigationStack` in a column. Tapping or clicking a
`NavigationLink` that appears in an earlier column sets the view that the
stack displays over its root view. Activating a link in the same column adds a
view to the stack. Either way, the link must present a data type for which the
stack has a corresponding `navigationDestination(for:destination:)` modifier.

On watchOS and tvOS, and with narrow sizes like on iPhone or on iPad in Slide
Over, the navigation split view collapses all of its columns into a stack, and
shows the last column that displays useful information. For example, the
three-column example above shows the list of departments to start, the
employees in the department after someone selects a department, and the
employee details when someone selects an employee. For rows in a list that
have `NavigationLink` instances, the list draws disclosure chevrons while in
the collapsed state.

### Control column visibility

You can programmatically control the visibility of navigation split view
columns by creating a `State` value of type `NavigationSplitViewVisibility`.
Then pass a `Binding` to that state to the appropriate initializer — such as
`init(columnVisibility:sidebar:detail:)` for two columns, or the
`init(columnVisibility:sidebar:content:detail:)` for three columns.

The following code updates the first example above to always hide the first
column when the view appears:

The split view ignores the visibility control when it collapses its columns
into a stack.

### Collapsed split views

At narrow size classes, such as on iPhone or Apple Watch, a navigation split
view collapses into a single stack. Typically SwiftUI automatically chooses
the view to show on top of this single stack, based on the content of the
split view’s columns.

For custom navigation experiences, you can provide more information to help
SwiftUI choose the right column. Create a `State` value of type
`NavigationSplitViewColumn`. Then pass a `Binding` to that state to the
appropriate initializer, such as
`init(preferredCompactColumn:sidebar:detail:)` or
`init(preferredCompactColumn:sidebar:content:detail:)`.

The following code shows the blue detail view when run on iPhone. When the
person using the app taps the back button, they’ll see the yellow view. The
value of `preferredPreferredCompactColumn` will change from `.detail` to
`.sidebar`:

### Customize a split view

To specify a preferred column width in a navigation split view, use the
`navigationSplitViewColumnWidth(_:)` modifier. To set minimum, maximum, and
ideal sizes for a column, use
`navigationSplitViewColumnWidth(min:ideal:max:)`. You can specify a different
modifier in each column. The navigation split view does its best to
accommodate the preferences that you specify, but might make adjustments based
on other constraints.

To specify how columns in a navigation split view interact, use the
`navigationSplitViewStyle(_:)` modifier with a `NavigationSplitViewStyle`
value. For example, you can specify whether to emphasize the detail column or
to give all of the columns equal prominence.

On some platforms, `NavigationSplitView` adds a `sidebarToggle` toolbar item.
Use the `toolbar(removing:)` modifier to remove the default item.

## Topics

### Creating a navigation split view

`init(sidebar: () -> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view.

`init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view.

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewStyle(_:)

Sets the style for navigation split views within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewStyle<S>(_ style: S) -> some View where S : NavigationSplitViewStyle
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified navigation split view style.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewColumnWidth(_:)

Sets a fixed, preferred width for the column containing this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewColumnWidth(_ width: CGFloat) -> some View
    

## Discussion

Apply this modifier to the content of a column in a `NavigationSplitView` to
specify a fixed preferred width for the column. Use
`navigationSplitViewColumnWidth(min:ideal:max:)` if you need to specify a
flexible width.

The following example shows a three-column navigation split view where the
first column has a preferred width of 150 points, and the second column has a
flexible, preferred width between 150 and 400 points:

Only some platforms enable resizing columns. If you specify a width that the
current presentation environment doesn’t support, SwiftUI may use a different
width for your column.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewColumnWidth(min:ideal:max:)

Sets a flexible, preferred width for the column containing this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewColumnWidth(
        min: CGFloat? = nil,
        ideal: CGFloat,
        max: CGFloat? = nil
    ) -> some View
    

## Discussion

Apply this modifier to the content of a column in a `NavigationSplitView` to
specify a preferred flexible width for the column. Use
`navigationSplitViewColumnWidth(_:)` if you need to specify a fixed width.

The following example shows a three-column navigation split view where the
first column has a preferred width of 150 points, and the second column has a
flexible, preferred width between 150 and 400 points:

Only some platforms enable resizing columns. If you specify a width that the
current presentation environment doesn’t support, SwiftUI may use a different
width for your column.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationSplitViewVisibility

The visibility of the leading columns in a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewVisibility

## Overview

Use a value of this type to control the visibility of the columns of a
`NavigationSplitView`. Create a `State` property with a value of this type,
and pass a `Binding` to that state to the
`init(columnVisibility:sidebar:detail:)` or
`init(columnVisibility:sidebar:content:detail:)` initializer when you create
the navigation split view. You can then modify the value elsewhere in your
code to:

  * Hide all but the trailing column with `detailOnly`.

  * Hide the leading column of a three-column navigation split view with `doubleColumn`.

  * Show all the columns with `all`.

  * Rely on the automatic behavior for the current context with `automatic`.

Note

Some platforms don’t respect every option. For example, macOS always displays
the content column.

## Topics

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Sendable`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationLink

A view that controls a navigation presentation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct NavigationLink<Label, Destination> where Label : View, Destination : View

## Overview

People click or tap a navigation link to present a view inside a
`NavigationStack` or `NavigationSplitView`. You control the visual appearance
of the link by providing view content in the link’s `label` closure. For
example, you can use a `Label` to display a link:

For a link composed only of text, you can use one of the convenience
initializers that takes a string and creates a `Text` view for you:

### Link to a destination view

You can perform navigation by initializing a link with a destination view that
you provide in the `destination` closure. For example, consider a
`ColorDetail` view that fills itself with a color:

The following `NavigationStack` presents three links to color detail views:

### Create a presentation link

Alternatively, you can use a navigation link to perform navigation based on a
presented data value. To support this, use the
`navigationDestination(for:destination:)` view modifier inside a navigation
stack to associate a view with a kind of data, and then present a value of
that data type from a navigation link. The following example reimplements the
previous example as a series of presentation links:

Separating the view from the data facilitates programmatic navigation because
you can manage navigation state by recording the presented data.

### Control a presentation link programmatically

To navigate programmatically, introduce a state variable that tracks the items
on a stack. For example, you can create an array of colors to store the stack
state from the previous example, and initialize it as an empty array to start
with an empty stack:

Then pass a `Binding` to the state to the navigation stack:

You can use the array to observe the current state of the stack. You can also
modify the array to change the contents of the stack. For example, you can
programmatically add `blue` to the array, and navigation to a new color detail
view using the following method:

### Coordinate with a list

You can also use a navigation link to control `List` selection in a
`NavigationSplitView`:

The list coordinates with the navigation logic so that changing the selection
state variable in another part of your code activates the navigation link with
the corresponding color. Similarly, if someone chooses the navigation link
associated with a particular color, the list updates the selection value that
other parts of your code can read.

## Topics

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

### Configuring the link

`func isDetailLink(Bool) -> some View`

Sets the navigation link to present its destination as the detail component of
the containing navigation view.

Available when `Label` conforms to `View` and `Destination` conforms to
`View`.

### Deprecated symbols

API Reference

Deprecated symbols

Review deprecated navigation link initializers.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

Structure

# NavigationStack

A view that displays a root view and enables you to present additional views
over the root view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    struct NavigationStack<Data, Root> where Root : View

## Overview

Use a navigation stack to present a stack of views over a root view. People
can add views to the top of the stack by clicking or tapping a
`NavigationLink`, and remove views using built-in, platform-appropriate
controls, like a Back button or a swipe gesture. The stack always displays the
most recently added view that hasn’t been removed, and doesn’t allow the root
view to be removed.

To create navigation links, associate a view with a data type by adding a
`navigationDestination(for:destination:)` modifier inside the stack’s view
hierarchy. Then initialize a `NavigationLink` that presents an instance of the
same kind of data. The following stack displays a `ParkDetails` view for
navigation links that present data of type `Park`:

In this example, the `List` acts as the root view and is always present.
Selecting a navigation link from the list adds a `ParkDetails` view to the
stack, so that it covers the list. Navigating back removes the detail view and
reveals the list again. The system disables backward navigation controls when
the stack is empty and the root view, namely the list, is visible.

### Manage navigation state

By default, a navigation stack manages state to keep track of the views on the
stack. However, your code can share control of the state by initializing the
stack with a binding to a collection of data values that you create. The stack
adds items to the collection as it adds views to the stack and removes items
when it removes views. For example, you can create a `State` property to
manage the navigation for the park detail view:

Initializing the state as an empty array indicates a stack with no views.
Provide a `Binding` to this state property using the dollar sign (`$`) prefix
when you create a stack using the `init(path:root:)` initializer:

Like before, when someone taps or clicks the navigation link for a park, the
stack displays the `ParkDetails` view using the associated park data. However,
now the stack also puts the park data in the `presentedParks` array. Your code
can observe this array to read the current stack state. It can also modify the
array to change the views on the stack. For example, you can create a method
that configures the stack with a specific set of parks:

The `showParks` method replaces the stack’s display with a view that shows
details for Sequoia, the last item in the new `presentedParks` array.
Navigating back from that view removes Sequoia from the array, which reveals a
view that shows details for Yosemite. Use a path to support deep links, state
restoration, or other kinds of programmatic navigation.

### Navigate to different view types

To create a stack that can present more than one kind of view, you can add
multiple `navigationDestination(for:destination:)` modifiers inside the
stack’s view hierarchy, with each modifier presenting a different data type.
The stack matches navigation links with navigation destinations based on their
respective data types.

To create a path for programmatic navigation that contains more than one kind
of data, you can use a `NavigationPath` instance as the path.

## Topics

### Creating a navigation stack

`init(root: () -> Root)`

Creates a navigation stack that manages its own navigation state.

### Creating a navigation stack with a path

`init(path: Binding<Data>, root: () -> Root)`

Creates a navigation stack with homogeneous navigation state that you can
control.

`init(path: Binding<NavigationPath>, root: () -> Root)`

Creates a navigation stack with heterogeneous navigation state that you can
control.

## Relationships

### Conforms To

  * `View`

## See Also

### Stacking views in one column

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Structure

# NavigationPath

A type-erased list of data representing the content of a navigation stack.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationPath

## Overview

You can manage the state of a `NavigationStack` by initializing the stack with
a binding to a collection of data. The stack stores data items in the
collection for each view on the stack. You also can read and write the
collection to observe and alter the stack’s state.

When a stack displays views that rely on only one kind of data, you can use a
standard collection, like an array, to hold the data. If you need to present
different kinds of data in a single stack, use a navigation path instead. The
path uses type erasure so you can manage a collection of heterogeneous
elements. The path also provides the usual collection controls for adding,
counting, and removing data elements.

### Serialize the path

When the values you present on the navigation stack conform to the `Codable`
protocol, you can use the path’s `codable` property to get a serializable
representation of the path. Use that representation to save and restore the
contents of the stack. For example, you can define an `ObservableObject` that
handles serializing and deserializing the path:

Then, using that object in your view, you can save the state of the navigation
path when the `Scene` enters the `ScenePhase.background` state:

## Topics

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

### Encoding a path

`var codable: NavigationPath.CodableRepresentation?`

A value that describes the contents of this path in a serializable format.

`struct CodableRepresentation`

A serializable representation of a navigation path.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(for:destination:)

Associates a destination view with a presented data type for use within a
navigation stack.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDestination<D, C>(
        for data: D.Type,
        @ViewBuilder destination: @escaping (D) -> C
    ) -> some View where D : Hashable, C : View
    

##  Parameters

`data`

    

The type of data that this destination matches.

`destination`

    

A view builder that defines a view to display when the stack’s navigation
state contains a value of type `data`. The closure takes one argument, which
is the value of the data to present.

## Discussion

Add this view modifer to a view inside a `NavigationStack` to describe the
view that the stack displays when presenting a particular kind of data. Use a
`NavigationLink` to present the data. For example, you can present a
`ColorDetail` view for each presentation of a `Color` instance:

You can add more than one navigation destination modifier to the stack if it
needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation stack can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(isPresented:destination:)

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDestination<V>(
        isPresented: Binding<Bool>,
        @ViewBuilder destination: () -> V
    ) -> some View where V : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view to present.

## Discussion

In general, favor binding a path to a navigation stack for programmatic
navigation. Add this view modifer to a view inside a `NavigationStack` to
programmatically push a single view onto the stack. This is useful for
building components that can push an associated view. For example, you can
present a `ColorDetail` view for a particular color:

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation stack can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(item:destination:)

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func navigationDestination<D, C>(
        item: Binding<Optional<D>>,
        @ViewBuilder destination: @escaping (D) -> C
    ) -> some View where D : Hashable, C : View
    

##  Parameters

`item`

    

A binding to the data presented, or `nil` if nothing is currently presented.

`destination`

    

A view builder that defines a view to display when `item` is not `nil`.

## Discussion

Add this view modifer to a view inside a `NavigationStack` or
`NavigationSplitView` to describe the view that the stack displays when
presenting a particular kind of data. Programmatically update the binding to
display or remove the view. For example, you can replace the view showing in
the detail column of a navigation split view:

When the person using the app taps on the Mint button, the mint color shows in
the detail and `colorShown` gets the value `Color.mint`. You can reset the
navigation split view to show the message “Select a color” by setting
`colorShown` back to `nil`.

You can add more than one navigation destination modifier to the stack if it
needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation split view can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

Structure

# NavigationSplitViewColumn

A view that represents a column in a navigation split view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewColumn

## Overview

A `NavigationSplitView` collapses into a single stack in some contexts, like
on iPhone or Apple Watch. Use this type with the `preferredCompactColumn`
parameter to control which column of the navigation split view appears on top
of the collapsed stack.

## Topics

### Getting a column

`static var sidebar: NavigationSplitViewColumn`

`static var content: NavigationSplitViewColumn`

`static var detail: NavigationSplitViewColumn`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a localized
string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle(_ titleKey: LocalizedStringKey) -> some View
    

##  Parameters

`titleKey`

    

The key to a localized string to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle(_ title: Text) -> some View
    

##  Parameters

`title`

    

The title to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle<S>(_ title: S) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The string to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a custom view.

watchOS 7.0+

    
    
    func navigationTitle<V>(@ViewBuilder _ title: () -> V) -> some View where V : View
    

##  Parameters

`title`

    

The view to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a string
binding.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationTitle(_ title: Binding<String>) -> some View
    

##  Parameters

`title`

    

The text of the title.

## Discussion

In iOS, iPadOS, and macOS, this allows editing the navigation title when the
title is displayed in the toolbar.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation, using a string.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle<S>(_ subtitle: S) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The subtitle to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle(_ subtitle: Text) -> some View
    

##  Parameters

`subtitle`

    

The subtitle to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation, using a localized
string.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle(_ subtitleKey: LocalizedStringKey) -> some View
    

##  Parameters

`subtitleKey`

    

The key to a localized string to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDocument<D>(_ document: D) -> some View where D : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDocument(_ url: URL) -> some View
    

##  Parameters

`document`

    

The URL content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I>(
        _ document: D,
        preview: SharePreview<I, Never>
    ) -> some View where D : Transferable, I : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I>(
        _ document: D,
        preview: SharePreview<Never, I>
    ) -> some View where D : Transferable, I : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D>(
        _ document: D,
        preview: SharePreview<Never, Never>
    ) -> some View where D : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I1, I2>(
        _ document: D,
        preview: SharePreview<I1, I2>
    ) -> some View where D : Transferable, I1 : Transferable, I2 : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationBarBackButtonHidden(_:)

Hides the navigation bar back button for the view.

iOS 13.0+  iPadOS 13.0+  macOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func navigationBarBackButtonHidden(_ hidesBackButton: Bool = true) -> some View
    

##  Parameters

`hidesBackButton`

    

A Boolean value that indicates whether to hide the back button. The default
value is `true`.

## Discussion

Use `navigationBarBackButtonHidden(_:)` to hide the back button for this view.

This modifier only takes effect when this view is inside of and visible within
a `NavigationView`.

## See Also

### Configuring the navigation bar

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

`struct NavigationBarItem`

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

Instance Method

# navigationBarTitleDisplayMode(_:)

Configures the title display mode for this view.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  watchOS 8.0+  visionOS 1.0+

    
    
    func navigationBarTitleDisplayMode(_ displayMode: NavigationBarItem.TitleDisplayMode) -> some View
    

##  Parameters

`displayMode`

    

The style to use for displaying the title.

## See Also

### Configuring the navigation bar

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`struct NavigationBarItem`

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

Structure

# NavigationBarItem

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct NavigationBarItem

## Overview

Use one of the `NavigationBarItem.TitleDisplayMode` values to configure a
navigation bar title’s display mode with the
`navigationBarTitleDisplayMode(_:)` view modifier.

## Topics

### Setting a title display mode

`enum TitleDisplayMode`

A style for displaying the title of a navigation bar.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring the navigation bar

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

Instance Property

# sidebarRowSize

The current size of sidebar rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var sidebarRowSize: SidebarRowSize { get set }

## Discussion

On macOS, reflects the value of the “Sidebar icon size” in System Settings’
Appearance settings.

This can be used to update the content shown in the sidebar in response to
this size. And it can be overridden to force a sidebar to a particularly size,
regardless of the user preference.

On other platforms, the value is always `.medium` and setting a different
value has no effect.

SwiftUI views like `Label` automatically adapt to the sidebar row size.

## See Also

### Configuring the sidebar

`enum SidebarRowSize`

The standard sizes of sidebar rows.

Enumeration

# SidebarRowSize

The standard sizes of sidebar rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    enum SidebarRowSize

## Overview

On macOS, sidebar rows have three different sizes: small, medium, and large.
The size is primarily controlled by the current users’ “Sidebar Icon Size” in
Appearance settings, and applies to all applications.

On all other platforms, the only supported sidebar size is `.medium`.

This size can be read or written in the environment using
`EnvironmentValues.sidebarRowSize`.

## Topics

### Getting row sizes

`case small`

The standard “small” row size

`case medium`

The standard “medium” row size

`case large`

The standard “large” row size

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring the sidebar

`var sidebarRowSize: SidebarRowSize`

The current size of sidebar rows.

Structure

# TabView

A view that switches between multiple child views using interactive user
interface elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct TabView<SelectionValue, Content> where SelectionValue : Hashable, Content : View

## Overview

To create a user interface with tabs, place views in a `TabView` and apply the
`tabItem(_:)` modifier to the contents of each tab. On iOS, you can also use
one of the badge modifiers, like `badge(_:)`, to assign a badge to each of the
tabs.

The following example creates a tab view with three tabs, each presenting a
custom child view. The first tab has a numeric badge and the third has a
string badge.

Use a `Label` for each tab item, or optionally a `Text`, an `Image`, or an
image followed by text. Passing any other type of view results in a visible
but empty tab item.

## Topics

### Creating a tab view

`init(content: () -> Content)`

Available when `SelectionValue` is `Int` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>?, content: () -> Content)`

Creates an instance that selects from content associated with `Selection`
values.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in tabs

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

Instance Method

# tabViewStyle(_:)

Sets the style for the tab view within the current environment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func tabViewStyle<S>(_ style: S) -> some View where S : TabViewStyle
    

##  Parameters

`style`

    

The style to apply to this tab view.

## See Also

### Presenting views in tabs

`struct TabView`

A view that switches between multiple child views using interactive user
interface elements.

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

Instance Method

# tabItem(_:)

Sets the tab bar item associated with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func tabItem<V>(@ViewBuilder _ label: () -> V) -> some View where V : View
    

##  Parameters

`label`

    

The tab bar item to associate with this view.

## Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a `TabView`. The
example below adds two views as tabs in a `TabView`:

## See Also

### Presenting views in tabs

`struct TabView`

A view that switches between multiple child views using interactive user
interface elements.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

Structure

# HSplitView

A layout container that arranges its children in a horizontal line and allows
the user to resize them using dividers placed between them.

macOS 10.15+

    
    
    struct HSplitView<Content> where Content : View

## Topics

### Creating a horizontal split view

`init(content: () -> Content)`

## Relationships

### Conforms To

  * `View`

## See Also

### Displaying views in multiple panes

`struct VSplitView`

A layout container that arranges its children in a vertical line and allows
the user to resize them using dividers placed between them.

Structure

# VSplitView

A layout container that arranges its children in a vertical line and allows
the user to resize them using dividers placed between them.

macOS 10.15+

    
    
    struct VSplitView<Content> where Content : View

## Topics

### Creating a vertical split view

`init(content: () -> Content)`

## Relationships

### Conforms To

  * `View`

## See Also

### Displaying views in multiple panes

`struct HSplitView`

A layout container that arranges its children in a horizontal line and allows
the user to resize them using dividers placed between them.

Structure

# NavigationView

A view for presenting a stack of views that represents a visible path in a
navigation hierarchy.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct NavigationView<Content> where Content : View

Deprecated

Use `NavigationStack` and `NavigationSplitView` instead. For more information,
see Migrating to new navigation types.

## Overview

Use a `NavigationView` to create a navigation-based app in which the user can
traverse a collection of views. Users navigate to a destination view by
selecting a `NavigationLink` that you provide. On iPadOS and macOS, the
destination content appears in the next column. Other platforms push a new
view onto the stack, and enable removing items from the stack with platform-
specific controls, like a Back button or a swipe gesture.

Use the `init(content:)` initializer to create a navigation view that directly
associates navigation links and their destination views:

Style a navigation view by modifying it with the `navigationViewStyle(_:)`
view modifier. Use other modifiers, like `navigationTitle(_:)`, on views
presented by the navigation view to customize the navigation interface for the
presented view.

## Topics

### Creating a navigation view

`init(content: () -> Content)`

Creates a destination-based navigation view.

### Styling navigation views

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

`protocol NavigationViewStyle`

A specification for the appearance and interaction of a navigation view.

## Relationships

### Conforms To

  * `View`



# NavigationSplitView

Initializer

# init(sidebar:detail:)

Creates a two-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

##  Parameters

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Creating a navigation split view

`init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view.

Initializer

# init(sidebar:content:detail:)

Creates a three-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

##  Parameters

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Creating a navigation split view

`init(sidebar: () -> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view.

Initializer

# init(columnVisibility:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading column.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

Initializer

# init(columnVisibility:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading columns.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

Initializer

# init(preferredCompactColumn:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(preferredCompactColumn:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(columnVisibility:preferredCompactColumn:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading column.

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading columns.

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.



# NSViewRepresentable

Instance Method

# makeNSView(context:)

Creates the view object and configures its initial state.

macOS 10.15+

    
    
    @MainActor
    func makeNSView(context: Self.Context) -> Self.NSViewType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your AppKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object.
Configure the view using your app’s current data and contents of the `context`
parameter. The system calls this method only once, when it creates your view
for the first time. For all subsequent updates, the system calls the
`updateNSView(_:context:)` method.

## See Also

### Creating and updating the view

`func updateNSView(Self.NSViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype NSViewType : NSView`

The type of view to present.

**Required**

Instance Method

# updateNSView(_:context:)

Updates the state of the specified view with new information from SwiftUI.

macOS 10.15+

    
    
    @MainActor
    func updateNSView(
        _ nsView: Self.NSViewType,
        context: Self.Context
    )

**Required**

##  Parameters

`nsView`

    

Your custom view object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding AppKit view. Use this method to update the
configuration of your view to match the new state information provided in the
`context` parameter.

## See Also

### Creating and updating the view

`func makeNSView(context: Self.Context) -> Self.NSViewType`

Creates the view object and configures its initial state.

**Required**

` typealias Context`

`associatedtype NSViewType : NSView`

The type of view to present.

**Required**

Type Alias

# NSViewRepresentable.Context

macOS 10.15+

    
    
    typealias Context = NSViewRepresentableContext<Self>

## See Also

### Creating and updating the view

`func makeNSView(context: Self.Context) -> Self.NSViewType`

Creates the view object and configures its initial state.

**Required**

` func updateNSView(Self.NSViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` associatedtype NSViewType : NSView`

The type of view to present.

**Required**

Associated Type

# NSViewType

The type of view to present.

macOS 10.15+

    
    
    associatedtype NSViewType : NSView

**Required**

## See Also

### Creating and updating the view

`func makeNSView(context: Self.Context) -> Self.NSViewType`

Creates the view object and configures its initial state.

**Required**

` func updateNSView(Self.NSViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

Instance Method

# sizeThatFits(_:nsView:context:)

Given a proposed size, returns the preferred size of the composite view.

macOS 13.0+

    
    
    @MainActor
    func sizeThatFits(
        _ proposal: ProposedViewSize,
        nsView: Self.NSViewType,
        context: Self.Context
    ) -> CGSize?

**Required** Default implementation provided.

##  Parameters

`proposal`

    

The proposed size for the view.

`nsView`

    

Your custom view object.

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

The composite size of the represented view controller. Returning a value of
`nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during
the same layout pass. SwiftUI views choose their own size, so one of the
values returned from this function will always be used as the actual size of
the composite view.

## Default Implementations

### NSViewRepresentable Implementations

`func sizeThatFits(ProposedViewSize, nsView: Self.NSViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

Type Method

# dismantleNSView(_:coordinator:)

Cleans up the presented AppKit view (and coordinator) in anticipation of their
removal.

macOS 10.15+

    
    
    @MainActor
    static func dismantleNSView(
        _ nsView: Self.NSViewType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`nsView`

    

Your custom view object.

`coordinator`

    

The custom coordinator you use to communicate changes back to SwiftUI. If you
do not use a custom coordinator instance, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
view. For example, you might use this method to remove observers or update
other parts of your SwiftUI interface.

## Default Implementations

### NSViewRepresentable Implementations

`static func dismantleNSView(Self.NSViewType, coordinator: Self.Coordinator)`

Cleans up the presented AppKit view (and coordinator) in anticipation of their
removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

macOS 10.15+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your view might affect other parts of your
app. In your implementation, create a custom Swift instance that can
communicate with other parts of your interface. For example, you might provide
an instance that binds its variables to SwiftUI properties, causing the two to
remain synchronized. If your view doesn’t interact with other parts of your
app, you don’t have to provide a coordinator.

SwiftUI calls this method before calling the `makeNSView(context:)` method.
The system provides your coordinator instance either directly or as part of a
context structure when calling the other methods of your representable
instance.

## Default Implementations

### NSViewRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates a `Coordinator` instance to coordinate with the `NSView`.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the view.

**Required**

Associated Type

# Coordinator

A type to coordinate with the view.

macOS 10.15+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

**Required** Default implementation provided.

Type Alias

# NSViewRepresentable.LayoutOptions

macOS 13.0+

    
    
    typealias LayoutOptions



# Namespace

Initializer

# init()

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()

Instance Property

# wrappedValue

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Namespace.ID { get }

## See Also

### Getting the namespace

`struct ID`

A namespace defined by the persistent identity of an `@Namespace` dynamic
property.

Structure

# Namespace.ID

A namespace defined by the persistent identity of an `@Namespace` dynamic
property.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct ID

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the namespace

`var wrappedValue: Namespace.ID`



# NSHostingController

Initializer

# init(rootView:)

Creates a hosting controller object that wraps the specified SwiftUI view.

macOS 10.15+

    
    
    @MainActor
    init(rootView: Content)

##  Parameters

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using the
hosting view controller.

## See Also

### Creating a hosting controller object

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

Initializer

# init(coder:rootView:)

Creates a hosting controller object from an archive and the specified SwiftUI
view.

macOS 10.15+

    
    
    @MainActor
    init?(
        coder: NSCoder,
        rootView: Content
    )

##  Parameters

`coder`

    

The decoder to use during initialization.

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using this
view controller.

## See Also

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

Initializer

# init(coder:)

Creates a hosting controller object from the contents of the specified
archive.

macOS 10.15+

    
    
    @MainActor
    required dynamic init?(coder: NSCoder)

##  Parameters

`coder`

    

The decoder to use during initialization.

## Discussion

The default implementation of this method throws an exception. To create your
view controller from an archive, override this method and initialize the
superclass using the `init(coder:rootView:)` method instead.

## See Also

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this view controller.

macOS 10.15+

    
    
    @MainActor
    var rootView: Content { get set }

## See Also

### Getting the root view

`var identifier: NSUserInterfaceItemIdentifier?`

Instance Property

# identifier

macOS 10.15+

    
    
    @MainActor
    override dynamic var identifier: NSUserInterfaceItemIdentifier? { get set }

## See Also

### Getting the root view

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# sizeThatFits(in:)

Calculates and returns the most appropriate size for the current view.

macOS 10.15+

    
    
    @MainActor
    func sizeThatFits(in size: CGSize) -> CGSize

##  Parameters

`size`

    

The proposed new size for the view.

## Return Value

The size that offers the best fit for the root view and its contents.

## See Also

### Configuring the controller

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# preferredContentSize

macOS 10.15+

    
    
    @MainActor
    override dynamic var preferredContentSize: NSSize { get set }

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# sizingOptions

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

macOS 13.0+

    
    
    @MainActor
    var sizingOptions: NSHostingSizingOptions { get set }

## Discussion

NSHostingController can create minimum, maximum, and ideal (content size)
constraints that are derived from its SwiftUI view content. These constraints
are only created when Auto Layout constraints are otherwise being used in the
containing window.

If the NSHostingController is set as the `contentViewController` of an
`NSWindow`, it will also update the window’s `contentMinSize` and
`contentMaxSize` based on the minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`,
`intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to
control this behavior. For instance, setting a value of `.minSize` will only
create the constraints necessary to maintain the minimum size of the SwiftUI
content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingController`
relative to its displayed content, such as the always being displayed in a
fixed frame, setting this to a value with fewer options can improve
performance as it reduces the amount of layout measurements that need to be
performed. If an `NSHostingController` has a `frame` that is smaller or larger
than that required to display its SwiftUI content, the content will be
centered within that frame.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# safeAreaRegions

The safe area regions that this view controller adds to its view.

macOS 13.3+

    
    
    @MainActor
    var safeAreaRegions: SafeAreaRegions { get set }

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# sceneBridgingOptions

The options for which aspects of the window will be managed by this
controller’s hosting view.

macOS 14.0+

    
    
    @MainActor
    var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }

## Discussion

`NSHostingController` will populate certain aspects of its associated window,
depending on which options are specified.

For example, a hosting controller can manage its window’s toolbar by including
the `.toolbars` option:

When this hosting controller is set as the `contentViewController` for a
window, the default value for this property will be `.all`, which includes the
options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.



# NSHostingSceneBridgingOptions

Type Property

# all

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

macOS 14.0+

    
    
    static let all: NSHostingSceneBridgingOptions

## See Also

### Geting bridging options

`static let title: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

`static let toolbars: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

Type Property

# title

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

macOS 14.0+

    
    
    static let title: NSHostingSceneBridgingOptions

## Discussion

Title bars populated in this manner overwrite any values set using AppKit.

## See Also

### Geting bridging options

`static let all: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

`static let toolbars: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

Type Property

# toolbars

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

macOS 14.0+

    
    
    static let toolbars: NSHostingSceneBridgingOptions

## Discussion

Toolbars populated in this manner overwrite any toolbar set on the window
using AppKit.

## See Also

### Geting bridging options

`static let all: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

`static let title: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

Initializer

# init(rawValue:)

Creates a new set from a raw value.

macOS 14.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value with which to create the hosting window options.

## See Also

### Creating a bridging options

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

macOS 14.0+

    
    
    let rawValue: Int

## See Also

### Creating a bridging options

`init(rawValue: Int)`

Creates a new set from a raw value.



# NavigationControlGroupStyle

Initializer

# init()

Creates a navigation control group style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init()



# NavigationLink

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder destination: () -> Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Presenting a destination view

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Initializer

# init(destination:label:)

Creates a navigation link that presents the destination view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        _ titleKey: LocalizedStringKey,
        value: P?
    ) where Label == Text, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`titleKey`

    

A localized string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, P>(
        _ title: S,
        value: P?
    ) where Label == Text, S : StringProtocol, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`title`

    

A string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(value:label:)

Creates a navigation link that presents the view corresponding to a value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        value: P?,
        @ViewBuilder label: () -> Label
    ) where P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

`label`

    

A label that describes the view that this link presents.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        _ titleKey: LocalizedStringKey,
        value: P?
    ) where Label == Text, P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`titleKey`

    

A localized string that describes the view that this link presents.

`value`

    

An optional value to present. When someone taps or clicks the link, SwiftUI
stores a copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, P>(
        _ title: S,
        value: P?
    ) where Label == Text, S : StringProtocol, P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`title`

    

A string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(value:label:)

Creates a navigation link that presents the view corresponding to a codable
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        value: P?,
        @ViewBuilder label: () -> Label
    ) where P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

`label`

    

A label that describes the view that this link presents.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Instance Method

# isDetailLink(_:)

Sets the navigation link to present its destination as the detail component of
the containing navigation view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func isDetailLink(_ isDetailLink: Bool) -> some View
    

Available when `Label` conforms to `View` and `Destination` conforms to
`View`.

##  Parameters

`isDetailLink`

    

A Boolean value that specifies whether this link presents its destination as
the detail component when used in a multi-column navigation view.

## Return Value

A view that applies the specified detail link behavior.

## Discussion

This method sets the behavior when the navigation link is used in a
`NavigationSplitView`, or a multi-column navigation view, such as one using
`ColumnNavigationViewStyle`.

For example, in a two-column navigation split view, if `isDetailLink` is
`true`, triggering the link in the sidebar column sets the contents of the
detail column to be the link’s destination view. If `isDetailLink` is `false`,
the link navigates to the destination view within the primary column.

If you do not set the detail link behavior with this method, the behavior
defaults to `true`.

The `isDetailLink` modifier only affects view-destination links. Links that
present data values always search for a matching navigation destination
beginning in the column that contains the link.

Collection

API Collection

# Deprecated symbols

Review deprecated navigation link initializers.

## Overview

For information about updating your use of navigation symbols, see Migrating
to new navigation types.

## Topics

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

### Creating links for WatchKit

`init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () ->
Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init(destinationName: String, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated



# NSViewControllerRepresentableContext

Instance Property

# coordinator

An object you use to communicate your AppKit view controller’s behavior and
state out to SwiftUI objects.

macOS 10.15+

    
    
    @MainActor
    let coordinator: ViewController.Coordinator

## Discussion

The coordinator is a custom object you define. When updating your view
controller, communicate changes to SwiftUI by updating the properties of your
coordinator, or by calling relevant methods to make those changes. The
implementation of those properties and methods are responsible for updating
the appropriate SwiftUI values. For example, you might define a property in
your coordinator that binds to a SwiftUI value, as shown in the following code
example. Changing the property updates the value of the corresponding SwiftUI
variable.

To create and configure your custom coordinator, implement the
`makeCoordinator()` method of your `NSViewControllerRepresentable` object.

## See Also

### Coordinating view-related interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

macOS 10.15+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating view-related interactions

`let coordinator: ViewController.Coordinator`

An object you use to communicate your AppKit view controller’s behavior and
state out to SwiftUI objects.

Instance Property

# environment

Environment data that describes the current state of the system.

macOS 10.15+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your view controller when
creating or updating it.



# NavigationStack

Initializer

# init(root:)

Creates a navigation stack that manages its own navigation state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(@ViewBuilder root: () -> Root) where Data == NavigationPath

##  Parameters

`root`

    

The view to display when the stack is empty.

## Discussion

If you want to access the navigation state, use `init(path:root:)` instead.

Initializer

# init(path:root:)

Creates a navigation stack with homogeneous navigation state that you can
control.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        path: Binding<Data>,
        @ViewBuilder root: () -> Root
    ) where Data : MutableCollection, Data : RandomAccessCollection, Data : RangeReplaceableCollection, Data.Element : Hashable

##  Parameters

`path`

    

A `Binding` to the navigation state for this stack.

`root`

    

The view to display when the stack is empty.

## Discussion

If you prefer to store the navigation state as a `NavigationPath`, use
`init(path:root:)` instead. If you don’t need access to the navigation state,
use `init(root:)`.

## See Also

### Creating a navigation stack with a path

`init(path: Binding<NavigationPath>, root: () -> Root)`

Creates a navigation stack with heterogeneous navigation state that you can
control.

Initializer

# init(path:root:)

Creates a navigation stack with heterogeneous navigation state that you can
control.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        path: Binding<NavigationPath>,
        @ViewBuilder root: () -> Root
    ) where Data == NavigationPath

##  Parameters

`path`

    

A `Binding` to the navigation state for this stack.

`root`

    

The view to display when the stack is empty.

## Discussion

If you prefer to store the navigation state as a collection of data values,
use `init(path:root:)` instead. If you don’t need access to the navigation
state, use `init(root:)`.

## See Also

### Creating a navigation stack with a path

`init(path: Binding<Data>, root: () -> Root)`

Creates a navigation stack with homogeneous navigation state that you can
control.



# NavigationBarItem.TitleDisplayMode

Case

# NavigationBarItem.TitleDisplayMode.automatic

Inherit the display mode from the previous navigation item.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    case automatic

## See Also

### Getting title display modes

`case inline`

Display the title within the standard bounds of the navigation bar.

`case large`

Display a large title within an expanded navigation bar.

Case

# NavigationBarItem.TitleDisplayMode.inline

Display the title within the standard bounds of the navigation bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    case inline

## See Also

### Getting title display modes

`case automatic`

Inherit the display mode from the previous navigation item.

`case large`

Display a large title within an expanded navigation bar.

Case

# NavigationBarItem.TitleDisplayMode.large

Display a large title within an expanded navigation bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 8.0+  visionOS 1.0+

    
    
    case large

## See Also

### Getting title display modes

`case automatic`

Inherit the display mode from the previous navigation item.

`case inline`

Display the title within the standard bounds of the navigation bar.



# NavigationSplitViewColumn

Type Property

# sidebar

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var sidebar: NavigationSplitViewColumn { get }

## See Also

### Getting a column

`static var content: NavigationSplitViewColumn`

`static var detail: NavigationSplitViewColumn`

Type Property

# content

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var content: NavigationSplitViewColumn { get }

## See Also

### Getting a column

`static var sidebar: NavigationSplitViewColumn`

`static var detail: NavigationSplitViewColumn`

Type Property

# detail

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var detail: NavigationSplitViewColumn { get }

## See Also

### Getting a column

`static var sidebar: NavigationSplitViewColumn`

`static var content: NavigationSplitViewColumn`



# NSViewRepresentableContext

Instance Property

# coordinator

An instance you use to communicate your AppKit view’s behavior and state out
to SwiftUI objects.

macOS 10.15+

    
    
    @MainActor
    let coordinator: View.Coordinator

## Discussion

The coordinator is a custom instance you define. When updating your view,
communicate changes to SwiftUI by updating the properties of your coordinator,
or by calling relevant methods to make those changes. The implementation of
those properties and methods are responsible for updating the appropriate
SwiftUI values. For example, you might define a property in your coordinator
that binds to a SwiftUI value, as shown in the following code example.
Changing the property updates the value of the corresponding SwiftUI variable.

To create and configure your custom coordinator, implement the
`makeCoordinator()` method of your `NSViewControllerRepresentable` object.

## See Also

### Coordinating view-related interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

macOS 10.15+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating view-related interactions

`let coordinator: View.Coordinator`

An instance you use to communicate your AppKit view’s behavior and state out
to SwiftUI objects.

Instance Property

# environment

Environment data that describes the current state of the system.

macOS 10.15+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your view when creating
or updating it.



