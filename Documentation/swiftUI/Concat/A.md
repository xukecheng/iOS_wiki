# Animatable

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: Self.AnimatableData { get set }

**Required** Default implementations provided.

## Default Implementations

### Animatable Implementations

`var animatableData: Self`

The data to animate.

Available when `Self` conforms to `VectorArithmetic`.

`var animatableData: EmptyAnimatableData`

The data to animate.

Available when `AnimatableData` is `EmptyAnimatableData`.

## See Also

### Animating data

`associatedtype AnimatableData : VectorArithmetic`

The type defining the data to animate.

**Required**

Associated Type

# AnimatableData

The type defining the data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype AnimatableData : VectorArithmetic

**Required**

## See Also

### Animating data

`var animatableData: Self.AnimatableData`

The data to animate.

**Required** Default implementations provided.



# AsyncImagePhase

Case

# AsyncImagePhase.empty

No image is loaded.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case empty

## See Also

### Getting load phases

`case success(Image)`

An image succesfully loaded.

`case failure(any Error)`

An image failed to load with an error.

Case

# AsyncImagePhase.success(_:)

An image succesfully loaded.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case success(Image)

## See Also

### Getting load phases

`case empty`

No image is loaded.

`case failure(any Error)`

An image failed to load with an error.

Case

# AsyncImagePhase.failure(_:)

An image failed to load with an error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case failure(any Error)

## See Also

### Getting load phases

`case empty`

No image is loaded.

`case success(Image)`

An image succesfully loaded.

Instance Property

# image

The loaded image, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var image: Image? { get }

## Discussion

If this value isn’t `nil`, the image load operation has finished, and you can
use the image to update the view. You can use the image directly, or you can
modify it in some way. For example, you can add a
`resizable(capInsets:resizingMode:)` modifier to make the image resizable.

Instance Property

# error

The error that occurred when attempting to load an image, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var error: (any Error)? { get }



# AccessibilityQuickActionStyle

Type Property

# outline

A presentation style that animates an outline around the view when the
accessibility quick action is active.

watchOS 9.0+

    
    
    static var outline: AccessibilityQuickActionOutlineStyle { get }

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

## Discussion

Use the `contentShape(_:_:eoFill:)` modifier to provide a shape for
`focusEffect` if necessary.

The following example shows how to add an
`accessibilityQuickAction(style:content:)` to play and pause music.

## See Also

### Getting built-in menu styles

`static var prompt: AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

Type Property

# prompt

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    static var prompt: AccessibilityQuickActionPromptStyle { get }

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

## Discussion

The following example shows how to add an
`accessibilityQuickAction(style:content:)` to pause and resume a workout.

## See Also

### Getting built-in menu styles

`static var outline: AccessibilityQuickActionOutlineStyle`

A presentation style that animates an outline around the view when the
accessibility quick action is active.

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

Structure

# AccessibilityQuickActionOutlineStyle

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    struct AccessibilityQuickActionOutlineStyle

## Overview

Don’t use this type directly. Instead, use `outline`.

## Relationships

### Conforms To

  * `AccessibilityQuickActionStyle`

## See Also

### Supporting types

`struct AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Structure

# AccessibilityQuickActionPromptStyle

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    struct AccessibilityQuickActionPromptStyle

## Overview

Don’t use this type directly. Instead, use `prompt`.

## Relationships

### Conforms To

  * `AccessibilityQuickActionStyle`

## See Also

### Supporting types

`struct AccessibilityQuickActionOutlineStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.



# AppKit integration

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



# App organization

Protocol

# App

A type that represents the structure and behavior of an app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol App

## Overview

Create an app by declaring a structure that conforms to the `App` protocol.
Implement the required `body` computed property to define the app’s content:

Precede the structure’s declaration with the @main attribute to indicate that
your custom `App` protocol conformer provides the entry point into your app.
The protocol provides a default implementation of the `main()` method that the
system calls to launch your app. You can have exactly one entry point among
all of your app’s files.

Compose the app’s body from instances that conform to the `Scene` protocol.
Each scene contains the root view of a view hierarchy and has a life cycle
managed by the system. SwiftUI provides some concrete scene types to handle
common scenarios, like for displaying documents or settings. You can also
create custom scenes.

You can declare state in your app to share across all of its scenes. For
example, you can use the `StateObject` attribute to initialize a data model,
and then provide that model on a view input as an `ObservedObject` or through
the environment as an `EnvironmentObject` to scenes in the app:

## Topics

### Implementing an app

`var body: Self.Body`

The content and behavior of the app.

**Required**

` associatedtype Body : Scene`

The type of scene representing the content of the app.

**Required**

### Running an app

`init()`

Creates an instance of the app using the body that you define for its content.

**Required**

` static func main()`

Initializes and runs the app.

## See Also

### Creating an app

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Backyard Birds: Building an app with SwiftData and widgets

Create an app with persistent data, interactive widgets, and an all new in-app
purchase experience.

Food Truck: Building a SwiftUI multiplatform app

Create a single codebase and app target for Mac, iPad, and iPhone.

Fruta: Building a Feature-Rich App with SwiftUI

Create a shared codebase to build a multiplatform app that offers widgets and
an App Clip.

Property List Key

# UILaunchScreen

The user interface to show while an app launches.

iOS 14.0+  iPadOS 14.0+

##  Details

Type

    

dictionary

## Discussion

You use this key to define the launch screen that the system displays while
your app launches. If you need to provide different launch screens in response
to being launched by different URL schemes, use `UILaunchScreens` instead.

Note

Use this key to configure the user interface during app launch in a way that
doesn’t rely on storyboards. If you prefer to use storyboards, use
`UILaunchStoryboardName` instead.

## Topics

### Main Interface

`property list key UIColorName`

The name of a color to use as the background color on the launch screen.

`property list key UIImageName`

The name of an image to display during app launch.

`property list key UIImageRespectsSafeAreaInsets`

A Boolean that specifies whether the launch image should respect the safe area
insets.

### Border Elements

`property list key UINavigationBar`

Navigation bar visibility and configuration during launch.

`property list key UITabBar`

Tab bar visibility and configuration during launch.

`property list key UIToolbar`

Toolbar visibility and configuration during launch.

## See Also

### Launch interface

`property list key UILaunchScreens`

The user interfaces to show while an app launches in response to different URL
schemes.

`property list key UILaunchStoryboardName`

The filename of the storyboard from which to generate the app’s launch image.

**Name:** Launch screen interface file base name

`property list key UILaunchStoryboards`

The launch storyboard to use to generate a launch image when your app opens
from a supported scheme.

`property list key LSUIPresentationMode`

The initial user-interface mode for the app.

**Name:** Application UI Presentation Mode

`property list key UILaunchToFullScreenByDefaultOnMac`

A Boolean value that indicates whether to launch your iPad app in full-screen
mode when running on a Mac.

Property List Key

# UILaunchScreens

The user interfaces to show while an app launches in response to different URL
schemes.

iOS 14.0+  iPadOS 14.0+

##  Details

Type

    

dictionary

## Discussion

You use this key if your app supports launching in response to one or more URL
schemes, and if you want to provide different launch screens for different
launch triggers. If you need only one launch screen, use `UILaunchScreen`
instead.

To define launch screens, create an array of dictionaries, each similar to the
one you might provide for `UILaunchScreen`, but with an added
`UILaunchScreenIdentifier` key that uniquely identifies the screen. Store the
array as the value for the `UILaunchScreenDefinitions` key.

To map from URL schemes to a launch screens, create a dictionary of schemes
and identifiers, and store it as the value for the
`UIURLToLaunchScreenAssociations` key. Additionally, indicate a default launch
screen by setting a value for the `UIDefaultLaunchScreen` key.

Note

Use this key to configure the user interface during app launch in a way that
doesn’t rely on storyboards. If you prefer to use storyboards to define the
launch screen, use the `UILaunchStoryboards` key instead.

## Topics

### Launch Screen Definitions

`property list key UILaunchScreenDefinitions`

A collection of launch screen configuration dictionaries.

### Associations

`property list key UIURLToLaunchScreenAssociations`

The mapping of URL schemes to launch screen configurations.

`property list key UIDefaultLaunchScreen`

The default launch screen configuration.

## See Also

### Launch interface

`property list key UILaunchScreen`

The user interface to show while an app launches.

`property list key UILaunchStoryboardName`

The filename of the storyboard from which to generate the app’s launch image.

**Name:** Launch screen interface file base name

`property list key UILaunchStoryboards`

The launch storyboard to use to generate a launch image when your app opens
from a supported scheme.

`property list key LSUIPresentationMode`

The initial user-interface mode for the app.

**Name:** Application UI Presentation Mode

`property list key UILaunchToFullScreenByDefaultOnMac`

A Boolean value that indicates whether to launch your iPad app in full-screen
mode when running on a Mac.

Structure

# UIApplicationDelegateAdaptor

A property wrapper type that you use to create a UIKit app delegate.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct UIApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : UIApplicationDelegate

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle,
define a type that conforms to the `UIApplicationDelegate` protocol, and
implement the delegate methods that you need. For example, you can implement
the `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method
to handle remote notification registration:

Then use the `UIApplicationDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given app. If you declare it more than once,
SwiftUI generates a runtime error.

If your app delegate conforms to the `ObservableObject` protocol, as in the
example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your app
using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an app’s life cycle events without using an app delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like
`application(_:didFinishLaunchingWithOptions:)`.

### Scene delegates

Some iOS apps define a `UIWindowSceneDelegate` to handle scene-based events,
like app shortcuts:

You can provide this kind of delegate to a SwiftUI app by returning the scene
delegate’s type from the `application(_:configurationForConnecting:options:)`
method inside your app delegate:

When you configure the `UISceneConfiguration` instance, you only need to
indicate the delegate class, and not a scene class or storyboard. SwiftUI
creates and manages the delegate instance, and sends it any relevant delegate
callbacks.

As with the app delegate, if you make your scene delegate an observable
object, SwiftUI automatically puts it in the `Environment`, from where you can
access it with the `EnvironmentObject` property wrapper, and create bindings
to its published properties.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`var wrappedValue: DelegateType`

The underlying app delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting iOS and iPadOS

UILaunchScreen

The user interface to show while an app launches.

UILaunchScreens

The user interfaces to show while an app launches in response to different URL
schemes.

Structure

# NSApplicationDelegateAdaptor

A property wrapper type that you use to create an AppKit app delegate.

macOS 11.0+

    
    
    @MainActor @propertyWrapper
    struct NSApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : NSApplicationDelegate

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle,
define a type that conforms to the `NSApplicationDelegate` protocol, and
implement the delegate methods that you need. For example, you can implement
the `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method
to handle remote notification registration:

Then use the `NSApplicationDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given app. If you declare it more than once,
SwiftUI generates a runtime error.

If your app delegate conforms to the `ObservableObject` protocol, as in the
example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your app
using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an app’s life cycle events without using an app delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like `applicationDidFinishLaunching(_:)`.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `Observable`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

Structure

# WKApplicationDelegateAdaptor

A property wrapper that is used in `App` to provide a delegate from WatchKit.

watchOS 7.0+

    
    
    @MainActor @propertyWrapper
    struct WKApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKApplicationDelegate

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting watchOS

`struct WKExtensionDelegateAdaptor`

A property wrapper type that you use to create a WatchKit extension delegate.

Structure

# WKExtensionDelegateAdaptor

A property wrapper type that you use to create a WatchKit extension delegate.

watchOS 7.0+

    
    
    @MainActor @propertyWrapper
    struct WKExtensionDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKExtensionDelegate

## Overview

To handle extension delegate callbacks in an extension that uses the SwiftUI
life cycle, define a type that conforms to the `WKExtensionDelegate` protocol,
and implement the delegate methods that you need. For example, you can
implement the `didRegisterForRemoteNotifications(withDeviceToken:)` method to
handle remote notification registration:

Then use the `WKExtensionDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given extension. If you declare it more than
once, SwiftUI generates a runtime error.

If your extension delegate conforms to the `ObservableObject` protocol, as in
the example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your
extension using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an externsion’s life cycle events without using a delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like `applicationDidFinishLaunching()`.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting watchOS

`struct WKApplicationDelegateAdaptor`

A property wrapper that is used in `App` to provide a delegate from WatchKit.



# AnyGesture

Initializer

# init(_:)

Creates an instance from another gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ gesture: T) where Value == T.Value, T : Gesture

##  Parameters

`gesture`

    

A gesture that you use to create a new gesture.



# App

Instance Property

# body

The content and behavior of the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @SceneBuilder @MainActor
    var body: Self.Body { get }

**Required**

## Discussion

For any app that you create, provide a computed `body` property that defines
your app’s scenes, which are instances that conform to the `Scene` protocol.
For example, you can create a simple app with a single scene containing a
single view:

Swift infers the app’s `Body` associated type based on the scene provided by
the `body` property.

## See Also

### Implementing an app

`associatedtype Body : Scene`

The type of scene representing the content of the app.

**Required**

Associated Type

# Body

The type of scene representing the content of the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : Scene

**Required**

## Discussion

When you create a custom app, Swift infers this type from your implementation
of the required `body` property.

## See Also

### Implementing an app

`var body: Self.Body`

The content and behavior of the app.

**Required**

Initializer

# init()

Creates an instance of the app using the body that you define for its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    init()

**Required**

## Discussion

Swift synthesizes a default initializer for structures that don’t provide one.
You typically rely on the default initializer for your app.

## See Also

### Running an app

`static func main()`

Initializes and runs the app.

Type Method

# main()

Initializes and runs the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    static func main()

## Discussion

If you precede your `App` conformer’s declaration with the @main attribute,
the system calls the conformer’s `main()` method to launch the app. SwiftUI
provides a default implementation of the method that manages the launch
process in a platform-appropriate way.

## See Also

### Running an app

`init()`

Creates an instance of the app using the body that you define for its content.

**Required**



# AnimationCompletionCriteria

Type Property

# logicallyComplete

The animation has logically completed, but may still be in its long tail.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let logicallyComplete: AnimationCompletionCriteria

## Discussion

If a subsequent change occurs that creates additional animations on properties
with `logicallyComplete` completion callbacks registered, then those callbacks
will fire when the animations from the change that they were registered with
logically complete, ignoring the new animations.

## See Also

### Getting the completion criteria

`static let removed: AnimationCompletionCriteria`

The entire animation is finished and will now be removed.

Type Property

# removed

The entire animation is finished and will now be removed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let removed: AnimationCompletionCriteria

## Discussion

If a subsequent change occurs that creates additional animations on properties
with `removed` completion callbacks registered, then those callbacks will only
fire when _all_ of the created animations are complete.

## See Also

### Getting the completion criteria

`static let logicallyComplete: AnimationCompletionCriteria`

The animation has logically completed, but may still be in its long tail.



# AutomaticFormStyle

Initializer

# init()

Creates a default form style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `automatic` static
variable to create this style:



# AccessibilityTextContentType

Type Property

# console

A type that represents text used for input, like in the Terminal app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let console: AccessibilityTextContentType

## See Also

### Getting content types

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# fileSystem

A type that represents text used by a file browser, like in the Finder app in
macOS.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let fileSystem: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# messaging

A type that represents text used in a message, like in the Messages app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let messaging: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# narrative

A type that represents text used in a story or poem, like in the Books app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let narrative: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# plain

A type that represents generic text that has no specific type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let plain: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# sourceCode

A type that represents text used in source code, like in Swift Playgrounds.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let sourceCode: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# spreadsheet

A type that represents text used in a grid of data, like in the Numbers app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let spreadsheet: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

Type Property

# wordProcessing

A type that represents text used in a document, like in the Pages app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let wordProcessing: AccessibilityTextContentType

## See Also

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.



# AlignmentID

Type Method

# defaultValue(in:)

Calculates a default value for the corresponding guide in the specified
context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func defaultValue(in context: ViewDimensions) -> CGFloat

**Required**

##  Parameters

`context`

    

The context of the view that you apply the alignment guide to. The context
gives you the view’s dimensions, as well as the values of other alignment
guides that apply to the view, including both built-in and custom guides. You
can use any of these values, if helpful, to calculate the value for your
custom guide.

## Return Value

The offset of the guide from the origin in the view’s coordinate space.

## Discussion

Implement this method when you create a type that conforms to the
`AlignmentID` protocol. Use the method to calculate the default offset of the
corresponding alignment guide. SwiftUI interprets the value that you return as
an offset in the coordinate space of the view that’s being laid out. For
example, you can use the context to return a value that’s one-third of the
height of the view:

You can override the default value that this method returns for a particular
guide by adding the `alignmentGuide(_:computeValue:)` view modifier to a
particular view.



# AttachmentContent Implementations

Instance Property

# body

RealityKit  SwiftUI  visionOS 1.0+

    
    
    var body: Never { get }

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

Type Alias

# ForEach.Body

RealityKit  SwiftUI  visionOS 1.0+

    
    
    typealias Body = Never

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.



# Animation

Type Property

# default

A default animation instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let `default`: Animation

## Discussion

The `default` animation is `spring(response:dampingFraction:blendDuration:)`
with:

  * `response` equal to `0.55`

  * `dampingFraction` equal to `1.0`

  * `blendDuration` equal to `0.0`

Prior to iOS 17, macOS 14, tvOS 17, and watchOS 10, the `default` animation is
`easeInOut`.

The global function `withAnimation(_:_:)` uses the default animation if you
don’t provide one. For instance, the following code listing shows an example
of using the `default` animation to flip the text “Hello” each time someone
clicks the Animate button.

Play

To use the `default` animation when adding the `animation(_:value:)` view
modifier, specify it explicitly as the animation type. For instance, the
following code shows an example of the `default` animation to spin the text
“Hello” each time someone clicks the Animate button.

Play

A `default` animation instance is only equal to other `default` animation
instances (using `==`), and not equal to other animation instances even when
the animations are identical. For example, if you create an animation using
the `spring(response:dampingFraction:blendDuration:)` modifier with the same
parameter values that `default` uses, the animation isn’t equal to `default`.
This behavior lets you differentiate between animations that you intentionally
choose and those that use the `default` animation.

Type Property

# linear

An animation that moves at a constant speed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var linear: Animation { get }

## Return Value

A linear animation with the default duration.

## Discussion

A linear animation provides a mechanical feel to the motion because its speed
is consistent from start to finish of the animation. This constant speed makes
a linear animation ideal for animating the movement of objects where changes
in the speed might feel awkward, such as with an activity indicator.

The following code shows an example of using linear animation to animate the
movement of a circle as it moves between the leading and trailing edges of the
view. The circle also animates its color change as it moves across the view.

Play

The `linear` animation has a default duration of 0.35 seconds. To specify a
different duration, use `linear(duration:)`.

## See Also

### Getting linear animations

`static func linear(duration: TimeInterval) -> Animation`

An animation that moves at a constant speed during a specified duration.

Type Method

# linear(duration:)

