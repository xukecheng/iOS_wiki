Type Property

# subscribed

The user is currently subscribed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let subscribed: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# expired

The subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let expired: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inBillingRetryPeriod

The subscription is in a billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inGracePeriod

The subscription is in a billing grace period state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inGracePeriod: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# revoked

The App Store has revoked the user’s access to the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let revoked: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

Instance Property

# localizedDescription

A string containing the localized description of the renewal state.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value of the renewal state to create.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalState, rhs: Product.SubscriptionInfo.RenewalState) -> Bool

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

### Comparing and hashing renewal states

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# rawValue

The raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalState.RawValue`

A type that represents the raw value of a renewal state.

Type Alias

# Product.SubscriptionInfo.RenewalState.RawValue

A type that represents the raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalState.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value of a renewal state.

Type Property

# subscribed

The user is currently subscribed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let subscribed: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# expired

The subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let expired: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inBillingRetryPeriod

The subscription is in a billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inGracePeriod

The subscription is in a billing grace period state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inGracePeriod: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# revoked

The App Store has revoked the user’s access to the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let revoked: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

Instance Property

# localizedDescription

A string containing the localized description of the renewal state.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value of the renewal state to create.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalState, rhs: Product.SubscriptionInfo.RenewalState) -> Bool

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

### Comparing and hashing renewal states

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# rawValue

The raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalState.RawValue`

A type that represents the raw value of a renewal state.

Type Alias

# Product.SubscriptionInfo.RenewalState.RawValue

A type that represents the raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalState.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value of a renewal state.

Type Property

# subscribed

The user is currently subscribed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let subscribed: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# expired

The subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let expired: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inBillingRetryPeriod

The subscription is in a billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inGracePeriod

The subscription is in a billing grace period state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inGracePeriod: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# revoked

The App Store has revoked the user’s access to the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let revoked: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

Instance Property

# localizedDescription

A string containing the localized description of the renewal state.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value of the renewal state to create.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalState, rhs: Product.SubscriptionInfo.RenewalState) -> Bool

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

### Comparing and hashing renewal states

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# rawValue

The raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalState.RawValue`

A type that represents the raw value of a renewal state.

Type Alias

# Product.SubscriptionInfo.RenewalState.RawValue

A type that represents the raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalState.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value of a renewal state.

Type Property

# subscribed

The user is currently subscribed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let subscribed: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# expired

The subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let expired: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inBillingRetryPeriod

The subscription is in a billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# inGracePeriod

The subscription is in a billing grace period state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inGracePeriod: Product.SubscriptionInfo.RenewalState

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let revoked: Product.SubscriptionInfo.RenewalState`

The App Store has revoked the user’s access to the subscription group.

Type Property

# revoked

The App Store has revoked the user’s access to the subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let revoked: Product.SubscriptionInfo.RenewalState

## See Also

### Getting the renewal state

`static let subscribed: Product.SubscriptionInfo.RenewalState`

The user is currently subscribed.

`static let expired: Product.SubscriptionInfo.RenewalState`

The subscription expired.

`static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing retry period.

`static let inGracePeriod: Product.SubscriptionInfo.RenewalState`

The subscription is in a billing grace period state.

Instance Property

# localizedDescription

A string containing the localized description of the renewal state.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value of the renewal state to create.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalState, rhs: Product.SubscriptionInfo.RenewalState) -> Bool

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

### Comparing and hashing renewal states

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing renewal states

`static func != (Product.SubscriptionInfo.RenewalState,
Product.SubscriptionInfo.RenewalState) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# rawValue

The raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalState.RawValue`

A type that represents the raw value of a renewal state.

Type Alias

# Product.SubscriptionInfo.RenewalState.RawValue

A type that represents the raw value of a renewal state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalState.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value of a renewal state.

