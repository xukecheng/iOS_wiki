Instance Method

# requestDidFinish(_:)

Tells the delegate that the request has completed.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func requestDidFinish(_ request: SKRequest)

##  Parameters

`request`

    

The request that completed.

## Discussion

This method is called after all processing of the request has been completed.
Typically, subclasses of `SKRequest` require the delegate to implement
additional methods to receive the response. When this method is called, your
delegate receives no further communication from the request and can release
it.

## See Also

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# request(_:didFailWithError:)

Tells the delegate that the request failed to execute.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func request(
        _ request: SKRequest,
        didFailWithError error: any Error
    )

##  Parameters

`request`

    

The request that failed.

`error`

    

The error that caused the request to fail.

## Discussion

When the request fails, your application should release the request. The
`requestDidFinish(_:)` method is not called after this method is called.

Instance Method

# requestDidFinish(_:)

Tells the delegate that the request has completed.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func requestDidFinish(_ request: SKRequest)

##  Parameters

`request`

    

The request that completed.

## Discussion

This method is called after all processing of the request has been completed.
Typically, subclasses of `SKRequest` require the delegate to implement
additional methods to receive the response. When this method is called, your
delegate receives no further communication from the request and can release
it.

## See Also

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# request(_:didFailWithError:)

Tells the delegate that the request failed to execute.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func request(
        _ request: SKRequest,
        didFailWithError error: any Error
    )

##  Parameters

`request`

    

The request that failed.

`error`

    

The error that caused the request to fail.

## Discussion

When the request fails, your application should release the request. The
`requestDidFinish(_:)` method is not called after this method is called.

