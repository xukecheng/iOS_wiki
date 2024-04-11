Instance Method

# makeUIView(context:)

Creates the view object and configures its initial state.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeUIView(context: Self.Context) -> Self.UIViewType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your UIKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object.
Configure the view using your app’s current data and contents of the `context`
parameter. The system calls this method only once, when it creates your view
for the first time. For all subsequent updates, the system calls the
`updateUIView(_:context:)` method.

## See Also

### Creating and updating the view

`func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Instance Method

# updateUIView(_:context:)

Updates the state of the specified view with new information from SwiftUI.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func updateUIView(
        _ uiView: Self.UIViewType,
        context: Self.Context
    )

**Required**

##  Parameters

`uiView`

    

Your custom view object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding UIKit view. Use this method to update the
configuration of your view to match the new state information provided in the
`context` parameter.

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Type Alias

# UIViewRepresentable.Context

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    typealias Context = UIViewRepresentableContext<Self>

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Associated Type

# UIViewType

The type of view to present.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype UIViewType : UIView

**Required**

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

Instance Method

# sizeThatFits(_:uiView:context:)

Given a proposed size, returns the preferred size of the composite view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    @MainActor
    func sizeThatFits(
        _ proposal: ProposedViewSize,
        uiView: Self.UIViewType,
        context: Self.Context
    ) -> CGSize?

**Required** Default implementation provided.

##  Parameters

`proposal`

    

The proposed size for the view.

`uiView`

    

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

### UIViewRepresentable Implementations

`func sizeThatFits(ProposedViewSize, uiView: Self.UIViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

Type Method

# dismantleUIView(_:coordinator:)

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    static func dismantleUIView(
        _ uiView: Self.UIViewType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`uiView`

    

Your custom view object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
view. For example, you might use this method to remove observers or update
other parts of your SwiftUI interface.

## Default Implementations

### UIViewRepresentable Implementations

`static func dismantleUIView(Self.UIViewType, coordinator: Self.Coordinator)`

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your view might affect other parts of your
app. In your implementation, create a custom Swift instance that can
communicate with other parts of your interface. For example, you might provide
an instance that binds its variables to SwiftUI properties, causing the two to
remain synchronized. If your view doesn’t interact with other parts of your
app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeUIView(context:)` method.
The system provides your coordinator either directly or as part of a context
structure when calling the other methods of your representable instance.

## Default Implementations

### UIViewRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the view.

**Required**

Associated Type

# Coordinator

A type to coordinate with the view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

**Required** Default implementation provided.

Type Alias

# UIViewRepresentable.LayoutOptions

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    typealias LayoutOptions

