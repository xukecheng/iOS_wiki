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

