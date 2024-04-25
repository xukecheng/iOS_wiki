Instance Method

# fetchStorePromotionOrder(completionHandler:)

Reads the product order override that determines the promoted product order on
this device.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+

    
    
    func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?) -> Void)? = nil)

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

This function returns an array of promoted products whose order is overridden
on the given device.

If all the products appear in the default order, this method returns an empty
array.

## See Also

### Managing promoted product order

`func update(storePromotionOrder: [SKProduct], completionHandler: (((any
Error)?) -> Void)?)`

Overrides the promoted product order on this device.

Instance Method

# update(storePromotionOrder:completionHandler:)

Overrides the promoted product order on this device.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+

    
    
    func update(
        storePromotionOrder promotionOrder: [SKProduct],
        completionHandler: (((any Error)?) -> Void)? = nil
    )

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

The default order of promoted in-app purchase products is set in App Store
Connect. You can override this order per device. For example, you can promote
an in-app purchase product that unlocks a specific level in your game when a
user reaches the level immediately before the specified level.

To override the default product order, put the product information for the
subset of products you want to reorder into an array, in the order you want
them to appear in. Pass the array to the
`update(storePromotionOrder:completionHandler:)` method. The products in the
array are shown at the beginning of the list, followed by the remaining in-app
purchase products, which are listed in the same relative order that you set in
App Store Connect.

To cancel order overrides, send an empty product array to the
`update(storePromotionOrder:completionHandler:)` method. The in-app purchase
products will be displayed in the default order.

## See Also

### Managing promoted product order

`func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?)
-> Void)?)`

Reads the product order override that determines the promoted product order on
this device.

Instance Method

# fetchStorePromotionVisibility(for:completionHandler:)

Reads the visibility setting of a promoted product in the App Store for this
device.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+

    
    
    func fetchStorePromotionVisibility(
        for product: SKProduct,
        completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)? = nil
    )

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

The default visibility for a promoted product is set in App Store Connect.
Call `fetchStorePromotionVisibility(for:completionHandler:)` to determine if a
product's visibility is set to the default value or if it has been overridden
to be hidden or shown.

## See Also

### Managing promoted product visibility

`func update(storePromotionVisibility: SKProductStorePromotionVisibility, for:
SKProduct, completionHandler: (((any Error)?) -> Void)?)`

Updates the visibility of the product on the App Store, per device.

`enum SKProductStorePromotionVisibility`

The visibility settings that determine if an in-app purchase is visible on a
device.

Instance Method

# update(storePromotionVisibility:for:completionHandler:)

Updates the visibility of the product on the App Store, per device.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+

    
    
    func update(
        storePromotionVisibility promotionVisibility: SKProductStorePromotionVisibility,
        for product: SKProduct,
        completionHandler: (((any Error)?) -> Void)? = nil
    )

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

An in-app purchase product's default visibility setting is set up in App Store
Connect. You can override the default setting, or return it to the default set
in App Store Connect using the values in `SKProductStorePromotionVisibility`.

Visibility settings apply per device.

## See Also

### Managing promoted product visibility

`func fetchStorePromotionVisibility(for: SKProduct, completionHandler:
((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)`

Reads the visibility setting of a promoted product in the App Store for this
device.

`enum SKProductStorePromotionVisibility`

The visibility settings that determine if an in-app purchase is visible on a
device.

Type Method

# default()

Returns the default product store promotion controller.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+

    
    
    class func `default`() -> Self