An animation that moves at a constant speed during a specified duration.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func linear(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

A linear animation with a specified duration.

## Discussion

A linear animation provides a mechanical feel to the motion because its speed
is consistent from start to finish of the animation. This constant speed makes
a linear animation ideal for animating the movement of objects where changes
in the speed might feel awkward, such as with an activity indicator.

Use `linear(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `linear` to perform the animation for a
default length of time.

The following code shows an example of using linear animation with a duration
of two seconds to animate the movement of a circle as it moves between the
leading and trailing edges of the view. The color of the circle also animates
from red to blue as it moves across the view.

Play

## See Also

### Getting linear animations

`static var linear: Animation`

An animation that moves at a constant speed.

Type Property

# easeIn

An animation that starts slowly and then increases speed towards the end of
the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeIn: Animation { get }

## Return Value

An ease-in animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease in animation, the motion starts slowly and
increases its speed towards the end.

The `easeIn` animation has a default duration of 0.35 seconds. To specify a
different duration, use `easeIn(duration:)`.

The following code shows an example of animating the size changes of a
`Circle` using the ease in animation.

Play

## See Also

### Getting eased animations

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Method

# easeIn(duration:)

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeIn(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-in animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease in animation, the motion starts slowly and
increases its speed towards the end.

Use `easeIn(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeIn` to perform the animation for a
default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease in animation with a duration of one second.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Property

# easeOut

An animation that starts quickly and then slows towards the end of the
movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeOut: Animation { get }

## Return Value

An ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease out animation, the motion starts quickly and
decreases its speed towards the end.

The `easeOut` animation has a default duration of 0.35 seconds. To specify a
different duration, use `easeOut(duration:)`.

The following code shows an example of animating the size changes of a
`Circle` using an ease out animation.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Method

# easeOut(duration:)

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeOut(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-out animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease out animation, the motion starts quickly and
decreases its speed towards the end.

Use `easeOut(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeOut` to perform the animation for a
default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease out animation with a duration of one second.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Property

# easeInOut

An animation that combines the behaviors of in and out easing animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeInOut: Animation { get }

## Return Value

An ease-in ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. An ease in and out animation starts slowly, increasing its
speed towards the halfway point, and finally decreasing the speed towards the
end of the animation.

The `easeInOut` animation has a default duration of 0.35 seconds. To specify
the duration, use the `easeInOut(duration:)` method.

The following code shows an example of animating the size changes of a
`Circle` using an ease in and out animation.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Method

# easeInOut(duration:)

An animation with a specified duration that combines the behaviors of in and
out easing animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeInOut(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-in ease-out animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. An ease in and out animation starts slowly, increasing its
speed towards the halfway point, and finally decreasing the speed towards the
end of the animation.

Use `easeInOut(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeInOut` to perform the animation for
a default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease in and out animation with a duration of one second.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

Type Property

# bouncy

A spring animation with a predefined duration and higher amount of bounce.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bouncy: Animation { get }

## See Also

### Getting built-in spring animations

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Method

# bouncy(duration:extraBounce:)

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func bouncy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.3.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Property

# smooth

A smooth spring animation with a predefined duration and no bounce.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var smooth: Animation { get }

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Method

# smooth(duration:extraBounce:)

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func smooth(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Property

# snappy

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var snappy: Animation { get }

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Method

# snappy(duration:extraBounce:)

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func snappy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.15.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

Type Property

# spring

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var spring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

### Customizing spring animations

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# spring(_:blendDuration:)

A persistent spring animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func spring(
        _ spring: Spring,
        blendDuration: TimeInterval = 0.0
    ) -> Animation

## Discussion

When mixed with other `spring()` or `interactiveSpring()` animations on the
same property, each animation will be replaced by their successor, preserving
velocity from one animation to the next. Optionally blends the duration values
between springs over a time period.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# spring(duration:bounce:blendDuration:)

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func spring(
        duration: TimeInterval = 0.5,
        bounce: Double = 0.0,
        blendDuration: Double = 0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`bounce`

    

How bouncy the spring should be. A value of 0 indicates no bounces (a
critically damped spring), positive values indicate increasing amounts of
bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and
negative values indicate overdamped springs with a minimum value of -1.0.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## Return Value

a spring animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# spring(response:dampingFraction:blendDuration:)

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func spring(
        response: Double = 0.5,
        dampingFraction: Double = 0.825,
        blendDuration: TimeInterval = 0
    ) -> Animation

##  Parameters

`response`

    

The stiffness of the spring, defined as an approximate duration in seconds. A
value of zero requests an infinitely-stiff spring, suitable for driving
interactive animations.

`dampingFraction`

    

The amount of drag applied to the value being animated, as a fraction of an
estimate of amount needed to produce critical damping.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the response
value of the spring.

## Return Value

a spring animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Property

# interactiveSpring

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var interactiveSpring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# interactiveSpring(response:dampingFraction:blendDuration:)

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interactiveSpring(
        response: Double = 0.15,
        dampingFraction: Double = 0.86,
        blendDuration: TimeInterval = 0.25
    ) -> Animation

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Property

# interpolatingSpring

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var interpolatingSpring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# interpolatingSpring(_:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        _ spring: Spring,
        initialVelocity: Double = 0.0
    ) -> Animation

## Discussion

These vales are used to interpolate within the `[from, to]` range of the
animated property. Preserves velocity across overlapping animations by adding
the effects of each animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# interpolatingSpring(duration:bounce:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        duration: TimeInterval = 0.5,
        bounce: Double = 0.0,
        initialVelocity: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`bounce`

    

How bouncy the spring should be. A value of 0 indicates no bounces (a
critically damped spring), positive values indicate increasing amounts of
bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and
negative values indicate overdamped springs with a minimum value of -1.0.

`initialVelocity`

    

the initial velocity of the spring, as a value in the range [0, 1]
representing the magnitude of the value being animated.

## Return Value

a spring animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# interpolatingSpring(mass:stiffness:damping:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        mass: Double = 1.0,
        stiffness: Double,
        damping: Double,
        initialVelocity: Double = 0.0
    ) -> Animation

##  Parameters

`mass`

    

The mass of the object attached to the spring.

`stiffness`

    

The stiffness of the spring.

`damping`

    

The spring damping value.

`initialVelocity`

    

the initial velocity of the spring, as a value in the range [0, 1]
representing the magnitude of the value being animated.

## Return Value

a spring animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Initializer

# init(_:)

Create an `Animation` that contains the specified custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<A>(_ base: A) where A : CustomAnimation

## See Also

### Creating custom animations

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

Type Method

# timingCurve(_:duration:)

Creates a new animation with speed controlled by the given curve.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func timingCurve(
        _ curve: UnitCurve,
        duration: TimeInterval
    ) -> Animation

##  Parameters

`timingCurve`

    

A curve that describes the speed of the animation over its duration.

`duration`

    

The duration of the animation, in seconds.

## See Also

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

Type Method

# timingCurve(_:_:_:_:duration:)

An animation created from a cubic Bézier timing curve.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func timingCurve(
        _ p1x: Double,
        _ p1y: Double,
        _ p2x: Double,
        _ p2y: Double,
        duration: TimeInterval = 0.35
    ) -> Animation

##  Parameters

`p1x`

    

The x-coordinate of the first control point of the cubic Bézier curve.

`p1y`

    

The y-coordinate of the first control point of the cubic Bézier curve.

`p2x`

    

The x-coordinate of the second control point of the cubic Bézier curve.

`p2y`

    

The y-coordinate of the second control point of the cubic Bézier curve.

`duration`

    

The length of time, expressed in seconds, the animation takes to complete.

## Return Value

A cubic Bézier timing curve animation.

## Discussion

Use this method to create a timing curve based on the control points of a
cubic Bézier curve. A cubic Bézier timing curve consists of a line whose
starting point is `(0, 0)` and whose end point is `(1, 1)`. Two additional
control points, `(p1x, p1y)` and `(p2x, p2y)`, define the shape of the curve.

The slope of the line defines the speed of the animation at that point in
time. A steep slopes causes the animation to appear to run faster, while a
shallower slope appears to run slower. The following illustration shows a
timing curve where the animation starts and finishes fast, but appears slower
through the middle section of the animation.

The following code uses the timing curve from the previous illustration to
animate a `Circle` as its size changes.

Play

## See Also

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

Instance Method

# delay(_:)

Delays the start of the animation by the specified number of seconds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func delay(_ delay: TimeInterval) -> Animation

##  Parameters

`delay`

    

The number of seconds to delay the start of the animation.

## Return Value

An animation with a delayed start.

## Discussion

Use this method to delay the start of an animation. For example, the following
code animates the height change of two capsules. Animation of the first
`Capsule` begins immediately. However, animation of the second one doesn’t
begin until a half second later.

Play

## See Also

### Configuring an animation

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# repeatCount(_:autoreverses:)

Repeats the animation for a specific number of times.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func repeatCount(
        _ repeatCount: Int,
        autoreverses: Bool = true
    ) -> Animation

##  Parameters

`repeatCount`

    

The number of times that the animation repeats. Each repeated sequence starts
at the beginning when `autoreverse` is `false`.

`autoreverses`

    

A Boolean value that indicates whether the animation sequence plays in reverse
after playing forward. Autoreverse counts towards the `repeatCount`. For
instance, a `repeatCount` of one plays the animation forward once, but it
doesn’t play in reverse even if `autoreverse` is `true`. When `autoreverse` is
`true` and `repeatCount` is `2`, the animation moves forward, then reverses,
then stops.

## Return Value

An animation that repeats for specific number of times.

## Discussion

Use this method to repeat the animation a specific number of times. For
example, in the following code, the animation moves a truck from one edge of
the view to the other edge. It repeats this animation three times.

Play

The first time the animation runs, the truck moves from the leading edge to
the trailing edge of the view. The second time the animation runs, the truck
moves from the trailing edge to the leading edge because `autoreverse` is
`true`. If `autoreverse` were `false`, the truck would jump back to leading
edge before moving to the trailing edge. The third time the animation runs,
the truck moves from the leading to the trailing edge of the view.

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# repeatForever(autoreverses:)

Repeats the animation for the lifespan of the view containing the animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func repeatForever(autoreverses: Bool = true) -> Animation

##  Parameters

`autoreverses`

    

A Boolean value that indicates whether the animation sequence plays in reverse
after playing forward.

## Return Value

An animation that continuously repeats.

## Discussion

Use this method to repeat the animation until the instance of the view no
longer exists, or the view’s explicit or structural identity changes. For
example, the following code continuously rotates a gear symbol for the
lifespan of the view.

Play

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# speed(_:)

Changes the duration of an animation by adjusting its speed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func speed(_ speed: Double) -> Animation

##  Parameters

`speed`

    

The speed at which SwiftUI performs the animation.

## Return Value

An animation with the adjusted speed.

## Discussion

Setting the speed of an animation changes the duration of the animation by a
factor of `speed`. A higher speed value causes a faster animation sequence due
to a shorter duration. For example, a one-second animation with a speed of
`2.0` completes in half the time (half a second).

Play

Setting `speed` to a lower number slows the animation, extending its duration.
For example, a one-second animation with a speed of `0.25` takes four seconds
to complete.

Play

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

Instance Property

# base

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var base: any CustomAnimation { get }

Instance Method

# animate(value:time:context:)

Calculates the current value of the animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animate<V>(
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> V? where V : VectorArithmetic

## Return Value

The current value of the animation, or `nil` if the animation has finished.

Instance Method

# logicallyComplete(after:)

Causes the animation to report logical completion after the specified
duration, if it has not already logically completed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func logicallyComplete(after duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The duration after which the animation should report that it is logically
complete.

## Return Value

An animation that reports logical completion after the given duration.

## Discussion

Note that the indicated duration will not cause the animation to continue
running after the base animation has fully completed.

If the animation is removed before the given duration is reached, logical
completion will be reported immediately.

Instance Method

# shouldMerge(previous:value:time:context:)

Returns a Boolean value that indicates whether the current animation should
merge with a previous animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func shouldMerge<V>(
        previous: Animation,
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> Bool where V : VectorArithmetic

Instance Method

# velocity(value:time:context:)

Calculates the current velocity of the animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity<V>(
        value: V,
        time: TimeInterval,
        context: AnimationContext<V>
    ) -> V? where V : VectorArithmetic

## Return Value

The current velocity of the animation, or `nil` if the the velocity isn’t
available.

Type Method

# interactiveSpring(duration:extraBounce:blendDuration:)

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interactiveSpring(
        duration: TimeInterval = 0.15,
        extraBounce: Double = 0.0,
        blendDuration: TimeInterval = 0.25
    ) -> Animation



# AnyView

Initializer

# init(_:)

Create an instance that type-erases `view`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(_ view: V) where V : View

## See Also

### Creating a view

`init<V>(erasing: V)`

Initializer

# init(erasing:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(erasing view: V) where V : View

## See Also

### Creating a view

`init<V>(V)`

Create an instance that type-erases `view`.



# Accessible descriptions

Enumeration

# AccessibilityLabeledPairRole

The role of an accessibility element in a label / content pair.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    enum AccessibilityLabeledPairRole

## Topics

### Getting roles

`case content`

This element represents the content part of the label / content pair.

`case label`

This element represents the label part of the label / content pair.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Applying labels

`func accessibilityLabel<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID,
in: Namespace.ID) -> some View`

Pairs an accessibility element representing a label with the element for the
matching content.

Enumeration

# AccessibilityHeadingLevel

The hierarchy of a heading in relation other headings.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum AccessibilityHeadingLevel

## Overview

Assistive technologies can use this to improve a users navigation through
multiple headings. When users navigate through top level headings they expect
the content for each heading to be unrelated.

For example, you can categorize a list of available products into sections,
like Fruits and Vegetables. With only top level headings, this list requires
no heading hierarchy, and you use the `AccessibilityHeadingLevel.unspecified`
heading level. On the other hand, if sections contain subsections, like if the
Fruits section has subsections for varieties of Apples, Pears, and so on, you
apply the `AccessibilityHeadingLevel.h1` level to Fruits and Vegetables, and
the `AccessibilityHeadingLevel.h2` level to Apples and Pears.

Except for `AccessibilityHeadingLevel.h1`, be sure to precede all leveled
headings by another heading with a level that’s one less.

## Topics

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Describing content

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

`struct AccessibilityTextContentType`

Textual context that assistive technologies can use to improve the
presentation of spoken text.

Structure

# AccessibilityTextContentType

Textual context that assistive technologies can use to improve the
presentation of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityTextContentType

## Overview

Use an `AccessibilityTextContentType` value when setting the accessibility
text content type of a view using the `accessibilityTextContentType(_:)`
modifier.

## Topics

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Describing content

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

`enum AccessibilityHeadingLevel`

The hierarchy of a heading in relation other headings.

Protocol

# AXChartDescriptorRepresentable

A type to generate an `AXChartDescriptor` object that you use to provide
information about a chart and its data for an accessible experience in
VoiceOver or other assistive technologies.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol AXChartDescriptorRepresentable

## Overview

Note that you may use the `@Environment` property wrapper inside the
implementation of your `AXChartDescriptorRepresentable`, in which case you
should implement `updateChartDescriptor`, which will be called when the
`Environment` changes.

For example, to provide accessibility for a view that represents a chart, you
would first declare your chart descriptor representable type:

Then, provide an instance of your `AXChartDescriptorRepresentable` type to
your view using the `accessibilityChartDescriptor` modifier:

## Topics

### Managing a descriptor

`func makeChartDescriptor() -> AXChartDescriptor`

Create the `AXChartDescriptor` for this view, and return it.

**Required**

` func updateChartDescriptor(AXChartDescriptor)`

Update the existing `AXChartDescriptor` for your view, based on changes in
your view or in the `Environment`.

**Required** Default implementation provided.

## See Also

### Describing charts

`func accessibilityChartDescriptor<R>(R) -> some View`

Adds a descriptor to a View that represents a chart to make the chart’s
contents accessible to all users.

Structure

# AccessibilityCustomContentKey

Key used to specify the identifier and label associated with an entry of
additional accessibility information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityCustomContentKey

## Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this
value as a parameter in order to simplify clearing or replacing entries of
additional information that are manipulated from multiple places in your code.

## Topics

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Adding custom descriptions

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

Structure

# AccessibilityTraits

A set of accessibility traits that describe how an element behaves.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityTraits

## Topics

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Assigning traits to content

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

`func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Removes the given traits from this view.

Instance Method

# speechAdjustedPitch(_:)

Raises or lowers the pitch of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAdjustedPitch(_ value: Double) -> some View
    

##  Parameters

`value`

    

The amount to raise or lower the pitch. Values between `-1` and `0` result in
a lower pitch while values between `0` and `1` result in a higher pitch. The
method clamps values to the range `-1` to `1`.

## Discussion

Use this modifier when you want to change the pitch of spoken text. The value
indicates how much higher or lower to change the pitch.

## See Also

### Configuring VoiceOver

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAlwaysIncludesPunctuation(_:)

Sets whether VoiceOver should always speak all punctuation in the text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that you set to `true` if VoiceOver should speak all
punctuation in the text. Defaults to `true`.

## Discussion

Use this modifier to control whether the system speaks punctuation characters
in the text. You might use this for code or other text where the punctuation
is relevant, or where you want VoiceOver to speak a verbatim transcription of
the text you provide. For example, given the text:

VoiceOver would speak “All the world apostrophe s a stage comma and all the
men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAnnouncementsQueued(_:)

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAnnouncementsQueued(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that determines if VoiceOver speaks changes to text
immediately or enqueues them behind existing speech. Defaults to `true`.

## Discussion

Use this modifier when you want affect the order in which the accessibility
system delivers spoken text. Announcements can occur automatically when the
label or value of an accessibility element changes.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechSpellsOutCharacters(_:)

Sets whether VoiceOver should speak the contents of the text view character by
character.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechSpellsOutCharacters(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that when `true` indicates VoiceOver should speak text as
individual characters. Defaults to `true`.

## Discussion

Use this modifier when you want VoiceOver to speak text as individual letters,
character by character. This is important for text that is not meant to be
spoken together, like:

  * An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.

  * A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.



# AppStorage

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a string user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == String

##  Parameters

`wrappedValue`

    

The default value if a string value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value : RawRepresentable, Value.RawValue == Int

##  Parameters

`wrappedValue`

    

The default value if an integer value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

A common usage is with enumerations:

enum MyEnum: Int { case a case b case c } struct MyView: View {
@AppStorage(“MyEnumValue”) private var value = MyEnum.a var body: some View {
… } }

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a user default as data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Data

##  Parameters

`wrappedValue`

    

The default value if a data value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Avoid storing large data blobs in user defaults, such as image data, as it can
negatively affect performance of your app. On tvOS, a
`NSUserDefaultsSizeLimitExceededNotification` notification is posted if the
total user default size reaches 512kB.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to an integer user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Int

##  Parameters

`wrappedValue`

    

The default value if an integer value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value : RawRepresentable, Value.RawValue == String

##  Parameters

`wrappedValue`

    

The default value if a string value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

A common usage is with enumerations:

enum MyEnum: String { case a case b case c } struct MyView: View {
@AppStorage(“MyEnumValue”) private var value = MyEnum.a var body: some View {
… } }

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a url user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == URL

##  Parameters

`wrappedValue`

    

The default value if a url value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a double user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Double

##  Parameters

`wrappedValue`

    

The default value if a double value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a boolean user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Bool

##  Parameters

`wrappedValue`

    

The default value if a boolean value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can save and restore table column state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<RowValue>(
        wrappedValue: Value = TableColumnCustomization<RowValue>(),
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable

##  Parameters

`wrappedValue`

    

The default value if table column state is not available for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Table column state is typically not bound from a table directly to
`AppStorage`, but instead indirecting through `State` or `SceneStorage`, and
using the app storage value as its initial value kept up to date on changes to
the direct backing.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

Initializer

# init(wrappedValue:_:store:)

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        wrappedValue: Value,
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == PersistentIdentifier

##  Parameters

`wrappedValue`

    

The default value if a data value is not specified for the given key.

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Use this property wrapper when the wrapped persistent identifier is known to
always be non-optional. For storing optional persistent identifiers, use
`AppStorage/init(_:store:)` instead.

## See Also

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional integer user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Int?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional string user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == String?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional double user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Double?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<R>(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == R?, R : RawRepresentable, R.RawValue == Int

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<R>(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == R?, R : RawRepresentable, R.RawValue == String

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional data user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Data?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional boolean user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == Bool?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional URL user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == URL?

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

Initializer

# init(_:store:)

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ key: String,
        store: UserDefaults? = nil
    ) where Value == PersistentIdentifier?

##  Parameters

`key`

    

The key to read and write the value to in the user defaults store.

`store`

    

The user defaults store to read and write to. A value of `nil` will use the
user default store from the environment.

## Discussion

Defaults to `nil` if there is no restored value.

## See Also

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

Instance Property

# wrappedValue

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## See Also

### Getting the value

`var projectedValue: Binding<Value>`

Instance Property

# projectedValue

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value> { get }

## See Also

### Getting the value

`var wrappedValue: Value`



# AngularGradient

Initializer

# init(gradient:center:angle:)

Creates a conic gradient that completes a full turn.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        gradient: Gradient,
        center: UnitPoint,
        angle: Angle = .zero
    )

## See Also

### Creating a full rotation angular gradient

`init(colors: [Color], center: UnitPoint, angle: Angle)`

Creates a conic gradient from a collection of colors that completes a full
turn.

`init(stops: [Gradient.Stop], center: UnitPoint, angle: Angle)`

Creates a conic gradient from a collection of color stops that completes a
full turn.

Initializer

# init(colors:center:angle:)

Creates a conic gradient from a collection of colors that completes a full
turn.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        colors: [Color],
        center: UnitPoint,
        angle: Angle = .zero
    )

## See Also

### Creating a full rotation angular gradient

`init(gradient: Gradient, center: UnitPoint, angle: Angle)`

Creates a conic gradient that completes a full turn.

`init(stops: [Gradient.Stop], center: UnitPoint, angle: Angle)`

Creates a conic gradient from a collection of color stops that completes a
full turn.

Initializer

# init(stops:center:angle:)

Creates a conic gradient from a collection of color stops that completes a
full turn.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        stops: [Gradient.Stop],
        center: UnitPoint,
        angle: Angle = .zero
    )

## See Also

### Creating a full rotation angular gradient

`init(gradient: Gradient, center: UnitPoint, angle: Angle)`

Creates a conic gradient that completes a full turn.

`init(colors: [Color], center: UnitPoint, angle: Angle)`

Creates a conic gradient from a collection of colors that completes a full
turn.

Initializer

# init(gradient:center:startAngle:endAngle:)

Creates an angular gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        gradient: Gradient,
        center: UnitPoint,
        startAngle: Angle = .zero,
        endAngle: Angle = .zero
    )

## See Also

### Creating a partial rotation angular gradient

`init(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle)`

Creates an angular gradient from a collection of colors.

`init(stops: [Gradient.Stop], center: UnitPoint, startAngle: Angle, endAngle:
Angle)`

Creates an angular gradient from a collection of color stops.

Initializer

# init(colors:center:startAngle:endAngle:)

Creates an angular gradient from a collection of colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        colors: [Color],
        center: UnitPoint,
        startAngle: Angle,
        endAngle: Angle
    )

## See Also

### Creating a partial rotation angular gradient

`init(gradient: Gradient, center: UnitPoint, startAngle: Angle, endAngle:
Angle)`

Creates an angular gradient.

`init(stops: [Gradient.Stop], center: UnitPoint, startAngle: Angle, endAngle:
Angle)`

Creates an angular gradient from a collection of color stops.

Initializer

# init(stops:center:startAngle:endAngle:)

Creates an angular gradient from a collection of color stops.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        stops: [Gradient.Stop],
        center: UnitPoint,
        startAngle: Angle,
        endAngle: Angle
    )

## See Also

### Creating a partial rotation angular gradient

`init(gradient: Gradient, center: UnitPoint, startAngle: Angle, endAngle:
Angle)`

Creates an angular gradient.

`init(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle)`

Creates an angular gradient from a collection of colors.



# Axis.Set

Type Property

# horizontal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let horizontal: Axis.Set

## See Also

### Getting axis sets

`static let vertical: Axis.Set`

Type Property

# vertical

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let vertical: Axis.Set

## See Also

### Getting axis sets

`static let horizontal: Axis.Set`



# AnyLayout

Initializer

# init(_:)

Creates a type-erased value that wraps the specified layout.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<L>(_ layout: L) where L : Layout

## Discussion

You can switch between type-erased layouts without losing the state of the
subviews.



# AccessoryBarButtonStyle

Initializer

# init()

Creates an accessory toolbar style

macOS 14.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

macOS 14.0+  visionOS 1.0+

    
    
    func makeBody(configuration: AccessoryBarButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



# AccessibilityFocusState

Initializer

# init()

Creates a new accessibility focus state of the type you provide.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>() where Value == T?, T : Hashable

## See Also

### Creating a focus state

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init()

Creates a new accessibility focus state for a Boolean value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init() where Value == Bool

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init(for:)

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>(for technologies: AccessibilityTechnologies) where Value == T?, T : Hashable

##  Parameters

`technologies`

    

One or more of the available `AccessibilityTechnologies`.

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init(for:)

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(for technologies: AccessibilityTechnologies) where Value == Bool

##  Parameters

`technologies`

    

One of the available `AccessibilityTechnologies`.

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

Instance Property

# projectedValue

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: AccessibilityFocusState<Value>.Binding { get }

## Discussion

Use `projectedValue` in conjunction with `accessibilityFocused(_:equals:)` to
establish bindings between view content and accessibility focus placement.

## See Also

### Getting the state

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

`struct Binding`

Instance Property

# wrappedValue

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

When focus is not in any view that is bound to this state, the wrapped value
will be `nil` (for optional-typed state) or `false` (for `Bool`\- typed
state).

## See Also

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`struct Binding`

Structure

# AccessibilityFocusState.Binding

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct Binding

## Topics

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

The currently focused element.

`var wrappedValue: Value`

The underlying value referenced by the bound property.

## See Also

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.



# AsymmetricTransition

Initializer

# init(insertion:removal:)

Creates a composite `Transition` that uses a different transition for
insertion versus removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        insertion: Insertion,
        removal: Removal
    )

Instance Property

# insertion

The `Transition` defining the insertion phase of `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var insertion: Insertion

## See Also

### Getting transition properties

`var removal: Removal`

The `Transition` defining the removal phase of `self`.

Instance Property

# removal

The `Transition` defining the removal phase of `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var removal: Removal

## See Also

### Getting transition properties

`var insertion: Insertion`

The `Transition` defining the insertion phase of `self`.



# AutomaticLabeledContentStyle

Initializer

# init()

Creates an automatic labeled content style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()



# AlternatingRowBackgroundBehavior

Type Property

# automatic

The automatic alternating row background behavior.

macOS 14.0+

    
    
    static let automatic: AlternatingRowBackgroundBehavior

## Discussion

This defers to default component behavior for alternating row backgrounds.
Some components, such as `Table` on macOS, will default to having alternating
row backgrounds; while List does not.

## See Also

### Getting alternating row background behavior

`static let enabled: AlternatingRowBackgroundBehavior`

Alternating rows will be enabled for applicable views.

`static let disabled: AlternatingRowBackgroundBehavior`

Alternating rows will be disabled for applicable views.

Type Property

# enabled

Alternating rows will be enabled for applicable views.

macOS 14.0+

    
    
    static let enabled: AlternatingRowBackgroundBehavior

## See Also

### Getting alternating row background behavior

`static let automatic: AlternatingRowBackgroundBehavior`

The automatic alternating row background behavior.

`static let disabled: AlternatingRowBackgroundBehavior`

Alternating rows will be disabled for applicable views.

Type Property

# disabled

Alternating rows will be disabled for applicable views.

macOS 14.0+

    
    
    static let disabled: AlternatingRowBackgroundBehavior

## See Also

### Getting alternating row background behavior

`static let automatic: AlternatingRowBackgroundBehavior`

The automatic alternating row background behavior.

`static let enabled: AlternatingRowBackgroundBehavior`

Alternating rows will be enabled for applicable views.



# Alert

Initializer

# init(title:message:dismissButton:)

Creates an alert with one button.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        dismissButton: Alert.Button? = nil
    )

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`dismissButton`

    

The button that dismisses the alert.

## See Also

### Creating an alert

`init(title: Text, message: Text?, primaryButton: Alert.Button,
secondaryButton: Alert.Button)`

Creates an alert with two buttons.

Deprecated

`static func sideBySideButtons(title: Text, message: Text?, primaryButton:
Alert.Button, secondaryButton: Alert.Button) -> Alert`

Creates a side by side button alert.

Deprecated

Initializer

# init(title:message:primaryButton:secondaryButton:)

Creates an alert with two buttons.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        primaryButton: Alert.Button,
        secondaryButton: Alert.Button
    )

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`primaryButton`

    

The first button to show in the alert.

`secondaryButton`

    

The second button to show in the alert.

## Discussion

The system determines the visual ordering of the buttons.

## See Also

### Creating an alert

`init(title: Text, message: Text?, dismissButton: Alert.Button?)`

Creates an alert with one button.

Deprecated

`static func sideBySideButtons(title: Text, message: Text?, primaryButton:
Alert.Button, secondaryButton: Alert.Button) -> Alert`

Creates a side by side button alert.

Deprecated

Type Method

# sideBySideButtons(title:message:primaryButton:secondaryButton:)

Creates a side by side button alert.

watchOS 6.0–10.4  Deprecated

    
    
    static func sideBySideButtons(
        title: Text,
        message: Text? = nil,
        primaryButton: Alert.Button,
        secondaryButton: Alert.Button
    ) -> Alert

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`primaryButton`

    

The first button to show in the alert.

`secondaryButton`

    

The second button to show in the alert.

## Discussion

The system determines the visual ordering of the buttons.

## See Also

### Creating an alert

`init(title: Text, message: Text?, dismissButton: Alert.Button?)`

Creates an alert with one button.

Deprecated

`init(title: Text, message: Text?, primaryButton: Alert.Button,
secondaryButton: Alert.Button)`

Creates an alert with two buttons.

Deprecated

Structure

# Alert.Button

A button that represents an operation of an alert presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct Button

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

## Topics

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.



# AccessibilityTechnologies

Type Property

# switchControl

The value that represents a Switch Control, allowing the use of the entire
system using controller buttons, a breath-controlled switch or similar
hardware.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var switchControl: AccessibilityTechnologies

## See Also

### Getting technology types

`static var voiceOver: AccessibilityTechnologies`

The value that represents the VoiceOver screen reader, allowing use of the
system without seeing the screen visually.

Type Property

# voiceOver

The value that represents the VoiceOver screen reader, allowing use of the
system without seeing the screen visually.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var voiceOver: AccessibilityTechnologies

## See Also

### Getting technology types

`static var switchControl: AccessibilityTechnologies`

The value that represents a Switch Control, allowing the use of the entire
system using controller buttons, a breath-controlled switch or similar
hardware.

Initializer

# init()

Creates a new accessibility technologies structure with an empy accessibility
technology set.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init()



# AccessibilityHeadingLevel

Case

# AccessibilityHeadingLevel.h1

Level 1 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h1

## See Also

### Getting the heading level

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.h2

Level 2 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h2

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.h3

Level 3 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h3

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.h4

Level 4 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h4

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.h5

Level 5 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h5

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.h6

Level 6 heading.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case h6

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case unspecified`

A heading without a hierarchy.

Case

# AccessibilityHeadingLevel.unspecified

A heading without a hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case unspecified

## See Also

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.



# AXChartDescriptorRepresentable

Instance Method

# makeChartDescriptor()

Create the `AXChartDescriptor` for this view, and return it.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func makeChartDescriptor() -> AXChartDescriptor

**Required**

## Discussion

This will be called once per identity of your `View`. It will not be run again
unless the identity of your `View` changes. If you need to update the
`AXChartDescriptor` based on changes in your `View`, or in the `Environment`,
implement `updateChartDescriptor`. This method will only be called if / when
accessibility needs the `AXChartDescriptor` of your view, for VoiceOver.

## See Also

### Managing a descriptor

`func updateChartDescriptor(AXChartDescriptor)`

Update the existing `AXChartDescriptor` for your view, based on changes in
your view or in the `Environment`.

**Required** Default implementation provided.

Instance Method

# updateChartDescriptor(_:)

Update the existing `AXChartDescriptor` for your view, based on changes in
your view or in the `Environment`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func updateChartDescriptor(_ descriptor: AXChartDescriptor)

**Required** Default implementation provided.

## Discussion

This will be called as needed, when accessibility needs your
`AXChartDescriptor` for VoiceOver. It will only be called if the inputs to
your views, or a relevant part of the `Environment`, have changed.

## Default Implementations

### AXChartDescriptorRepresentable Implementations

`func updateChartDescriptor(AXChartDescriptor)`

Update the existing `AXChartDescriptor` for your view, based on changes in
your view or in the `Environment`.

## See Also

### Managing a descriptor

`func makeChartDescriptor() -> AXChartDescriptor`

Create the `AXChartDescriptor` for this view, and return it.

**Required**



# AutomaticTextEditorStyle

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()



# AccessibilityZoomGestureAction.Direction

Case

# AccessibilityZoomGestureAction.Direction.zoomIn

The gesture direction that represents zooming in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    case zoomIn

## See Also

### Getting the direction

`case zoomOut`

The gesture direction that represents zooming out.

Case

# AccessibilityZoomGestureAction.Direction.zoomOut

The gesture direction that represents zooming out.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    case zoomOut

## See Also

### Getting the direction

`case zoomIn`

The gesture direction that represents zooming in.



# Accessibility fundamentals

Structure

# AccessibilityChildBehavior

Defines the behavior for the child elements of the new parent element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityChildBehavior

## Topics

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Creating accessible elements

`func accessibilityElement(children: AccessibilityChildBehavior) -> some View`

Creates a new accessibility element, or modifies the
`AccessibilityChildBehavior` of the existing accessibility element.

`func accessibilityChildren<V>(children: () -> V) -> some View`

Replaces the existing accessibility element’s children with one or more new
synthetic accessibility elements.

`func accessibilityRepresentation<V>(representation: () -> V) -> some View`

Replaces one or more accessibility elements for this view with new
accessibility elements.

Structure

# AccessibilityTechnologies

Accessibility technologies available to the system.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityTechnologies

## Topics

### Getting technology types

`static var switchControl: AccessibilityTechnologies`

The value that represents a Switch Control, allowing the use of the entire
system using controller buttons, a breath-controlled switch or similar
hardware.

`static var voiceOver: AccessibilityTechnologies`

The value that represents the VoiceOver screen reader, allowing use of the
system without seeing the screen visually.

### Creating a technology type

`init()`

Creates a new accessibility technologies structure with an empy accessibility
technology set.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Supporting types

`struct AccessibilityAttachmentModifier`

A view modifier that adds accessibility properties to the view

Structure

# AccessibilityAttachmentModifier

A view modifier that adds accessibility properties to the view

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityAttachmentModifier

## Relationships

### Conforms To

  * `ViewModifier`

## See Also

### Supporting types

`struct AccessibilityTechnologies`

Accessibility technologies available to the system.



# AccessibilityFocusState.Binding

Instance Property

# projectedValue

The currently focused element.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: AccessibilityFocusState<Value>.Binding { get }

## See Also

### Getting the state

`var wrappedValue: Value`

The underlying value referenced by the bound property.

Instance Property

# wrappedValue

The underlying value referenced by the bound property.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## See Also

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

The currently focused element.



# AnyShapeStyle

Initializer

# init(_:)

Create an instance from `style`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S>(_ style: S) where S : ShapeStyle



# AccessibilityZoomGestureAction

Instance Property

# direction

The zoom gesture’s direction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let direction: AccessibilityZoomGestureAction.Direction

## See Also

### Getting the action’s direction

`enum Direction`

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

Enumeration

# AccessibilityZoomGestureAction.Direction

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    enum Direction

## Topics

### Getting the direction

`case zoomIn`

The gesture direction that represents zooming in.

`case zoomOut`

The gesture direction that represents zooming out.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the action’s direction

`let direction: AccessibilityZoomGestureAction.Direction`

The zoom gesture’s direction.

Instance Property

# location

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let location: UnitPoint

## See Also

### Getting location information

`let point: CGPoint`

The zoom gesture’s activation point within the window’s coordinate space.

Instance Property

# point

The zoom gesture’s activation point within the window’s coordinate space.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let point: CGPoint

## See Also

### Getting location information

`let location: UnitPoint`

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.



# AccessibilityTraits

Type Property

# allowsDirectInteraction

The accessibility element allows direct touch interaction for VoiceOver users.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let allowsDirectInteraction: AccessibilityTraits

## See Also

### Getting traits

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# causesPageTurn

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let causesPageTurn: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isButton

The accessibility element is a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isButton: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isHeader

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isHeader: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isImage

The accessibility element is an image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isImage: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isKeyboardKey

The accessibility element behaves as a keyboard key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isKeyboardKey: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isLink

The accessibility element is a link.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isLink: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isModal

The accessibility element is modal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isModal: AccessibilityTraits

## Discussion

Use this trait to restrict which accessibility elements an assistive
technology can navigate. When a modal accessibility element is visible,
sibling accessibility elements that are not modal are ignored.

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isSearchField

The accessibility element is a search field.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isSearchField: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isSelected

The accessibility element is currently selected.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isSelected: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isStaticText

The accessibility element is a static text that cannot be modified by the
user.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isStaticText: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isSummaryElement

The accessibility element provides summary information when the application
starts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let isSummaryElement: AccessibilityTraits

## Discussion

Use this trait to characterize an accessibility element that provides a
summary of current conditions, settings, or state, like the temperature in the
Weather app.

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# isToggle

The accessibility element is a toggle.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let isToggle: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# playsSound

The accessibility element plays its own sound when activated.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let playsSound: AccessibilityTraits

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# startsMediaSession

The accessibility element starts a media session when it is activated.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let startsMediaSession: AccessibilityTraits

## Discussion

Use this trait to silence the audio output of an assistive technology, such as
VoiceOver, during a media session that should not be interrupted. For example,
you might use this trait to silence VoiceOver speech while the user is
recording audio.

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

Type Property

# updatesFrequently

The accessibility element frequently updates its label or value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let updatesFrequently: AccessibilityTraits

## Discussion

Use this trait when you want an assistive technology to poll for changes when
it needs updated information. For example, you might use this trait to
characterize the readout of a stopwatch.

## See Also

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.



# Accessible navigation

Protocol

# AccessibilityRotorContent

Content within an accessibility rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol AccessibilityRotorContent

## Overview

Generally generated from control flow constructs like `ForEach` and `if`, and
`AccessibilityRotorEntry`.

## Topics

### Supporting types

`var body: Self.Body`

The internal content of this `AccessibilityRotorContent`.

**Required**

` associatedtype Body : AccessibilityRotorContent`

The type for the internal content of this `AccessibilityRotorContent`.

**Required**

## Relationships

### Conforming Types

  * `AccessibilityRotorEntry`

Conforms when `ID` conforms to `Hashable`.

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

  * `Group`

Conforms when `Content` conforms to `AccessibilityRotorContent`.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`struct AccessibilityRotorContentBuilder`

Result builder you use to generate rotor entry content.

`struct AccessibilityRotorEntry`

A struct representing an entry in an Accessibility Rotor.

Available when `ID` conforms to `Hashable`.

Structure

# AccessibilityRotorContentBuilder

Result builder you use to generate rotor entry content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct AccessibilityRotorContentBuilder

## Topics

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`protocol AccessibilityRotorContent`

Content within an accessibility rotor.

`struct AccessibilityRotorEntry`

A struct representing an entry in an Accessibility Rotor.

Structure

# AccessibilityRotorEntry

A struct representing an entry in an Accessibility Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityRotorEntry<ID> where ID : Hashable

## Overview

An Accessibility Rotor is a shortcut for Accessibility users to quickly
navigate to specific elements of the user interface, and optionally specific
ranges of text within those elements.

An entry in a Rotor may contain a label to identify the entry to the user, and
identifier used to determine which Accessibility element the Rotor entry
should navigate to, as well as an optional range used for entries that
navigate to a specific position in the text of their associated Accessibility
element. An entry can also specify a handler to be called before the entry is
navigated to, to do any manual work needed to bring the Accessibility element
on-screen.

In the following example, a Message application creates a Rotor allowing users
to navigate to specifically the messages originating from VIPs.

An entry may also be created using an optional namespace, for situations where
there are multiple Accessibility elements within a ForEach iteration or where
a `ScrollView` is not present. In this case, the `prepare` closure may be
needed in order to scroll the element into position using `ScrollViewReader`.
The same namespace should be passed to calls to
`accessibilityRotorEntry(id:in:)` to tag the Accessibility elements associated
with this entry.

In the following example, a Message application creates a Rotor allowing users
to navigate to specifically the messages originating from VIPs. The Rotor
entries are associated with the content text of the message, which is one of
the two views within the ForEach that generate Accessibility elements. That
view is tagged with `accessibilityRotorEntry(id:in:)` so that it can be found
by the `AccessibilityRotorEntry`, and `ScrollViewReader` is used with the
`prepare` closure to scroll it into position.

## Topics

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

## Relationships

### Conforms To

  * `AccessibilityRotorContent`

Conforms when `ID` conforms to `Hashable`.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`protocol AccessibilityRotorContent`

Content within an accessibility rotor.

Available when `ID` conforms to `Hashable`.

`struct AccessibilityRotorContentBuilder`

Result builder you use to generate rotor entry content.

Structure

# AccessibilitySystemRotor

Designates a Rotor that replaces one of the automatic, system-provided Rotors
with a developer-provided Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilitySystemRotor

## Topics

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

### Iterating through headings

`static var headings: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all headings.

