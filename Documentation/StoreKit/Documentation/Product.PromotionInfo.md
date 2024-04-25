Instance Property

# productID

The product identifier of the promoted in-app purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    let productID: Product.ID

Type Method

# updateProductOrder(byID:)

Sets the display order of promoted in-app purchases in the App Store, using
product identifiers.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateProductOrder(byID order: some Collection<String>) async throws

##  Parameters

`order`

    

A collection of product identifiers (`Product.ID`) in the order that you want
the promoted in-app purchases to appear, from first to last. Use an empty list
to cancel previous changes.

## Discussion

Call this static method to override the default order of promoted in-app
purchases on the current device. You provide the product identifiers of the
promoted in-app purchases to set their order.

To hide a promoted in-app purchase so it doesn't display in the App Store for
the user, don't include its product identifier when calling this method. You
may want to do this, for example, if the user has already purchased the
product, or if it isn't relevant to them for some other reason.

To set the order using `Product.PromotionInfo` objects instead of product
identifiers, see `updateAll(_:)`.

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection
in the `order` parameter. All in-app purchases then display in the default
order.

Type Property

# currentOrder

Gets the customized order of the promotion info objects the represent promoted
products.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static var currentOrder: [Product.PromotionInfo] { get async throws }

## Discussion

This asynchronous array returns a list of `Product.PromotionInfo` objects in
the custom order they appear in on the device.

Note

This list is empty if you don’t override the order, and the App Store displays
the products in their default order.

For information about setting the default order using App Store Connect, see
Promote in-app purchases.

Instance Property

# visibility

A value that indicates whether the promoted in-app purchase is visible or
hidden on the user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    var visibility: Product.PromotionInfo.Visibility

## Discussion

To override the visibility of a promoted in-app purchase, set the `visibility`
value and then call `update()` to save the change. You can also call
`updateProductVisibility(_:for:)` to set the visibility.

The default value is
`Product.PromotionInfo.Visibility.appStoreConnectDefault`.

## See Also

### Managing promotion visibility

`enum Product.PromotionInfo.Visibility`

The visibility states for product promotion information.

`static func updateProductVisibility(Product.PromotionInfo.Visibility, for:
Product.ID)`

Updates a value that indicates whether a promoted in-app purchase appears in
the App Store on the user's device.

Type Method

# updateProductVisibility(_:for:)

Updates a value that indicates whether a promoted in-app purchase appears in
the App Store on the user's device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateProductVisibility(
        _ visibility: Product.PromotionInfo.Visibility,
        for productID: Product.ID
    ) async throws

##  Parameters

`visibility`

    

A visibility value of `Product.PromotionInfo.Visibility` that determines
whether a promoted in-app purchase appears in the App Store on the user's
device.

`productID`

    

The product identifier of the promoted in-app purchase.

## Discussion

Call this method to change the visibility setting for a promoted in-app
purchase. Changes take effect after you call this method.

The following code example updates a promoted product's visibility after the
user purchases it. The purchased product is hidden to avoid showing it again
on the device.

## See Also

### Managing promotion visibility

`var visibility: Product.PromotionInfo.Visibility`

A value that indicates whether the promoted in-app purchase is visible or
hidden on the user’s device.

`enum Product.PromotionInfo.Visibility`

The visibility states for product promotion information.

Instance Method

# update()

Saves your changes to the promoted product’s visibility.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    func update() async throws

## Discussion

If you change the `visibility` value by setting it directly, call `update()`
to save your changes to the App Store server. Changes take effect after you
call `update()` or `updateAll(_:)`.

## See Also

### Updating order and visibility

`static func updateAll(some Collection<Product.PromotionInfo>)`

Sets the order and visibility of all the promoted products and saves your
changes.

Type Method

# updateAll(_:)

Sets the order and visibility of all the promoted products and saves your
changes.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateAll(_ promotions: some Collection<Product.PromotionInfo>) async throws

##  Parameters

`promotions`

    

A collection of `Product.PromotionInfo` objects that you list in the order
they are to appear in the App Store on the user’s device. Use an empty
collection to cancel previous changes.

## Discussion

Call this static method to set the order of promoted in-app purchases for the
user. Calling this method overrides any previous order and visibility that you
set for this user.

To remove a promoted in-app purchase so it doesn’t display for a user, there
are two options:

  * Don’t include it in the `promotions` collection.

  * Change its `visibility` value to `Product.PromotionInfo.Visibility.hidden`.

To set the order of promoted in-app purchases using product identifiers
instead of `Product.PromotionInfo` objects, see `updateProductOrder(byID:)`.

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection
in `promotions`. All in-app purchases then display in the default order.

## See Also

### Updating order and visibility

`func update()`

Saves your changes to the promoted product’s visibility.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func != (lhs: Product.PromotionInfo, rhs: Product.PromotionInfo) -> Bool

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

### Comparing promotion info

