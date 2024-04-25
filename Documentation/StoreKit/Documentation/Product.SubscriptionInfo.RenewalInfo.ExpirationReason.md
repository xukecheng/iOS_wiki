Type Property

# autoRenewDisabled

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# billingError

The auto-renewable subscription expired because of a billing error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## Discussion

Check the value of `isInBillingRetry` to determine whether an auto-renewable
subscription is in a billing retry state.

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# didNotConsentToPriceIncrease

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# productUnavailable

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# unknown

The auto-renewable subscription expired for an unknown reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

Instance Property

# localizedDescription

The localized text that describes the expiration reason.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw value that represents an expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Discussion

Use raw values to help parse the `jsonRepresentation` property of the
`Product.SubscriptionInfo.RenewalInfo`.

When subscription renewal information has an `expirationReason` value, its
`jsonRepresentation` contains an integer that represents the expiration
reason, which is its raw value. Compare the JSON data directly to the
expiration reason’s `rawValue`.

You can also use the `rawValue` to create an expiration reason instance by
calling `init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue`

A type that represents the raw value of a subscription expiration reason.

Type Alias

# Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue

A type that represents the raw value of a subscription expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value that represents an expiration reason.

Initializer

# init(rawValue:)

Creates an expiration reason instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

An integer that represents an expiration reason.

## Discussion

Typically, you get an expiration reason from the `expirationReason` property
of `Product.SubscriptionInfo.RenewalInfo` and you don’t need to instantiate it
yourself.

However, if you use the `jsonRepresentation` property of
`Product.SubscriptionInfo.RenewalInfo`, you can use raw values and the
initializer to help parse the JSON data. The data contains the integer
representation of the ownership type, which is its raw value. Call
`init(rawValue:)` to create your own instance from that raw value.
Alternatively, you can compare the JSON data directly to the expiration
reason’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason, rhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool

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

### Comparing and hashing expiration reasons

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

## See Also

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

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

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# autoRenewDisabled

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# billingError

The auto-renewable subscription expired because of a billing error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## Discussion

Check the value of `isInBillingRetry` to determine whether an auto-renewable
subscription is in a billing retry state.

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# didNotConsentToPriceIncrease

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# productUnavailable

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# unknown

The auto-renewable subscription expired for an unknown reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

Instance Property

# localizedDescription

The localized text that describes the expiration reason.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw value that represents an expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Discussion

Use raw values to help parse the `jsonRepresentation` property of the
`Product.SubscriptionInfo.RenewalInfo`.

When subscription renewal information has an `expirationReason` value, its
`jsonRepresentation` contains an integer that represents the expiration
reason, which is its raw value. Compare the JSON data directly to the
expiration reason’s `rawValue`.

You can also use the `rawValue` to create an expiration reason instance by
calling `init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue`

A type that represents the raw value of a subscription expiration reason.

Type Alias

# Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue

A type that represents the raw value of a subscription expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value that represents an expiration reason.

Initializer

# init(rawValue:)

Creates an expiration reason instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

An integer that represents an expiration reason.

## Discussion

Typically, you get an expiration reason from the `expirationReason` property
of `Product.SubscriptionInfo.RenewalInfo` and you don’t need to instantiate it
yourself.

However, if you use the `jsonRepresentation` property of
`Product.SubscriptionInfo.RenewalInfo`, you can use raw values and the
initializer to help parse the JSON data. The data contains the integer
representation of the ownership type, which is its raw value. Call
`init(rawValue:)` to create your own instance from that raw value.
Alternatively, you can compare the JSON data directly to the expiration
reason’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason, rhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool

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

### Comparing and hashing expiration reasons

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

## See Also

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

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

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# autoRenewDisabled

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# billingError

The auto-renewable subscription expired because of a billing error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## Discussion

Check the value of `isInBillingRetry` to determine whether an auto-renewable
subscription is in a billing retry state.

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# didNotConsentToPriceIncrease

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# productUnavailable

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# unknown

The auto-renewable subscription expired for an unknown reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

