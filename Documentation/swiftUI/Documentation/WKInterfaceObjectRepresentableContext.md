Instance Property

# coordinator

The view’s associated coordinator.

watchOS 6.0+

    
    
    @MainActor
    let coordinator: Representable.Coordinator

## See Also

### Coordinating interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

watchOS 6.0+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

Instance Property

# environment

The current environment.

watchOS 6.0+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your interface object
when creating or updating it.

