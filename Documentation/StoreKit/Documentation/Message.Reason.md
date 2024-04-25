Type Property

# billingIssue

A message the App Store sends that informs people of a billing problem and
enables them to update billing information.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static let billingIssue: Message.Reason

## Discussion

If an auto-renewable subscription fails to renew due to a billing issue, the
subscription enters a billing retry state, and the App Store sends a message
with the `billingIssue` reason.

When a billing issue is in effect, StoreKit displays a Billing Problem message
sheet when your app launches, or when your app asks to display it.

The sheet informs people of the billing issue, and displays an in-app sheet to
enable them to correct the issue without leaving your app. Note that people
can also resolve billing issues outside of your app by navigating to the
manage payments section in Apple ID settings. For more information, see
support.apple.com.

Apple attempts to renew the subscription during the billing retry period, up
to 60 days. During this period, the App Store sends the `billingIssue` message
in the following intervals:

Billing retry interval| Message frequency  
---|---  
Days 1–3| Every 24 hours  
Days 4–16| Every 72 hours  
Days 17–30| Every 96 hours  
Days 31–60| Every 120 hours  
  
The App Store stops sending further messages when the user resolves the
billing issue, cancels the subscription, or when the billing retry period
ends. StoreKit ensures that the sheet appears only if the message is
applicable when your app calls `display(in:)` or `DisplayMessageAction`.

For more information about the billing retry state, see `isInBillingRetry` in
`Product.SubscriptionInfo.RenewalInfo`.

### Test the message in the sandbox environment

You can simulate billing issues in the sandbox environment to test how the
system presents the `billingIssue` message in your app, and how your app
handles it if you choose to delay or suppress its presentation. For more
information, including step-by-step test cases, see Testing failing
subscription renewals and in-app purchases.

## See Also

### Getting the message reasons

`static let generic: Message.Reason`

A message the App Store sends for a generic reason.

`static let priceIncreaseConsent: Message.Reason`

A message the App Store sends when you increase the price of an auto-renewable
subscription and the price increase requires the user’s consent.

Type Property

# generic

A message the App Store sends for a generic reason.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let generic: Message.Reason

## See Also

### Getting the message reasons

`static let billingIssue: Message.Reason`

A message the App Store sends that informs people of a billing problem and
enables them to update billing information.

`static let priceIncreaseConsent: Message.Reason`

A message the App Store sends when you increase the price of an auto-renewable
subscription and the price increase requires the user’s consent.

Type Property

# priceIncreaseConsent

A message the App Store sends when you increase the price of an auto-renewable
subscription and the price increase requires the user’s consent.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let priceIncreaseConsent: Message.Reason

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

## See Also

### Getting the message reasons

`static let billingIssue: Message.Reason`

A message the App Store sends that informs people of a billing problem and
enables them to update billing information.

`static let generic: Message.Reason`

A message the App Store sends for a generic reason.

Instance Property

# localizedDescription

A localized description of the App Store message.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Creates a message reason using the raw value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(rawValue: Int)

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating a message reason

`typealias Message.Reason.RawValue`

A type representing the raw value of a message reason.

`let rawValue: Int`

The raw value of a message reason.

Type Alias

# Message.Reason.RawValue

A type representing the raw value of a message reason.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Message.Reason.RawValue = Int

## See Also

### Creating a message reason

`init(rawValue: Int)`

Creates a message reason using the raw value.

`let rawValue: Int`

The raw value of a message reason.

Instance Property

# rawValue

The raw value of a message reason.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating a message reason

`init(rawValue: Int)`

Creates a message reason using the raw value.

`typealias Message.Reason.RawValue`

A type representing the raw value of a message reason.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: Message.Reason, rhs: Message.Reason) -> Bool

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

### Comparing and hashing message reasons

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

## See Also

### Comparing and hashing message reasons

`static func != (Message.Reason, Message.Reason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing message reasons

`static func != (Message.Reason, Message.Reason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

