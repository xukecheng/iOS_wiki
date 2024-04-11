Class

# UIHostingController

A UIKit view controller that manages a SwiftUI view hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    class UIHostingController<Content> where Content : View

## Overview

Create a `UIHostingController` object when you want to integrate SwiftUI views
into a UIKit view hierarchy. At creation time, specify the SwiftUI view you
want to use as the root view for this view controller; you can change that
view later using the `rootView` property. Use the hosting controller like you
would any other view controller, by presenting it or embedding it as a child
view controller in your interface.

## Topics

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

### Checking for modality

`var isModalInPresentation: Bool`

### Managing the size

`var sizingOptions: UIHostingControllerSizingOptions`

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

`func preferredContentSizeDidChange(forChildContentContainer: any
UIContentContainer)`

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Available when `Content` conforms to `View`.

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarStyle: UIViewController?`

`var childForStatusBarHidden: UIViewController?`

### Configuring the home indicator

`var prefersHomeIndicatorAutoHidden: Bool`

A Boolean value that indicates whether the view controller prefers the home
indicator to be hidden or shown.

`var childForHomeIndicatorAutoHidden: UIViewController?`

### Configuring the interface appearance

`var preferredUserInterfaceStyle: UIUserInterfaceStyle`

The preferred interface style for this view controller.

`var preferredScreenEdgesDeferringSystemGestures: UIRectEdge`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`var childForScreenEdgesDeferringSystemGestures: UIViewController?`

### Accessing the available key commands

`var keyCommands: [UIKeyCommand]?`

### Managing undo

`var undoManager: UndoManager?`

### Instance Properties

`var childViewControllerForPreferredContainerBackgroundStyle:
UIViewController?`

`var preferredContainerBackgroundStyle: UIContainerBackgroundStyle`

### Instance Methods

`func addChild(UIViewController)`

## Relationships

### Inherits From

  * `UIViewController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSCoding`
  * `NSExtensionRequestHandling`
  * `NSObjectProtocol`
  * `NSTouchBarProvider`
  * `UIActivityItemsConfigurationProviding`
  * `UIAppearanceContainer`
  * `UIContentContainer`
  * `UIFocusEnvironment`
  * `UIPasteConfigurationSupporting`
  * `UIResponderStandardEditActions`
  * `UIStateRestoring`
  * `UITraitChangeObservable`
  * `UITraitEnvironment`
  * `UIUserActivityRestoring`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`struct UIHostingControllerSizingOptions`

Options for how a hosting controller tracks its content’s size.

`struct UIHostingConfiguration`

A content configuration suitable for hosting a hierarchy of SwiftUI views.

Structure

# UIHostingControllerSizingOptions

Options for how a hosting controller tracks its content’s size.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct UIHostingControllerSizingOptions

## Topics

### Getting sizing options

`static let intrinsicContentSize: UIHostingControllerSizingOptions`

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

`static let preferredContentSize: UIHostingControllerSizingOptions`

The hosting controller tracks its content’s ideal size in its preferred
content size.

### Creating a sizing option

`init(rawValue: Int)`

Creates a new option set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`class UIHostingController`

A UIKit view controller that manages a SwiftUI view hierarchy.

`struct UIHostingConfiguration`

A content configuration suitable for hosting a hierarchy of SwiftUI views.

Structure

# UIHostingConfiguration

A content configuration suitable for hosting a hierarchy of SwiftUI views.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    struct UIHostingConfiguration<Content, Background> where Content : View, Background : View

## Overview

Use a value of this type, which conforms to the `UIContentConfiguration`
protocol, with a `UICollectionViewCell` or `UITableViewCell` to host a
hierarchy of SwiftUI views in a collection or table view, respectively. For
example, the following shows a stack with an image and text inside the cell:

You can also customize the background of the containing cell. The following
example draws a blue background:

When used in a list layout, certain APIs are bridged automatically, like swipe
actions and separator alignment. The following example shows a trailing yellow
star swipe action:

## Topics

### Creating and updating a configuration

`init(content: () -> Content)`

Creates a hosting configuration with the given contents.

Available when `Content` conforms to `View` and `Background` is `EmptyView`.

### Setting the background

`func background<S>(S) -> UIHostingConfiguration<Content,
_UIHostingConfigurationBackgroundView<S>>`

Sets the background contents for the hosting configuration’s enclosing cell.

`func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>`

Sets the background contents for the hosting configuration’s enclosing cell.

### Setting margins

`func margins(Edge.Set, EdgeInsets) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

