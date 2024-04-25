Instance Property

# product

The in-app purchase product to merchandise.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var product: Product? { get }

## See Also

### Getting a product's information

`let state: Product.TaskState`

The product task state that indicates the product’s loading phase.

`let hasCurrentEntitlement: Bool`

A Boolean value that indicates whether an in-app purchase transaction exists
for the product.

Instance Property

# state

The product task state that indicates the product’s loading phase.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let state: Product.TaskState

## See Also

### Getting a product's information

`var product: Product?`

The in-app purchase product to merchandise.

`let hasCurrentEntitlement: Bool`

A Boolean value that indicates whether an in-app purchase transaction exists
for the product.

Instance Property

# hasCurrentEntitlement

A Boolean value that indicates whether an in-app purchase transaction exists
for the product.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let hasCurrentEntitlement: Bool

## Discussion

Use the `hasCurrentEntitlement` property to determine whether a purchase may
succeed, for a porduct that people can purchase only once. For example, if
hasCurrentEntitlement is false, you may choose not to display a purchase
button for the product, because the person has already purchased it.

Important

Don’t use this value to determine whether to enable access to the product;
check the in-app purchase transaction information instead (`Transaction`).

## See Also

### Getting a product's information

`var product: Product?`

The in-app purchase product to merchandise.

`let state: Product.TaskState`

The product task state that indicates the product’s loading phase.

Instance Property

# icon

A decorative view for merchandising the product.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let icon: ProductViewStyleConfiguration.Icon

## See Also

### Getting a product view's icon

`struct ProductViewStyleConfiguration.Icon`

A type-erased icon of an in-app purchase product.

Instance Method

# purchase()

Initiates a purchase action for the product.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func purchase()

## Discussion

Use this method instead of calling `purchase(options:)`directly on the
product.

Instance Property

# descriptionVisibility

StoreKit  SwiftUI  iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+
tvOS 17.4+  watchOS 10.4+  visionOS 1.1+  Xcode 15.3+

    
    
    let descriptionVisibility: Visibility