`static func headings(level: AccessibilityHeadingLevel) ->
AccessibilitySystemRotor`

System Rotors allowing users to iterate through all headings, of various
heading levels.

### Iterating through links

`static var links: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all links.

`static func links(visited: Bool) -> AccessibilitySystemRotor`

System Rotors allowing users to iterate through links or visited links.

### Iterating through other elements

`static var images: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all images.

`static var landmarks: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all landmarks.

`static var lists: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all lists.

`static var tables: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all tables.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Replacing system rotors

`func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () ->
Content) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor(AccessibilitySystemRotor, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.
The Rotor will be attached to the current Accessibility element, and each
entry will go the specified range of that element.



# App extensions

Article

# Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

## Overview

Widgets display relevant, glanceable content that people can quickly access
for more details. Your app can provide a variety of widgets, letting people
focus on the information that’s most important to them.

A good way to get started with widgets and WidgetKit is by adding a _static_
widget to your app. A static widget doesn’t need any configuration by the
user. For example, a static widget might show a stock market summary, or the
next event on the user’s calendar. The _data_ the widget shows is dynamic, but
the _type_ of data it shows is fixed. Consider the information your app
presents, and choose something that people would find useful to see at a
glance on their device.

Widgets can display data in many sizes, from small watch complications or
Dynamic Island presentations, to extra large iPad and macOS widgets. The
example that follows below focuses on a single size widget, the small system
size, or `WidgetFamily.systemSmall`. The example widget displays the status of
a hypothetical game, such as player turn or the health level of a character.

You build widgets using SwiftUI. While there are similarities to how you
present views in your app, some aspects are unique to developing widgets. For
more information about using SwiftUI, see SwiftUI. However, not all SwiftUI
views work in widgets. For a list of the views that work in widgets, see
SwiftUI views for widgets.

### Add a widget target to your app

The Widget Extension template provides a starting point for creating your
widget. The template creates an extension target that contains a single
widget. Later, you can add additional widgets to the same extension to display
different types of information or to support additional widget sizes.

  1. Open your app project in Xcode and choose File > New > Target.

  2. From the Application Extension group, select Widget Extension, and then click Next.

  3. Enter the name of your extension.

  4. Deselect the Include Live Activity and Include Configuration App Intent checkboxes, if they’re selected.

  5. Click Finish.

Note

Live Activities use WidgetKit and share many aspects of their design and
implementation with the widgets in your app. If your app supports Live
Activities, consider implementing them at the same time you add your widgets.
For more information about Live Activities, see Displaying live data with Live
Activities.

The widget extension template provides an initial implementation that conforms
to the `Widget` protocol. The widget’s `body` property determines the type of
content that the widget presents. Static widgets use a `StaticConfiguration`
for the `body` property. Other types of widget configurations include:

  * `AppIntentConfiguration` that enables user customization, such as a weather widget that needs a zip or postal code for a city, or a package-tracking widget that needs a tracking number.

  * `ActivityConfiguration` to present live data, such as scores during a sporting event or a food delivery estimate.

For more information about these other widget configurations, see Making a
configurable widget and Displaying live data with Live Activities.

### Add configuration details

To configure a static widget, provide the following information:

`kind`

    

A string that identifies the widget. This is an identifier you choose, and
should be descriptive of what the widget represents.

`provider`

    

An object that conforms to `TimelineProvider` and produces a _timeline_ that
tells WidgetKit when to render the widget. A timeline is a sequence that
contains a custom `TimelineEntry` type you define. The entries in this
sequence identify the date when you want WidgetKit to update the widget’s
content and includes properties your widget’s view needs to render in the
custom type.

`content`

    

A closure that contains SwiftUI views. WidgetKit invokes this to render the
widget’s content, passing a `TimelineEntry` parameter from the provider.

Use modifiers to provide additional configuration details, including a display
name, a description, and the families the widget supports. The following code
shows a widget that provides general status for a game:

The widget’s provider generates a timeline for the widget, and includes the
game-status details in each entry. When the date of each timeline entry
arrives, WidgetKit invokes the `content` closure to display the widget’s
content. Finally, the modifiers specify the name and description shown in the
widget gallery, and the sizes that the widget supports.

Important

For an app’s widget to appear in the widget gallery, a person must launch the
app that contains the widget at least once after the app is installed.

Note the usage of the `@main` attribute on this widget. This attribute
indicates that the `GameStatusWidget` is the entry point for the widget
extension, implying that the extension contains a single widget. To support
multiple widgets, see the `WidgetBundle`.

### Provide timeline entries

The timeline provider you define generates a sequence of timeline entries.
Each specifies the date and time to update the widget’s content, and includes
the data your widget needs to render its view. The game-status widget might
define its timeline entry to include a string that represents the status of
the game, as follows:

WidgetKit calls `getTimeline(in:completion:)` to request a the timeline from
the provider. The timeline consists of one or more timeline entries and a
reload policy that informs WidgetKit when to request a subsequent timeline.

The following example shows how the game-status widget’s provider generates a
timeline that consists of a single entry with the current game status from the
server, and a reload policy to request a new timeline in 15 minutes:

In this example, if the widget didn’t have the current status from the server,
it could store a reference to the completion, perform an asynchronous request
to the server to fetch the game status, and call the completion when that
request completes.

For more information about generating timelines, see Keeping a widget up to
date. For more information about handling network, see Making network requests
in a widget extension.

### Generate a preview for the widget gallery

In order for people to be able to use your widget, it needs to be available in
the widget gallery. To show your widget in the widget gallery, WidgetKit asks
the provider for a _preview snapshot_ that displays generic data. WidgetKit
makes this request by calling the provider’s `getSnapshot(in:completion:)`
method with the `context` parameter’s `isPreview` property set to `true`.

In response, you need to create the preview snapshot quickly. If your widget
would normally need assets or information that takes time to generate or fetch
from a server, use sample data instead.

In the following code, the game-status widget’s provider implements the
snapshot method by showing the game status if it’s available, falling back to
an empty status if it doesn’t have the status from its server:

### Display content in your widget

Widgets define their content using a SwiftUI view, commonly by composing other
SwiftUI views. As shown in the Add configuration details section, the widget’s
configuration contains the closure that WidgetKit invokes to render the
widget’s content.

When people add your widget from the widget gallery, they choose the specific
family — for example, small or medium — from the ones your widget supports.
The widget’s content closure has to be capable of rendering each family the
widget supports. WidgetKit sets the corresponding family and additional
properties, such as the color scheme (light or dark), in the SwiftUI
environment.

In the game-status widget’s configuration shown above, the content closure
uses a `GameStatusView` to display the status. Because this widget only
supports the `.systemSmall` family, it uses a composed `GameTurnSummary`
SwiftUI view to display a summary of the game’s current status. For any other
family size, it shows the default view, which indicates that game status is
unavailable.

In your widget, as you add more supported families to the widget’s
configuration, you would add additional cases in the widget view’s `body`
property for each additional family.

Note

The view declares its body with `@ViewBuilder` because the type of view it
uses varies.

### Display a placeholder widget

A placeholder view is similar to a preview snapshot, but instead of showing
example data to let people see the type of data the widget displays, it shows
a generic visual representation with no specific content. When WidgetKit
renders your widget, it may need to render your content as a placeholder, for
example, while you load data in the background or if you tell the system that
your widget contains sensitive information.

### Hide sensitive content

Widgets and watch complications may show sensitive information and can be
highly visible, especially on devices with an Always-On display. When you
create your widget or watch complication, review its content and consider
hiding sensitive information.

To let people decide whether a widget should show sensitive data on a locked
device, mark views that contain sensitive information using the
`privacySensitive(_:)` modifier. In iOS, people can configure whether to show
sensitive data on the Lock Screen and during Always On. In Settings, they can
deactivate data access for Lock Screen widgets in the ALLOW ACCESS WHEN LOCKED
section of Settings > Face ID & Passcode. On Apple Watch, people can configure
whether to show sensitive data during Always On by Choosing Settings > Display
& Brightness > Always On > Hide Sensitive Complications. They can choose to
show redacted content for all or individual complications.

If a person chooses to hide privacy sensitive content, WidgetKit renders a
placeholder or redactions you configure. To configure redactions, implement
the `redacted(reason:)` callback, read out the `privacy` property, and provide
custom placeholder views. You can also choose to render a view as unredacted
with the `unredacted()` view modifier.

As an alternative to marking individual views as privacy sensitive, for
example, if your entire widget content is privacy sensitive, add the Data
Protection capability to your widget extension. Until a person unlocks their
device to match the privacy level you chose, WidgetKit displays placeholder
instead of the widget content. First, enable the Data Protection capability
for your widget extension in Xcode, then set the `Data Protection Entitlement`
entitlement to the value that fits the level of privacy you want to offer:

`NSFileProtectionComplete`

    

WidgetKit hides widget content when the device is locked. Additionally, iOS
widgets aren’t available as iPhone widgets on Mac.

`NSFileProtectionCompleteUnlessOpen`

    

WidgetKit hides widget content when the device is passcode locked.
Additionally, iOS widgets aren’t available as iPhone widgets on Mac.

If you choose the `NSFileProtectionCompleteUntilFirstUserAuthentication` or
`NSFileProtectionNone` protection level for your widget extension:

  * WidgetKit uses its default behavior and displays a placeholder until a person authenticates after they reboot their device.

  * iOS widgets are available as iPhone widgets on Mac.

### Add dynamic content to your widget

Widgets typically present read-only information and don’t generally support
interactive elements such as scrolling lists or text input. Starting with iOS
17 and macOS 14, widgets support some interactive elements and animations. For
details on adding interactivity to your widgets, see Adding interactivity to
widgets and Live Activities.

For a list of views that WidgetKit supports, see SwiftUI views for widgets.
WidgetKit ignores other views when it renders the widget’s’ content.

Although the display of a widget is based on a snapshot of your view, you can
use various SwiftUI views that continue to update while your widget is
visible. For more about providing dynamic content, see Keeping a widget up to
date.

### Respond to user interactions

When people interact with your widget, beyond interactive elements described
above, the system launches your app to handle the request. When the system
activates your app, navigate to the details that correspond to the widget’s
content. Your widget can specify a URL to inform the app what content to
display. To configure custom URLs in your widget:

  * For all widgets, add the `widgetURL(_:)` view modifier to a view in your widget’s view hierarchy. If the widget’s view hierarchy includes more than one `widgetURL` modifier, the behavior is undefined.

  * For widgets that use `WidgetFamily.systemMedium`, `WidgetFamily.systemLarge`, or `WidgetFamily.systemExtraLarge`, add one or more `Link` controls to your widget’s view hierarchy. You can use both `widgetURL` and `Link` controls. If the interaction targets a `Link` control, the system uses the URL in that control. For interactions anywhere else in the widget, the system uses the URL specified in the `widgetURL` view modifier.

For more details about adding links from your widgets to your app, see Linking
to specific app scenes from your widget or Live Activity.

### Preview widgets in Xcode

Xcode allows you to look at previews of your widgets without running your app
in Simulator or on a test device. The following example shows the preview code
from the Emoji Rangers widget of the Building Widgets Using WidgetKit and
SwiftUI sample code project. Note how it uses the `widgetFamily` environment
value to avoid manually specifying a name for each widget.

As you support more widget families in your widget, you can add more preview
views to see multiple sizes in a single preview.

### Expand your widget’s capabilities

To give people flexible access to your app’s content, you can support
additional families, add additional widget types, make your widgets user-
configurable, or add support for Live Activities if your app presents live
data. To explore a plan to support additional features, see Developing a
WidgetKit strategy.

To explore WidgetKit code for the first time, see the following sample code
projects:

  * Building Widgets Using WidgetKit and SwiftUI is the sample code project associated with the WWDC20 code-alongs Widgets Code-along, part 1: The adventure begins, Widgets Code-along, part 2: Alternate timelines, and Widgets Code-along, part 3: Advancing timelines, where you learn how to build your first widget.

  * Emoji Rangers: Supporting Live Activities, interactivity, and animations expands the Emoji Rangers sample code project to include Lock Screen widgets, Live Activities, interactivity, and animations.

  * Fruta: Building a Feature-Rich App with SwiftUI and Backyard Birds: Building an app with SwiftData and widgets are sample code projects that support widgets in addition to other technologies like App Clips and SwiftData.

### Create multiple widget extensions

You can include multiple widget types in your widget extension, although your
app can contain multiple extensions. For example, if some of your widgets use
location information and others don’t, keep the widgets that use location
information in a separate extension. This allows the system to prompt someone
for authorization to use location information only for the widgets from the
extension that uses location information. For details about bundling multiple
widgets in an extension, see `WidgetBundle`.

## See Also

### Widget creation

Supporting additional widget sizes

Offer widgets in additional contexts by adding support for various widget
sizes.

Creating accessory widgets and watch complications

Support accessory widgets that appear on the Lock Screen and as complications
on Apple Watch.

Migrating ClockKit complications to WidgetKit

Leverage WidgetKit’s API to create watchOS complications using SwiftUI.

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Emoji Rangers: Supporting Live Activities, interactivity, and animations

Offer Live Activities, animate data updates, and add interactivity to widgets.

Backyard Birds: Building an app with SwiftData and widgets

Create an app with persistent data, interactive widgets, and an all new in-app
purchase experience.

Fruta: Building a Feature-Rich App with SwiftUI

Create a shared codebase to build a multiplatform app that offers widgets and
an App Clip.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct StaticConfiguration`

An object describing the content of a widget that has no user-configurable
options.

`enum WidgetFamily`

Values that define the widget’s size and shape.

`struct WidgetRenderingMode`

Constants that indicate the rendering mode for a widget.

Article

# Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

## Overview

Widgets use SwiftUI views to display their content. WidgetKit renders the
views on your behalf in a separate process. As a result, your widget extension
is not continually active, even if the widget is onscreen. Despite your widget
not always being active, there are several ways you can keep its content up to
date.

### Plan reloads within a budget

Reloading widgets consumes system resources and causes battery drain due to
additional networking and processing. To reduce this performance impact and
maintain all-day battery life, limit the frequency and number of updates you
request to what’s necessary.

To manage system load, WidgetKit uses a budget to distribute widget reloads
over the course of the day. The budget allocation is dynamic and takes many
factors into account, including:

  * The frequency and times the widget is visible to the user.

  * The widget’s last reload time.

  * Whether the widget’s containing app is active.

WidgetKit maintains different budgets for each active widget the user adds to
their device. For example, if the user adds two instances of a configurable
sports widget, showing information for two different teams, each widget has
its own budget.

A widget’s budget applies to a 24-hour period. WidgetKit tunes the 24-hour
window to the user’s daily usage pattern, which means the daily budget doesn’t
necessarily reset at exactly midnight. For a widget the user frequently views,
a daily budget typically includes from 40 to 70 refreshes. This rate roughly
translates to widget reloads every 15 to 60 minutes, but it’s common for these
intervals to vary due to the many factors involved.

Note

The system takes a few days to learn the user’s behavior. During this learning
period, your widget may receive more reloads than normal.

Cases in which WidgetKit doesn’t count reloads against your widget’s budget
include when:

  * The widget’s containing app is in the foreground.

  * The widget’s containing app has an active audio or navigation session.

  * The widget performs an app intent, such as when the user taps a button or toggles a switch.

  * The widget performs an animation.

  * The system locale changes.

  * Dynamic Type or Accessibility settings change.

For cases such as system appearance changes or system locale changes, don’t
request a timeline reload from your app. The system updates your widgets
automatically. In StandBy, the system refreshes your widget’s display at a
system-defined rate that doesn’t count against the its budget.

Although your widget timeline provider drives your reload schedule, WidgetKit
sometimes reloads your widget to help keep its content fresh. Some common
scenarios include:

  * If a widget is on a Home Screen page that the user rarely visits, WidgetKit may reduce the frequency of reloads for that widget. Later, when the user views the page, WidgetKit may reload the widget when it becomes visible.

  * For widgets that use Location Services, WidgetKit reloads them after a significant location change happens. For more information related to reloads for widgets that use Location Services, see Accessing location information in widgets.

If your widget can predict points in time that it should reload, the best
approach is to generate a timeline for as many future dates as possible. Keep
the interval of entries in the timeline as large as possible for the content
you display. WidgetKit imposes a minimum amount of time before it reloads a
widget. Your timeline provider should create timeline entries that are at
least about 5 minutes apart. WidgetKit may coalesce reloads across multiple
widgets, affecting the exact time a widget is reloaded.

### Generate a timeline for predictable events

Many widgets have predictable points in time where it makes sense to update
their content. For example, a widget that displays weather information might
update the temperature hourly throughout the day. A stock market widget could
update its content frequently during open market hours, but not at all over
the weekend. By planning these times in advance, WidgetKit automatically
refreshes your widget when the appropriate time arrives.

When you define your widget, you implement a custom `TimelineProvider`.
WidgetKit gets a timeline from your provider, and uses it to track when to
update your widget. A timeline is an array of `TimelineEntry` objects. Each
entry in the timeline has a date and time, and additional information the
widget needs to display its view. In addition to the timeline entries, the
timeline specifies a refresh policy that tells WidgetKit when to request a new
timeline.

The following is an example of a game widget that displays a character’s
health level. When the health level is less then 100 percent, the character
recovers at a rate of 25 percent per hour. For example, when the character’s
health level is 25 percent, it takes 3 hours to fully recover to 100 percent.
The following diagram shows how WidgetKit requests the timeline from the
provider, rendering the widget at each time specified in the timeline entries.

When WidgetKit initially requests the timeline, the provider creates one with
four entries. The first entry represents the current time, followed by three
entries at hourly intervals. With the refresh policy set to the default
`atEnd`, WidgetKit requests a new timeline after the last date in the
timeline’s entries. When each date in the timeline arrives, WidgetKit invokes
the widget’s content closure and displays the result. After the last timeline
entry passes, WidgetKit repeats the process by asking the provider for a new
timeline. Because the character’s health has reached 100 percent, the provider
responds with a single entry for the current time and a refresh policy set to
`never`. With this setting, WidgetKit doesn’t ask for another timeline until
the app uses `WidgetCenter` to tell WidgetKit to request a new timeline.

In addition to the `atEnd` and `never` refresh policies, a provider can
specify a different date altogether if the timeline might change before or
after reaching the end of the entries. For example, if a dragon will appear in
2 hours to challenge the character to a battle, the provider sets the reload
policy to `after(_:)`, passing a date 2 hours in the future. The following
diagram shows how WidgetKit, after rendering the widget at the 2-hour mark,
requests a new one.

Due to the battle with the dragon, the character’s healing will take 2
additional hours to reach 100 percent. The new timeline consists of two
entries, one for the current time, and a second entry 2 hours in the future.
The timeline specifies `atEnd` for the refresh policy, indicating there are no
more known events that might alter the timeline.

When the 2 hours have passed, and the character’s health is at 100 percent,
WidgetKit asks the provider for a new timeline. Because the character’s health
has recovered, the provider generates the same final timeline as the first
diagram above. When the user plays the game and the character’s health level
changes, the app uses `WidgetCenter` to have WidgetKit refresh the timeline
and update the widget.

In addition to specifying a date _before_ the end of the timeline, the
provider can specify a date _after_ the end of the timeline. This is useful
when you know that the widget’s state will not change until a later time. For
example, a stock market widget could create a timeline at the close of the
market on Friday with an `after(_:)` refresh policy specifying the time the
market opens on Monday. Because the stock market is closed over the weekend,
there is no need to update the widget until the market opens.

Important

Plan ahead if your widget makes requests to a server when it reloads and uses
`after(_:)` with a specific date in timeline entries. WidgetKit tries to
respect the date you specify, which may cause a significant increase in server
load when multiple devices reload your widget at around the same time.

### Inform WidgetKit when a timeline changes

Your app can tell WidgetKit to request a new timeline when something affects a
widget’s current timeline. In the game widget example above, if the app
receives a push notification indicating a teammate has given the character a
healing potion, the app can tell WidgetKit to reload the timeline and update
the widget’s content. To reload a specific type of widget, your app uses
`WidgetCenter`, as shown here:

The `kind` parameter contains the same string as the value used to create the
widget’s `WidgetConfiguration`.

If your widgets have user-configurable properties, avoid unnecessary reloads
by using WidgetCenter to verify that a widget with the appropriate settings
exists. For example, when the game receives a push notification about a
character receiving a healing potion, it verifies that a widget is showing
that character before reloading the timeline.

In the following code, the app calls `getCurrentConfigurations(_:)` to
retrieve the list of user-configured widgets. It then iterates through the
resulting `WidgetInfo` objects to find one with an `intent` configured with
the character that received the healing potion. If it finds one, the app calls
`reloadTimelines(ofKind:)` for that widget’s `kind`.

If your app uses `WidgetBundle` to support multiple widgets, you can use
`WidgetCenter` to reload the timelines for all your widgets. For example, if
your widgets require the user to sign in to an account but they have signed
out, you can reload all the widgets by calling:

### Display dynamic dates

Even though your widget doesn’t run continually, it can display time-based
information that WidgetKit updates live. For example, it might display a
countdown timer that continues to count down even if your widget extension
isn’t running. For more information, see Displaying dynamic dates in widgets.

### Load data from your server before updating the timeline

You may need to load new data from your server before reloading a timeline. To
do this, use the system’s URL loading system and a `URLSession`. To learn
more, see Making network requests in a widget extension.

## See Also

### Timeline management

`protocol TimelineProvider`

A type that advises WidgetKit when to update a widget’s display.

`protocol IntentTimelineProvider`

A type that advises WidgetKit when to update a user-configurable widget’s
display.

`struct TimelineProviderContext`

An object that contains details about how a widget is rendered, including its
size and whether it appears in the widget gallery.

`protocol TimelineEntry`

A type that specifies the date to display a widget, and, optionally, indicates
the current relevance of the widget’s content.

`struct Timeline`

An object that specifies a date for WidgetKit to update a widget’s view.

`class WidgetCenter`

An object that contains a list of user-configured widgets and is used for
reloading widget timelines.

`protocol AppIntentTimelineProvider`

A type that advises WidgetKit when to update a user-configurable widget’s
display.

Article

# Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

## Overview

To make the most relevant information easily accessible to people, widgets can
provide customizable properties. For example, a person can select a specific
stock for a stock quote widget, or enter a tracking number for a package
delivery widget. Widgets define customizable properties by using app intents,
the same mechanism that Siri Suggestions and Siri Shortcuts use for
customizing those interactions.

To add configurable properties to your widget:

  1. Add custom app intent types that conform to `WidgetConfigurationIntent` to define the configurable properties to your Xcode project.

  2. Specify an `AppIntentTimelineProvider` as your widget’s timeline provider to incorporate the person’s choices into your timeline entries.

  3. Add code to your custom app intent types to provide the data if their properties rely on dynamic data.

If your app already supports Siri Suggestions or Siri Shortcuts and you have a
custom app intent, you’ve probably done most of the work already. Otherwise,
consider leveraging the work you do for your widget to add support for Siri
Suggestions or Siri Shortcuts. For more information on how to get the most
from app intents, see App Intents.

Note

Prior to iOS 17, iPadOS 17, and macOS 14, configurable widgets used SiriKit
Intents. For information on migrating your configurable widgets from the
SiriKit Intents to the App Intents framework, see Migrating widgets from
SiriKit Intents to App Intents.

### Add a custom app intent to your project

To show the character’s information, the person needs a way to select the
character. The following code shows how to define a custom app intent to
represent the choice the person makes:

The static `title` property describes the action the intent enables the person
to take. Use a title case string that combines a verb with a noun. Set the
static `description` to a human-readable string that describes the intent.

To add parameters to the intent, add one or more `@Parameter` property
wrappers. WidgetKit uses the parameter type information to automatically
create the user interface for editing the widget. For example, if the type is
`String`, the person enters a string value. If the type is an `Int`, they use
a number pad. For a parameter that is a predefined, static, list of values,
define a custom type that conforms to `AppEnum`.

Note

The order of the parameters in the intent determines the order in which they
appear when a person edits your widget.

In the example above, the parameter uses a custom `CharacterDetail` type the
app defines to represent a character in the game. To use a custom type as an
app intent parameter, it must conform to `AppEntity`. To implement the
`CharacterDetail` parameter type, the game-status widget uses a structure that
exists in the game’s project. This structure defines a list of available
characters and their details, as follows:

Because characters might vary from game to game, the intent generates the list
dynamically at runtime. WidgetKit uses the app entity’s `defaultQuery`
property to access the dynamic values, as described below.

If your widget includes nonoptional parameters, you must supply a default
value. For types such as `String`, `Int`, or enumerations that use `AppEnum`,
one option is to supply a default value as follows:

A second option is to use a query type that implements `defaultResult()`, as
shown in the next section.

For custom intents with parameters that conform to `AppEntity`, implement
initializer methods to provide default values for the nonoptional parameters,
such as the `init(character:)` method in the code for `SelectCharacterIntent`
shown above. In your timeline provider’s `placeholder(in:)` method, use one of
these initializer methods to initialize the app intent that you pass to the
timeline entry. These methods enable you to customize the placeholder with
values that might be different from the default, if needed.

### Implement a query to provide dynamic values

Some of the tasks that an `EntityQuery` performs include:

  * Mapping `AppEntity` identifiers to the corresponding entity instances.

  * Providing a list of suggested values when a person edits a widget.

  * Specifying a default value for a parameter.

When a person edits a widget with a custom intent that provides dynamic
values, the system invokes the query object’s `suggestedEntities()` method to
get the list of possible choices.

In the entity query, the result is an array of all the `CharacterDetail` types
available.

With the configuration of the custom app intent done, a person can edit the
widget to select a specific character to display.

After the person edits the widget and selects a character, the next step is to
incorporate that choice into the widget’s display.

### Handle customized values in your widget

To support configurable properties, a widget uses the
`AppIntentTimelineProvider` configuration. For example, the character-details
widget defines its configuration as follows:

The `SelectCharacterIntent` parameter determines the customizable properties
for the widget. The configuration uses `CharacterDetailProvider` to manage the
timeline events for the widget. For more information about timeline providers,
see Keeping a widget up to date.

After a person edits the widget, WidgetKit passes the customized values to the
provider when requesting timeline entries. You typically include relevant
details from the intent in the timeline entries the provider generates. In the
following example, the provider uses the `defaultQuery` to look up the
`CharacterDetail` using the character’s `id` in the intent, and then creates a
timeline with an entry containing the character’s detail:

When you include the customized values in the timeline entry, your widget’s
view can display the appropriate content.

### Access customized values in your app

When a person taps on a widget to open your app, WidgetKit passes the
customized intent to your app in an `NSUserActivity`. In your app’s code that
handles the user activity, such as `onContinueUserActivity(_:perform:)` for a
SwiftUI app or `scene(_:continue:)` for a UIKit app, use the
`widgetConfigurationIntent(of:)` method to access the widget’s intent.

To access the intent of any widget that the user has installed, use
`getCurrentConfigurations(_:)` to fetch the `WidgetInfo` objects. Iterate over
the `WidgetInfo` objects and call `widgetConfigurationIntent(of:)`.

### Offer preconfigured complications on Apple Watch

Starting in watchOS 9, iOS 16, and iPadOS 17, you can use WidgetKit to
implement accessory-family widgets that appear as complications on Apple
Watch. Like widgets in iOS and macOS, watch complications use custom intents
to display user-configurable data, and implementing configurable widgets in
watchOS works the same as in iOS or macOS. However, watchOS doesn’t offer a
dedicated user interface for configuring complications. To display data that’s
most relevant to the user in your watch complication, you can create
preconfigured complications and recommend them to your users in the list of
available complications.

In your `AppIntentTimelineProvider` code, implement `recommendations()` and
return the `AppIntentRecommendation` objects you create using your custom
intents.

When your app receives new data that’s relevant to your recommended widget
configurations, invalidate the now outdated recommendations by calling
`invalidateConfigurationRecommendations()`. This tells WidgetKit to get new
recommendations for your preconfigured complications. When you invalidate the
recommendations for preconfigured complications, make sure you return updated
`AppIntentRecommendation` objects in the `recommendations()` callback.

## See Also

### Configurable widgets

Migrating widgets from SiriKit Intents to App Intents

Configure your widgets for backward compatibility.

`struct AppIntentConfiguration`

An object describing the content of a widget that uses a custom intent to
provide user-configurable options.

`struct WidgetInfo`

A structure that contains information about user-configured widgets.

`struct AppIntentRecommendation`

An object that describes a recommended intent configuration for a user-
customizable widget.

`struct IntentConfiguration`

An object describing the content of a widget that uses a custom intent
definition to provide user-configurable options.

`struct IntentRecommendation`

An object that describes a recommended intent configuration for a user-
customizable widget.

Protocol

# Widget

The configuration and content of a widget to display on the Home screen or in
Notification Center.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol Widget

## Overview

Widgets show glanceable and relevant content from your app right on the iOS
Home screen or in Notification Center on macOS. Users can add, configure, and
arrange widgets to suit their individual needs. You can provide multiple types
of widgets, each presenting a specific kind of information. When users want
more information, like to read the full article for a headline or to see the
details of a package delivery, the widget lets them get to the information in
your app quickly.

There are three key components to a widget:

  * A configuration that determines whether the widget is configurable, identifies the widget, and defines the SwiftUI views that show the widget’s content.

  * A timeline provider that drives the process of updating the widget’s view over time.

  * SwiftUI views used by WidgetKit to display the widget.

For information about adding a widget extension to your app, and keeping your
widget up to date, see Creating a widget extension and Keeping a widget up to
date, respectively.

By adding a custom SiriKit intent definition, you can let users customize
their widgets to show the information that’s most relevant to them. If you’ve
already added support for Siri or Shortcuts, you’re well on your way to
supporting customizable widgets. For more information, see Making a
configurable widget.

## Topics

### Implementing a widget

`var body: Self.Body`

The content and behavior of the widget.

**Required**

` associatedtype Body : WidgetConfiguration`

The type of configuration representing the content of the widget.

**Required**

### Running a widget

`init()`

Creates a widget using `body` as its content.

**Required**

` static func main()`

Initializes and runs the widget.

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Protocol

# WidgetBundle

A container used to expose multiple widgets from a single widget extension.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol WidgetBundle

## Overview

To support multiple types of widgets, add the `@main` attribute to a structure
that conforms to `WidgetBundle`. For example, a game might have one widget to
display summary information about the game and a second widget to display
detailed information about individual characters.

## Topics

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

### Running a widget bundle

`init()`

Creates a widget bundle using the bundle’s body as its content.

**Required**

` static func main()`

Initializes and runs the widget bundle.

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Structure

# LimitedAvailabilityConfiguration

A type-erased widget configuration.

iOS 16.1+  iPadOS 16.1+  macOS 13.0+  Mac Catalyst 16.1+  watchOS 9.1+
visionOS 1.0+

    
    
    @frozen
    struct LimitedAvailabilityConfiguration

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `WidgetConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Protocol

# WidgetConfiguration

A type that describes a widget’s content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol WidgetConfiguration

## Topics

### Implementing a widget

`var body: Self.Body`

The content and behavior of this widget.

**Required**

` associatedtype Body : WidgetConfiguration`

The type of widget configuration representing the body of this configuration.

**Required**

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

## Relationships

### Conforming Types

  * `EmptyWidgetConfiguration`
  * `LimitedAvailabilityConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Structure

# EmptyWidgetConfiguration

An empty widget configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @frozen
    struct EmptyWidgetConfiguration

## Topics

### Creating a configuration

`init()`

## Relationships

### Conforms To

  * `Sendable`
  * `WidgetConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

Instance Method

# widgetLabel(_:)

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

A string that contains the text which WidgetKit displays alongside the
complication.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style. For
example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(_:)

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

A label generated from a localized string.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style based
on the clock face. For example, setting the font and rendering the text along
a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(label:)

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<Label>(@ViewBuilder label: () -> Label) -> some View where Label : View
    

##  Parameters

`label`

    

A view that WidgetKit can display alongside the accessory family widget’s main
SwiftUI view. You can use a `Image`, `Text`, `Gauge`, `ProgressView`, or a
container with multiple subviews.

## Discussion

The system only displays labels on widget-based complications in watchOS. The
system ignores any labels attached to widgets on the Lock Screen on iPhone.
Therefore, you can use the same code to display an accessory family widget on
both iPhone and Apple Watch.

To create the widget label, call `widgetLabel(label:)`on a complication’s main
SwiftUI view. Pass the desired content as the `label` parameter. The label can
be a `Gauge`, `ProgressView`, `Text`, or `Image`. To provide multiple views,
wrap your views in a container, such as a `VStack`. WidgetKit determines
whether it can use any of the label’s content. If it can’t, it ignores the
label.

WidgetKit configures the label so that the watch face presents a unified look.
For example, it sets the size for an image, the font for text, and can even
render text and gauges along a curve.

The following widget families support widget labels:

`WidgetKit/WidgetFamily/accessoryCorner`

    

In watchOS, this widget-based complication can display a `Gauge`, a
`ProgressView`, or a `Text`. Adding a label to an accessory corner causes the
main SwiftUI view to shrink to make space for the label. If you pass a view
containing multiple, valid subviews, the system picks which view to display as
the widget label.

`WidgetKit/WidgetFamily/accessoryCircular`

    

In watchOS, the widget-based complication can display either an `Image` or a
`Text`. To pass both an image and text, wrap those views in a container.

However, WidgetKit only renders the label along the bezel on the Infograph
watch face (the top circular complication). On all other circular
complications — including widgets on all other platforms — WidgetKit ignores
the label.

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

Instance Method

# widgetAccentable(_:)

Adds the view and all of its subviews to the accented group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetAccentable(_ accentable: Bool = true) -> some View
    

##  Parameters

`accentable`

    

A Boolean value that indicates whether to add the view and its subviews to the
accented group.

## Discussion

When the system renders the widget using the
`WidgetKit/WidgetRenderingMode/accented` mode, it divides the widget’s view
hierarchy into two groups: the accented group and the default group. It then
applies a different color to each group.

When applying the colors, the system treats the widget’s views as if they were
template images. It ignores the view’s color — rendering the new colors based
on the view’s alpha channel.

To control your view’s appearance, add the `widgetAccentable(_:)` modifier to
part of your view’s hierarchy. If the `accentable` parameter is `true`, the
system adds that view and all of its subviews to the accent group. It puts all
other views in the default group.

Important

After you call `widgetAccentable(true)` on a view moving it into the accented
group, calling `widgetAccentable(false)` on its subviews doesn’t move the
subviews back into the default group.

Instance Method

# dynamicIsland(verticalPlacement:)

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
    

##  Parameters

`verticalPlacement`

    

The vertical placement for a view that’s part of an expanded Live Activity in
the Dynamic Island.

## Return Value

A view with the specified vertical placement.



# AccessibilityCustomContentKey

Initializer

# init(_:)

Create an `AccessibilityCustomContentKey` with the specified label.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ labelKey: LocalizedStringKey)

