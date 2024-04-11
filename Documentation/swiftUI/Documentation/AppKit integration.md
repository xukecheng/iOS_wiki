Class

# NSHostingController

An AppKit view controller that hosts SwiftUI view hierarchy.

macOS 10.15+

    
    
    @MainActor
    class NSHostingController<Content> where Content : View

## Overview

Create an `NSHostingController` object when you want to integrate SwiftUI
views into an AppKit view hierarchy. At creation time, specify the SwiftUI
view you want to use as the root view for this view controller; you can change
that view later using the `rootView` property. Use the hosting controller like
you would any other view controller, by presenting it or embedding it as a
child view controller in your interface.

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

### Getting the root view

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

`var identifier: NSUserInterfaceItemIdentifier?`

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

## Relationships

### Inherits From

  * `NSViewController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSCoding`
  * `NSEditor`
  * `NSExtensionRequestHandling`
  * `NSObjectProtocol`
  * `NSSeguePerforming`
  * `NSStandardKeyBindingResponding`
  * `NSTouchBarProvider`
  * `NSUserActivityRestoring`
  * `NSUserInterfaceItemIdentification`

## See Also

### Displaying SwiftUI views in AppKit

`class NSHostingView`

An AppKit view that hosts a SwiftUI view hierarchy.

`struct NSHostingSizingOptions`

Options for how hosting views and controllers reflect their content’s size
into Auto Layout constraints.

`struct NSHostingSceneBridgingOptions`

Options for how hosting views and controllers manage aspects of the associated
window.

Class

# NSHostingView

An AppKit view that hosts a SwiftUI view hierarchy.

macOS 10.15+

    
    
    @MainActor
    class NSHostingView<Content> where Content : View

## Overview

You use `NSHostingView` objects to integrate SwiftUI views into your AppKit
view hierarchies. A hosting view is an `NSView` object that manages a single
SwiftUI view, which may itself contain other SwiftUI views. Because it is an
`NSView` object, you can integrate it into your existing AppKit view
hierarchies to implement portions of your UI. For example, you can use a
hosting view to implement a custom control.

A hosting view acts as a bridge between your SwiftUI views and your AppKit
interface. During layout, the hosting view reports the content size
preferences of your SwiftUI views back to the AppKit layout system so that it
can size the view appropriately. The hosting view also coordinates event
delivery.

## Topics

### Creating a hosting view

`init(rootView: Content)`

Creates a hosting view object that wraps the specified SwiftUI view.

`init?(coder: NSCoder)`

Creates a hosting view object from the contents of the specified archive.

`func prepareForReuse()`

### Getting the root view

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

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

`func makeTouchBar() -> NSTouchBar?`

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

