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