`func margins(Edge.Set, CGFloat) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

### Setting a size

`func minSize(width: CGFloat?, height: CGFloat?) ->
UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

`func minSize() -> UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

Deprecated

## Relationships

### Conforms To

  * `UIContentConfiguration`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`class UIHostingController`

A UIKit view controller that manages a SwiftUI view hierarchy.

`struct UIHostingControllerSizingOptions`

Options for how a hosting controller tracks its content’s size.

Protocol

# UIViewRepresentable

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    protocol UIViewRepresentable : View where Self.Body == Never

## Overview

Use a `UIViewRepresentable` instance to create and manage a `UIView` object in
your SwiftUI interface. Adopt this protocol in one of your app’s custom
instances, and use its methods to create, update, and tear down your view. The
creation and update processes parallel the behavior of SwiftUI views, and you
use them to configure your view with your app’s current state information. Use
the teardown process to remove your view cleanly from your SwiftUI. For
example, you might use the teardown process to notify other objects that the
view is disappearing.

To add your view into your SwiftUI interface, create your
`UIViewRepresentable` instance and add it to your SwiftUI interface. The
system calls the methods of your representable instance at appropriate times
to create and update the view. The following example shows the inclusion of a
custom `MyRepresentedCustomView` structure in the view hierarchy.

The system doesn’t automatically communicate changes occurring within your
view to other parts of your SwiftUI interface. When you want your view to
coordinate with other SwiftUI views, you must provide a `Coordinator` instance
to facilitate those interactions. For example, you use a coordinator to
forward target-action and delegate messages from your view to any SwiftUI
views.

## Topics

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, uiView: Self.UIViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view

`static func dismantleUIView(Self.UIViewType, coordinator: Self.Coordinator)`

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the view.

**Required**

### Performing layout

`typealias LayoutOptions`

## Relationships

### Inherits From

  * `View`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Structure

# UIViewRepresentableContext

Contextual information about the state of the system that you use to create
and update your UIKit view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    struct UIViewRepresentableContext<Representable> where Representable : UIViewRepresentable

## Overview

A `UIViewRepresentableContext` structure contains details about the current
state of the system. When creating and updating your view, the system creates
one of these structures and passes it to the appropriate method of your custom
`UIViewRepresentable` instance. Use the information in this structure to
configure your view. For example, use the provided environment values to
configure the appearance of your view. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

`var transaction: Transaction`

The current transaction.

### Getting the current environment data

`var environment: EnvironmentValues`

The current environment.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Protocol

# UIViewControllerRepresentable

A view that represents a UIKit view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    protocol UIViewControllerRepresentable : View where Self.Body == Never

## Overview

Use a `UIViewControllerRepresentable` instance to create and manage a
`UIViewController` object in your SwiftUI interface. Adopt this protocol in
one of your app’s custom instances, and use its methods to create, update, and
tear down your view controller. The creation and update processes parallel the
behavior of SwiftUI views, and you use them to configure your view controller
with your app’s current state information. Use the teardown process to remove
your view controller cleanly from your SwiftUI. For example, you might use the
teardown process to notify other objects that the view controller is
disappearing.

To add your view controller into your SwiftUI interface, create your
`UIViewControllerRepresentable` instance and add it to your SwiftUI interface.
The system calls the methods of your custom instance at appropriate times.

The system doesn’t automatically communicate changes occurring within your
view controller to other parts of your SwiftUI interface. When you want your
view controller to coordinate with other SwiftUI views, you must provide a
`Coordinator` instance to facilitate those interactions. For example, you use
a coordinator to forward target-action and delegate messages from your view
controller to any SwiftUI views.

## Topics

### Creating and updating the view controller

`func makeUIViewController(context: Self.Context) ->
Self.UIViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateUIViewController(Self.UIViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewControllerType : UIViewController`

The type of view controller to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, uiViewController:
Self.UIViewControllerType, context: Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view controller

`static func dismantleUIViewController(Self.UIViewControllerType, coordinator:
Self.Coordinator)`

Cleans up the presented view controller (and coordinator) in anticipation of
their removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the view controller.

**Required**

### Performing layout

`typealias LayoutOptions`

## Relationships

### Inherits From

  * `View`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Structure

# UIViewControllerRepresentableContext

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    struct UIViewControllerRepresentableContext<Representable> where Representable : UIViewControllerRepresentable

## Overview

A `UIViewControllerRepresentableContext` structure contains details about the
current state of the system. When creating and updating your view controller,
the system creates one of these structures and passes it to the appropriate
method of your custom `UIViewControllerRepresentable` instance. Use the
information in this structure to configure your view controller. For example,
use the provided environment values to configure the appearance of your view
controller and views. Don’t create this structure yourself.

## Topics

### Coordinating view controller interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

`var transaction: Transaction`

The current transaction.

### Getting the environment data

`var environment: EnvironmentValues`

Environment values that describe the current state of the system.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

Protocol

# UITraitBridgedEnvironmentKey

An environment key that is bridged to a UIKit trait.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    protocol UITraitBridgedEnvironmentKey : EnvironmentKey

## Overview

Use this protocol to allow the same underlying data to be accessed using an
environment key in SwiftUI and trait in UIKit. As the bridging is
bidirectional, values written to the trait in UIKit can be read using the
environment key in SwiftUI, and values written to the environment key in
SwiftUI can be read from the trait in UIKit.

Given a custom UIKit trait named `MyTrait` with `myTrait` properties on both
`UITraitCollection` and `UIMutableTraits`:

You can declare an environment key to represent the same data:

Bridge the environment key and the trait by conforming to the
`UITraitBridgedEnvironmentKey` protocol, providing implementations of
`read(from:)` and `write(to:value:)` to losslessly convert the environment
value from and to the corresponding trait value:

## Topics

### Managing the keys

`static func read(from: UITraitCollection) -> Self.Value`

Reads the trait value from the trait collection, and returns the equivalent
environment value.

**Required**

` static func write(to: inout any UIMutableTraits, value: Self.Value)`

**Required**

## Relationships

### Inherits From

  * `EnvironmentKey`

Class

# UIHostingOrnament

A model that represents an ornament suitable for being hosted in UIKit.

visionOS 1.0+

    
    
    class UIHostingOrnament<Content> where Content : View

## Overview

Use a `UIHostingOrnament` when you want to add ornaments to a UIKit view
controller. For example, the following adds a single bottom ornament to the
current view controller:

## Topics

### Creating a hosting ornament

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this ornament.

### Setting the alignment

`var contentAlignment: Alignment`

The alignment in the ornament used to position it.

### Initializers

`init(sceneAnchor: UnitPoint, contentAlignment: Alignment, content: () ->
Content)`

Creates an ornament with the specified alignment and content.

### Instance Properties

`var sceneAnchor: UnitPoint`

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

## Relationships

### Inherits From

  * `UIOrnament`

## See Also

### Hosting an ornament in UIKit

`class UIOrnament`

The abstract base class that represents an ornament.

Class

# UIOrnament

The abstract base class that represents an ornament.

visionOS 1.0+

    
    
    class UIOrnament

## Overview

You don’t create an instance of this class directly. Instead use
`UIHostingOrnament` when you want to add ornaments to a UIKit view controller.

## Relationships

### Inherited By

  * `UIHostingOrnament`

## See Also

### Hosting an ornament in UIKit

`class UIHostingOrnament`

A model that represents an ornament suitable for being hosted in UIKit.

