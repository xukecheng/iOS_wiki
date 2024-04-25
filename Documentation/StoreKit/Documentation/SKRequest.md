Instance Method

# start()

Sends the request to the Apple App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func start()

## Discussion

The results for a request are sent to the request’s delegate.

## See Also

### Controlling the Request

`func cancel()`

Cancels a previously started request.

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# cancel()

Cancels a previously started request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func cancel()

## Discussion

When you cancel a request, the delegate is not called with an error.

## See Also

### Controlling the Request

`func start()`

Sends the request to the Apple App Store.

Instance Property

# delegate

The delegate of the request object.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    weak var delegate: (any SKRequestDelegate)? { get set }

## Discussion

The delegate must adopt the `SKRequestDelegate` protocol, although most
subclasses of `SKRequest` provide a more specific protocol to implement.

## See Also

### Accessing the Delegate

`protocol SKRequestDelegate`

Common methods that are implemented by delegates for any subclass of the
`SKRequest` abstract class.

Instance Method

# start()

Sends the request to the Apple App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func start()

## Discussion

The results for a request are sent to the request’s delegate.

## See Also

### Controlling the Request

`func cancel()`

Cancels a previously started request.

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# cancel()

Cancels a previously started request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func cancel()

## Discussion

When you cancel a request, the delegate is not called with an error.

## See Also

### Controlling the Request

`func start()`

Sends the request to the Apple App Store.

Instance Property

# delegate

The delegate of the request object.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    weak var delegate: (any SKRequestDelegate)? { get set }

## Discussion

The delegate must adopt the `SKRequestDelegate` protocol, although most
subclasses of `SKRequest` provide a more specific protocol to implement.

## See Also

### Accessing the Delegate

`protocol SKRequestDelegate`

Common methods that are implemented by delegates for any subclass of the
`SKRequest` abstract class.

