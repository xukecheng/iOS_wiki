Enumeration Case

# ExternalPurchase.NoticeResult.cancelled

Describes when people chose to cancel and not view external purchases.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    case cancelled

## Discussion

If your app’s call to `presentNoticeSheet()` results in this value, you must
not show external purchases.

## See Also

### Getting notice sheet results

`case continuedWithExternalPurchaseToken(token: String)`

Describes when people chose to continue to view external purchases, and
provides the external purchase token.

Enumeration Case

# ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)

Describes when people chose to continue to view external purchases, and
provides the external purchase token.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 15.3+

    
    
    case continuedWithExternalPurchaseToken(token: String)

##  Parameters

`token`

    

The external purchase token.

## Discussion

When your app calls `presentNoticeSheet()` and it results in this value:
`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`,
your app can proceed to present external purchases.

Important

Record and use the token to report the customer’s external purchases to Apple.
For more information, see External Purchase Server API.

``

## See Also

### Getting notice sheet results

`case cancelled`

Describes when people chose to cancel and not view external purchases.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 15.4+  watchOS
10.4+  visionOS 1.0+  Xcode 13.3+

    
    
    static func != (lhs: ExternalPurchase.NoticeResult, rhs: ExternalPurchase.NoticeResult) -> Bool

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

### Comparing and hashing results

`static func == (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    static func == (a: ExternalPurchase.NoticeResult, b: ExternalPurchase.NoticeResult) -> Bool

## See Also

### Comparing and hashing results

`static func != (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing results

`static func != (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing results

`static func != (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (ExternalPurchase.NoticeResult, ExternalPurchase.NoticeResult)
-> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

