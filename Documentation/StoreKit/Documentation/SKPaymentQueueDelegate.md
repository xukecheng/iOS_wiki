Instance Method

# paymentQueue(_:shouldContinue:in:)

Asks the delegate whether to continue the transaction if the device’s App
Store storefront changes during a transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func paymentQueue(
        _ paymentQueue: SKPaymentQueue,
        shouldContinue transaction: SKPaymentTransaction,
        in newStorefront: SKStorefront
    ) -> Bool

## Discussion

StoreKit calls this delegate method if the storefront changes while processing
a transaction.

  * Return `true` if you wish to continue the transaction within the updated storefront. 

  * Return `false` to stop the transaction. The transaction will fail with the error `SKError.Code.storeProductNotAvailable`. In this case, consider displaying a message to the user indicating that the product isn't available in the current storefront.

If the delegate isn't implemented, `paymentQueue(_:shouldContinue:in:)`
defaults to `true`.

This call times out after approximately one second, defaulting to `false` and
causing the transaction to fail. The delegate should return as quickly as
possible. Don't perform any networking calls in this method. Your app should
cache product availability information locally before starting a transaction.

See `SKStorefront` for more information.

Instance Method

# paymentQueueShouldShowPriceConsent(_:)

Asks the delegate whether to immediately display a price consent sheet.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    optional func paymentQueueShouldShowPriceConsent(_ paymentQueue: SKPaymentQueue) -> Bool

## Discussion

This method applies only to auto-renewable subscription price increases that
require customer consent.

The default return value for this optional method is `true`. By default, the
system displays the price consent sheet when you increase the subscription
price in App Store Connect and the subscriber hasn’t yet taken action.

The system calls your delegate’s method, if appropriate, when you add the
first observer to `SKPaymentQueue`, and any time the app comes to foreground.

If you return `false`, the system won’t show the price consent sheet. You can
choose to display it later by calling `showPriceConsentIfNeeded()`. You may
want to delay showing the sheet if it would interrupt your user’s interaction
in your app.

Note

When you increase the price of an auto-renewable subscription and it requires
customer consent, Apple informs affected subscribers through an email, push
notification, and an in-app price consent sheet and asks them to agree to the
new price. If they don’t agree or take no action, their subscription expires
at the end of their current billing cycle. For more information, see Managing
Prices and Manage pricing for auto-renewable subscriptions.

In Mac apps built with Mac Catalyst, the system doesn’t show the price consent
sheet regardless of the return value.

## See Also

### Related Documentation

`func showPriceConsentIfNeeded()`

Asks the system to display the price consent sheet if the user hasn’t yet
responded to a subscription price increase.