##  Parameters

`labelKey`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”. This will also be used as the
identifier.

## See Also

### Creating a key

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

Initializer

# init(_:id:)

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: String
    )

##  Parameters

`label`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”.

`id`

    

String used to identify the additional information entry to SwiftUI. Adding an
entry will replace any previous value with the same identifier.

## See Also

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

Initializer

# init(_:id:)

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: String
    )

##  Parameters

`labelKey`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”.

`id`

    

String used to identify the additional information entry to SwiftUI. Adding an
entry will replace any previous value with the same identifier.

## See Also

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.



# AnyTransition

Type Property

# identity

A transition that returns the input view, unmodified, as the output view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let identity: AnyTransition

## See Also

### Getting built-in transitions

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# move(edge:)

Returns a transition that moves the view away, towards the specified edge of
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func move(edge: Edge) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# offset(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func offset(_ offset: CGSize) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# offset(x:y:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# opacity

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let opacity: AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# push(from:)

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func push(from edge: Edge) -> AnyTransition

##  Parameters

`edge`

    

the edge from which the view will be animated in.

## Return Value

A transition that animates a view by moving and fading it.

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# scale

Returns a transition that scales the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var scale: AnyTransition { get }

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# scale(scale:anchor:)

Returns a transition that scales the view by the specified amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func scale(
        scale: CGFloat,
        anchor: UnitPoint = .center
    ) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# slide

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var slide: AnyTransition { get }

## Discussion

See Also

`AnyTransition.move(edge:)`

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

Instance Method

# animation(_:)

Attaches an animation to this transition.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> AnyTransition

## See Also

### Combining and configuring transitions

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

Type Method

# asymmetric(insertion:removal:)

Provides a composite transition that uses a different transition for insertion
versus removal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func asymmetric(
        insertion: AnyTransition,
        removal: AnyTransition
    ) -> AnyTransition

## See Also

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

Instance Method

# combined(with:)

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func combined(with other: AnyTransition) -> AnyTransition

## See Also

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

Initializer

# init(_:)

Create an instance that type-erases `transition`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<T>(_ transition: T) where T : Transition

## See Also

### Creating a custom transition

`static func modifier<E>(active: E, identity: E) -> AnyTransition`

Returns a transition defined between an active modifier and an identity
modifier.

Type Method

# modifier(active:identity:)

Returns a transition defined between an active modifier and an identity
modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func modifier<E>(
        active: E,
        identity: E
    ) -> AnyTransition where E : ViewModifier

## See Also

### Creating a custom transition

`init<T>(T)`

Create an instance that type-erases `transition`.



# Accessibility modifiers

Instance Method

# speechAdjustedPitch(_:)

Raises or lowers the pitch of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAdjustedPitch(_ value: Double) -> some View
    

##  Parameters

`value`

    

The amount to raise or lower the pitch. Values between `-1` and `0` result in
a lower pitch while values between `0` and `1` result in a higher pitch. The
method clamps values to the range `-1` to `1`.

## Discussion

Use this modifier when you want to change the pitch of spoken text. The value
indicates how much higher or lower to change the pitch.

## See Also

### Configuring VoiceOver

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAlwaysIncludesPunctuation(_:)

Sets whether VoiceOver should always speak all punctuation in the text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that you set to `true` if VoiceOver should speak all
punctuation in the text. Defaults to `true`.

## Discussion

Use this modifier to control whether the system speaks punctuation characters
in the text. You might use this for code or other text where the punctuation
is relevant, or where you want VoiceOver to speak a verbatim transcription of
the text you provide. For example, given the text:

VoiceOver would speak “All the world apostrophe s a stage comma and all the
men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAnnouncementsQueued(_:)

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAnnouncementsQueued(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that determines if VoiceOver speaks changes to text
immediately or enqueues them behind existing speech. Defaults to `true`.

## Discussion

Use this modifier when you want affect the order in which the accessibility
system delivers spoken text. Announcements can occur automatically when the
label or value of an accessibility element changes.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechSpellsOutCharacters(_:)

Sets whether VoiceOver should speak the contents of the text view character by
character.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechSpellsOutCharacters(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that when `true` indicates VoiceOver should speak text as
individual characters. Defaults to `true`.

## Discussion

Use this modifier when you want VoiceOver to speak text as individual letters,
character by character. This is important for text that is not meant to be
spoken together, like:

  * An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.

  * A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.



# Accessible controls

Structure

# AccessibilityActionKind

The structure that defines the kinds of available accessibility actions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityActionKind

## Topics

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let delete: AccessibilityActionKind`

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let magicTap: AccessibilityActionKind`

`static let showMenu: AccessibilityActionKind`

### Creating an action type

`init(named: Text)`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Adding actions to views

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`enum AccessibilityAdjustmentDirection`

A directional indicator you use when making an accessibility adjustment.

Enumeration

# AccessibilityAdjustmentDirection

A directional indicator you use when making an accessibility adjustment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum AccessibilityAdjustmentDirection

## Topics

### Getting an adjustment direction

`case decrement`

`case increment`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding actions to views

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityActionKind`

The structure that defines the kinds of available accessibility actions.

Protocol

# AccessibilityQuickActionStyle

A type that describes the presentation style of an accessibility quick action.

watchOS 9.0+

    
    
    protocol AccessibilityQuickActionStyle

## Topics

### Getting built-in menu styles

`static var outline: AccessibilityQuickActionOutlineStyle`

A presentation style that animates an outline around the view when the
accessibility quick action is active.

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

`static var prompt: AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

### Supporting types

`struct AccessibilityQuickActionOutlineStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

`struct AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

## Relationships

### Conforming Types

  * `AccessibilityQuickActionOutlineStyle`
  * `AccessibilityQuickActionPromptStyle`

## See Also

### Offering Quick Actions to people

`func accessibilityQuickAction<Style, Content>(style: Style, content: () ->
Content) -> some View`

Adds a quick action to be shown by the system when active.

`func accessibilityQuickAction<Style, Content>(style: Style, isActive:
Binding<Bool>, content: () -> Content) -> some View`

Adds a quick action to be shown by the system when active.

Structure

# AccessibilityDirectTouchOptions

An option set that defines the functionality of a view’s direct touch area.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AccessibilityDirectTouchOptions

## Topics

### Getting the options

`static let requiresActivation: AccessibilityDirectTouchOptions`

Prevents touch passthrough with the direct touch area until an assistive
technology, such as VoiceOver, has activated the direct touch area through a
user action, for example a double tap.

`static let silentOnTouch: AccessibilityDirectTouchOptions`

Allows a direct touch area to immediately receive touch events without an
assitive technology, such as VoiceOver, speaking. Appropriate for apps that
provide direct audio feedback on touch that would conflict with speech
feedback.

### Creating a set of options

`init(rawValue: AccessibilityDirectTouchOptions.RawValue)`

Create a set of direct touch options

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Making gestures accessible

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityZoomGestureAction`

Position and direction information of a zoom gesture that someone performs
with an assistive technology like VoiceOver.

Structure

# AccessibilityZoomGestureAction

Position and direction information of a zoom gesture that someone performs
with an assistive technology like VoiceOver.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AccessibilityZoomGestureAction

## Topics

### Getting the action’s direction

`let direction: AccessibilityZoomGestureAction.Direction`

The zoom gesture’s direction.

`enum Direction`

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

### Getting location information

`let location: UnitPoint`

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.

`let point: CGPoint`

The zoom gesture’s activation point within the window’s coordinate space.

## See Also

### Making gestures accessible

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityDirectTouchOptions`

An option set that defines the functionality of a view’s direct touch area.

Structure

# AccessibilityFocusState

A property wrapper type that can read and write a value that SwiftUI updates
as the focus of any active accessibility technology, such as VoiceOver,
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct AccessibilityFocusState<Value> where Value : Hashable

## Overview

Use this capability to request that VoiceOver or other accessibility
technologies programmatically focus on a specific element, or to determine
whether VoiceOver or other accessibility technologies are focused on
particular elements. Use `accessibilityFocused(_:equals:)` or
`accessibilityFocused(_:)` in conjunction with this property wrapper to
identify accessibility elements for which you want to get or set accessibility
focus. When accessibility focus enters the modified accessibility element, the
framework updates the wrapped value of this property to match a given
prototype value. When accessibility focus leaves, SwiftUI resets the wrapped
value of an optional property to `nil` or the wrapped value of a Boolean
property to `false`. Setting the property’s value programmatically has the
reverse effect, causing accessibility focus to move to whichever accessibility
element is associated with the updated value.

In the example below, when `notification` changes, and its `isPriority`
property is `true`, the accessibility focus moves to the notification `Text`
element above the rest of the view’s content:

To allow for cases where accessibility focus is completely absent from the
tree of accessibility elements, or accessibility technologies are not active,
the wrapped value must be either optional or Boolean.

Some initializers of `AccessibilityFocusState` also allow specifying
accessibility technologies, determining to which types of accessibility focus
this binding applies. If you specify no accessibility technologies, SwiftUI
uses an aggregate of any and all active accessibility technologies.

## Topics

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

`struct Binding`

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Controlling focus

`func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some
View`

Modifies this view by binding its accessibility element’s focus state to the
given boolean state value.

`func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding,
equals: Value) -> some View`

Modifies this view by binding its accessibility element’s focus state to the
given state value.



# Alignment

Type Property

# topLeading

A guide that marks the top and leading edges of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let topLeading: Alignment

## Discussion

This alignment combines the `leading` horizontal guide and the `top` vertical
guide:

## See Also

### Getting top guides

`static let top: Alignment`

A guide that marks the top edge of the view.

`static let topTrailing: Alignment`

A guide that marks the top and trailing edges of the view.

Type Property

# top

A guide that marks the top edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let top: Alignment

## Discussion

This alignment combines the `center` horizontal guide and the `top` vertical
guide:

## See Also

### Getting top guides

`static let topLeading: Alignment`

A guide that marks the top and leading edges of the view.

`static let topTrailing: Alignment`

A guide that marks the top and trailing edges of the view.

Type Property

# topTrailing

A guide that marks the top and trailing edges of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let topTrailing: Alignment

## Discussion

This alignment combines the `trailing` horizontal guide and the `top` vertical
guide:

## See Also

### Getting top guides

`static let topLeading: Alignment`

A guide that marks the top and leading edges of the view.

`static let top: Alignment`

A guide that marks the top edge of the view.

Type Property

# leading

A guide that marks the leading edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let leading: Alignment

## Discussion

This alignment combines the `leading` horizontal guide and the `center`
vertical guide:

## See Also

### Getting middle guides

`static let center: Alignment`

A guide that marks the center of the view.

`static let trailing: Alignment`

A guide that marks the trailing edge of the view.

Type Property

# center

A guide that marks the center of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let center: Alignment

## Discussion

This alignment combines the `center` horizontal guide and the `center`
vertical guide:

## See Also

### Getting middle guides

`static let leading: Alignment`

A guide that marks the leading edge of the view.

`static let trailing: Alignment`

A guide that marks the trailing edge of the view.

Type Property

# trailing

A guide that marks the trailing edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let trailing: Alignment

## Discussion

This alignment combines the `trailing` horizontal guide and the `center`
vertical guide:

## See Also

### Getting middle guides

`static let leading: Alignment`

A guide that marks the leading edge of the view.

`static let center: Alignment`

A guide that marks the center of the view.

Type Property

# bottomLeading

A guide that marks the bottom and leading edges of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottomLeading: Alignment

## Discussion

This alignment combines the `leading` horizontal guide and the `bottom`
vertical guide:

## See Also

### Getting bottom guides

`static let bottom: Alignment`

A guide that marks the bottom edge of the view.

`static let bottomTrailing: Alignment`

A guide that marks the bottom and trailing edges of the view.

Type Property

# bottom

A guide that marks the bottom edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottom: Alignment

## Discussion

This alignment combines the `center` horizontal guide and the `bottom`
vertical guide:

## See Also

### Getting bottom guides

`static let bottomLeading: Alignment`

A guide that marks the bottom and leading edges of the view.

`static let bottomTrailing: Alignment`

A guide that marks the bottom and trailing edges of the view.

Type Property

# bottomTrailing

A guide that marks the bottom and trailing edges of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottomTrailing: Alignment

## Discussion

This alignment combines the `trailing` horizontal guide and the `bottom`
vertical guide:

## See Also

### Getting bottom guides

`static let bottomLeading: Alignment`

A guide that marks the bottom and leading edges of the view.

`static let bottom: Alignment`

A guide that marks the bottom edge of the view.

Type Property

# leadingFirstTextBaseline

A guide that marks the leading edge and top-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var leadingFirstTextBaseline: Alignment { get }

## Discussion

This alignment combines the `leading` horizontal guide and the
`firstTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

Type Property

# centerFirstTextBaseline

A guide that marks the top-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var centerFirstTextBaseline: Alignment { get }

## Discussion

This alignment combines the `center` horizontal guide and the
`firstTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

Type Property

# trailingFirstTextBaseline

A guide that marks the trailing edge and top-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var trailingFirstTextBaseline: Alignment { get }

## Discussion

This alignment combines the `trailing` horizontal guide and the
`firstTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

Type Property

# leadingLastTextBaseline

A guide that marks the leading edge and bottom-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var leadingLastTextBaseline: Alignment { get }

## Discussion

This alignment combines the `leading` horizontal guide and the
`lastTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

Type Property

# centerLastTextBaseline

A guide that marks the bottom-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var centerLastTextBaseline: Alignment { get }

## Discussion

This alignment combines the `center` horizontal guide and the
`lastTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

Type Property

# trailingLastTextBaseline

A guide that marks the trailing edge and bottom-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var trailingLastTextBaseline: Alignment { get }

## Discussion

This alignment combines the `trailing` horizontal guide and the
`lastTextBaseline` vertical guide:

## See Also

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

Initializer

# init(horizontal:vertical:)

Creates a custom alignment value with the specified horizontal and vertical
alignment guides.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        horizontal: HorizontalAlignment,
        vertical: VerticalAlignment
    )

##  Parameters

`horizontal`

    

The alignment on the horizontal axis.

`vertical`

    

The alignment on the vertical axis.

## Discussion

SwiftUI provides a variety of built-in alignments that combine built-in
`HorizontalAlignment` and `VerticalAlignment` guides. Use this initializer to
create a custom alignment that makes use of a custom horizontal or vertical
guide, or both.

For example, you can combine a custom vertical guide called `firstThird` with
the built-in `center` guide, and use it to configure a `ZStack`:

For more information about creating custom guides, including the code that
creates the custom `firstThird` alignment in the example above, see
`AlignmentID`.

## See Also

### Creating a custom alignment

`var horizontal: HorizontalAlignment`

The alignment on the horizontal axis.

`var vertical: VerticalAlignment`

The alignment on the vertical axis.

Instance Property

# horizontal

The alignment on the horizontal axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var horizontal: HorizontalAlignment

## Discussion

Set this value when you initialize an alignment using the
`init(horizontal:vertical:)` method. Use one of the built-in
`HorizontalAlignment` guides, like `center`, or a custom guide that you
create.

For information about creating custom guides, see `AlignmentID`.

## See Also

### Creating a custom alignment

`init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)`

Creates a custom alignment value with the specified horizontal and vertical
alignment guides.

`var vertical: VerticalAlignment`

The alignment on the vertical axis.

Instance Property

# vertical

The alignment on the vertical axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var vertical: VerticalAlignment

## Discussion

Set this value when you initialize an alignment using the
`init(horizontal:vertical:)` method. Use one of the built-in
`VerticalAlignment` guides, like `center`, or a custom guide that you create.

For information about creating custom guides, see `AlignmentID`.

## See Also

### Creating a custom alignment

`init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)`

Creates a custom alignment value with the specified horizontal and vertical
alignment guides.

`var horizontal: HorizontalAlignment`

The alignment on the horizontal axis.



# AccessibilityAdjustmentDirection

Case

# AccessibilityAdjustmentDirection.decrement

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case decrement

## See Also

### Getting an adjustment direction

`case increment`

Case

# AccessibilityAdjustmentDirection.increment

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case increment

## See Also

### Getting an adjustment direction

`case decrement`



# AutomaticDisclosureGroupStyle

Initializer

# init()

Creates an automatic disclosure group style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init()



# Anchor

Structure

# Anchor.Source

A type-erased geometry value that produces an anchored value of a given type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Source

## Overview

SwiftUI passes anchored geometry values around the view tree via preference
keys. It then converts them back into the local coordinate space using a
`GeometryProxy` value.

## Topics

### Getting point anchor sources

`static func point(CGPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

`static func unitPoint(UnitPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

### Getting rectangle anchor sources

`static func rect(CGRect) -> Anchor<Value>.Source`

Returns an anchor source rect defined by `r` in the current view.

Available when `Value` is `CGRect`.

`static var bounds: Anchor<CGRect>.Source`

An anchor source rect defined as the entire bounding rect of the current view.

Available when `Value` is `CGRect`.

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

### Creating an anchor source

`init<T>(Anchor<T>.Source?)`

`init<T>([Anchor<T>.Source])`

## Relationships

### Conforms To

  * `Sendable`



# AnyShape

Initializer

# init(_:)

Create an any shape instance from a shape.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(_ shape: S) where S : Shape



# AnimationTimelineSchedule

Initializer

# init(minimumInterval:paused:)

Create a pausable schedule of dates updating at a frequency no more quickly
than the provided interval.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        minimumInterval: Double? = nil,
        paused: Bool = false
    )

##  Parameters

`minimumInterval`

    

The minimum interval to update the schedule at. Pass nil to let the system
pick an appropriate update interval.

`paused`

    

If the schedule should stop generating updates.

Instance Method

# entries(from:mode:)

Returns entries at the frequency of the animation schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from start: Date,
        mode: TimelineScheduleMode
    ) -> AnimationTimelineSchedule.Entries

## Discussion

When in `.lowFrequency` mode, return no entries, effectively pausing the
animation.



# Animations

Function

# withAnimation(_:_:)

Returns the result of recomputing the view’s body with the provided animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withAnimation<Result>(
        _ animation: Animation? = .default,
        _ body: () throws -> Result
    ) rethrows -> Result

## Discussion

This function sets the given `Animation` as the `animation` property of the
thread’s current `Transaction`.

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Function

# withAnimation(_:completionCriteria:_:completion:)

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func withAnimation<Result>(
        _ animation: Animation? = .default,
        completionCriteria: AnimationCompletionCriteria = .logicallyComplete,
        _ body: () throws -> Result,
        completion: @escaping () -> Void
    ) rethrows -> Result

## Discussion

This function sets the given `Animation` as the `animation` property of the
thread’s current `Transaction` as well as calling
`Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no
animations are created by the changes in `body`, then the callback will be
called immediately after `body`.

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Structure

# AnimationCompletionCriteria

The criteria that determines when an animation is considered finished.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationCompletionCriteria

## Topics

### Getting the completion criteria

`static let logicallyComplete: AnimationCompletionCriteria`

The animation has logically completed, but may still be in its long tail.

`static let removed: AnimationCompletionCriteria`

The entire animation is finished and will now be removed.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Structure

# Animation

The way a view changes over time to create a smooth visual transition from one
state to another.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Animation

## Overview

An `Animation` provides a visual transition of a view when a state value
changes from one value to another. The characteristics of this transition vary
according to the animation type. For instance, a `linear` animation provides a
mechanical feel to the animation because its speed is consistent from start to
finish. In contrast, an animation that uses easing, like `easeOut`, offers a
more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the `animation(_:value:)` modifier, and
specify both an animation type and the value to animate. For instance, the
`Circle` view in the following code performs an `easeIn` animation each time
the state variable `scale` changes:

Play

When the value of `scale` changes, the modifier `scaleEffect(_:anchor:)`
resizes `Circle` according to the new value. SwiftUI can animate the
transition between sizes because `Circle` conforms to the `Shape` protocol.
Shapes in SwiftUI conform to the `Animatable` protocol, which describes how to
animate a property of a view.

In addition to adding an animation to a view, you can also configure the
animation by applying animation modifiers to the animation type. For example,
you can:

  * Delay the start of the animation by using the `delay(_:)` modifier.

  * Repeat the animation by using the `repeatCount(_:autoreverses:)` or `repeatForever(autoreverses:)` modifiers.

  * Change the speed of the animation by using the `speed(_:)` modifier.

For example, the `Circle` view in the following code repeats the `easeIn`
animation three times by using the `repeatCount(_:autoreverses:)` modifier:

Play

A view can also perform an animation when a binding value changes. To specify
the animation type on a binding, call its `animation(_:)` method. For example,
the view in the following code performs a `linear` animation, moving the box
truck between the leading and trailing edges of the view. The truck moves each
time a person clicks the `Toggle` control, which changes the value of the
`$isTrailing` binding.

Play

## Topics

### Getting the default animation

`static let `default`: Animation`

A default animation instance.

### Getting linear animations

`static var linear: Animation`

An animation that moves at a constant speed.

`static func linear(duration: TimeInterval) -> Animation`

An animation that moves at a constant speed during a specified duration.

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

### Instance Properties

`var base: any CustomAnimation`

### Instance Methods

`func animate<V>(value: V, time: TimeInterval, context: inout
AnimationContext<V>) -> V?`

Calculates the current value of the animation.

`func logicallyComplete(after: TimeInterval) -> Animation`

Causes the animation to report logical completion after the specified
duration, if it has not already logically completed.

`func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval,
context: inout AnimationContext<V>) -> Bool`

Returns a Boolean value that indicates whether the current animation should
merge with a previous animation.

`func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>)
-> V?`

Calculates the current velocity of the animation.

### Type Methods

`static func interactiveSpring(duration: TimeInterval, extraBounce: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

## Relationships

### Conforms To

  * `CustomDebugStringConvertible`
  * `CustomReflectable`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

Instance Method

# animation(_:)

Applies the given animation to this view when this view changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some View
    

Available when `Self` conforms to `Equatable`.

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## Return Value

A view that applies `animation` to this view whenever it changes.

## See Also

### Adding state-based animation to a view

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:value:)

Applies the given animation to this view when the specified value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        value: V
    ) -> some View where V : Equatable
    

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

`value`

    

A value to monitor for changes.

## Return Value

A view that applies `animation` to this view whenever `value` changes.

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:body:)

Applies the given animation to all animatable values within the `body`
closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation,
while the contents of MyView are animated with the implicit transaction’s
animation:

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

Instance Method

# phaseAnimator(_:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change continuously.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the
second phase. Update the effects that you apply to the proxy view accordingly,
and the modifier animates the change for you. As soon as the animation
completes, the procedure repeats using successive phases until reaching the
last phase, at which point the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# phaseAnimator(_:trigger:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`trigger`

    

A value whose changes cause the animator to use the next phase.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides
its `content` closure with the value of the second phase. Update the effects
that you apply to the proxy view accordingly, and the modifier animates the
change for you. The next time the `trigger` input changes, this procedure
repeats using successive phases until reaching the last phase, at which point
the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Structure

# PhaseAnimator

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PhaseAnimator<Phase, Content> where Phase : Equatable, Content : View

## Overview

Use one of the phase animator view modifiers like
`phaseAnimator(_:content:animation:)` to create a phased animation in your
app.

## Topics

### Creating a phase animator

`init(some Sequence<Phase>, content: (Phase) -> Content, animation: (Phase) ->
Animation?)`

Cycles through a sequence of phases continuously, animating updates to a view
on each phase change.

`init(some Sequence<Phase>, trigger: some Equatable, content: (Phase) ->
Content, animation: (Phase) -> Animation?)`

Cycles through a sequence of phases in response to changes in a specified
value, animating updates to a view on each phase change.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

Instance Method

# keyframeAnimator(initialValue:repeating:content:keyframes:)

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        repeating: Bool = true,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`repeating`

    

Whether the keyframes are currently repeating. If false, the value at the
beginning of the keyframe timeline will be provided to the content closure.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# keyframeAnimator(initialValue:trigger:content:keyframes:)

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`trigger`

    

A value to observe for changes.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

If the trigger value changes while animating, the `keyframes` closure will be
called with the current interpolated value, and the keyframes that you return
define a new animation that replaces the old one. The previous velocity will
be preserved, so cubic or spring keyframes will maintain continuity from the
previous animation if they do not specify a custom initial velocity.

When a keyframe animation finishes, the animator will remain at the end value,
which becomes the initial value for the next animation.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeAnimator

A container that animates its content with keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeAnimator<Value, KeyframePath, Content> where Value == KeyframePath.Value, KeyframePath : Keyframes, Content : View

## Overview

The `content` closure updates every frame while animating, so avoid performing
any expensive operations directly within `content`.

## Topics

### Creating a phase animator

`init(initialValue: Value, repeating: Bool, content: (Value) -> Content,
keyframes: (Value) -> KeyframePath)`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`init(initialValue: Value, trigger: some Equatable, content: (Value) ->
Content, keyframes: (Value) -> KeyframePath)`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Protocol

# Keyframes

A type that defines changes to a value over time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol Keyframes<Value>

## Topics

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

## Relationships

### Conforming Types

  * `KeyframeTrack`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTimeline

A description of how a value changes over time, modeled using keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeTimeline<Value>

## Overview

Unlike other animations in SwiftUI (using `Animation`), keyframes don’t
interpolate between from and to values that SwiftUI provides as state changes.
Instead, keyframes fully define the path that a value takes over time using
the tracks that make up their body.

`Keyframes` values are roughly analogous to video clips; they have a set
duration, and you can scrub and evaluate them for any time within the
duration.

The `Keyframes` structure also allows you to compute an interpolated value at
a specific time, which you can use when integrating keyframes into custom use
cases.

For example, you can use a `Keyframes` instance to define animations for a
type conforming to `Animatable:`

For animations that involve multiple coordinated changes, you can include
multiple nested tracks:

Multiple nested tracks update the initial value in the order that they are
declared. This means that if multiple nested plans change the same property of
the root value, the value from the last competing track will be used.

## Topics

### Creating a keyframe timeline

`init(initialValue: Value, content: () -> some Keyframes<Value>)`

Creates a new instance using the initial value and content that you provide.

### Getting the duration

`var duration: TimeInterval`

The duration of the content in seconds.

### Getting an interpolated value

`func value(time: Double) -> Value`

Returns the interpolated value at the given time.

`func value(progress: Double) -> Value`

Returns the interpolated value at the given progress in the range zero to one.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTrack

A sequence of keyframes animating a single property of a root type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeTrack<Root, Value, Content> where Value == Content.Value, Content : KeyframeTrackContent

## Topics

### Creating a keyframe track

`init(content: () -> Content)`

Creates an instance that animates the entire value from the root of the key
path.

`init(WritableKeyPath<Root, Value>, content: () -> Content)`

Creates an instance that animates the property of the root value at the given
key path.

## Relationships

### Conforms To

  * `Keyframes`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTrackContentBuilder

The builder that creates keyframe track content from the keyframes that you
define within a closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct KeyframeTrackContentBuilder<Value> where Value : Animatable

## Topics

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframesBuilder

A builder that combines keyframe content values into a single value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct KeyframesBuilder<Value>

## Topics

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Protocol

# KeyframeTrackContent

A group of keyframes that define an interpolation curve of an animatable
value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol KeyframeTrackContent<Value>

## Topics

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Body : KeyframeTrackContent`

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

## Relationships

### Conforming Types

  * `CubicKeyframe`
  * `KeyframeTrackContentBuilder.Conditional`

Conforms when `Value` conforms to `Animatable`.

  * `LinearKeyframe`
  * `MoveKeyframe`
  * `SpringKeyframe`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# CubicKeyframe

A keyframe that uses a cubic curve to smoothly interpolate between values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct CubicKeyframe<Value> where Value : Animatable

## Overview

If you don’t specify a start or end velocity, SwiftUI automatically computes a
curve that maintains smooth motion between keyframes.

Adjacent cubic keyframes result in a Catmull-Rom spline.

If a cubic keyframe follows a different type of keyframe, such as a linear
keyframe, the end velocity of the segment defined by the previous keyframe
will be used as the starting velocity.

Likewise, if a cubic keyframe is followed by a different type of keyframe, the
initial velocity of the next segment is used as the end velocity of the
segment defined by this keyframe.

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval, startVelocity: Value?, endVelocity:
Value?)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# LinearKeyframe

