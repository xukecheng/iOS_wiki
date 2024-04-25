Enumeration Case

# Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately

A subscription-renewal behavior in the testing environment that cancels the
subscription, resulting in only one subscription period.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    case cancelImmediately

## Discussion

Choose this option for test cases that require an auto-renewable subscription
that won't renew.

## See Also

### Renewal behaviors in the testing environment

`case renewUntilNow`

A subscription-renewal behavior in the testing environment that allows the
subscription to renew continuously, up to the current date.

Enumeration Case

# Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow

A subscription-renewal behavior in the testing environment that allows the
subscription to renew continuously, up to the current date.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    case renewUntilNow

## Discussion

Choose this option to create test cases that require an auto-renewable
subscription that continues to renew. If you set the purchase date in
`purchaseDate(_:renewalBehavior:)`to the past, the testing environment
generates transactions for all the subscription renewals up to the current
date.

## See Also

### Renewal behaviors in the testing environment

`case cancelImmediately`

A subscription-renewal behavior in the testing environment that cancels the
subscription, resulting in only one subscription period.

Initializer

# init(from:)

Creates a subscription renewal behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    init(from decoder: any Decoder) throws

## Relationships

### From Protocol

  * `Decodable`

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Default implementations

`var hashValue: Int`

The hash value.

`static func == (Product.PurchaseOption.SubscriptionRenewalBehavior,
Product.PurchaseOption.SubscriptionRenewalBehavior) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func encode(to: any Encoder)`

Encodes this value into the given encoder.

Instance Property

# hashValue

The hash value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Default implementations

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`static func == (Product.PurchaseOption.SubscriptionRenewalBehavior,
Product.PurchaseOption.SubscriptionRenewalBehavior) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func encode(to: any Encoder)`

Encodes this value into the given encoder.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    static func == (a: Product.PurchaseOption.SubscriptionRenewalBehavior, b: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Bool

##  Parameters

`a`

    

A value to compare.

`b`

    

Another value to compare.

## See Also

### Default implementations

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

`func encode(to: any Encoder)`

Encodes this value into the given encoder.

Instance Method

# encode(to:)

Encodes this value into the given encoder.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    func encode(to encoder: any Encoder) throws

##  Parameters

`encoder`

    

The encoder to write data to.

## Relationships

### From Protocol

  * `Encodable`

## See Also

### Default implementations

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

`static func == (Product.PurchaseOption.SubscriptionRenewalBehavior,
Product.PurchaseOption.SubscriptionRenewalBehavior) -> Bool`

Returns a Boolean value indicating whether two values are equal.

