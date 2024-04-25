Type Property

# privacyPolicy

The privacy policy type.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var privacyPolicy: SubscriptionStorePolicyKind { get }

## See Also

### Getting policy types

`static var termsOfService: SubscriptionStorePolicyKind`

The terms of service policy type.

Type Property

# termsOfService

The terms of service policy type.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var termsOfService: SubscriptionStorePolicyKind { get }

## See Also

### Getting policy types

`static var privacyPolicy: SubscriptionStorePolicyKind`

The privacy policy type.

Instance Property

# hashValue

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing policy types

`func hash(into: inout Hasher)`

`static func != (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Instance Method

# hash(into:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing policy types

`var hashValue: Int`

`static func != (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func != (lhs: SubscriptionStorePolicyKind, rhs: SubscriptionStorePolicyKind) -> Bool

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

### Comparing and hashing policy types

`var hashValue: Int`

`func hash(into: inout Hasher)`

`static func == (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Operator

# ==(_:_:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func == (a: SubscriptionStorePolicyKind, b: SubscriptionStorePolicyKind) -> Bool

## See Also

### Comparing and hashing policy types

`var hashValue: Int`

`func hash(into: inout Hasher)`

`static func != (SubscriptionStorePolicyKind, SubscriptionStorePolicyKind) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