A keyframe that uses simple linear interpolation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct LinearKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval, timingCurve: UnitCurve)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# MoveKeyframe

A keyframe that immediately moves to the given value without interpolating.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct MoveKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value)`

Creates a new keyframe using the given value.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# SpringKeyframe

A keyframe that uses a spring function to interpolate to the given value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SpringKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval?, spring: Spring, startVelocity: Value?)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

Protocol

# CustomAnimation

A type that defines how an animatable value changes over time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol CustomAnimation : Hashable

## Overview

Use this protocol to create a type that changes an animatable value over time,
which produces a custom visual transition of a view. For example, the follow
code changes an animatable value using an elastic ease-in ease-out function:

Note

To maintain state during the life span of a custom animation, use the `state`
property available on the `context` parameter value. You can also use
context’s `environment` property to retrieve environment values from the view
that created the custom animation. For more information, see
`AnimationContext`.

To create an `Animation` instance of a custom animation, use the `init(_:)`
initializer, passing in an instance of a custom animation; for example:

To help make view code more readable, extend `Animation` and add a static
property and function that returns an `Animation` instance of a custom
animation. For example, the following code adds the static property
`elasticEaseInEaseOut` that returns the elastic ease-in ease-out animation
with a default duration of `0.35` seconds. Next, the code adds a method that
returns the animation with a specified duration.

To animate a view with the elastic ease-in ease-out animation, a view calls
either `.elasticEaseInEaseOut` or `.elasticEaseInEaseOut(duration:)`. For
example, the follow code includes an Animate button that, when clicked,
animates a circle as it moves from one edge of the view to the other, using
the elastic ease-in ease-out animation with a duration of `5` seconds:

Play

## Topics

### Animating a value

`func animate<V>(value: V, time: TimeInterval, context: inout
AnimationContext<V>) -> V?`

Calculates the value of the animation at the specified time.

**Required**

### Getting the velocity

`func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>)
-> V?`

Calculates the velocity of the animation at a specified time.

**Required** Default implementation provided.

### Determining whether to merge

`func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval,
context: inout AnimationContext<V>) -> Bool`

Determines whether an instance of the animation can merge with other instance
of the same type.

**Required** Default implementation provided.

## Relationships

### Inherits From

  * `Equatable`
  * `Hashable`

## See Also

### Creating custom animations

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# AnimationContext

Contextual values that a custom animation can use to manage state and access a
view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationContext<Value> where Value : VectorArithmetic

## Overview

The system provides an `AnimationContext` to a `CustomAnimation` instance so
that the animation can store and retrieve values in an instance of
`AnimationState`. To access these values, use the context’s `state` property.

For more convenient access to state, create an `AnimationStateKey` and extend
`AnimationContext` to include a computed property that gets and sets the
`AnimationState` value. Then use this property instead of `state` to retrieve
the state of a custom animation. For example, the following code creates an
animation state key named `PausableState`. Then the code extends
`AnimationContext` to include the `pausableState` property:

To access the pausable state, the custom animation `PausableAnimation` uses
the `pausableState` property instead of the `state` property:

The animation can also retrieve environment values of the view that created
the animation. To retrieve a view’s environment value, use the context’s
`environment` property. For instance, the following code creates a custom
`EnvironmentKey` named `AnimationPausedKey`, and the view
`PausableAnimationView` uses the key to store the paused state:

Then the custom animation `PausableAnimation` retrieves the paused state from
the view’s environment using the `environment` property:

## Topics

### Managing state

`var state: AnimationState<Value>`

The current state of a custom animation.

### Retrieving view environment values

`var environment: EnvironmentValues`

The current environment of the view that created the custom animation.

### Creating context

`func withState<T>(AnimationState<T>) -> AnimationContext<T>`

Creates a new context from another one with a state that you provide.

### Instance Properties

`var isLogicallyComplete: Bool`

Set this to `true` to indicate that an animation is logically complete.

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# AnimationState

A container that stores the state for a custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationState<Value> where Value : VectorArithmetic

## Overview

An `AnimationContext` uses this type to store state for a `CustomAnimation`.
To retrieve the stored state of a context, you can use the `state` property.
However, a more convenient way to access the animation state is to define an
`AnimationStateKey` and extend `AnimationContext` with a computed property
that gets and sets the animation state, as shown in the following code:

When creating an `AnimationStateKey`, it’s convenient to define the state
values that your custom animation needs. For example, the following code adds
the properties `paused` and `pauseTime` to the `PausableState` animation state
key:

To access the pausable state in a `PausableAnimation`, the follow code calls
`pausableState` instead of using the context’s `state` property. And because
the animation state key `PausableState` defines properties for state values,
the custom animation can read and write those values.

### Storing state for secondary animations

A custom animation can also use `AnimationState` to store the state of a
secondary animation. For example, the following code creates an
`AnimationStateKey` that includes the property `secondaryState`, which a
custom animation can use to store other state:

The custom animation `TargetAnimation` uses `TargetState` to store state data
in `secondaryState` for another animation that runs as part of the target
animation.

## Topics

### Creating animation state

`init()`

Create an empty state container.

### Accessing custom keys

`subscript<K>(K.Type) -> K.Value`

Accesses the state for a custom key.

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Protocol

# AnimationStateKey

A key for accessing animation state values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol AnimationStateKey

## Overview

To access animation state from an `AnimationContext` in a custom animation,
create an `AnimationStateKey`. For example, the following code creates an
animation state key named `PausableState` and sets the value for the required
`defaultValue` property. The code also defines properties for state values
that the custom animation needs when calculating animation values. Keeping the
state values in the animation state key makes it more convenient to read and
write those values in the implementation of a `CustomAnimation`.

To make accessing the value of the animation state key more convenient, define
a property for it by extending `AnimationContext`:

Then, you can read and write your state in an instance of `CustomAnimation`
using the `AnimationContext`:

## Topics

### Setting the default value

`static var defaultValue: Self.Value`

The default value for the animation state key.

**Required**

` associatedtype Value`

The associated type representing the type of the animation state key’s value.

**Required**

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# UnitCurve

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct UnitCurve

## Overview

The horizontal (x) axis defines the input progress: a single input progress
value in the range [0,1] must be provided when evaluating a curve.

The vertical (y) axis maps to the output progress: when a curve is evaluated,
the y component of the point that intersects the input progress is returned.

## Topics

### Getting a linear curve

`static let linear: UnitCurve`

A linear curve.

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

### Creating a general Bezier curve

`static func bezier(startControlPoint: UnitPoint, endControlPoint: UnitPoint)
-> UnitCurve`

Creates a new curve using bezier control points.

### Inverting a curve

`var inverse: UnitCurve`

Returns a copy of the curve with its x and y components swapped.

### Getting curve characteristics

`func value(at: Double) -> Double`

Returns the output value (y component) of the curve at the given time.

`func velocity(at: Double) -> Double`

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

### Deprecated symbols

`static let easeInEaseOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct Spring`

A representation of a spring’s motion.

Structure

# Spring

A representation of a spring’s motion.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Spring

## Overview

Use this type to convert between different representations of spring
parameters:

You can also use it to query for a spring’s position and its other properties
for a given set of inputs:

## Topics

### Creating a spring

`init(duration: TimeInterval, bounce: Double)`

Creates a spring with the specified duration and bounce.

`init(mass: Double, stiffness: Double, damping: Double, allowOverDamping:
Bool)`

Creates a spring with the specified mass, stiffness, and damping.

`init(response: Double, dampingRatio: Double)`

Creates a spring with the specified response and damping ratio.

`init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)`

Creates a spring with the specified duration and damping ratio.

### Getting built-in springs

`static var bouncy: Spring`

A spring with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and higher amount of bounce that can be
tuned.

`static var smooth: Spring`

A smooth spring with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Spring`

A smooth spring with a predefined duration and no bounce that can be tuned.

`static var snappy: Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

### Getting spring characteristics

`var bounce: Double`

How bouncy the spring is.

`var damping: Double`

Defines how the spring’s motion should be damped due to the forces of
friction.

`var dampingRatio: Double`

The amount of drag applied, as a fraction of the amount needed to produce
critical damping.

`var duration: TimeInterval`

The perceptual duration, which defines the pace of the spring.

`var mass: Double`

The mass of the object attached to the end of the spring.

`var response: Double`

The stiffness of the spring, defined as an approximate duration in seconds.

`var settlingDuration: TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`var stiffness: Double`

The spring stiffness coefficient.

### Getting spring state

`func value<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the value of the spring at a given time given a target amount of
change.

`func value<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the value of the spring at a given time for a starting and ending
value for the spring to travel.

`func velocity<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a target amount of
change.

`func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a starting and
ending value for the spring to travel.

### Setting spring state

`func update<V>(value: inout V, velocity: inout V, target: V, deltaTime:
TimeInterval)`

Updates the current value and velocity of a spring.

### Calculating forces and durations

`func force<V>(target: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, target, and
velocity amount of change.

`func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, velocity, and
divisor from the starting and end values for the spring to travel.

`func settlingDuration<V>(target: V, initialVelocity: V, epsilon: Double) ->
TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V,
epsilon: Double) -> TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

Protocol

# Animatable

A type that describes how to animate a property of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol Animatable

## Topics

### Animating data

`var animatableData: Self.AnimatableData`

The data to animate.

**Required** Default implementations provided.

`associatedtype AnimatableData : VectorArithmetic`

The type defining the data to animate.

**Required**

## Relationships

### Inherited By

  * `AnimatableModifier`
  * `GeometryEffect`
  * `InsettableShape`
  * `Layout`
  * `Shape`
  * `VisualEffect`

### Conforming Types

  * `Angle`
  * `AnyLayout`
  * `AnyShape`
  * `ButtonBorderShape`
  * `Capsule`
  * `Circle`
  * `Color.Resolved`
  * `ContainerRelativeShape`
  * `EdgeInsets`
  * `EdgeInsets3D`
  * `Ellipse`
  * `EmptyVisualEffect`
  * `GridLayout`
  * `HStackLayout`
  * `OffsetShape`
  * `Path`
  * `Rectangle`
  * `RectangleCornerRadii`
  * `RotatedShape`
  * `RoundedRectangle`
  * `ScaledShape`
  * `StrokeStyle`
  * `TransformedShape`
  * `UnevenRoundedRectangle`
  * `UnitPoint`
  * `UnitPoint3D`
  * `VStackLayout`
  * `ZStackLayout`

## See Also

### Making data animatable

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

`struct EmptyAnimatableData`

An empty type for animatable data.

Structure

# AnimatablePair

A pair of animatable values, which is itself animatable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic

## Topics

### Creating an animatable pair

`init(First, Second)`

Creates an animated pair with the provided values.

### Getting the constituent animations

`var first: First`

The first value.

`var second: Second`

The second value.

### Manipulating values

`var magnitudeSquared: Double`

The dot-product of this animated pair with itself.

## Relationships

### Conforms To

  * `AdditiveArithmetic`
  * `Equatable`
  * `Sendable`
  * `VectorArithmetic`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

`struct EmptyAnimatableData`

An empty type for animatable data.

Protocol

# VectorArithmetic

A type that can serve as the animatable data of an animatable type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol VectorArithmetic : AdditiveArithmetic

## Overview

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar
multiplication and a way to query the vector magnitude of the value. Use this
type as the `animatableData` associated type of a type that conforms to the
`Animatable` protocol.

## Topics

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

## Relationships

### Inherits From

  * `AdditiveArithmetic`
  * `Equatable`

### Conforming Types

  * `AnimatablePair`
  * `EmptyAnimatableData`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`struct EmptyAnimatableData`

An empty type for animatable data.

Structure

# EmptyAnimatableData

An empty type for animatable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyAnimatableData

## Overview

This type is suitable for use as the `animatableData` property of types that
do not have any animatable properties.

## Topics

### Creating the data

`init()`

### Manipulating the data

`var magnitudeSquared: Double`

The dot-product of this animatable data instance with itself.

## Relationships

### Conforms To

  * `AdditiveArithmetic`
  * `Equatable`
  * `Sendable`
  * `VectorArithmetic`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

Article

# Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

## Overview

When you schedule periodic updates to your user interface with `TimelineView`,
updates continue to run even when your app is in the `ScenePhase.background`
or `ScenePhase.inactive` state, making this an ideal choice for keeping a
watchOS app up-to-date while in the Always On state. Additionally, you can use
a `TimelineView` to drive other changes — such as animation — when your app is
running in the foreground.

### Set up the timeline

Specify the part of your user interface that receives periodic updates using a
`TimelineView`.

The `TimelineView` structure takes a schedule that determines when the system
makes updates. It also takes a `ViewBuilder` that defines the updatable
content. The system then calls the view builder, passing the context for each
update.

The `TimelineView.Context` instance contains both the time and the current
`TimelineView.Context.Cadence` for the updates. When creating the updatable
content for the `TimelineView`, use the time from the context, not the current
system time. When in Always On, the system may request views up to 5 minutes
in the future.

The cadence also indicates the current maximum rate for updates that the
`TimelineView` receives:

`TimelineView.Context.Cadence.live`

    

Receives high-frequency updates that are suitable for driving animation.

`TimelineView.Context.Cadence.seconds`

    

Receives up to one update per second.

`TimelineView.Context.Cadence.minutes`

    

Receives up to one update per minute.

The cadence can change from update to update. Always check the current value
and hide information that isn’t relevant. For example, a timer app may show
the time remaining in minutes, seconds, and hundredths of a second when it
receives updates at the `TimelineView.Context.Cadence.live` frequency. It can
also play animation at that frequency.

When the updates drop to the `TimelineView.Context.Cadence.seconds` frequency,
the app hides the hundredths of seconds and swaps the animation for a static
image. The countdown only shows minutes and seconds.

If the frequency drops to `TimelineView.Context.Cadence.minutes`, the app also
hides the seconds and only shows the time remaining to the nearest minute.

### Specify the schedule

When you create a `TimelineView`, you must specify the update schedule, which
is an instance that adopts the `TimelineSchedule` protocol. While you can
create your own custom schedules, SwiftUI provides schedules for many common
use cases.

The system attempts to trigger updates based on the schedule, but it can delay
or defer an update based on the system’s current state. Additionally, if the
schedule is more frequent than the current cadence, the system throttles the
updates to the cadence.

Common schedules include:

`EveryMinuteTimelineSchedule`

    

A schedule to update the `TimelineView` every minute. These updates align with
the system clock. For example, if the schedule starts at 1:00 pm, you’d get
updates at 1:01, 1:02, 1:03, and so on.

`PeriodicTimelineSchedule`

    

A schedule to update your interface at a regular, repeating interval. When you
create this schedule, you specify the starting time and the interval between
updates.

`AnimationTimelineSchedule`

    

A schedule to create a `TimelineView` instance with high-frequency updates for
animated content. When you create the schedule, you can set both the minimum
interval and a Boolean value that indicates whether the animation is currently
paused. If you don’t set a minimum interval, the system picks an appropriate
update interval. Additionally, it only updates the view when the paused
parameter is `false`.

`ExplicitTimelineSchedule`

    

A schedule to specify a list of update times. For example, an app that plays
audiobooks might schedule updates for the beginning of each chapter. When you
create an explicit timeline, you pass a `Sequence`, such as an `Array` of
`Date` instances. The system updates the `TimelineView` at the time specified
by each date in the sequence.

### Update during always on

You can use timeline views to update your watchOS app while it’s in the Always
On state; however, you must be able to specify the view’s contents given a
`Date` instance for a time in the future. To improve performance, the system
may ask for views up to 5 minutes in the future. For example, an egg timer
could use a `TimelineView` to display the time remaining during Always On
because it can calculate the amount of time remaining given any arbitrary time
in the future.

When your app is active and in the foreground, the timeline schedule runs in
the `TimelineScheduleMode.normal` mode, and your `TimelineView` can receive
updates at the `TimelineView.Context.Cadence.live` cadence. When your app
transitions into Always On, the timeline schedule also transitions into the
`TimelineScheduleMode.lowFrequency` mode, the cadence generally drops, and the
system may batch-load future updates.

Note

In the Always On state, apps running a background session may not need to use
a `TimelineView` to update their user interface. Any changes the app makes
while running in the background continue to update its interface; however, to
preserve battery life, the system only refreshes the user interface about once
per second. For more information, see Designing your app for the Always On
state.

While the actual cadence can vary depending on the requested schedule and the
current state of the system, apps generally receive an update frequency based
on whether they have background runtime or are inactive, frontmost apps.

Apps with background runtime receive updates at the
`TimelineView.Context.Cadence.seconds` frequency. This would include apps with
an active background session (like workout or background audio apps) or apps
executing a background refresh task.

Inactive apps receive updates as long as they remain in the frontmost state,
generally at the `TimelineView.Context.Cadence.minutes` frequency. However, if
you request a short burst of updates at the
`TimelineView.Context.Cadence.seconds` frequency, the system provides that
cadence if possible.

For example, an egg timer could use an `ExplicitTimelineSchedule` to set up
per-minute updates for most of the countdown, and switch to per-second updates
for the last minute. If conditions permit, the system provides
`TimelineView.Context.Cadence.seconds` updates for the last minute.

## See Also

### App experience

API Reference

Setting up a watchOS project

Create a new watchOS project or add a watch target to an existing iOS project.

Creating independent watchOS apps

Set up a watchOS app that installs and runs without a companion iOS app.

Keeping your watchOS content up to date

Ensure that your app’s content is relevant and up to date.

Authenticating users on Apple Watch

Create an account sign-up and sign-in strategy for your app.

Responding to the Action button on Apple Watch Ultra

Use App Intents to register actions for your app.

Structure

# TimelineView

A view that updates according to a schedule that you provide.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct TimelineView<Schedule, Content> where Schedule : TimelineSchedule

## Overview

A timeline view acts as a container with no appearance of its own. Instead, it
redraws the content it contains at scheduled points in time. For example, you
can update the face of an analog timer once per second:

The closure that creates the content receives an input of type
`TimelineView.Context` that you can use to customize the content’s appearance.
The context includes the `date` that triggered the update. In the example
above, the timeline view sends that date to an analog timer that you create so
the timer view knows how to draw the hands on its face.

The context also includes a `cadence` property that you can use to hide
unnecessary detail. For example, you can use the cadence to decide when it’s
appropriate to display the timer’s second hand:

The system might use a cadence that’s slower than the schedule’s update rate.
For example, a view on watchOS might remain visible when the user lowers their
wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the
`TimelineSchedule` protocol, or use one of the built-in schedule types:

  * Use an `everyMinute` schedule to update at the beginning of each minute.

  * Use a `periodic(from:by:)` schedule to update periodically with a custom start time and interval between updates.

  * Use an `explicit(_:)` schedule when you need a finite number, or irregular set of updates.

For a schedule containing only dates in the past, the timeline view shows the
last date in the schedule. For a schedule containing only dates in the future,
the timeline draws its content using the current date until the first
scheduled date arrives.

## Topics

### Creating a timeline

`init(Schedule, content: (TimelineViewDefaultContext) -> Content)`

Creates a new timeline view that uses the given schedule.

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

`struct Context`

Information passed to a timeline view’s content callback.

### Deprecated symbols

`init(Schedule, content: (TimelineView<Schedule, Content>.Context) ->
Content)`

Creates a new timeline view that uses the given schedule.

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `View`

Conforms when `Schedule` conforms to `TimelineSchedule` and `Content` conforms
to `View`.

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`protocol TimelineSchedule`

A type that provides a sequence of dates for use as a schedule.

`typealias TimelineViewDefaultContext`

Information passed to a timeline view’s content callback.

Protocol

# TimelineSchedule

A type that provides a sequence of dates for use as a schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol TimelineSchedule

## Overview

Types that conform to this protocol implement a particular kind of schedule by
defining an `entries(from:mode:)` method that returns a sequence of dates. Use
a timeline schedule type when you initialize a `TimelineView`. For example,
you can create a timeline view that updates every second, starting from some
`startDate`, using a periodic schedule returned by `periodic(from:by:)`:

You can also create custom timeline schedules. The timeline view updates its
content according to the sequence of dates produced by the schedule.

## Topics

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

### Getting a sequence of dates

`func entries(from: Date, mode: Self.Mode) -> Self.Entries`

Provides a sequence of dates starting around a given date.

**Required**

` associatedtype Entries : Sequence`

The sequence of dates within a schedule.

**Required**

### Specifying a mode

`typealias Mode`

An alias for the timeline schedule update mode.

`enum TimelineScheduleMode`

A mode of operation for timeline schedule updates.

### Supporting types

`struct AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

