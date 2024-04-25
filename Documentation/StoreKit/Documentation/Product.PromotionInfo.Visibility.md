Enumeration Case

# Product.PromotionInfo.Visibility.appStoreConnectDefault

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case appStoreConnectDefault

## Discussion

When a promoted in-app purchase has a visibility value of
`Product.PromotionInfo.Visibility.appStoreConnectDefault`, the in-app purchase
is:

  * Visible if the setting in App Store Connect makes it visible

  * Hidden if the setting in App Store Connect makes it hidden

Use this value to control the visibility for promoted in-app purchases in App
Store Connect, globally, for all users. For example, if you have a product to
promote on a holiday, start by manually setting it as hidden using App Store
Connect. On the holiday, change the setting to make the promotion visible. If
the promotion visibility in the app is the default
(`Product.PromotionInfo.Visibility.appStoreConnectDefault`), it becomes
visible for all users automatically.

For more information about the visibility settings in App Store Connect, see
Promote in-app purchases.

## See Also

### Getting visibility states

`case hidden`

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

`case visible`

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

Enumeration Case

# Product.PromotionInfo.Visibility.hidden

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case hidden

## Discussion

A promoted in-app purchase with this visibility setting isn’t visible on the
App Store on a user’s device.

## See Also

### Getting visibility states

`case appStoreConnectDefault`

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

`case visible`

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

Enumeration Case

# Product.PromotionInfo.Visibility.visible

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case visible

## Discussion

A promoted in-app purchase with this visibility setting is visible on the App
Store on a user’s device.

## See Also

### Getting visibility states

`case appStoreConnectDefault`

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

`case hidden`

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

Initializer

# init(rawValue:)

Creates a visibility state.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    init?(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value that represents the visibility of a promoted in-app purchase.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating visibility states

`typealias Product.PromotionInfo.Visibility.RawValue`

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

`var rawValue: Int`

The raw value that represents the visiblity state of a promoted in-app
purchase.

Type Alias

# Product.PromotionInfo.Visibility.RawValue

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    typealias Product.PromotionInfo.Visibility.RawValue = Int

## See Also

### Creating visibility states

`init?(rawValue: Int)`

Creates a visibility state.

`var rawValue: Int`

The raw value that represents the visiblity state of a promoted in-app
purchase.

Instance Property

# rawValue

The raw value that represents the visiblity state of a promoted in-app
purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    var rawValue: Int { get }

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating visibility states

`init?(rawValue: Int)`

Creates a visibility state.

`typealias Product.PromotionInfo.Visibility.RawValue`

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func != (lhs: Product.PromotionInfo.Visibility, rhs: Product.PromotionInfo.Visibility) -> Bool

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

### Comparing and hashing visibility

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    func hash(into hasher: inout Hasher)

## See Also

### Comparing and hashing visibility

`static func != (Product.PromotionInfo.Visibility,
Product.PromotionInfo.Visibility) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing visibility

`static func != (Product.PromotionInfo.Visibility,
Product.PromotionInfo.Visibility) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Enumeration Case

# Product.PromotionInfo.Visibility.appStoreConnectDefault

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case appStoreConnectDefault

## Discussion

When a promoted in-app purchase has a visibility value of
`Product.PromotionInfo.Visibility.appStoreConnectDefault`, the in-app purchase
is:

  * Visible if the setting in App Store Connect makes it visible

  * Hidden if the setting in App Store Connect makes it hidden

Use this value to control the visibility for promoted in-app purchases in App
Store Connect, globally, for all users. For example, if you have a product to
promote on a holiday, start by manually setting it as hidden using App Store
Connect. On the holiday, change the setting to make the promotion visible. If
the promotion visibility in the app is the default
(`Product.PromotionInfo.Visibility.appStoreConnectDefault`), it becomes
visible for all users automatically.

For more information about the visibility settings in App Store Connect, see
Promote in-app purchases.

## See Also

### Getting visibility states

`case hidden`

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

`case visible`

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

Enumeration Case

# Product.PromotionInfo.Visibility.hidden

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case hidden

## Discussion

A promoted in-app purchase with this visibility setting isn’t visible on the
App Store on a user’s device.

## See Also

### Getting visibility states

`case appStoreConnectDefault`

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

`case visible`

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

Enumeration Case

# Product.PromotionInfo.Visibility.visible

A visibility value that makes a promoted in-app purchase visible on the App
Store on a user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    case visible

## Discussion

A promoted in-app purchase with this visibility setting is visible on the App
Store on a user’s device.

## See Also

### Getting visibility states

`case appStoreConnectDefault`

A visibility value for a promoted in-app purchase that uses the visibility
setting from App Store Connect.

`case hidden`

A visibility value that hides a promoted in-app purchase on the App Store on a
user’s device.

Initializer

# init(rawValue:)

Creates a visibility state.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    init?(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value that represents the visibility of a promoted in-app purchase.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating visibility states

`typealias Product.PromotionInfo.Visibility.RawValue`

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

`var rawValue: Int`

The raw value that represents the visiblity state of a promoted in-app
purchase.

Type Alias

# Product.PromotionInfo.Visibility.RawValue

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    typealias Product.PromotionInfo.Visibility.RawValue = Int

## See Also

### Creating visibility states

`init?(rawValue: Int)`

Creates a visibility state.

`var rawValue: Int`

The raw value that represents the visiblity state of a promoted in-app
purchase.

Instance Property

# rawValue

The raw value that represents the visiblity state of a promoted in-app
purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    var rawValue: Int { get }

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating visibility states

`init?(rawValue: Int)`

Creates a visibility state.

`typealias Product.PromotionInfo.Visibility.RawValue`

A type that represents the raw value of the visibility state of a promoted in-
app purchase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func != (lhs: Product.PromotionInfo.Visibility, rhs: Product.PromotionInfo.Visibility) -> Bool

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

### Comparing and hashing visibility

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    func hash(into hasher: inout Hasher)

## See Also

### Comparing and hashing visibility

`static func != (Product.PromotionInfo.Visibility,
Product.PromotionInfo.Visibility) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing visibility

`static func != (Product.PromotionInfo.Visibility,
Product.PromotionInfo.Visibility) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

