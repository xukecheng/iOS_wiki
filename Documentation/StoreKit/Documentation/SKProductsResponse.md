Instance Property

# products

A list of products, one product for each valid product identifier provided in
the original request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var products: [SKProduct] { get }

## Discussion

The array consists of a list of `SKProduct` objects.

## See Also

### Response Information

`var invalidProductIdentifiers: [String]`

An array of product identifier strings that the App Store doesn’t recognize.

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# invalidProductIdentifiers

An array of product identifier strings that the App Store doesn’t recognize.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var invalidProductIdentifiers: [String] { get }

## Discussion

The App Store may not recognize your product identifiers unless you meet
following criteria, as applicable:

  * Agree to the latest Apple Developer Program License Agreement.

  * Complete all the financial agreements as described in the Agreements, Tax, and Banking Overview. When you renew your developer membership, see if you need to make updates to your agreements. When your developer membership expires, your financial agreements expire as well.

  * Your app uses an explicit App ID.

  * Clear the in-app purchases for sale in App Store Connect. See Set availability for in-app purchase.

  * Modified in-app purchases are available to the App Store servers.

  * The product identifier specified in App Store Connect matches the identifier used by the `SKProductsRequest` object in your app. 

  * Upload the content of your product to App Store Connect. See Upload in-app purchase content to App Store Connect.

For more troubleshooting information, see Fetching product information from
the App Store.

## See Also

### Response Information

`var products: [SKProduct]`

A list of products, one product for each valid product identifier provided in
the original request.