`struct EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

`struct ExplicitTimelineSchedule`

A schedule for updating a timeline view at explicit points in time.

`struct PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

## Relationships

### Conforming Types

  * `AnimationTimelineSchedule`
  * `EveryMinuteTimelineSchedule`
  * `ExplicitTimelineSchedule`
  * `PeriodicTimelineSchedule`

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`struct TimelineView`

A view that updates according to a schedule that you provide.

`typealias TimelineViewDefaultContext`

Information passed to a timeline view’s content callback.

Type Alias

# TimelineViewDefaultContext

Information passed to a timeline view’s content callback.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    typealias TimelineViewDefaultContext = TimelineView<EveryMinuteTimelineSchedule, Never>.Context

## Discussion

The context includes both the date from the schedule that triggered the
callback, and a cadence that you can use to customize the appearance of your
view. For example, you might choose to display the second hand of an analog
clock only when the cadence is `TimelineView.Context.Cadence.seconds` or
faster.

Note

This type alias uses a specific concrete instance of `TimelineView.Context`
that all timeline views can use. It does this to prevent introducing an
unnecessary generic parameter dependency on the context type.

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`struct TimelineView`

A view that updates according to a schedule that you provide.

`protocol TimelineSchedule`

A type that provides a sequence of dates for use as a schedule.

Instance Method

# matchedGeometryEffect(id:in:properties:anchor:isSource:)

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func matchedGeometryEffect<ID>(
        id: ID,
        in namespace: Namespace.ID,
        properties: MatchedGeometryProperties = .frame,
        anchor: UnitPoint = .center,
        isSource: Bool = true
    ) -> some View where ID : Hashable
    

##  Parameters

`id`

    

The identifier, often derived from the identifier of the data being displayed
by the view.

`namespace`

    

The namespace in which defines the `id`. New namespaces are created by adding
an `@Namespace` variable to a `View` type and reading its value in the view’s
body method.

`properties`

    

The properties to copy from the source view.

`anchor`

    

The relative location in the view used to produce its shared position value.

`isSource`

    

True if the view should be used as the source of geometry for other views in
the group.

## Return Value

A new view that defines an entry in the global database of views synchronizing
their geometry.

## Discussion

This method sets the geometry of each view in the group from the inserted view
with `isSource = true` (known as the “source” view), updating the values
marked by `properties`.

If inserting a view in the same transaction that another view with the same
key is removed, the system will interpolate their frame rectangles in window
space to make it appear that there is a single view moving from its old
position to its new position. The usual transition mechanisms define how each
of the two views is rendered during the transition (e.g. fade in/out, scale,
etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of
the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true`
is not exactly one results are undefined, due to it not being clear which is
the source view.

## See Also

### Synchronizing geometries

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Structure

# MatchedGeometryProperties

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct MatchedGeometryProperties

## Topics

### Matching properties

`static let frame: MatchedGeometryProperties`

Both the `position` and `size` properties.

`static let position: MatchedGeometryProperties`

The view’s position, in window coordinates.

`static let size: MatchedGeometryProperties`

The view’s size, in local coordinates.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Protocol

# GeometryEffect

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol GeometryEffect : Animatable, ViewModifier where Self.Body == Never

## Overview

The only change the effect makes to the view’s ancestors and descendants is to
change the coordinate transform to and from them.

## Topics

### Applying effects

`func effectValue(size: CGSize) -> ProjectionTransform`

Returns the current value of the effect.

**Required**

` func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>`

Returns an effect that produces the same geometry transform as this effect,
but only applies the transform while rendering its view.

## Relationships

### Inherits From

  * `Animatable`
  * `ViewModifier`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Structure

# Namespace

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct Namespace

## Topics

### Creating a namespace

`init()`

### Getting the namespace

`var wrappedValue: Namespace.ID`

`struct ID`

A namespace defined by the persistent identity of an `@Namespace` dynamic
property.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Instance Method

# geometryGroup()

Isolates the geometry (e.g. position and size) of the view from its parent
view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func geometryGroup() -> some View
    

## Discussion

By default SwiftUI views push position and size changes down through the view
hierarchy, so that only views that draw something (known as leaf views) apply
the current animation to their frame rectangle. However in some cases this
coalescing behavior can give undesirable results; inserting a geometry group
can correct that. A group acts as a barrier between the parent view and its
subviews, forcing the position and size values to be resolved and animated by
the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member
views of each row in the stack apply (and animate as) a single geometric
transform from their ancestor view, rather than letting the effects of the
ancestor views be applied separately to each leaf view. If the members of
`ItemView` may be added and removed at different times the group ensures that
they stay locked together as animations are applied.

Returns: a new view whose geometry is isolated from that of its parent view.

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transition<T>(_ transition: T) -> some View where T : Transition
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a custom RotatingFadeTransition transition to show it.

## See Also

### Defining transitions

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transition(_ t: AnyTransition) -> some View
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a slide transition to show it.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Protocol

# Transition

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol Transition

## Overview

A transition should generally be made by applying one or more modifiers to the
`content`. For symmetric transitions, the `isIdentity` property on `phase` can
be used to change the properties of modifiers. For asymmetric transitions, the
phase itself can be used to change those properties. Transitions should not
use any identity-affecting changes like `.id`, `if`, and `switch` on the
`content`, since doing so would reset the state of the view they’re applied
to, causing wasted work and potentially surprising behavior when it appears
and disappears.

The following code defines a transition that can be used to change the opacity
and rotation when a view appears and disappears.

  * See Also: `TransitionPhase`

  * See Also: `AnyTransition`

## Topics

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

### Configuring a transition

`func animation(Animation?) -> some Transition`

Attaches an animation to this transition.

`static var properties: TransitionProperties`

Returns the properties this transition type has.

**Required** Default implementation provided.

### Using a transition

`func apply<V>(content: V, phase: TransitionPhase) -> some View`

`func combined<T>(with: T) -> some Transition`

### Creating a custom transition

`func body(content: Self.Content, phase: TransitionPhase) -> Self.Body`

Gets the current body of the caller.

**Required**

` associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

## Relationships

### Conforming Types

  * `AsymmetricTransition`
  * `BlurReplaceTransition`
  * `IdentityTransition`
  * `MoveTransition`
  * `OffsetTransition`
  * `OpacityTransition`
  * `PushTransition`
  * `ScaleTransition`
  * `SlideTransition`
  * `SymbolEffectTransition`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# TransitionProperties

The properties a `Transition` can have.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct TransitionProperties

## Overview

A transition can have properties that specify high level information about it.
This can determine how a transition interacts with other features like
Accessibility settings.

  * See Also: `Transition`

## Topics

### Creating the transition properties

`init(hasMotion: Bool)`

`var hasMotion: Bool`

Whether the transition includes motion.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Enumeration

# TransitionPhase

An indication of which the current stage of a transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    enum TransitionPhase

## Overview

When a view is appearing with a transition, the transition will first be shown
with the `willAppear` phase, then will be immediately moved to the `identity`
phase. When a view is being removed, its transition is changed from the
`identity` phase to the `didDisappear` phase. If a view is removed while it is
still transitioning in, then its phase will change to `didDisappear`. If a
view is re-added while it is transitioning out, its phase will change back to
`identity`.

In the `identity` phase, transitions should generally not make any visual
change to the view they are applied to, since the transition’s view
modifications in the `identity` phase will be applied to the view as long as
it is visible. In the `willAppear` and `didDisappear` phases, transitions
should apply a change that will be animated to create the transition. If no
animatable change is applied, then the transition will be a no-op.

  * See Also: `Transition`

  * See Also: `AnyTransition`

## Topics

### Getting the phase

`case identity`

The transition is being applied to a view that is in the view hierarchy.

`case willAppear`

The transition is being applied to a view that is about to be inserted into
the view hierarchy.

`case didDisappear`

The transition is being applied to a view that has been requested to be
removed from the view hierarchy.

### Getting phase characteristics

`var isIdentity: Bool`

A Boolean that indicates whether the transition should have an identity
effect, i.e. not change the appearance of its view.

`var value: Double`

A value that can be used to multiply effects that are applied differently
depending on the phase.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# AsymmetricTransition

A composite `Transition` that uses a different transition for insertion versus
removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AsymmetricTransition<Insertion, Removal> where Insertion : Transition, Removal : Transition

## Topics

### Creating the transition

`init(insertion: Insertion, removal: Removal)`

Creates a composite `Transition` that uses a different transition for
insertion versus removal.

### Getting transition properties

`var insertion: Insertion`

The `Transition` defining the insertion phase of `self`.

`var removal: Removal`

The `Transition` defining the removal phase of `self`.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# AnyTransition

A type-erased transition.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyTransition

## Overview

  * See Also: `Transition`

## Topics

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

### Creating a custom transition

`init<T>(T)`

Create an instance that type-erases `transition`.

`static func modifier<E>(active: E, identity: E) -> AnyTransition`

Returns a transition defined between an active modifier and an identity
modifier.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# contentTransition

The current method of animating the contents of views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransition: ContentTransition { get set }

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# contentTransitionAddsDrawingGroup

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransitionAddsDrawingGroup: Bool { get set }

## Discussion

Setting this value to `true` causes SwiftUI to wrap content transitions with a
`drawingGroup(opaque:colorMode:)` modifier.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# ContentTransition

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ContentTransition

## Overview

Set the behavior of content transitions within a view with the
`contentTransition(_:)` modifier, passing in one of the defined transitions,
such as `opacity` or `interpolate` as the parameter.

Tip

Content transitions only take effect within transactions that apply an
`Animation` to the views inside the `contentTransition(_:)` modifier.

Content transitions only take effect within the context of an `Animation`
block.

## Topics

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# PlaceholderContentView

A placeholder used to construct an inline modifier, transition, or other
helper type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PlaceholderContentView<Value>

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `View`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

Function

# withTransaction(_:_:)

Executes a closure with the specified transaction and returns the result.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withTransaction<Result>(
        _ transaction: Transaction,
        _ body: () throws -> Result
    ) rethrows -> Result

##  Parameters

`transaction `

    

An instance of a transaction, set as the thread’s current transaction.

`body`

    

A closure to execute.

## Return Value

The result of executing the closure with the specified transaction.

## See Also

### Moving an animation to another view

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Function

# withTransaction(_:_:_:)

Executes a closure with the specified transaction key path and value and
returns the result.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withTransaction<R, V>(
        _ keyPath: WritableKeyPath<Transaction, V>,
        _ value: V,
        _ body: () throws -> R
    ) rethrows -> R

##  Parameters

`keyPath`

    

A key path that indicates the property of the `Transaction` structure to
update.

`value`

    

The new value to set for the item specified by `keyPath`.

`body`

    

A closure to execute.

## Return Value

The result of executing the closure with the specified transaction value.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
    

##  Parameters

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical animations controlled by a button that executes all three
animations simultaneously:

  * The first animation rotates the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third animation uses the `transaction(_:)` modifier to replace the rotation animation affecting the “Animation\nReplaced” `Text` view with a spring animation.

The following code implements these animations:

Use this modifier on leaf views such as `Image` or `Button` rather than
container views such as `VStack` or `HStack`. The transformation applies to
all child views within this view; calling `transaction(_:)` on a container
view can lead to unbounded scope of execution depending on the depth of the
view hierarchy.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(value:_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction(
        value: some Equatable,
        _ transform: @escaping (inout Transaction) -> Void
    ) -> some View
    

##  Parameters

`value`

    

A value to monitor for changes.

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view whenever `value` changes.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical views controlled by a button that changes all three
simultaneously:

  * The first view animates rotating the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\nReplaced” `Text` view.

The following code implements these animations:

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:body:)

Applies the given transaction mutation function to all animations used within
the `body` closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction<V>(
        _ transform: @escaping (inout Transaction) -> Void,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the changes to the transaction performed in the `transform` will only
affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation,
while the contents of MyView are animated with the implicit transaction:

  * See Also: `Transaction.disablesAnimations`

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Structure

# Transaction

The context of the current state-processing update.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Transaction

## Overview

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed,
plus any global values set by calling `withTransaction(_:_:)` or
`withAnimation(_:_:)`.

## Topics

### Creating a transaction

`init()`

Creates a transaction.

`init(animation: Animation?)`

Creates a transaction and assigns its animation property.

### Managing animations

`var animation: Animation?`

The animation, if any, associated with the current state change.

`var disablesAnimations: Bool`

A Boolean value that indicates whether views should disable animations.

`func addAnimationCompletion(criteria: AnimationCompletionCriteria, () ->
Void)`

Adds a completion to run when the animations created with this transaction are
all complete.

### Managing window dismissal

`var dismissBehavior: DismissBehavior`

The behavior for how windows will dismiss programmatically when used in
conjunction with `DismissWindowAction`.

### Getting information about a transaction

`var isContinuous: Bool`

A Boolean value that indicates whether the transaction originated from an
action that produces a sequence of values.

`var scrollTargetAnchor: UnitPoint?`

The preferred alignment of the view within a scroll view’s visible region when
scrolling to a view.

`var tracksVelocity: Bool`

Whether this transaction will track the velocity of any animatable properties
that change.

`subscript<K>(K.Type) -> K.Value`

Accesses the transaction value associated with a custom key.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`protocol TransactionKey`

A key for accessing values in a transaction.

Protocol

# TransactionKey

A key for accessing values in a transaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol TransactionKey

## Overview

You can create custom transaction values by extending the `Transaction`
structure with new properties. First declare a new transaction key type and
specify a value for the required `defaultValue` property:

The Swift compiler automatically infers the associated `Value` type as the
type you specify for the default value. Then use the key to define a new
transaction value property:

Clients of your transaction value never use the key directly. Instead, they
use the key path of your custom transaction value property. To set the
transaction value for a change, wrap that change in a call to
`withTransaction`:

To set it for a view and all its subviews, add the `transaction(value:_:)`
view modifier to that view:

To use the value from inside `MyView` or one of its descendants, use the
`transaction(_:)` view modifier:

## Topics

### Setting a default value

`static var defaultValue: Self.Value`

The default value for the transaction key.

**Required**

` associatedtype Value`

The associated type representing the type of the transaction key’s value.

**Required**

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

Protocol

# AnimatableModifier

A modifier that can create another modifier with animation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    protocol AnimatableModifier : Animatable, ViewModifier

Deprecated

Use `Animatable` instead.

## Relationships

### Inherits From

  * `Animatable`
  * `ViewModifier`



# AccessibilityLabeledPairRole

Case

# AccessibilityLabeledPairRole.content

This element represents the content part of the label / content pair.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case content

## Discussion

For example, it might be the custom control itself.

## See Also

### Getting roles

`case label`

This element represents the label part of the label / content pair.

Case

# AccessibilityLabeledPairRole.label

This element represents the label part of the label / content pair.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case label

## Discussion

For example, it might be the explanatory text to the left of a control,
describing what the control does.

## See Also

### Getting roles

`case content`

This element represents the content part of the label / content pair.



# AnimationContext

Instance Property

# state

The current state of a custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var state: AnimationState<Value>

## Discussion

An instance of `CustomAnimation` uses this property to read and write state
values as the animation runs.

An alternative to using the `state` property in a custom animation is to
create an `AnimationStateKey` type and extend `AnimationContext` with a custom
property that returns the state as a custom type. For example, the following
code creates a state key named `PausableState`. It’s convenient to store state
values in the key type, so the `PausableState` structure includes properties
for the stored state values `paused` and `pauseTime`.

To provide access the pausable state, the following code extends
`AnimationContext` to include the `pausableState` property. This property
returns an instance of the custom `PausableState` structure stored in `state`,
and it can also store a new `PausableState` instance in `state`.

Now a custom animation can use the `pausableState` property instead of the
`state` property as a convenient way to read and write state values as the
animation runs.

Instance Property

# environment

The current environment of the view that created the custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var environment: EnvironmentValues { get }

## Discussion

An instance of `CustomAnimation` uses this property to read environment values
from the view that created the animation. To learn more about environment
values including how to define custom environment values, see
`EnvironmentValues`.

Instance Method

# withState(_:)

Creates a new context from another one with a state that you provide.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func withState<T>(_ state: AnimationState<T>) -> AnimationContext<T> where T : VectorArithmetic

##  Parameters

`state`

    

The initial state for the new context.

## Return Value

A new context that contains the specified state.

## Discussion

Use this method to create a new context that contains the state that you
provide and view environment values from the original context.

Instance Property

# isLogicallyComplete

Set this to `true` to indicate that an animation is logically complete.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isLogicallyComplete: Bool

## Discussion

This controls when AnimationCompletionCriteria.logicallyComplete completion
callbacks are fired. This should be set to `true` at most once in the life of
an animation, changing back to `false` later will be ignored. If this is never
set to `true`, the behavior is equivalent to if this had been set to `true`
just as the animation finished (by returning `nil`).



# AccessoryLinearGaugeStyle

Initializer

# init()

Creates an accessory linear gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# AccessoryLinearCapacityGaugeStyle

Initializer

# init()

Creates an accessory linear capacity gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# AutomaticImmersionStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# Axis

Case

# Axis.horizontal

The horizontal dimension.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case horizontal

## See Also

### Getting axes

`case vertical`

The vertical dimension.

Case

# Axis.vertical

The vertical dimension.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case vertical

## See Also

### Getting axes

`case horizontal`

The horizontal dimension.

Structure

# Axis.Set

An efficient set of axes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting axis sets

`static let horizontal: Axis.Set`

`static let vertical: Axis.Set`

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`



# Auxiliary view modifiers

Article

# Configure your apps navigation titles

Use a navigation title to display the current navigation state of an
interface.

## Overview

On iOS and watchOS, when a view is navigated to inside of a navigation stack,
that view’s title is displayed in the navigation bar. On iPadOS, the primary
destination’s navigation title is reflected as the window’s title in the App
Switcher. Similarly on macOS, the primary destination’s title is used as the
window title in the titlebar, Windows menu and Mission Control.

In its simplest form, you can provide a string or a localized string key to a
navigation title modifier directly.

The title of your apps toolbar can be further customized using additional
navigation related modifiers. For example, you can associate a `URL` or your
own type conforming to `Transferable` to your view using the navigation
document modifier.

In iOS and iPadOS, this will construct a title that can present a menu by
tapping the navigation title in the app’s navigation bar. The menu contains
content providing information related to the URL and a draggable icon for
sharing.

In macOS, this item will construct a proxy icon for manipulating the file
backing the document.

When providing a transferable type, you should typically provide a
`SharePreview` which provides the appropriate content for rendering the
preview in the header of the menu.

### Renaming

You can provide a text binding to the navigation title modifier and SwiftUI
will automatically configure the toolbar to allow editing of the navigation
title on iOS or macOS. SwiftUI automatically syncs the navigation title with
the value of the string binding provided to the text field.

You can provide a string binding to the navigation title to configure the
title’s text field. SwiftUI will automatically place a rename action in the
titl menu alongside the actions originating from your app’s commands.

In iOS, when using a text field in a navigation title, SwiftUI creates a
button in the toolbar title. When triggered, this button updates the
navigation title to display an inline text field that will update the binding
you provide as the user types.

## See Also

### Navigation titles

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

Instance Method

# contextMenu(menuItems:)

Adds a context menu to a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0–7.0  Deprecated  visionOS 1.0+

    
    
    func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

## Return Value

A view that can display a context menu.

## Discussion

Use this modifier to add a context menu to a view in your app’s user
interface. Compose the menu by returning controls like `Button`, `Toggle`, and
`Picker` from the `menuItems` closure. You can also use `Menu` to define
submenus or `Section` to group items.

The following example creates a `Text` view that has a context menu with two
buttons:

People can activate the menu with an action like Control-clicking, or by using
the touch and hold gesture in iOS and iPadOS:

The system dismisses the menu if someone makes a selection, or taps or clicks
outside the menu.

If you want to show a preview beside the menu, use
`contextMenu(menuItems:preview:)`. To add a context menu to a container that
supports selection, like a `List` or a `Table`, and to distinguish between
menu activation on a selection and activation in an empty area of the
container, use `contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(menuItems:preview:)

Adds a context menu with a preview to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    func contextMenu<M, P>(
        @ViewBuilder menuItems: () -> M,
        @ViewBuilder preview: () -> P
    ) -> some View where M : View, P : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

`preview`

    

A view that the system displays along with the menu.

## Return Value

A view that can display a context menu with a preview.

## Discussion

When you use this modifer to add a context menu to a view in your app’s user
interface, the system shows a preview beside the menu. Compose the menu by
returning controls like `Button`, `Toggle`, and `Picker` from the `menuItems`
closure. You can also use `Menu` to define submenus or `Section` to group
items.

Define the preview by returning a view from the `preview` closure. The system
sizes the preview to match the size of its content. For example, you can add a
two button context menu to a `Text` view, and include an `Image` as a preview:

When someone activates the context menu with an action like touch and hold in
iOS or iPadOS, the system displays the image and the menu:

Note

This view modifier produces a context menu on macOS, but that platform doesn’t
display the preview.

If you don’t need a preview, use `contextMenu(menuItems:)` instead. If you
want to add a context menu to a container that supports selection, like a
`List` or a `Table`, and you want to distinguish between menu activation on a
selection and activation in an empty area of the container, use
`contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(forSelectionType:menu:primaryAction:)

Adds an item-based context menu to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func contextMenu<I, M>(
        forSelectionType itemType: I.Type = I.self,
        @ViewBuilder menu: @escaping (Set<I>) -> M,
        primaryAction: ((Set<I>) -> Void)? = nil
    ) -> some View where I : Hashable, M : View
    

##  Parameters

`itemType`

    

The identifier type of the items. Ensure that this matches the container’s
selection type.

`menu`

    

A closure that produces the menu. A single parameter to the closure contains
the set of items to act on. An empty set indicates menu activation over the
empty area of the selectable container, while a non-empty set indicates menu
activation over selected items. Use controls like `Button`, `Picker`, and
`Toggle` to define the menu items. You can also create submenus using `Menu`,
or group items with `Section`. You can deactivate the context menu by
returning nothing from the closure.

`primaryAction`

    

A closure that defines the action to perform in response to the primary
interaction. A single parameter to the closure contains the set of items to
act on.

## Return Value

A view that can display an item-based context menu.

## Discussion

You can add an item-based context menu to a container that supports selection,
like a `List` or a `Table`. In the closure that you use to define the menu,
you receive a collection of items that depends on the selection state of the
container and the location where the person clicks or taps to activate the
menu. The collection contains:

  * The selected item or items, when people initiate the context menu from any selected item.

  * Nothing, if people tap or click to activate the context menu from an empty part of the container. This is true even when one or more items is currently selected.

You can vary the menu contents according to the number of selected items. For
example, the following code has a list that defines an empty area menu, a
single item menu, and a multi-item menu:

The above example assumes that the `Item` type conforms to the `Identifiable`
protocol, and relies on the associated `ID` type for both selection and
context menu presentation.

If you add the modifier to a view hierarchy that doesn’t have a container that
supports selection, the context menu never activates. To add a context menu
that doesn’t depend on selection behavior, use `contextMenu(menuItems:)`. To
add a context menu to a specific row in a table, use
`contextMenu(menuItems:)`.

### Add a primary action

Optionally, you can add a custom primary action to the context menu. In macOS,
a single click on a row in a selectable container selects that row, and a
double click performs the primary action. In iOS and iPadOS, tapping on the
row activates the primary action. To select a row without performing an
action, either enter edit mode or hold shift or command on a keyboard while
tapping the row.

For example, you can modify the context menu from the previous example so that
double clicking the row on macOS opens a new window for selected items. Get
the `OpenWindowAction` from the environment:

Then call `openWindow` from inside the `primaryAction` closure for each item:

The open window action depends on the declaration of a `WindowGroup` scene in
your `App` that responds to the `Item` type:

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

Instance Method

# badge(_:)

Generates a badge for the view from a text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ label: Text?) -> some View
    

##  Parameters

`label`

    

An optional `Text` view to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

Use this initializer when you want to style a `Text` view for use as a badge.
The following example customizes the badge with the `monospacedDigit()`,
`foregroundColor(_:)`, and `bold()` modifiers.

Styling the text view has no effect when the badge appears in a `TabView`.

## See Also

### Displaying a badge on a list item

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge<S>(_ label: S?) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

An optional string to display as a badge. Set the value to `nil` to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:)`. The following example shows a list with a “Default”
badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ key: LocalizedStringKey?) -> some View
    

##  Parameters

`key`

    

An optional string key to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`. The following example shows a list with a
“Default” badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from an integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ count: Int) -> some View
    

##  Parameters

`count`

    

An integer value to display in the badge. Set the value to zero to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count`
represented by a badge on one of the rows:

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badgeProminence(_:)

Specifies the prominence of badges created by this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func badgeProminence(_ prominence: BadgeProminence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply to badges.

## Discussion

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# help(_:)

Adds help text to a view using a localized string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ textKey: LocalizedStringKey) -> some View
    

##  Parameters

`textKey`

    

The key for the localized text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help<S>(_ text: S) -> some View where S : StringProtocol
    

##  Parameters

`text`

    

The text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a text view that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ text: Text) -> some View
    

##  Parameters

`text`

    

The `Text` view to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

Instance Method

# statusBarHidden(_:)

Sets the visibility of the status bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func statusBarHidden(_ hidden: Bool = true) -> some View
    

##  Parameters

`hidden`

    

A Boolean value that indicates whether to hide the status bar.

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# touchBar(content:)

Sets the content that the Touch Bar displays.

macOS 10.15+

    
    
    func touchBar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A collection of views to be displayed by the Touch Bar.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the
Touch Bar. The content is displayed by the Touch Bar when appropriate,
depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and
then added to the Touch Bar:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBar(_:)

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

macOS 10.15+

    
    
    func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View
    

##  Parameters

`touchBar`

    

