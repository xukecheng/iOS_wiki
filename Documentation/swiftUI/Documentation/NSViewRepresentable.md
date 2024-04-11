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

