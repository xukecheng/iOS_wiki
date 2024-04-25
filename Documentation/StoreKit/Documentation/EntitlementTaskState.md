Enumeration Case

# EntitlementTaskState.loading

The task is loading the entitlement in the background.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Getting the task state

`case success(Value)`

The task successfully loaded the entitlement.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.success(_:)

The task successfully loaded the entitlement.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(Value)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.failure(_:)

The task failed to load the entitlement, with an error.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case success(Value)`

The task successfully loaded the entitlement.

Instance Property

# transaction

The transaction value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var transaction: VerificationResult<Transaction>? { get }

Available when `Value` is `VerificationResult``<``Transaction``>?`.

## Discussion

Use `transaction` as a convenience to access the transaction value in code
that doesn’t depend on the reason a transaction isn’t available. The value is
`nil` while the transaction is loading, if it fails to load for any reason, or
if the customer isn’t entitled to the product.

## See Also

### Getting the transaction with the entitlement

`var value: Value?`

The entitlement value if the task is successful.

Instance Property

# value

The entitlement value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var value: Value? { get }

## Discussion

This value is `nil` while the value is loading, or if it fails to load for any
reason.

Use `value` as a convenience to access the entitlement value in code that
doesn’t depend on the reason the value can’t be accessed if it fails to load.

## See Also

### Getting the transaction with the entitlement

`var transaction: VerificationResult<Transaction>?`

The transaction value if the task is successful.

Available when `Value` is `VerificationResult``<``Transaction``>?`.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>

##  Parameters

`transform`

    

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Enumeration Case

# EntitlementTaskState.loading

The task is loading the entitlement in the background.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Getting the task state

`case success(Value)`

The task successfully loaded the entitlement.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.success(_:)

The task successfully loaded the entitlement.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(Value)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.failure(_:)

The task failed to load the entitlement, with an error.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case success(Value)`

The task successfully loaded the entitlement.

Instance Property

# transaction

The transaction value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var transaction: VerificationResult<Transaction>? { get }

Available when `Value` is `VerificationResult``<``Transaction``>?`.

## Discussion

Use `transaction` as a convenience to access the transaction value in code
that doesn’t depend on the reason a transaction isn’t available. The value is
`nil` while the transaction is loading, if it fails to load for any reason, or
if the customer isn’t entitled to the product.

## See Also

### Getting the transaction with the entitlement

`var value: Value?`

The entitlement value if the task is successful.

Instance Property

# value

The entitlement value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var value: Value? { get }

## Discussion

This value is `nil` while the value is loading, or if it fails to load for any
reason.

Use `value` as a convenience to access the entitlement value in code that
doesn’t depend on the reason the value can’t be accessed if it fails to load.

## See Also

### Getting the transaction with the entitlement

`var transaction: VerificationResult<Transaction>?`

The transaction value if the task is successful.

Available when `Value` is `VerificationResult``<``Transaction``>?`.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>

##  Parameters

`transform`

    

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Enumeration Case

# EntitlementTaskState.loading

The task is loading the entitlement in the background.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Getting the task state

`case success(Value)`

The task successfully loaded the entitlement.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.success(_:)

The task successfully loaded the entitlement.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(Value)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case failure(any Error)`

The task failed to load the entitlement, with an error.

Enumeration Case

# EntitlementTaskState.failure(_:)

The task failed to load the entitlement, with an error.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

## See Also

### Getting the task state

`case loading`

The task is loading the entitlement in the background.

`case success(Value)`

The task successfully loaded the entitlement.

Instance Property

# transaction

The transaction value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var transaction: VerificationResult<Transaction>? { get }

Available when `Value` is `VerificationResult``<``Transaction``>?`.

## Discussion

Use `transaction` as a convenience to access the transaction value in code
that doesn’t depend on the reason a transaction isn’t available. The value is
`nil` while the transaction is loading, if it fails to load for any reason, or
if the customer isn’t entitled to the product.

## See Also

### Getting the transaction with the entitlement

`var value: Value?`

The entitlement value if the task is successful.

Instance Property

# value

The entitlement value if the task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var value: Value? { get }

## Discussion

This value is `nil` while the value is loading, or if it fails to load for any
reason.

Use `value` as a convenience to access the entitlement value in code that
doesn’t depend on the reason the value can’t be accessed if it fails to load.

## See Also

### Getting the transaction with the entitlement

`var transaction: VerificationResult<Transaction>?`

The transaction value if the task is successful.

Available when `Value` is `VerificationResult``<``Transaction``>?`.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>

##  Parameters

`transform`

    

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# flatMap(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func flatMap<NewValue>(_ transform: (Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

Generic Instance Method

# map(_:)

Returns a new state, mapping the entitlement value if successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func map<NewValue>(_ transform: (Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>

## See Also

### Helper methods

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func flatMap<NewValue>((Value) -> EntitlementTaskState<NewValue>) ->
EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

`func map<NewValue>((Value) -> NewValue) -> EntitlementTaskState<NewValue>`

Returns a new state, mapping the entitlement value if successful.

