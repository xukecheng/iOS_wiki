Class

# WKHostingController

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

watchOS 6.0+

    
    
    @MainActor
    class WKHostingController<Body> where Body : View

## Overview

A `WKHostingController` presents and manages your app’s main interface using
SwiftUI views. You must subclass `WKHostingController` and override the `body`
property to provide the set of SwiftUI views you want to display. Display the
content of your hosting controller as you would any other
`WKInterfaceController` object. For example, you can include it as one of your
app’s root interface controllers, or present it modally.

## Topics

### Creating a hosting controller object

`init()`

Creates a hosting controller object that you can use to implement your app’s
main interface using SwiftUI views

### Getting the root view

`var body: Body`

The root view of the view hierarchy to display for your interface controller.

### Updating the root view

`func updateBodyIfNeeded()`

Updates the interface controller’s set of views immediately, if updates are
pending.

`func setNeedsBodyUpdate()`

Invalidates the current SwiftUI views and triggers an update during the next
cycle.

## Relationships

### Inherits From

  * `WKInterfaceController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSObjectProtocol`

## See Also

### Displaying SwiftUI views in WatchKit

`class WKUserNotificationHostingController`

A WatchKit user notification interface controller that hosts a SwiftUI view
hierarchy.

Class

# WKUserNotificationHostingController

A WatchKit user notification interface controller that hosts a SwiftUI view
hierarchy.

watchOS 6.0+

    
    
    @MainActor
    class WKUserNotificationHostingController<Body> where Body : View

## Overview

A `WKUserNotificationHostingController` presents and manages your app’s
notification interface using SwiftUI views. You must subclass
`WKUserNotificationHostingController` and override the `body` property to
provide the set of SwiftUI views you want to display. In the storyboard of
your watch app, specify the name of your custom class for your dynamic
interactive interface.

## Topics

### Creating a hosting controller object

`init()`

Creates a notification hosting controller object that you can use to implement
your notification interfaces using SwiftUI views.

### Getting the root view

`var body: Body`

The root view of the view hierarchy to display for your notification
interface.

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

## Relationships

### Inherits From

  * `WKUserNotificationInterfaceController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSObjectProtocol`

## See Also

### Displaying SwiftUI views in WatchKit

`class WKHostingController`

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

Protocol

# WKInterfaceObjectRepresentable

A view that represents a WatchKit interface object.

watchOS 6.0+

    
    
    protocol WKInterfaceObjectRepresentable : View where Self.Body == Never

## Overview

Use a `WKInterfaceObjectRepresentable` instance to create and manage a
`WKInterfaceObject` in your SwiftUI interface. Adopt this protocol in one of
your app’s custom instances, and use its methods to create, update, and tear
down your interface object. The creation and update processes parallel the
behavior of SwiftUI views, and you use them to configure your interface object
with your app’s current state information. Use the teardown process to remove
your interface object cleanly from your SwiftUI. For example, you might use
the teardown process to notify other parts of your app that the interface
object is disappearing.

To add your interface object into your SwiftUI interface, create your
`WKInterfaceObjectRepresentable` instance and add it to your SwiftUI
interface. The system calls the methods of your representable instance at
appropriate times to create and update the interface object.

The system doesn’t automatically communicate changes occurring within your
interface object to other parts of your SwiftUI interface. When you want your
interface object to coordinate with other SwiftUI views, you must provide a
`Coordinator` instance to facilitate those interactions. For example, you use
a coordinator to forward target-action and delegate messages from your
interface object to any SwiftUI views.

## Topics

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

` typealias Context`

### Cleaning up the interface object

`static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType,
coordinator: Self.Coordinator)`

Cleans up the presented WatchKit interface object (and its coordinator) in
anticipation of their removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**

` associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

## Relationships

### Inherits From

  * `View`

## See Also

### Adding WatchKit views to SwiftUI view hierarchies

`struct WKInterfaceObjectRepresentableContext`

Contextual information about the state of the system that you use to create
and update your WatchKit interface object.

Structure

# WKInterfaceObjectRepresentableContext

Contextual information about the state of the system that you use to create
and update your WatchKit interface object.

watchOS 6.0+

    
    
    @MainActor
    struct WKInterfaceObjectRepresentableContext<Representable> where Representable : WKInterfaceObjectRepresentable

## Overview

A `WKInterfaceObjectRepresentableContext` structure contains details about the
current state of the system. When creating and updating your interface
objects, the system creates one of these structures and passes it to the
appropriate method of your custom `WKInterfaceObjectRepresentable` instance.
Use the information in this structure to configure your object. Don’t create
this structure yourself.

## Topics

### Coordinating interactions

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

### Adding WatchKit views to SwiftUI view hierarchies

`protocol WKInterfaceObjectRepresentable`

A view that represents a WatchKit interface object.

