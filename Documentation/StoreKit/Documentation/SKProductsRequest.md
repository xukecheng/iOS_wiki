Initializer

# init(productIdentifiers:)

Initializes the request with the set of product identifiers.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    init(productIdentifiers: Set<String>)

##  Parameters

`productIdentifiers`

    

The list of product identifiers for the products you wish to retrieve
descriptions of.

## Return Value

The initialized request object.

## See Also

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# delegate

The delegate that receives the response of the app's products request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    weak var delegate: (any SKProductsRequestDelegate)? { get set }

## See Also

### Setting the Delegate

`protocol SKProductsRequestDelegate`

A set of methods the delegate implements so it receives the product
information your app requests.

