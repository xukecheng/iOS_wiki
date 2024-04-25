Type Property

# automatic

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var automatic: AutomaticProductViewStyle { get }

Available when `Self` is `AutomaticProductViewStyle`.

## See Also

### Getting built-in product view styles

`static var compact: CompactProductViewStyle`

An product view style suitable for layouts where less space is available, or
for displaying more items in a small amount of space.

Available when `Self` is `CompactProductViewStyle`.

`static var large: LargeProductViewStyle`

A product view style suitable for layouts where the in-app purchase content is
prominent.

Available when `Self` is `LargeProductViewStyle`.

`static var regular: RegularProductViewStyle`

A product view style that uses a standard, platform-appropriate layout.

Available when `Self` is `RegularProductViewStyle`.

Type Property

# compact

An product view style suitable for layouts where less space is available, or
for displaying more items in a small amount of space.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  Xcode 15.0+

    
    
    static var compact: CompactProductViewStyle { get }

Available when `Self` is `CompactProductViewStyle`.

## See Also

### Getting built-in product view styles

`static var automatic: AutomaticProductViewStyle`

Available when `Self` is `AutomaticProductViewStyle`.

`static var large: LargeProductViewStyle`

A product view style suitable for layouts where the in-app purchase content is
prominent.

Available when `Self` is `LargeProductViewStyle`.

`static var regular: RegularProductViewStyle`

A product view style that uses a standard, platform-appropriate layout.

Available when `Self` is `RegularProductViewStyle`.

Type Property

# large

A product view style suitable for layouts where the in-app purchase content is
prominent.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
visionOS 1.0+  Xcode 15.0+

    
    
    static var large: LargeProductViewStyle { get }

Available when `Self` is `LargeProductViewStyle`.

## See Also

### Getting built-in product view styles

`static var automatic: AutomaticProductViewStyle`

Available when `Self` is `AutomaticProductViewStyle`.

`static var compact: CompactProductViewStyle`

An product view style suitable for layouts where less space is available, or
for displaying more items in a small amount of space.

Available when `Self` is `CompactProductViewStyle`.

`static var regular: RegularProductViewStyle`

A product view style that uses a standard, platform-appropriate layout.

Available when `Self` is `RegularProductViewStyle`.

Type Property

# regular

A product view style that uses a standard, platform-appropriate layout.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var regular: RegularProductViewStyle { get }

Available when `Self` is `RegularProductViewStyle`.

## See Also

### Getting built-in product view styles

`static var automatic: AutomaticProductViewStyle`

Available when `Self` is `AutomaticProductViewStyle`.

`static var compact: CompactProductViewStyle`

An product view style suitable for layouts where less space is available, or
for displaying more items in a small amount of space.

Available when `Self` is `CompactProductViewStyle`.

`static var large: LargeProductViewStyle`

A product view style suitable for layouts where the in-app purchase content is
prominent.

Available when `Self` is `LargeProductViewStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a product view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of a product view style.

## See Also

### Creating custom product views

`typealias ProductViewStyle.Configuration`

A type that represents the properties of a product view style.

`associatedtype Body`

A view that represents the body of a product view.

**Required**

Type Alias

# ProductViewStyle.Configuration

A type that represents the properties of a product view style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias ProductViewStyle.Configuration = ProductViewStyleConfiguration

## See Also

### Creating custom product views

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a product view.

**Required**

` associatedtype Body`

A view that represents the body of a product view.

**Required**

# Body

A view that represents the body of a product view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom product views

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a product view.

**Required**

` typealias ProductViewStyle.Configuration`

A type that represents the properties of a product view style.

