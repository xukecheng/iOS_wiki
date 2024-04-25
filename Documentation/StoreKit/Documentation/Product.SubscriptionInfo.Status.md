Type Property

# updates

The asynchronous sequence that emits status information when a subscription’s
status changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Product.SubscriptionInfo.Status.Statuses { get }

## See Also

### Monitoring subscription status changes

`static var all: AsyncStream<(groupID: String, statuses:
[Product.SubscriptionInfo.Status])>`

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Type Property

# all

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }

## See Also

### Monitoring subscription status changes

`static var updates: Product.SubscriptionInfo.Status.Statuses`

The asynchronous sequence that emits status information when a subscription’s
status changes.

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# renewalInfo

The signed renewal information for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# transaction

The latest transaction for the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let transaction: VerificationResult<Transaction>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.Status, rhs: Product.SubscriptionInfo.Status) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing status

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo.Status, b: Product.SubscriptionInfo.Status) -> Bool

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# updates

The asynchronous sequence that emits status information when a subscription’s
status changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Product.SubscriptionInfo.Status.Statuses { get }

## See Also

### Monitoring subscription status changes

`static var all: AsyncStream<(groupID: String, statuses:
[Product.SubscriptionInfo.Status])>`

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Type Property

# all

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }

## See Also

### Monitoring subscription status changes

`static var updates: Product.SubscriptionInfo.Status.Statuses`

The asynchronous sequence that emits status information when a subscription’s
status changes.

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# renewalInfo

The signed renewal information for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# transaction

The latest transaction for the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let transaction: VerificationResult<Transaction>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.Status, rhs: Product.SubscriptionInfo.Status) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing status

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo.Status, b: Product.SubscriptionInfo.Status) -> Bool

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# updates

The asynchronous sequence that emits status information when a subscription’s
status changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Product.SubscriptionInfo.Status.Statuses { get }

## See Also

### Monitoring subscription status changes

`static var all: AsyncStream<(groupID: String, statuses:
[Product.SubscriptionInfo.Status])>`

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Type Property

# all

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }

## See Also

### Monitoring subscription status changes

`static var updates: Product.SubscriptionInfo.Status.Statuses`

The asynchronous sequence that emits status information when a subscription’s
status changes.

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# renewalInfo

The signed renewal information for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# transaction

The latest transaction for the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let transaction: VerificationResult<Transaction>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.Status, rhs: Product.SubscriptionInfo.Status) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing status

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo.Status, b: Product.SubscriptionInfo.Status) -> Bool

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# updates

The asynchronous sequence that emits status information when a subscription’s
status changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Product.SubscriptionInfo.Status.Statuses { get }

## See Also

### Monitoring subscription status changes

`static var all: AsyncStream<(groupID: String, statuses:
[Product.SubscriptionInfo.Status])>`

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Type Property

# all

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }

## See Also

### Monitoring subscription status changes

`static var updates: Product.SubscriptionInfo.Status.Statuses`

The asynchronous sequence that emits status information when a subscription’s
status changes.

`struct Product.SubscriptionInfo.Status.Statuses`

An asynchronous sequence that listens for new subscription status information.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# renewalInfo

The signed renewal information for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# transaction

The latest transaction for the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let transaction: VerificationResult<Transaction>

## See Also

### Getting subscription status information

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.Status, rhs: Product.SubscriptionInfo.Status) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing status

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo.Status, b: Product.SubscriptionInfo.Status) -> Bool

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing status

`static func != (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.Status,
Product.SubscriptionInfo.Status) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

