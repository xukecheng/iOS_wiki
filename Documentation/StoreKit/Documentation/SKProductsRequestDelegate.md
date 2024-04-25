Instance Method

# productsRequest(_:didReceive:)

Accepts the App Store response that contains the app-requested product
information.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func productsRequest(
        _ request: SKProductsRequest,
        didReceive response: SKProductsResponse
    )

**Required**

##  Parameters

`request`

    

The product request sent to the Apple App Store.

`response`

    

Detailed information about the list of products.

## See Also

### Related Documentation

In-App Purchase Programming Guide