A collection of views that the Touch Bar displays.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` to provide a static set of views that are displayed by the
Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content
the Touch Bar displays:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPrincipal(_:)

Sets principal views that have special significance to this Touch Bar.

macOS 10.15+

    
    
    func touchBarItemPrincipal(_ principal: Bool = true) -> some View
    

##  Parameters

`principal`

    

A Boolean value that indicates whether to display this view prominently in the
Touch Bar compared to other views.

## Return Value

A Touch Bar view with one element centered in the Touch Bar row.

## Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in
the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch
Bar view.

Note

Multiple visible bars may each specify a principal view, but the system only
honors one of them.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarCustomizationLabel(_:)

Sets a user-visible string that identifies the view’s functionality.

macOS 10.15+

    
    
    func touchBarCustomizationLabel(_ label: Text) -> some View
    

##  Parameters

`label`

    

A `Text` view containing the customization label.

## Return Value

A Touch Bar element with a set customization label.

## Discussion

This string is visible during user customization.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPresence(_:)

Sets the behavior of the user-customized view.

macOS 10.15+

    
    
    func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View
    

##  Parameters

`presence`

    

One of the allowed `TouchBarItemPresence` descriptions.

## Return Value

A trait that describes the behavior for this Touch Bar view.

## Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a
particular Touch Bar view during customization by the user.

Touch Bar views may be:

  * `.required`: not allowed to be removed by the user.

  * `.default`: shown by default prior to user customization, but removable.

  * `.optional`: not visible by default, but can be added through the customization palette.

Each `TouchBarItemPresence` must be initialized with a string that is a
globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar
by default, except for the “Clubs” item. It’s set to `.optional` but is
configurable by the user:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.



# AnyGradient

Initializer

# init(_:)

Creates a new instance from the specified gradient.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ gradient: Gradient)

Instance Method

# colorSpace(_:)

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func colorSpace(_ space: Gradient.ColorSpace) -> AnyGradient

##  Parameters

`space`

    

The color space the new gradient will use to interpolate its constituent
colors.

## Return Value

A new gradient that interpolates its colors in the specified color space.

## Discussion



# Accessible appearance

Instance Property

# legibilityWeight

The font weight to apply to text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var legibilityWeight: LegibilityWeight? { get set }

## Discussion

This value reflects the value of the Bold Text display setting found in the
Accessibility settings.

## See Also

### Improving legibility

`var accessibilityShowButtonShapes: Bool`

Whether the system preference for Show Button Shapes is enabled.

`var accessibilityReduceTransparency: Bool`

Whether the system preference for Reduce Transparency is enabled.

`enum LegibilityWeight`

The Accessibility Bold Text user setting options.

Enumeration

# LegibilityWeight

The Accessibility Bold Text user setting options.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum LegibilityWeight

## Overview

The app can’t override the user’s choice before iOS 16, tvOS 16 or watchOS
9.0.

## Topics

### Getting weights

`case regular`

Use regular font weight (no Accessibility Bold).

`case bold`

Use heavier font weight (force Accessibility Bold).

### Creating a weight

`init?(UILegibilityWeight)`

Creates a legibility weight from its UILegibilityWeight equivalent.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Improving legibility

`var accessibilityShowButtonShapes: Bool`

Whether the system preference for Show Button Shapes is enabled.

`var accessibilityReduceTransparency: Bool`

Whether the system preference for Reduce Transparency is enabled.

`var legibilityWeight: LegibilityWeight?`

The font weight to apply to text.



# AutomaticMenuBarExtraStyle

Initializer

# init()

Creates an automatic menu bar extra style.

macOS 13.0+

    
    
    init()



# Anchor.Source

Type Method

# point(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func point(_ p: CGPoint) -> Anchor<Value>.Source

Available when `Value` is `CGPoint`.

## See Also

### Getting point anchor sources

`static func unitPoint(UnitPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

Type Method

# unitPoint(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func unitPoint(_ p: UnitPoint) -> Anchor<Value>.Source

Available when `Value` is `CGPoint`.

## See Also

### Getting point anchor sources

`static func point(CGPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

Type Method

# rect(_:)

Returns an anchor source rect defined by `r` in the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func rect(_ r: CGRect) -> Anchor<Value>.Source

Available when `Value` is `CGRect`.

## See Also

### Getting rectangle anchor sources

`static var bounds: Anchor<CGRect>.Source`

An anchor source rect defined as the entire bounding rect of the current view.

Available when `Value` is `CGRect`.

Type Property

# bounds

An anchor source rect defined as the entire bounding rect of the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bounds: Anchor<CGRect>.Source { get }

Available when `Value` is `CGRect`.

## See Also

### Getting rectangle anchor sources

`static func rect(CGRect) -> Anchor<Value>.Source`

Returns an anchor source rect defined by `r` in the current view.

Available when `Value` is `CGRect`.

Type Property

# topLeading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var topLeading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# top

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var top: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# topTrailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var topTrailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# leading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var leading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# center

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var center: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# trailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var trailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottomTrailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottomTrailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottom

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottom: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottomLeading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottomLeading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ anchor: Anchor<T>.Source?) where Value == T?

## See Also

### Creating an anchor source

`init<T>([Anchor<T>.Source])`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ array: [Anchor<T>.Source]) where Value == [T]

## See Also

### Creating an anchor source

`init<T>(Anchor<T>.Source?)`



# AnimationState

Initializer

# init()

Create an empty state container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()

## Discussion

You don’t typically create an instance of `AnimationState` directly. Instead,
the `AnimationContext` provides the animation state to an instance of
`CustomAnimation`.

Instance Subscript

# subscript(_:)

Accesses the state for a custom key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : AnimationStateKey { get set }

## Overview

Create a custom animation state value by defining a key that conforms to the
`AnimationStateKey` protocol and provide the `defaultValue` for the key. Also
include properties to read and write state values that your `CustomAnimation`
uses. For example, the following code defines a key named `PausableState` that
has two state values, `paused` and `pauseTime`:

Use that key with the subscript operator of the `AnimationState` structure to
get and set a value for the key. For more convenient access to the key value,
extend `AnimationContext` with a computed property that gets and sets the
key’s value.

To access the state values in a `CustomAnimation`, call the custom computed
property, then read and write the state values that the custom
`AnimationStateKey` provides.



# AccessoryCircularGaugeStyle

Initializer

# init()

Creates an accessory circular gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# AccessibilityDirectTouchOptions

Type Property

# requiresActivation

Prevents touch passthrough with the direct touch area until an assistive
technology, such as VoiceOver, has activated the direct touch area through a
user action, for example a double tap.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let requiresActivation: AccessibilityDirectTouchOptions

## See Also

### Getting the options

`static let silentOnTouch: AccessibilityDirectTouchOptions`

Allows a direct touch area to immediately receive touch events without an
assitive technology, such as VoiceOver, speaking. Appropriate for apps that
provide direct audio feedback on touch that would conflict with speech
feedback.

Type Property

# silentOnTouch

Allows a direct touch area to immediately receive touch events without an
assitive technology, such as VoiceOver, speaking. Appropriate for apps that
provide direct audio feedback on touch that would conflict with speech
feedback.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let silentOnTouch: AccessibilityDirectTouchOptions

## See Also

### Getting the options

`static let requiresActivation: AccessibilityDirectTouchOptions`

Prevents touch passthrough with the direct touch area until an assistive
technology, such as VoiceOver, has activated the direct touch area through a
user action, for example a double tap.

Initializer

# init(rawValue:)

Create a set of direct touch options

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(rawValue: AccessibilityDirectTouchOptions.RawValue)



# AccessibilityRotorContent

Instance Property

# body

The internal content of this `AccessibilityRotorContent`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @AccessibilityRotorContentBuilder
    var body: Self.Body { get }

**Required**

## See Also

### Supporting types

`associatedtype Body : AccessibilityRotorContent`

The type for the internal content of this `AccessibilityRotorContent`.

**Required**

Associated Type

# Body

The type for the internal content of this `AccessibilityRotorContent`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    associatedtype Body : AccessibilityRotorContent

**Required**

## See Also

### Supporting types

`var body: Self.Body`

The internal content of this `AccessibilityRotorContent`.

**Required**



# AccessibilityRotorContentBuilder

Type Method

# buildBlock(_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent, C5 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent, C5 : AccessibilityRotorContent, C6 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent, C5 : AccessibilityRotorContent, C6 : AccessibilityRotorContent, C7 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent, C5 : AccessibilityRotorContent, C6 : AccessibilityRotorContent, C7 : AccessibilityRotorContent, C8 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> some AccessibilityRotorContent where C0 : AccessibilityRotorContent, C1 : AccessibilityRotorContent, C2 : AccessibilityRotorContent, C3 : AccessibilityRotorContent, C4 : AccessibilityRotorContent, C5 : AccessibilityRotorContent, C6 : AccessibilityRotorContent, C7 : AccessibilityRotorContent, C8 : AccessibilityRotorContent, C9 : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildIf(_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildIf<Content>(_ content: Content?) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent
    

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : AccessibilityRotorContent

## See Also

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`



# AccessoryCircularCapacityGaugeStyle

Initializer

# init()

Creates an accessory circular capacity gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# Appearance modifiers

Instance Method

# backgroundStyle(_:)

Sets the specified style to render backgrounds within the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

## Discussion

The following example uses this modifier to set the `backgroundStyle`
environment value to a `blue` color that includes a subtle `gradient`. SwiftUI
fills the `Circle` shape that acts as a background element with this style:

To restore the default background style, set the `backgroundStyle` environment
value to `nil` using the `environment(_:_:)` modifer:

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:)

Sets a view’s foreground elements to use a given style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The color or pattern to use when filling in the foreground elements. To
indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or one
of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`. To
set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

## Return Value

A view that uses the given foreground style.

## Discussion

Use this method to style foreground content like text, shapes, and template
images (including symbols):

The example above creates a row of `teal` foreground elements:

You can use any style that conforms to the `ShapeStyle` protocol, like the
`teal` color in the example above, or the
`linearGradient(colors:startPoint:endPoint:)` gradient shown below:

Tip

If you want to fill a single `Shape` instance with a style, use the
`fill(style:)` shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a
`Color` that you load from an asset catalog can have different light and dark
appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a
style of their own, but instead modify other styles. In particular, they
modify the primary level of the current foreground style to the degree given
by the hierarchical style’s name. To find the current foreground style to
modify, SwiftUI looks for the innermost containing style that you apply with
the `foregroundStyle(_:)` or the `foregroundColor(_:)` modifier. If you
haven’t specified a style, SwiftUI uses the default foreground style, as in
the following example:

If you add a foreground style on the enclosing `VStack`, the hierarchical
styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect
for foreground elements in that view, or in any of its child views, that it
would otherwise gain from adding a background material — for example, using
the `background(_:ignoresSafeAreaEdges:)` modifier. However, hierarchical
styles applied to the default foreground don’t disable vibrancy.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:)

Sets the primary and secondary levels of the foreground style in the child
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2>(
        _ primary: S1,
        _ secondary: S2
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:_:)

Sets the primary, secondary, and tertiary levels of the foreground style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2, S3>(
        _ primary: S1,
        _ secondary: S2,
        _ tertiary: S3
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

`tertiary`

    

The tertiary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# allowedDynamicRange(_:)

Returns a new view configured with the specified allowed dynamic range.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func allowedDynamicRange(_ range: Image.DynamicRange?) -> some View
    

##  Parameters

`range`

    

the requested dynamic range, or nil to restore the default allowed range.

## Return Value

a new view.

## Discussion

The following example enables HDR rendering within a view hierarchy:

## See Also

### Colors and patterns

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

Instance Method

# tint(_:)

Sets the tint within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tint<S>(_ tint: S?) -> some View where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

Use this method to override the default accent color for this view with a
given styling. Unlike an app’s accent color, which can be overridden by user
preference, tint is always respected and should be used as a way to provide
additional meaning to the control.

Controls which are unable to style themselves using the given type of
`ShapeStyle` will try to approximate the styling as best as they can (i.e.
controls which can not style themselves using a gradient will attempt to use
the color of the gradient’s first stop).

This example shows a linear dashboard styled gauge tinted with a gradient from
`green` to `red`.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint(Color?) -> some View`

Sets the tint color within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# tint(_:)

Sets the tint color within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func tint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The tint `Color` to apply.

## Discussion

Use this method to override the default accent color for this view. Unlike an
app’s accent color, which can be overridden by user preference, the tint color
is always respected and should be used as a way to provide additional meaning
to the control.

This example shows Answer and Decline buttons with `green` and `red` tint
colors, respectively.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# listRowSeparatorTint(_:edges:)

Sets the tint color associated with a row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the row separators, or `nil` to use the default color
for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose row separators are
tinted based on row-specific data:

To hide a row separators, use `listRowSeparator(_:edges:)`. To hide or change
the tint color for a section separator, use `listSectionSeparator(_:edges:)`
and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparatorTint(_:edges:)