`static func == (Product.PromotionInfo, Product.PromotionInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func == (a: Product.PromotionInfo, b: Product.PromotionInfo) -> Bool

## See Also

### Comparing promotion info

`static func != (Product.PromotionInfo, Product.PromotionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Instance Property

# productID

The product identifier of the promoted in-app purchase.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    let productID: Product.ID

Type Method

# updateProductOrder(byID:)

Sets the display order of promoted in-app purchases in the App Store, using
product identifiers.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateProductOrder(byID order: some Collection<String>) async throws

##  Parameters

`order`

    

A collection of product identifiers (`Product.ID`) in the order that you want
the promoted in-app purchases to appear, from first to last. Use an empty list
to cancel previous changes.

## Discussion

Call this static method to override the default order of promoted in-app
purchases on the current device. You provide the product identifiers of the
promoted in-app purchases to set their order.

To hide a promoted in-app purchase so it doesn't display in the App Store for
the user, don't include its product identifier when calling this method. You
may want to do this, for example, if the user has already purchased the
product, or if it isn't relevant to them for some other reason.

To set the order using `Product.PromotionInfo` objects instead of product
identifiers, see `updateAll(_:)`.

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection
in the `order` parameter. All in-app purchases then display in the default
order.

Type Property

# currentOrder

Gets the customized order of the promotion info objects the represent promoted
products.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static var currentOrder: [Product.PromotionInfo] { get async throws }

## Discussion

This asynchronous array returns a list of `Product.PromotionInfo` objects in
the custom order they appear in on the device.

Note

This list is empty if you don’t override the order, and the App Store displays
the products in their default order.

For information about setting the default order using App Store Connect, see
Promote in-app purchases.

Instance Property

# visibility

A value that indicates whether the promoted in-app purchase is visible or
hidden on the user’s device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    var visibility: Product.PromotionInfo.Visibility

## Discussion

To override the visibility of a promoted in-app purchase, set the `visibility`
value and then call `update()` to save the change. You can also call
`updateProductVisibility(_:for:)` to set the visibility.

The default value is
`Product.PromotionInfo.Visibility.appStoreConnectDefault`.

## See Also

### Managing promotion visibility

`enum Product.PromotionInfo.Visibility`

The visibility states for product promotion information.

`static func updateProductVisibility(Product.PromotionInfo.Visibility, for:
Product.ID)`

Updates a value that indicates whether a promoted in-app purchase appears in
the App Store on the user's device.

Type Method

# updateProductVisibility(_:for:)

Updates a value that indicates whether a promoted in-app purchase appears in
the App Store on the user's device.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateProductVisibility(
        _ visibility: Product.PromotionInfo.Visibility,
        for productID: Product.ID
    ) async throws

##  Parameters

`visibility`

    

A visibility value of `Product.PromotionInfo.Visibility` that determines
whether a promoted in-app purchase appears in the App Store on the user's
device.

`productID`

    

The product identifier of the promoted in-app purchase.

## Discussion

Call this method to change the visibility setting for a promoted in-app
purchase. Changes take effect after you call this method.

The following code example updates a promoted product's visibility after the
user purchases it. The purchased product is hidden to avoid showing it again
on the device.

## See Also

### Managing promotion visibility

`var visibility: Product.PromotionInfo.Visibility`

A value that indicates whether the promoted in-app purchase is visible or
hidden on the user’s device.

`enum Product.PromotionInfo.Visibility`

The visibility states for product promotion information.

Instance Method

# update()

Saves your changes to the promoted product’s visibility.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    func update() async throws

## Discussion

If you change the `visibility` value by setting it directly, call `update()`
to save your changes to the App Store server. Changes take effect after you
call `update()` or `updateAll(_:)`.

## See Also

### Updating order and visibility

`static func updateAll(some Collection<Product.PromotionInfo>)`

Sets the order and visibility of all the promoted products and saves your
changes.

Type Method

# updateAll(_:)

Sets the order and visibility of all the promoted products and saves your
changes.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func updateAll(_ promotions: some Collection<Product.PromotionInfo>) async throws

##  Parameters

`promotions`

    

A collection of `Product.PromotionInfo` objects that you list in the order
they are to appear in the App Store on the user’s device. Use an empty
collection to cancel previous changes.

## Discussion

Call this static method to set the order of promoted in-app purchases for the
user. Calling this method overrides any previous order and visibility that you
set for this user.

To remove a promoted in-app purchase so it doesn’t display for a user, there
are two options:

  * Don’t include it in the `promotions` collection.

  * Change its `visibility` value to `Product.PromotionInfo.Visibility.hidden`.

To set the order of promoted in-app purchases using product identifiers
instead of `Product.PromotionInfo` objects, see `updateProductOrder(byID:)`.

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection
in `promotions`. All in-app purchases then display in the default order.

## See Also

### Updating order and visibility

`func update()`

Saves your changes to the promoted product’s visibility.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func != (lhs: Product.PromotionInfo, rhs: Product.PromotionInfo) -> Bool

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

### Comparing promotion info

`static func == (Product.PromotionInfo, Product.PromotionInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func == (a: Product.PromotionInfo, b: Product.PromotionInfo) -> Bool

## See Also

### Comparing promotion info

`static func != (Product.PromotionInfo, Product.PromotionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