`func cursorUpdate(with: NSEvent)`

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesCancelled(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

### Responding to gestures

`func magnify(with: NSEvent)`

`func rotate(with: NSEvent)`

`func scrollWheel(with: NSEvent)`

### Handling drag and drop

`func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType:
NSPasteboard.PasteboardType?) -> Any?`

### Providing a context menu

`func menu(for: NSEvent) -> NSMenu?`

### Responding to actions

`func responds(to: Selector!) -> Bool`

`func forwardingTarget(for: Selector!) -> Any?`

`func doCommand(by: Selector)`

### Configuring the responder behavior

`var acceptsFirstResponder: Bool`

`var needsPanelToBecomeKey: Bool`

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

### Testing for hits

`func hitTest(NSPoint) -> NSView?`

### Managing accessibility behaviors

`var accessibilityFocusedUIElement: Any?`

`func accessibilityChildren() -> [Any]?`

`func accessibilityChildrenInNavigationOrder() -> [any
NSAccessibilityElementProtocol]?`

`func accessibilityHitTest(NSPoint) -> Any?`

`func accessibilityRole() -> NSAccessibility.Role?`

`func accessibilitySubrole() -> NSAccessibility.Subrole?`

`func isAccessibilityElement() -> Bool`

### Bridging with SwiftUI

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this hosting
view.

## Relationships

### Inherits From

  * `NSView`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSAccessibilityElementProtocol`
  * `NSAccessibilityProtocol`
  * `NSAnimatablePropertyContainer`
  * `NSAppearanceCustomization`
  * `NSCoding`
  * `NSDraggingDestination`
  * `NSDraggingSource`
  * `NSObjectProtocol`
  * `NSStandardKeyBindingResponding`
  * `NSTouchBarProvider`
  * `NSUserActivityRestoring`
  * `NSUserInterfaceItemIdentification`
  * `NSUserInterfaceValidations`

## See Also

### Displaying SwiftUI views in AppKit

`class NSHostingController`

An AppKit view controller that hosts SwiftUI view hierarchy.

`struct NSHostingSizingOptions`

Options for how hosting views and controllers reflect their content’s size
into Auto Layout constraints.

`struct NSHostingSceneBridgingOptions`

Options for how hosting views and controllers manage aspects of the associated
window.

Structure

# NSHostingSizingOptions

Options for how hosting views and controllers reflect their content’s size
into Auto Layout constraints.

macOS 13.0+

    
    
    struct NSHostingSizingOptions

## Topics

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

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

### Creating a sizing option

`init(rawValue: Int)`

Creates a new options from a raw value.

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

### Displaying SwiftUI views in AppKit

`class NSHostingController`

An AppKit view controller that hosts SwiftUI view hierarchy.

`class NSHostingView`

An AppKit view that hosts a SwiftUI view hierarchy.

`struct NSHostingSceneBridgingOptions`

Options for how hosting views and controllers manage aspects of the associated
window.

Structure

# NSHostingSceneBridgingOptions

Options for how hosting views and controllers manage aspects of the associated
window.

macOS 14.0+

    
    
    struct NSHostingSceneBridgingOptions

## Topics

### Geting bridging options

`static let all: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

`static let title: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

`static let toolbars: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

### Creating a bridging options

`init(rawValue: Int)`

Creates a new set from a raw value.

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

### Displaying SwiftUI views in AppKit

`class NSHostingController`

An AppKit view controller that hosts SwiftUI view hierarchy.

`class NSHostingView`

An AppKit view that hosts a SwiftUI view hierarchy.

`struct NSHostingSizingOptions`

Options for how hosting views and controllers reflect their content’s size
into Auto Layout constraints.

Protocol

# NSViewRepresentable

A wrapper that you use to integrate an AppKit view into your SwiftUI view
hierarchy.

macOS 10.15+

    
    
    protocol NSViewRepresentable : View where Self.Body == Never

## Overview

Use an `NSViewRepresentable` instance to create and manage an `NSView` object
in your SwiftUI interface. Adopt this protocol in one of your app’s custom
instances, and use its methods to create, update, and tear down your view. The
creation and update processes parallel the behavior of SwiftUI views, and you
use them to configure your view with your app’s current state information. Use
the teardown process to remove your view cleanly from your SwiftUI. For
example, you might use the teardown process to notify other objects that the
view is disappearing.

To add your view into your SwiftUI interface, create your
`NSViewRepresentable` instance and add it to your SwiftUI interface. The
system calls the methods of your representable instance at appropriate times
to create and update the view. The following example shows the inclusion of a
custom `MyRepresentedCustomView` struct in the view hierarchy.

The system doesn’t automatically communicate changes occurring within your
view controller to other parts of your SwiftUI interface. When you want your
view controller to coordinate with other SwiftUI views, you must provide a
`Coordinator` object to facilitate those interactions. For example, you use a
coordinator to forward target-action and delegate messages from your view
controller to any SwiftUI views.

## Topics

### Creating and updating the view

`func makeNSView(context: Self.Context) -> Self.NSViewType`

Creates the view object and configures its initial state.

**Required**

` func updateNSView(Self.NSViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype NSViewType : NSView`

The type of view to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, nsView: Self.NSViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view

`static func dismantleNSView(Self.NSViewType, coordinator: Self.Coordinator)`

Cleans up the presented AppKit view (and coordinator) in anticipation of their
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

### Adding AppKit views to SwiftUI view hierarchies

`struct NSViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view.

`protocol NSViewControllerRepresentable`

A wrapper that you use to integrate an AppKit view controller into your
SwiftUI interface.

`struct NSViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view controller.

Structure

# NSViewRepresentableContext

Contextual information about the state of the system that you use to create
and update your AppKit view.

macOS 10.15+

    
    
    @MainActor
    struct NSViewRepresentableContext<View> where View : NSViewRepresentable

## Overview

An `NSViewRepresentableContext` structure contains details about the current
state of the system. When creating and updating your view, the system creates
one of these structures and passes it to the appropriate method of your custom
`NSViewRepresentable` instance. Use the information in this structure to
configure your view. For example, use the provided environment values to
configure the appearance of your view. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions

`let coordinator: View.Coordinator`

An instance you use to communicate your AppKit view’s behavior and state out
to SwiftUI objects.

`var transaction: Transaction`

The current transaction.

### Getting the current environment data

`var environment: EnvironmentValues`

Environment data that describes the current state of the system.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding AppKit views to SwiftUI view hierarchies

`protocol NSViewRepresentable`

A wrapper that you use to integrate an AppKit view into your SwiftUI view
hierarchy.

`protocol NSViewControllerRepresentable`

A wrapper that you use to integrate an AppKit view controller into your
SwiftUI interface.

`struct NSViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view controller.

Protocol

# NSViewControllerRepresentable

A wrapper that you use to integrate an AppKit view controller into your
SwiftUI interface.

macOS 10.15+

    
    
    protocol NSViewControllerRepresentable : View where Self.Body == Never

## Overview

Use an `NSViewControllerRepresentable` instance to create and manage an
`NSViewController` object in your SwiftUI interface. Adopt this protocol in
one of your app’s custom instances, and use its methods to create, update, and
tear down your view controller. The creation and update processes parallel the
behavior of SwiftUI views, and you use them to configure your view controller
with your app’s current state information. Use the teardown process to remove
your view controller cleanly from your SwiftUI. For example, you might use the
teardown process to notify other objects that the view controller is
disappearing.

To add your view controller into your SwiftUI interface, create your
`NSViewControllerRepresentable` instance and add it to your SwiftUI interface.
The system calls the methods of your custom instance at appropriate times.

The system doesn’t automatically communicate changes occurring within your
view controller to other parts of your SwiftUI interface. When you want your
view controller to coordinate with other SwiftUI views, you must provide a
`Coordinator` instance to facilitate those interactions. For example, you use
a coordinator to forward target-action and delegate messages from your view
controller to any SwiftUI views.

## Topics

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

`associatedtype NSViewControllerType : NSViewController`

The type of view controller to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, nsViewController:
Self.NSViewControllerType, context: Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view controller

`static func dismantleNSViewController(Self.NSViewControllerType, coordinator:
Self.Coordinator)`

Cleans up the presented view controller (and coordinator) in anticipation of
its removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom object that you use to communicate changes from your view
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

### Adding AppKit views to SwiftUI view hierarchies

`protocol NSViewRepresentable`

A wrapper that you use to integrate an AppKit view into your SwiftUI view
hierarchy.

`struct NSViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view.

`struct NSViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view controller.

Structure

# NSViewControllerRepresentableContext

Contextual information about the state of the system that you use to create
and update your AppKit view controller.

macOS 10.15+

    
    
    @MainActor
    struct NSViewControllerRepresentableContext<ViewController> where ViewController : NSViewControllerRepresentable

## Overview

An `NSViewControllerRepresentableContext` structure contains details about the
current state of the system. When creating and updating your view controller,
the system creates one of these structures and passes it to the appropriate
method of your custom `NSViewControllerRepresentable` instance. Use the
information in this structure to configure your view controller. For example,
use the provided environment values to configure the appearance of your view
controller and views. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions

`let coordinator: ViewController.Coordinator`

An object you use to communicate your AppKit view controller’s behavior and
state out to SwiftUI objects.

`var transaction: Transaction`

The current transaction.

### Getting the current environment data

`var environment: EnvironmentValues`

Environment data that describes the current state of the system.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding AppKit views to SwiftUI view hierarchies

`protocol NSViewRepresentable`

A wrapper that you use to integrate an AppKit view into your SwiftUI view
hierarchy.

`struct NSViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your AppKit view.

`protocol NSViewControllerRepresentable`

A wrapper that you use to integrate an AppKit view controller into your
SwiftUI interface.

