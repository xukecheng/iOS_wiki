Instance Property

# delegate

The store view controller’s delegate.

iOS 6.0+  iPadOS 6.0+  macOS 11.0+  Mac Catalyst 13.0+

    
    
    weak var delegate: (any SKStoreProductViewControllerDelegate)? { get set }

## Discussion

Your application must set the delegate before presenting the store view
controller.

## See Also

### Setting a delegate

`protocol SKStoreProductViewControllerDelegate`

A protocol called when the user dismisses the store screen.

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# loadProduct(withParameters:completionBlock:)

Loads a new product screen to display.

iOS 6.0+  iPadOS 6.0+  macOS 11.0+  Mac Catalyst 13.0+

    
    
    func loadProduct(
        withParameters parameters: [String : Any],
        completionBlock block: ((Bool, (any Error)?) -> Void)? = nil
    )

##  Parameters

`parameters`

    

A dictionary describing the content you want the view controller to display.
See Product Dictionary Keys for keys that describe the product. See Ad network
install-validation keys for keys that describe an impression in an advertising
campaign.

`block`

    

A block to be called when the product information has been loaded from the App
Store. The completion block is called on the main thread and receives the
following parameters:

`result`

    

`true` if the product information was successfully loaded, otherwise `false`.

`error`

    

If an error occurred, this object describes the error. If the product
information was successfully loaded, this value is `nil`.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

For a seamless user experience, load the product information before presenting
the `SKStoreProductViewController` view controller. However, if you load the
product information while presenting the view controller, once loaded, the
product data replaces the contents of the view controller.

## See Also

### Loading a new product screen

Offering media for sale in your app

Allow users to purchase media in the App Store from within your app.

`func loadProduct(withParameters: [String : Any], impression: SKAdImpression,
completionBlock: ((Bool, (any Error)?) -> Void)?)`

API Reference

Product Dictionary Keys

Keys for identifying products and the tokens for affiliates and campaigns.

Instance Method

# loadProduct(withParameters:impression:completionBlock:)

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    func loadProduct(
        withParameters parameters: [String : Any],
        impression: SKAdImpression,
        completionBlock block: ((Bool, (any Error)?) -> Void)? = nil
    )

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

## See Also

### Loading a new product screen

Offering media for sale in your app

Allow users to purchase media in the App Store from within your app.

`func loadProduct(withParameters: [String : Any], completionBlock: ((Bool,
(any Error)?) -> Void)?)`

Loads a new product screen to display.

API Reference

Product Dictionary Keys

Keys for identifying products and the tokens for affiliates and campaigns.

Instance Method

# loadProduct(parameters:impression:)

AdAttributionKit  StoreKit  iOS 17.4+  iPadOS 17.4+  Xcode 15.3+

    
    
    @MainActor
    func loadProduct(
        parameters: [String : Any],
        impression: AppImpression
    ) async throws