Sets the tint color associated with a section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the section separators, or `nil` to use the default
color for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are
tinted based on section-specific data:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To hide a
section separator, use `listSectionSeparator(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listItemTint(_:)

Sets a fixed tint color for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The color to use to tint the content. Use `nil` to avoid overriding the
inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

Note

This modifier is equivalent to using the version of the modifier that takes a
`ListItemTint` value and specifying the `tint` color in the corresponding
`fixed(_:)` input.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets the tint effect for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: ListItemTint?) -> some View
    

##  Parameters

`tint`

    

The tint effect to use. Use `nil` to avoid overriding the inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# preferredColorScheme(_:)

Sets the preferred color scheme for this presentation.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme for this view.

## Return Value

A view that sets the color scheme.

## Discussion

Use one of the values in `ColorScheme` with this modifier to set a preferred
color scheme for the nearest enclosing presentation, like a popover, a sheet,
or a window. The value that you set overrides the user’s Dark Mode selection
for that presentation. In the example below, the `Toggle` controls an
`isDarkMode` state variable, which in turn controls the color scheme of the
sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this
case are a `List` and a `Toggle` — the value that you set propagates up
through the view hierarchy to the enclosing presentation, or until another
color scheme modifier higher in the hierarchy overrides it. The value you set
also flows down to all child views of the enclosing presentation.

A common use for this modifier is to create side-by-side previews of the same
view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read
the `colorScheme` environment value:

## See Also

### Detecting and requesting the light or dark appearance

`var colorScheme: ColorScheme`

The color scheme of this environment.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Instance Method

# preferredSurroundingsEffect(_:)

Applies an effect to passthrough video.

visionOS 1.0+

    
    
    func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some View
    

##  Parameters

`effect`

    

The effect that you want to apply.

## Return Value

A view that exhibits the specified preference.

## Discussion

Use this modifier to indicate a preference for the appearance of passthrough
video when displaying the modified view. For example, you can enhance the
immersiveness of a scene that uses the default `mixed` immersion style by
applying the `systemDark` preference to a view inside the scene:

When the system presents the `Orbit` view in the above code, it also dims
passthrough video. This helps to draw attention to the scene’s virtual content
while still enabling people to remain aware of their surroundings.

Note

This modifier expresses a preference, but the system might not be able to
honor it.

Use a value of `nil` to indicate that you have no preference. You typically do
this to counteract a preference expressed by a view lower in the view
hierarchy.

## See Also

### Configuring passthrough

`struct SurroundingsEffect`

Effects that the system can apply to passthrough video.

Instance Method

# border(_:width:)

Adds a border to this view with the specified style and width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func border<S>(
        _ content: S,
        width: CGFloat = 1
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

A value that conforms to the `ShapeStyle` protocol, like a `Color` or
`HierarchicalShapeStyle`, that SwiftUI uses to fill the border.

`width`

    

The thickness of the border. The default is 1 pixel.

## Return Value

A view that adds a border with the specified style and width to this view.

## Discussion

Use this modifier to draw a border of a specified width around the view’s
frame. By default, the border appears inside the bounds of this view. For
example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same
width before adding the border:

## See Also

### Styling content

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# overlay(alignment:content:)

Layers the views that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the foreground views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw in front of this
view, stacked in the order that you list them. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a foreground.

## Discussion

Use this modifier to place one or more views in front of another view. For
example, you can place a group of stars on a `RoundedRectangle`:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can place a star and a
`Circle` on a field of `blue`:

Both the overlay modifier and the implicit `ZStack` composed from the overlay
content — the circle and the star — use a default `center` alignment. The star
appears centered on the circle, and both appear as a composite view centered
in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack
rather than to the individual views in the closure. You can see this if you
add the `bottom` alignment:

The circle and the star move down as a unit to align the stack’s bottom edge
with the bottom edge of the square, while the star remains centered on the
circle:

To control the placement of individual items inside the `content` closure,
either use a different overlay modifier for each item, as the earlier example
of stars in the corners of a rectangle demonstrates, or add an explicit
`ZStack` inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the
circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the
modified view and the overlay content into a `ZStack`. This can produce a
simpler view hierarchy, but changes the layout priority that SwiftUI applies
to the views. Use the overlay modifier when you want the modified view to
dominate the layout.

If you want to specify a `ShapeStyle` like a `Color` or a `Material` as the
overlay, use `overlay(_:ignoresSafeAreaEdges:)` instead. To specify a `Shape`,
use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:ignoresSafeAreaEdges:)

Layers the specified style in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI layers in
front of the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the overlay.
The default value is `all`. Specify an empty set to respect safe area insets
on all edges.

## Return Value

A view with the specified style drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `ShapeStyle` protocol,
like a `Color`, `Material`, or `HierarchicalShapeStyle`, in front of a view.
For example, you can overlay the `ultraThinMaterial` over a `Circle`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
overlay fills the entirety of the circle’s frame (which happens to be wider
than the circle is tall):

SwiftUI also limits the style’s extent to the view’s container-relative shape.
You can see this effect if you constrain the `CoveredCircle` view with a
`containerShape(_:)` modifier:

The overlay takes on the specified container shape:

By default, the overlay ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the overlay rather than
a style, use `overlay(alignment:content:)` instead. If you want to specify a
`Shape`, use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:in:fillStyle:)

Layers a shape that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws in front of
the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol — like
a `Rectangle`, `Circle`, or `Capsule` — in front of a view. Specify a
`ShapeStyle` that’s used to fill the shape. For example, you can overlay the
outline of one rectangle in front of another:

The example above uses the `inset(by:)` method to slightly reduce the size of
the overlaid rectangle, and the `stroke(lineWidth:)` method to fill only the
shape’s outline. This creates an inset border:

This modifier is a convenience method for layering a shape over a view. To
handle the more general case of overlaying a `View` — or a stack of views —
with control over the position, use `overlay(alignment:content:)` instead. To
cover a view with a `ShapeStyle`, use `overlay(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(alignment:content:)

Layers the views that you specify behind this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw behind this view,
stacked in a cascading order from bottom to top. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a background.

## Discussion

Use this modifier to place one or more views behind another view. For example,
you can place a collection of stars beind a `Text` view:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places behind the text:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can layer a vertical bar
behind a circle, with both of those behind a horizontal bar:

Both the background modifier and the implicit `ZStack` composed from the
background content — the circle and the vertical bar — use a default `center`
alignment. The vertical bar appears centered behind the circle, and both
appear as a composite view centered behind the horizontal bar:

If you specify an alignment for the background, it applies to the implicit
stack rather than to the individual views in the closure. You can see this if
you add the `leading` alignment:

The vertical bar and the circle move as a unit to align the stack with the
leading edge of the horizontal bar, while the vertical bar remains centered on
the circle:

To control the placement of individual items inside the `content` closure,
either use a different background modifier for each item, as the earlier
example of stars under text demonstrates, or add an explicit `ZStack` inside
the content closure with its own alignment:

The stack alignment ensures that the circle’s leading edge aligns with the
vertical bar’s, while the background modifier aligns the composite view with
the horizontal bar:

You can achieve layering without a background modifier by putting both the
modified view and the background content into a `ZStack`. This produces a
simpler view hierarchy, but it changes the layout priority that SwiftUI
applies to the views. Use the background modifier when you want the modified
view to dominate the layout.

If you want to specify a `ShapeStyle` like a `HierarchicalShapeStyle` or a
`Material` as the background, use `background(_:ignoresSafeAreaEdges:)`
instead. To specify a `Shape` or `InsettableShape`, use
`background(_:in:fillStyle:)` or `background(_:in:fillStyle:)`, respectively.
To configure the background of a presentation, like a sheet, use
`presentationBackground(alignment:content:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:ignoresSafeAreaEdges:)

Sets the view’s background to a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI draws behind
the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the specified style drawn behind it.

## Discussion

Use this modifier to place a type that conforms to the `ShapeStyle` protocol —
like a `Color`, `Material`, or `HierarchicalShapeStyle` — behind a view. For
example, you can add the `regularMaterial` behind a `Label`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
background fills the entirety of the label’s frame, which includes the
padding:

SwiftUI limits the background style’s extent to the modified view’s container-
relative shape. You can see this effect if you constrain the `FlagLabel` view
with a `containerShape(_:)` modifier:

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(ignoresSafeAreaEdges:)

Sets the view’s background to the default background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the `background` shape style drawn behind it.

## Discussion

This modifier behaves like `background(_:ignoresSafeAreaEdges:)`, except that
it always uses the `background` shape style. For example, you can add a
background to a `Label`:

Without the background modifier, the teal color behind the label shows through
the label. With the modifier, the label’s text and icon appear backed by a
region filled with a color that’s appropriate for light or dark appearance:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to an insettable shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : InsettableShape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `InsettableShape`
protocol — like a `Rectangle`, `Circle`, or `Capsule` — behind a view. Specify
the `ShapeStyle` that’s used to fill the shape. For example, you can place a
`RoundedRectangle` behind a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to an insettable shape filled with the default
background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified insettable
shape. For example, you can use a `RoundedRectangle` as a background on a
`Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to a shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol behind
a view. Specify the `ShapeStyle` that’s used to fill the shape. For example,
you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to a shape filled with the default background
style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified shape. For
example, you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# alternatingRowBackgrounds(_:)

Overrides whether lists and tables in this view have alternating row
backgrounds.

macOS 14.0+

    
    
    func alternatingRowBackgrounds(_ behavior: AlternatingRowBackgroundBehavior = .enabled) -> some View
    

##  Parameters

`behavior`

    

Whether alternating row backgrounds are enabled or not.

## Discussion

This can be used in conjunction with an explicit list or table style or used
by itself to customize the row backgrounds of the automatic style. The only
list style this has no effect on is `.sidebar.`

This is able to be combined with `scrollContentBackground(_:)` and applies an
alternating row background on top of the overall list or table background.

This can also be combined with `listRowBackground`, which overrides the
background for a specific list row, replacing the automatic alternating
background for that row.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# listRowBackground(_:)

Places a custom background view behind a list row item.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowBackground<V>(_ view: V?) -> some View where V : View
    

##  Parameters

`view`

    

The `View` to use as the background behind the list row view.

## Return Value

A list row view with `view` as its background view.

## Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list
row item.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowBackground(_:)`
modifier then places the view you supply behind each of the list row items:

## See Also

### Configuring backgrounds

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# scrollContentBackground(_:)

Specifies the visibility of the background for scrollable views within this
view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func scrollContentBackground(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

the visibility to use for the background.

## Discussion

The following example hides the standard system background of the List.

## See Also

### Managing content visibility

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

Instance Method

# containerBackground(_:for:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<S>(
        _ style: S,
        for container: ContainerBackgroundPlacement
    ) -> some View where S : ShapeStyle
    

## Discussion

The following example uses a `LinearGradient` as a background:

The `.containerBackground(_:for:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

  * Parameters

    * style: The shape style to use as the container background.

    * container: The container that will use the background.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(for:alignment:content:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<V>(
        for container: ContainerBackgroundPlacement,
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`container`

    

The container that will use the background.

`content`

    

The view to use as the background of the container.

## Discussion

The following example uses a custom `View` as a background:

The `.containerBackground(for:alignment:content:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# glassBackgroundEffect(displayMode:)

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

visionOS 1.0+

    
    
    func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode = .always) -> some View
    

##  Parameters

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

## See Also

### Adding a glass background

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# glassBackgroundEffect(in:displayMode:)

Fills the view’s background with a glass material using a shape that you
specify.

visionOS 1.0+

    
    
    func glassBackgroundEffect<S>(
        in shape: S,
        displayMode: GlassBackgroundDisplayMode = .always
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An `InsettableShape` instance that SwiftUI draws behind the view. Unsupported
shapes resolve to a rectangle.

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

Prefer a shape for the background that has rounded corners. An unsupported
shape style resolves to a rectangle.

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# defaultWheelPickerItemHeight(_:)

Sets the default wheel-style picker item height.

watchOS 6.0+  visionOS 1.0+

    
    
    func defaultWheelPickerItemHeight(_ height: CGFloat) -> some View
    

##  Parameters

`height`

    

The height for the picker items.

## Discussion

Use `defaultWheelPickerItemHeight(_:)` when you need to change the default
item height in a picker control. In this example, the view sets the default
height for picker elements to 30 points.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# horizontalRadioGroupLayout()

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

macOS 10.15+

    
    
    func horizontalRadioGroupLayout() -> some View
    

## Discussion

Use `horizontalRadioGroupLayout()` to configure the visual layout of radio
buttons in a `Picker` so that the radio buttons are arranged horizontally in
the view.

The example below shows two `Picker` controls configured as radio button
groups; the first group shows the default vertical layout; the second group
shows the effect of `horizontalRadioGroupLayout()` which renders the radio
buttons horizontally.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# controlSize(_:)

Sets the size for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func controlSize(_ controlSize: ControlSize) -> some View
    

##  Parameters

`controlSize`

    

One of the control sizes specified in the `ControlSize` enumeration.

## Discussion

Use `controlSize(_:)` to override the system default size for controls in this
view. In this example, a view displays several typical controls at `.mini`,
`.small` and `.regular` sizes.

## See Also

### Sizing controls

`var controlSize: ControlSize`

The size to apply to controls within a view.

`enum ControlSize`

The size classes, like regular or small, that you can apply to controls within
a view.

Instance Method

# buttonBorderShape(_:)

Sets the border shape for buttons in this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func buttonBorderShape(_ shape: ButtonBorderShape) -> some View
    

##  Parameters

`shape`

    

the shape to use.

## Discussion

The border shape is used to draw the platter for a bordered button. On macOS,
the specified border shape is only applied to bordered buttons in widgets.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonRepeatBehavior(_:)

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View
    

##  Parameters

`behavior`

    

A value of `enabled` means that buttons should enable repeating behavior and a
value of `disabled` means that buttons should disallow repeating behavior.

## Discussion

Apply this to buttons that increment or decrement a value or perform some
other inherently iterative operation. Interactions such as pressing-and-
holding on the button, holding the button’s keyboard shortcut, or holding down
the space key while the button is focused will trigger this repeat behavior.

This affects all system button styles, as well as automatically affects custom
`ButtonStyle` conforming types. This does not automatically apply to custom
`PrimitiveButtonStyle` conforming types, and the
`EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their
custom gestures as appropriate.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# headerProminence(_:)

Sets the header prominence for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func headerProminence(_ prominence: Prominence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply.

## Discussion

In the following example, the section header appears with increased
prominence:

## See Also

### Configuring headers

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Method

# scrollDisabled(_:)

Disables or enables scrolling in scrollable views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollDisabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean that indicates whether scrolling is disabled.

## Discussion

Use this modifier to control whether a `ScrollView` can scroll:

SwiftUI passes the disabled property through the environment, which means you
can use this modifier to disable scrolling for all scroll views within a view
hierarchy. In the following example, the modifier affects both scroll views:

You can also use this modifier to disable scrolling for other kinds of
scrollable views, like a `List` or a `TextEditor`.

## See Also

### Disabling scrolling

`var isScrollEnabled: Bool`

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

Instance Method

# scrollBounceBehavior(_:axes:)

Configures the bounce behavior of scrollable views along the specified axis.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func scrollBounceBehavior(
        _ behavior: ScrollBounceBehavior,
        axes: Axis.Set = [.vertical]
    ) -> some View
    

##  Parameters

`behavior`

    

The bounce behavior to apply to any scrollable views within the configured
view. Use one of the `ScrollBounceBehavior` values.

`axes`

    

The set of axes to apply `behavior` to. The default is `Axis.vertical`.

## Return Value

A view that’s configured with the specified scroll bounce behavior.

## Discussion

Use this modifier to indicate whether scrollable views bounce when people
scroll to the end of the view’s content, taking into account the relative
sizes of the view and its content. For example, the following `ScrollView`
only enables bounce behavior if its content is large enough to require
scrolling:

The modifier passes the scroll bounce mode through the `Environment`, which
means that the mode affects any scrollable views in the modified view
hierarchy. Provide an axis to the modifier to constrain the kinds of
scrollable views that the mode affects. For example, all the scroll views in
the following example can access the mode value, but only the two nested
scroll views are affected, because only they use horizontal scrolling:

You can use this modifier to configure any kind of scrollable view, including
`ScrollView`, `List`, `Table`, and `TextEditor`:

## See Also

### Configuring scroll bounce behavior

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Method

# scrollIndicatorsFlash(onAppear:)

Flashes the scroll indicators of a scrollable view when it appears.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(onAppear: Bool) -> some View
    

##  Parameters

`onAppear`

    

A Boolean value that indicates whether the scroll indicators flash when the
scroll view appears.

## Return Value

A view that flashes any visible scroll indicators when it first appears.

## Discussion

Use this modifier to control whether the scroll indicators of a scroll view
briefly flash when the view first appears. For example, you can make the
indicators flash by setting the `onAppear` parameter to `true`:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a value changes, use `scrollIndicatorsFlash(trigger:)`
instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollIndicatorsFlash(trigger:)

Flashes the scroll indicators of scrollable views when a value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(trigger value: some Equatable) -> some View
    

##  Parameters

`value`

    

The value that causes scroll indicators to flash. The value must conform to
the `Equatable` protocol.

## Return Value

A view that flashes any visible scroll indicators when a value changes.

## Discussion

When the value that you provide to this modifier changes, the scroll
indicators of any scrollable views within the modified view hierarchy briefly
flash. The following example configures the scroll indicators to flash any
time `flashCount` changes:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a scroll view initially appears, use
`scrollIndicatorsFlash(onAppear:)` instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# menuOrder(_:)

Sets the preferred order of items for menus presented from this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func menuOrder(_ order: MenuOrder) -> some View
    

##  Parameters

`order`

    

The menu item ordering strategy to apply.

## Return Value

A view that uses the specified menu ordering strategy.

## Discussion

Use this modifier to override the default menu order. On supported platforms,
`priority` order keeps the first items closer to the user’s point of
interaction, whereas `fixed` order always orders items from top to bottom.

On iOS, the `automatic` order resolves to `fixed` for menus presented within
scrollable content. Pickers that use the `menu` style also default to `fixed`
order. In all other cases, menus default to `priority` order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to `fixed`
order.

The following example creates a menu that presents its content in a fixed
order from top to bottom:

You can use this modifier on controls that present a menu. For example, the
code below creates a `Picker` using the `menu` style with a priority-based
order:

You can also use this modifier on context menus. The example below creates a
context menu that presents its content in a fixed order:

The modifier has no effect when applied to a subsection or submenu of a menu.

## See Also

### Setting a preferred order

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

`struct MenuOrder`

The order in which a menu presents its content.

Instance Method

# menuActionDismissBehavior(_:)

Tells a menu whether to dismiss after performing an action.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func menuActionDismissBehavior(_ behavior: MenuActionDismissBehavior) -> some View
    

##  Parameters

`dismissal`

    

The menu action dismissal behavior to apply.

## Return Value

A view that has the specified menu dismissal behavior.

## Discussion

Use this modifier to control the dismissal behavior of a menu. In the example
below, the menu doesn’t dismiss after someone chooses either the increase or
decrease action:

You can use this modifier on any controls that present a menu, like a `Picker`
that uses the `menu` style or a `ControlGroup`. For example, the code below
creates a picker that disables dismissal when someone selects one of the
options:

You can also use this modifier on context menus. The example below creates a
context menu that stays presented after someone selects an action to run:

## See Also

### Configuring menu dismissal

`struct MenuActionDismissBehavior`

The set of menu dismissal behavior options.

Instance Method

# paletteSelectionEffect(_:)

Specifies the selection effect to apply to a palette item.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func paletteSelectionEffect(_ effect: PaletteSelectionEffect) -> some View
    

##  Parameters

`effect`

    

The type of effect to apply when a palette item is selected.

## Discussion

`automatic` applies the system’s default appearance when selected. When using
un-tinted SF Symbols or template images, the current tint color is applied to
the selected items’ image. If the provided SF Symbols have custom tints, a
stroke is drawn around selected items.

If you wish to provide a specific image (or SF Symbol) to indicate selection,
use `custom` to forgo the system’s default selection appearance allowing the
provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system
selection behavior:

If a specific SF Symbol variant is preferable instead, use
`symbolVariant(_:)`.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ text: Text?) -> some View
    

##  Parameters

`text`

    

The explicit text value to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ stringKey: LocalizedStringKey) -> some View
    

##  Parameters

`stringKey`

    

The localized string key to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent<S>(_ string: S) -> some View where S : StringProtocol
    

##  Parameters

`string`

    

The string to use as a type select equivalent for a view in a collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# symbolEffect(_:options:isActive:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        isActive: Bool = true
    ) -> some View where T : IndefiniteSymbolEffect, T : SymbolEffect
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`isActive`

    

whether the effect is active or inactive.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a repeating pulse effect to two symbol images:

## See Also

### Managing symbol effects

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffect(_:options:value:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T, U>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        value: U
    ) -> some View where T : DiscreteSymbolEffect, T : SymbolEffect, U : Equatable
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`value`

    

the value to monitor for changes, the animation is triggered each time the
value changes.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a bounce effect to two symbol images, the animation
will play each time `counter` changes:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffectsRemoved(_:)

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffectsRemoved(_ isEnabled: Bool = true) -> some View
    

##  Parameters

`isEnabled`

    

Whether to remove inherited symbol effects or not.

## Return Value

a copy of the view with its symbol effects either removed or left unchanged.

## Discussion

The following example adds a repeating pulse effect to two symbol images, but
then disables the effect on one of them:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# privacySensitive(_:)

Marks the view as containing sensitive, private user data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func privacySensitive(_ sensitive: Bool = true) -> some View
    

## Discussion

SwiftUI redacts views marked with this modifier when you apply the `privacy`
redaction reason.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# redacted(reason:)

Adds a reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func redacted(reason: RedactionReasons) -> some View
    

## Discussion

Adding a redaction is an additive process: any redaction provided will be
added to the reasons provided by the parent.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# unredacted()

Removes any reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func unredacted() -> some View
    

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# invalidatableContent(_:)

Mark the receiver as their content might be invalidated.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func invalidatableContent(_ invalidatable: Bool = true) -> some View
    

##  Parameters

`invalidatable`

    

Whether the receiver content might be invalidated.

## Discussion

Use this modifier to annotate views that display values that are derived from
the current state of your data and might be invalidated in response of, for
example, user interaction.

The view will change its appearance when `RedactionReasons.invalidated` is
present in the environment.

In an interactive widget a view is invalidated from the moment the user
interacts with a control on the widget to the moment when a new timeline
update has been presented.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

Instance Method

# hidden()

Hides this view unconditionally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hidden() -> some View
    

## Return Value

A hidden view.

## Discussion

Hidden views are invisible and can’t receive or respond to interactions.
However, they do remain in the view hierarchy and affect layout. Use this
modifier if you want to include a view for layout purposes, but don’t want it
to display.

The third circle takes up space, because it’s still present, but SwiftUI
doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if`
statement instead:

Depending on the current value of the `isHidden` state variable in the example
above, controlled by the `Toggle` instance, SwiftUI draws the circle or
completely omits it from the layout.

## See Also

### Hiding views

`func opacity(Double) -> some View`

Sets the transparency of this view.

Instance Method

# labelsHidden()

Hides the labels of any controls contained within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func labelsHidden() -> some View
    

## Discussion

Use this modifier when you want to omit a label from one or more controls in
your user interface. For example, the first `Toggle` in the following example
hides its label:

The `VStack` in the example above centers the first toggle’s control element
in the available space, while it centers the second toggle’s combined label
and control element:

Always provide a label for controls, even when you hide the label, because
SwiftUI uses labels for other purposes, including accessibility.

Note

This modifier doesn’t work for all labels. It applies to labels that are
separate from the rest of the control’s interface, like they are for `Toggle`,
but not to controls like a bordered button where the label is inside the
button’s border.

## See Also

### Hiding system elements

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# menuIndicator(_:)

Sets the menu indicator visibility for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for
controls in this view. For example, the code below creates a menu without an
indicator:

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

Instance Method

# listRowSeparator(_:edges:)

Sets the display mode for the separator associated with this specific row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this row’s separators.

`edges`

    

The set of row edges for which this preference applies. The list style might
already decide to not display separators for some edges, typically the top
edge. The default is `all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are
hidden:

To change the color of a row separators, use `listRowSeparatorTint(_:edges:)`.
To hide or change the tint color for a section separators, use
`listSectionSeparator(_:edges:)` and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparator(_:edges:)

Sets whether to hide the separator associated with a list section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this section’s separators.

`edges`

    

The set of row edges for which the preference applies. The list style might
already decide to not display separators for some edges. The default is `all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections
separator are hidden:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To set the
tint color for a section separator, use `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

Instance Method

# persistentSystemOverlays(_:)

Sets the preferred visibility of the non-transient system views overlaying the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func persistentSystemOverlays(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value that indicates the visibility of the non-transient system views
overlaying the app.

## Discussion

Use this modifier if you would like to customise the immersive experience of
your app by hiding or showing system overlays that may affect user experience.
The following example hides every persistent system overlay.

Note that this modifier only sets a preference and, ultimately the system will
decide if it will honour it or not.

These non-transient system views include:

  * The Home indicator

  * The SharePlay indicator

  * The Multi-task indicator and Picture-in-picture on iPad

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# scrollIndicators(_:axes:)

Sets the visibility of scroll indicators within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollIndicators(
        _ visibility: ScrollIndicatorVisibility,
        axes: Axis.Set = [.vertical, .horizontal]
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility to apply to scrollable views.

`axes`

    

The axes of scrollable views that the visibility applies to.

## Return Value

A view with the specified scroll indicator visibility.

## Discussion

Use this modifier to hide or show scroll indicators on scrollable content in
views like a `ScrollView`, `List`, or `TextEditor`. This modifier applies the
prefered visibility to any scrollable content within a view hierarchy.

Use the `hidden` value to indicate that you prefer that views never show
scroll indicators along a given axis. Use `visible` when you prefer that views
show scroll indicators. Depending on platform conventions, visible scroll
indicators might only appear while scrolling. Pass `automatic` to allow views
to decide whether or not to show their indicators.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollClipDisabled(_:)

Sets whether a scroll view clips its content to its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollClipDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that specifies whether to disable scroll view clipping.

## Return Value

A view that disables or enables scroll view clipping.

## Discussion

By default, a scroll view clips its content to its bounds, but you can disable
that behavior by using this modifier. For example, if the views inside the
scroll view have shadows that extend beyond the bounds of the scroll view, you
can use this modifier to avoid clipping the shadows:

The scroll view in the above example clips when the content view’s `disabled`
input is `false`, as it does if you omit the modifier, but not when the input
is `true`:

  * True 
  * False 

While you might want to avoid clipping parts of views that exceed the bounds
of the scroll view, like the shadows in the above example, you typically still
want the scroll view to clip at some point. Create custom clipping by using
the `clipShape(_:style:)` modifier to add a different clip shape. The
following code disables the default clipping and then adds rectangular
clipping that exceeds the bounds of the scroll view by the default padding
amount:

## See Also

### Managing content visibility

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

Instance Method

# tableColumnHeaders(_:)

Controls the visibility of a `Table`’s column header views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func tableColumnHeaders(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value of `visible` will show table columns, `hidden` will remove them, and
`automatic` will defer to default behavior.

## Discussion

By default, `Table` will display a global header view with the labels of each
table column. This area is also where users can sort, resize, and rearrange
the columns. For simple cases that don’t require those features, this header
can be hidden.

This will not affect the header of any `Section`s in a table.

## See Also

### Customizing columns

`struct TableColumnCustomization`

A representation of the state of the columns in a table.

`struct TableColumnCustomizationBehavior`

A set of customization behaviors of a column that a table can offer to a user.

Instance Method

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some View
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some Scene`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# sensoryFeedback(_:trigger:)

Plays the specified `feedback` when the provided `trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

## Discussion

For example, you could play feedback when a state value changes:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(trigger:_:)

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        trigger: T,
        _ feedback: @escaping (T, T) -> SensoryFeedback?
    ) -> some View where T : Equatable
    

##  Parameters

`trigger`

    

A value to monitor for changes to determine when to play.

`feedback`

    

A closure to determine whether to play the feedback and what type of feedback
to play when `trigger` changes.

## Discussion

For example, you could play different feedback for different state
transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(_:trigger:condition:)

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T,
        condition: @escaping (T, T) -> Bool
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

`condition`

    

A closure to determine whether to play the feedback when `trigger` changes.

## Discussion

For example, you could play feedback for certain state transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# widgetAccentable(_:)

Adds the view and all of its subviews to the accented group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetAccentable(_ accentable: Bool = true) -> some View
    

##  Parameters

`accentable`

    

A Boolean value that indicates whether to add the view and its subviews to the
accented group.

## Discussion

When the system renders the widget using the
`WidgetKit/WidgetRenderingMode/accented` mode, it divides the widget’s view
hierarchy into two groups: the accented group and the default group. It then
applies a different color to each group.

When applying the colors, the system treats the widget’s views as if they were
template images. It ignores the view’s color — rendering the new colors based
on the view’s alpha channel.

To control your view’s appearance, add the `widgetAccentable(_:)` modifier to
part of your view’s hierarchy. If the `accentable` parameter is `true`, the
system adds that view and all of its subviews to the accent group. It puts all
other views in the default group.

Important

After you call `widgetAccentable(true)` on a view moving it into the accented
group, calling `widgetAccentable(false)` on its subviews doesn’t move the
subviews back into the default group.

Instance Method

# widgetCurvesContent(_:)

Displays the widget’s content along a curve if the context allows it.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func widgetCurvesContent(_ curvesContent: Bool = true) -> some View
    

##  Parameters

`curvesContent`

    

A Boolean value that indicates whether the system curves the widget label’s
content, if the context allows.

## Discussion

The system positions the widget’s content along a curve that follows the
corner of the watch face when displaying a `WidgetFamily/accessoryCorner`
complication. The widget must use a `widgetLabel(_:)` modifier, and the
curving effect modifies only text, SF Symbols, and images.

When displaying an `.accessoryCorner` complication, the system places the
widget label on the inside of the curve, and the widget’s content on the
outside, as shown below.

The system can also curve text, SF symbols, and image content from a
`ViewThatFits` view.

## See Also

### Widget configuration

`func widgetAccentable(Bool) -> some View`

Adds the view and all of its subviews to the accented group.

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

`func dynamicIsland(verticalPlacement:
DynamicIslandExpandedRegionVerticalPlacement) -> some View`

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

Instance Method

# widgetLabel(_:)

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

A string that contains the text which WidgetKit displays alongside the
complication.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style. For
example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(_:)

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

A label generated from a localized string.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style based
on the clock face. For example, setting the font and rendering the text along
a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(label:)

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<Label>(@ViewBuilder label: () -> Label) -> some View where Label : View
    

##  Parameters

`label`

    

A view that WidgetKit can display alongside the accessory family widget’s main
SwiftUI view. You can use a `Image`, `Text`, `Gauge`, `ProgressView`, or a
container with multiple subviews.

## Discussion

The system only displays labels on widget-based complications in watchOS. The
system ignores any labels attached to widgets on the Lock Screen on iPhone.
Therefore, you can use the same code to display an accessory family widget on
both iPhone and Apple Watch.

To create the widget label, call `widgetLabel(label:)`on a complication’s main
SwiftUI view. Pass the desired content as the `label` parameter. The label can
be a `Gauge`, `ProgressView`, `Text`, or `Image`. To provide multiple views,
wrap your views in a container, such as a `VStack`. WidgetKit determines
whether it can use any of the label’s content. If it can’t, it ignores the
label.

WidgetKit configures the label so that the watch face presents a unified look.
For example, it sets the size for an image, the font for text, and can even
render text and gauges along a curve.

The following widget families support widget labels:

`WidgetKit/WidgetFamily/accessoryCorner`

    

In watchOS, this widget-based complication can display a `Gauge`, a
`ProgressView`, or a `Text`. Adding a label to an accessory corner causes the
main SwiftUI view to shrink to make space for the label. If you pass a view
containing multiple, valid subviews, the system picks which view to display as
the widget label.

`WidgetKit/WidgetFamily/accessoryCircular`

    

In watchOS, the widget-based complication can display either an `Image` or a
`Text`. To pass both an image and text, wrap those views in a container.

However, WidgetKit only renders the label along the bezel on the Infograph
watch face (the top circular complication). On all other circular
complications — including widgets on all other platforms — WidgetKit ignores
the label.

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

Instance Method

# dynamicIsland(verticalPlacement:)

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
    

##  Parameters

`verticalPlacement`

    

The vertical placement for a view that’s part of an expanded Live Activity in
the Dynamic Island.

## Return Value

A view with the specified vertical placement.



# AnimationStateKey

Type Property

# defaultValue

The default value for the animation state key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required**

## See Also

### Setting the default value

`associatedtype Value`

The associated type representing the type of the animation state key’s value.

**Required**

Associated Type

# Value

The associated type representing the type of the animation state key’s value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Setting the default value

`static var defaultValue: Self.Value`

The default value for the animation state key.

**Required**



# AutomaticNavigationSplitViewStyle

Initializer

# init()

Creates an instance of the automatic navigation split view style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use `automatic` to construct this style.



# AccessibilityRotorEntry

Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`labelKey`

    

Localized string used to show this Rotor entry to users. If no label is
specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    ) where ID == Never, L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users. If no label is
specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text? = nil,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    ) where ID == Never

##  Parameters

`label`

    

Optional localized string used to show this Rotor entry to users. If no label
is specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`label`

    

Localized string used to show this Rotor entry to users.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    ) where L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the either label or accessibility value of
the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`labelKey`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

Initializer

# init(_:_:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        _ id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    ) where L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

Initializer

# init(_:id:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.



# AccessibilitySystemRotor

Type Property

# textFields

System Rotor allowing users to iterate through all text fields.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var textFields: AccessibilitySystemRotor { get }

## See Also

### Iterating through text

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

Type Property

# boldText

System Rotor allowing users to iterate through all the ranges of bolded text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var boldText: AccessibilitySystemRotor { get }

## See Also

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

Type Property

# italicText

System Rotor allowing users to iterate through all the ranges of italicized
text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var italicText: AccessibilitySystemRotor { get }

## See Also

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

Type Property

# underlineText

System Rotor allowing users to iterate through all the ranges of underlined
text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var underlineText: AccessibilitySystemRotor { get }

## See Also

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

Type Property

# misspelledWords

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var misspelledWords: AccessibilitySystemRotor { get }

## See Also

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

Type Property

# headings

System Rotor allowing users to iterate through all headings.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var headings: AccessibilitySystemRotor { get }

## See Also

### Iterating through headings

`static func headings(level: AccessibilityHeadingLevel) ->
AccessibilitySystemRotor`

System Rotors allowing users to iterate through all headings, of various
heading levels.

Type Method

# headings(level:)

System Rotors allowing users to iterate through all headings, of various
heading levels.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func headings(level: AccessibilityHeadingLevel) -> AccessibilitySystemRotor

## See Also

### Iterating through headings

`static var headings: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all headings.

Type Property

# links

System Rotor allowing users to iterate through all links.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var links: AccessibilitySystemRotor { get }

## See Also

### Iterating through links

`static func links(visited: Bool) -> AccessibilitySystemRotor`

System Rotors allowing users to iterate through links or visited links.

Type Method

# links(visited:)

System Rotors allowing users to iterate through links or visited links.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func links(visited: Bool) -> AccessibilitySystemRotor

## See Also

### Iterating through links

`static var links: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all links.

Type Property

# images

System Rotor allowing users to iterate through all images.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var images: AccessibilitySystemRotor { get }

## See Also

### Iterating through other elements

`static var landmarks: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all landmarks.

`static var lists: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all lists.

`static var tables: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all tables.

Type Property

# landmarks

System Rotor allowing users to iterate through all landmarks.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var landmarks: AccessibilitySystemRotor { get }

## See Also

### Iterating through other elements

`static var images: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all images.

`static var lists: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all lists.

`static var tables: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all tables.

Type Property

# lists

System Rotor allowing users to iterate through all lists.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var lists: AccessibilitySystemRotor { get }

## See Also

### Iterating through other elements

`static var images: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all images.

`static var landmarks: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all landmarks.

`static var tables: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all tables.

Type Property

# tables

System Rotor allowing users to iterate through all tables.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var tables: AccessibilitySystemRotor { get }

## See Also

### Iterating through other elements

`static var images: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all images.

`static var landmarks: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all landmarks.

`static var lists: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all lists.



# AnimatablePair

Initializer

# init(_:_:)

Creates an animated pair with the provided values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ first: First,
        _ second: Second
    )

Instance Property

# first

The first value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var first: First

## See Also

### Getting the constituent animations

`var second: Second`

The second value.

Instance Property

# second

The second value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var second: Second

## See Also

### Getting the constituent animations

`var first: First`

The first value.

Instance Property

# magnitudeSquared

The dot-product of this animated pair with itself.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var magnitudeSquared: Double { get }



# AccessibilityActionKind

Type Property

# default

The value that represents the default accessibility action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let `default`: AccessibilityActionKind

## See Also

### Getting the kind of action

`static let delete: AccessibilityActionKind`

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let magicTap: AccessibilityActionKind`

`static let showMenu: AccessibilityActionKind`

Type Property

# delete

macOS 10.15+

    
    
    static let delete: AccessibilityActionKind

## See Also

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let magicTap: AccessibilityActionKind`

`static let showMenu: AccessibilityActionKind`

Type Property

# escape

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let escape: AccessibilityActionKind

## See Also

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let delete: AccessibilityActionKind`

`static let magicTap: AccessibilityActionKind`

`static let showMenu: AccessibilityActionKind`

Type Property

# magicTap

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static let magicTap: AccessibilityActionKind

## See Also

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let delete: AccessibilityActionKind`

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let showMenu: AccessibilityActionKind`

Type Property

# showMenu

macOS 10.15+

    
    
    static let showMenu: AccessibilityActionKind

## See Also

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let delete: AccessibilityActionKind`

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let magicTap: AccessibilityActionKind`

Initializer

# init(named:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(named name: Text)



# Angle

Type Property

# zero

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var zero: Angle { get }

## See Also

### Getting constant angles

`static func degrees(Double) -> Angle`

`static func radians(Double) -> Angle`

Type Method

# degrees(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func degrees(_ degrees: Double) -> Angle

## See Also

### Getting constant angles

`static var zero: Angle`

`static func radians(Double) -> Angle`

Type Method

# radians(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func radians(_ radians: Double) -> Angle

## See Also

### Getting constant angles

`static var zero: Angle`

`static func degrees(Double) -> Angle`

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating an angle

`init(degrees: Double)`

`init(radians: Double)`

`init(Angle2D)`

Initializer

# init(degrees:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(degrees: Double)

## See Also

### Creating an angle

`init()`

`init(radians: Double)`

`init(Angle2D)`

Initializer

# init(radians:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(radians: Double)

## See Also

### Creating an angle

`init()`

`init(degrees: Double)`

`init(Angle2D)`

Initializer

# init(_:)

visionOS 1.0+

    
    
    init(_ angle: Angle2D)

## See Also

### Creating an angle

`init()`

`init(degrees: Double)`

`init(radians: Double)`

Instance Property

# degrees

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var degrees: Double { get set }

## See Also

### Getting the angle size

`var radians: Double`

Instance Property

# radians

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var radians: Double

## See Also

### Getting the angle size

`var degrees: Double`



# AccessibilityChildBehavior

Type Property

# combine

Any child accessibility element’s properties are merged into the new
accessibility element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let combine: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view represented by a single accessibility
element. The new accessibility element merges properties from all non-hidden
children. Some properties may be transformed or ignored to achieve the ideal
combined result. For example, not all of `AccessibilityTraits` are merged and
a `default` action may become a named action (`init(named:)`).

A new accessibility element is created when:

  * The view contains multiple or zero accessibility elements

  * The view wraps a `UIViewRepresentable`/`NSViewRepresentable`.

Note

If an accessibility element is not created, the `AccessibilityChildBehavior`
of the existing accessibility element is modified.

## See Also

### Getting behaviors

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

Type Property

# contain

Any child accessibility elements become children of the new accessibility
element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let contain: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view to be an accessibility container. An
accessibility container groups child accessibility elements which improves
navigation. For example, all children of an accessibility container are
navigated in order before navigating through the next accessibility container.

A new accessibility element is created when:

  * The view contains multiple or zero accessibility elements

  * The view contains a single accessibility element with no children

Note

If an accessibility element is not created, the `AccessibilityChildBehavior`
of the existing accessibility element is modified.

## See Also

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

Type Property

# ignore

Any child accessibility elements become hidden.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let ignore: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view represented by a single accessibility
element. The new accessibility element has no initial properties. So you will
need to use other accessibility modifiers, such as `accessibilityLabel(_:)`,
to begin making it accessible.

Before using the `ignore`behavior, consider using the `combine` behavior.

Note

A new accessibility element is always created.

## See Also

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.



# AccessoryBarActionButtonStyle

Initializer

# init()

Creates an accessory toolbar action button style

macOS 14.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

macOS 14.0+  visionOS 1.0+

    
    
    func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



# ActionSheet

Initializer

# init(title:message:buttons:)

Creates an action sheet with the provided buttons.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        buttons: [ActionSheet.Button] = [.cancel()]
    )

Deprecated

Use a `View` modifier like
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the action sheet.

`message`

    

The message to display in the body of the action sheet.

`buttons`

    

The buttons to show in the action sheet.

Type Alias

# ActionSheet.Button

A button representing an operation of an action sheet presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    typealias Button = Alert.Button

Deprecated

Use a `View` modifier like
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

## Discussion

The `ActionSheet` button is type-aliased to the `Alert` button type, which
provides default, cancel, and destructive styles.



# AsyncImage

Initializer

# init(url:scale:)

Loads and displays an image from the specified URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        url: URL?,
        scale: CGFloat = 1
    ) where Content == Image

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

## Discussion

Until the image loads, SwiftUI displays a default placeholder. When the load
operation completes successfully, SwiftUI updates the view to show the loaded
image. If the operation fails, SwiftUI continues to display the placeholder.
The following example loads and displays an icon from an example server:

If you want to customize the placeholder or apply image-specific modifiers —
like `resizable(capInsets:resizingMode:)` — to the loaded image, use the
`init(url:scale:content:placeholder:)` initializer instead.

## See Also

### Loading an image

`init<I, P>(url: URL?, scale: CGFloat, content: (Image) -> I, placeholder: ()
-> P)`

Loads and displays a modifiable image from the specified URL using a custom
placeholder until the image loads.

Initializer

# init(url:scale:content:placeholder:)

Loads and displays a modifiable image from the specified URL using a custom
placeholder until the image loads.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<I, P>(
        url: URL?,
        scale: CGFloat = 1,
        @ViewBuilder content: @escaping (Image) -> I,
        @ViewBuilder placeholder: @escaping () -> P
    ) where Content == _ConditionalContent<I, P>, I : View, P : View

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

`content`

    

A closure that takes the loaded image as an input, and returns the view to
show. You can return the image directly, or modify it as needed before
returning it.

`placeholder`

    

A closure that returns the view to show until the load operation completes
successfully.

## Discussion

Until the image loads, SwiftUI displays the placeholder view that you specify.
When the load operation completes successfully, SwiftUI updates the view to
show content that you specify, which you create using the loaded image. For
example, you can show a green placeholder, followed by a tiled version of the
loaded image:

If the load operation fails, SwiftUI continues to display the placeholder. To
be able to display a different view on a load error, use the
`init(url:scale:transaction:content:)` initializer instead.

## See Also

### Loading an image

`init(url: URL?, scale: CGFloat)`

Loads and displays an image from the specified URL.

Initializer

# init(url:scale:transaction:content:)

Loads and displays a modifiable image from the specified URL in phases.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        url: URL?,
        scale: CGFloat = 1,
        transaction: Transaction = Transaction(),
        @ViewBuilder content: @escaping (AsyncImagePhase) -> Content
    )

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

`transaction`

    

The transaction to use when the phase changes.

`content`

    

A closure that takes the load phase as an input, and returns the view to
display for the specified phase.

## Discussion

If you set the asynchronous image’s URL to `nil`, or after you set the URL to
a value but before the load operation completes, the phase is
`AsyncImagePhase.empty`. After the operation completes, the phase becomes
either `AsyncImagePhase.failure(_:)` or `AsyncImagePhase.success(_:)`. In the
first case, the phase’s `error` value indicates the reason for failure. In the
second case, the phase’s `image` property contains the loaded image. Use the
phase to drive the output of the `content` closure, which defines the view’s
appearance:

To add transitions when you change the URL, apply an identifier to the
`AsyncImage`.



# Alert.Button

Type Method

# default(_:action:)

Creates an alert button with the default style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func `default`(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button with the default style.

## See Also

### Getting a button

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# cancel(_:)

Creates an alert button that indicates cancellation, with a system-provided
label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func cancel(_ action: (() -> Void)? = {}) -> Alert.Button

##  Parameters

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates cancellation.

## Discussion

The system automatically chooses locale-appropriate text for the button’s
label.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# cancel(_:action:)

Creates an alert button that indicates cancellation, with a custom label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func cancel(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates cancellation.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# destructive(_:action:)

Creates an alert button with a style that indicates a destructive action.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func destructive(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates a destructive action.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.



