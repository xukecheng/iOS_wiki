Type Property

# current

The current App Store storefront for product purchases.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var current: Storefront? { get async }

## Discussion

Use `current` to determine a customer's current storefront region and offer
in-app products suitable for that region. You maintain your own list of
product identifiers and the storefronts in which you make them available.

## See Also

### Identifying the storefront

`let countryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront.

`let id: String`

An Apple-defined value that uniquely identifies an App Store storefront.

`typealias Storefront.ID`

The type that represents a storefront identifier.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Storefront` conforms to `AnyObject`.

Instance Property

# countryCode

The three-letter code that represents the country or region associated with
the App Store storefront.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let countryCode: String

## Discussion

This property uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

### Identifying the storefront

`static var current: Storefront?`

The current App Store storefront for product purchases.

`let id: String`

An Apple-defined value that uniquely identifies an App Store storefront.

`typealias Storefront.ID`

The type that represents a storefront identifier.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Storefront` conforms to `AnyObject`.

Instance Property

# id

An Apple-defined value that uniquely identifies an App Store storefront.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: String

## Relationships

### From Protocol

  * `Identifiable`

## See Also

### Identifying the storefront

`static var current: Storefront?`

The current App Store storefront for product purchases.

`let countryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront.

`typealias Storefront.ID`

The type that represents a storefront identifier.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Storefront` conforms to `AnyObject`.

Type Alias

# Storefront.ID

The type that represents a storefront identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Storefront.ID = String

## See Also

### Identifying the storefront

`static var current: Storefront?`

The current App Store storefront for product purchases.

`let countryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront.

`let id: String`

An Apple-defined value that uniquely identifies an App Store storefront.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Storefront` conforms to `AnyObject`.

Instance Property

# id

The stable identity of the entity associated with this instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+  Xcode 11.0+

    
    
    var id: ObjectIdentifier { get }

Available when `Storefront` conforms to `AnyObject`.

## Discussion

Note

This documentation comment was inherited from `Identifiable`.

## See Also

### Identifying the storefront

`static var current: Storefront?`

The current App Store storefront for product purchases.

`let countryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront.

`let id: String`

An Apple-defined value that uniquely identifies an App Store storefront.

`typealias Storefront.ID`

The type that represents a storefront identifier.

Type Property

# updates

The asynchronous sequence that emits storefront information when the system
updates the storefront.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Storefront.Storefronts { get }

## Discussion

The storefront value can change at any time. Use `updates` to listen for
changes in this value. Respond to storefront changes by refreshing the list of
your available products.

## See Also

### Listening for storefront changes

`struct Storefront.Storefronts`

An asynchronous sequence that listens for changes to the storefront.