Instance Property

# localizedDescription

The localized text that describes the expiration reason.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw value that represents an expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Discussion

Use raw values to help parse the `jsonRepresentation` property of the
`Product.SubscriptionInfo.RenewalInfo`.

When subscription renewal information has an `expirationReason` value, its
`jsonRepresentation` contains an integer that represents the expiration
reason, which is its raw value. Compare the JSON data directly to the
expiration reason’s `rawValue`.

You can also use the `rawValue` to create an expiration reason instance by
calling `init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue`

A type that represents the raw value of a subscription expiration reason.

Type Alias

# Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue

A type that represents the raw value of a subscription expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value that represents an expiration reason.

Initializer

# init(rawValue:)

Creates an expiration reason instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

An integer that represents an expiration reason.

## Discussion

Typically, you get an expiration reason from the `expirationReason` property
of `Product.SubscriptionInfo.RenewalInfo` and you don’t need to instantiate it
yourself.

However, if you use the `jsonRepresentation` property of
`Product.SubscriptionInfo.RenewalInfo`, you can use raw values and the
initializer to help parse the JSON data. The data contains the integer
representation of the ownership type, which is its raw value. Call
`init(rawValue:)` to create your own instance from that raw value.
Alternatively, you can compare the JSON data directly to the expiration
reason’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason, rhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool

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

### Comparing and hashing expiration reasons

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

## See Also

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

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

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# autoRenewDisabled

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# billingError

The auto-renewable subscription expired because of a billing error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## Discussion

Check the value of `isInBillingRetry` to determine whether an auto-renewable
subscription is in a billing retry state.

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# didNotConsentToPriceIncrease

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# productUnavailable

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired for an unknown reason.

Type Property

# unknown

The auto-renewable subscription expired for an unknown reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason

## See Also

### Getting the expiration reason

`static let autoRenewDisabled:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the customer voluntarily
canceled their subscription.

`static let billingError:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because of a billing error.

`static let didNotConsentToPriceIncrease:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The subscription expired because the customer didn’t consent to an auto-
renewable subscription price increase that requires customer consent.

`static let productUnavailable:
Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The auto-renewable subscription expired because the product was unavailable
for purchase at the time of the renewal.

Instance Property

# localizedDescription

The localized text that describes the expiration reason.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw value that represents an expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Discussion

Use raw values to help parse the `jsonRepresentation` property of the
`Product.SubscriptionInfo.RenewalInfo`.

When subscription renewal information has an `expirationReason` value, its
`jsonRepresentation` contains an integer that represents the expiration
reason, which is its raw value. Compare the JSON data directly to the
expiration reason’s `rawValue`.

You can also use the `rawValue` to create an expiration reason instance by
calling `init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue`

A type that represents the raw value of a subscription expiration reason.

Type Alias

# Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue

A type that represents the raw value of a subscription expiration reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionInfo.RenewalInfo.ExpirationReason.RawValue = Int

## See Also

### Accessing the raw value

`let rawValue: Int`

The raw value that represents an expiration reason.

Initializer

# init(rawValue:)

Creates an expiration reason instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

An integer that represents an expiration reason.

## Discussion

Typically, you get an expiration reason from the `expirationReason` property
of `Product.SubscriptionInfo.RenewalInfo` and you don’t need to instantiate it
yourself.

However, if you use the `jsonRepresentation` property of
`Product.SubscriptionInfo.RenewalInfo`, you can use raw values and the
initializer to help parse the JSON data. The data contains the integer
representation of the ownership type, which is its raw value. Call
`init(rawValue:)` to create your own instance from that raw value.
Alternatively, you can compare the JSON data directly to the expiration
reason’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason, rhs: Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool

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

### Comparing and hashing expiration reasons

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

## See Also

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

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

### Comparing and hashing expiration reasons

`static func != (Product.SubscriptionInfo.RenewalInfo.ExpirationReason,
Product.SubscriptionInfo.RenewalInfo.ExpirationReason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

