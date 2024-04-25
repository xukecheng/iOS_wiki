Type Property

# consumable

A consumable in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let consumable: Product.ProductType

## See Also

### Getting the Product Type

`static let nonConsumable: Product.ProductType`

A non-consumable in-app purchase.

`static let nonRenewable: Product.ProductType`

A non-renewing subscription.

`static let autoRenewable: Product.ProductType`

An auto-renewable subscription.

Type Property

# nonConsumable

A non-consumable in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let nonConsumable: Product.ProductType

## See Also

### Getting the Product Type

`static let consumable: Product.ProductType`

A consumable in-app purchase.

`static let nonRenewable: Product.ProductType`

A non-renewing subscription.

`static let autoRenewable: Product.ProductType`

An auto-renewable subscription.

Type Property

# nonRenewable

A non-renewing subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let nonRenewable: Product.ProductType

## See Also

### Getting the Product Type

`static let consumable: Product.ProductType`

A consumable in-app purchase.

`static let nonConsumable: Product.ProductType`

A non-consumable in-app purchase.

`static let autoRenewable: Product.ProductType`

An auto-renewable subscription.

Type Property

# autoRenewable

An auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let autoRenewable: Product.ProductType

## See Also

### Getting the Product Type

`static let consumable: Product.ProductType`

A consumable in-app purchase.

`static let nonConsumable: Product.ProductType`

A non-consumable in-app purchase.

`static let nonRenewable: Product.ProductType`

A non-renewing subscription.

Instance Property

# localizedDescription

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating a Product Type

`let rawValue: String`

The value for product type as a backing value.

`typealias Product.ProductType.RawValue`

Instance Property

# rawValue

The value for product type as a backing value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating a Product Type

`init(rawValue: String)`

`typealias Product.ProductType.RawValue`

Type Alias

# Product.ProductType.RawValue

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.ProductType.RawValue = String

## See Also

### Creating a Product Type

`init(rawValue: String)`

`let rawValue: String`

The value for product type as a backing value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.ProductType, rhs: Product.ProductType) -> Bool

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

### Comparing and Hashing Product Types

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

### Comparing and Hashing Product Types

`static func != (Product.ProductType, Product.ProductType) -> Bool`

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

### Comparing and Hashing Product Types

`static func != (Product.ProductType, Product.ProductType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

