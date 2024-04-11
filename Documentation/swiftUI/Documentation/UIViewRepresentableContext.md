Instance Property

# coordinator

The view’s associated coordinator.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    let coordinator: Representable.Coordinator

## See Also

### Coordinating view-related interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating view-related interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

Instance Property

# environment

The current environment.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your view when creating
or updating it.

