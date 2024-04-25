Enumeration Case

# ProductIconPhase.loading

The promotional image is in the process of loading.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Getting the promotional image's load phases

`case success(Image)`

The promotional image successfully loaded.

`case unavailable`

The promotional image isn’t available for download.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.success(_:)

The promotional image successfully loaded.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(Image)

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case unavailable`

The promotional image isn’t available for download.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.unavailable

The promotional image isn’t available for download.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case unavailable

## Discussion

You set up promotional images for in-app purchases in App Store Connect.

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case success(Image)`

The promotional image successfully loaded.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.failure(_:)

The promotional image failed to load, with an error.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

##  Parameters

`Error`

    

The reason that the promotional image failed to load.

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case success(Image)`

The promotional image successfully loaded.

`case unavailable`

The promotional image isn’t available for download.

Instance Property

# promotionalIcon

The promotional image, if the loading task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var promotionalIcon: Image? { get }

## Discussion

This value is `nil` while the image is loading, or if the system can’t access
the promotional image for any reason. Use this value as a convenience to
access the image in code that doesn’t depend on the reason an image may not be
accessible.

For information about setting up promotional images, see Promote in-app
purchases.

Instance Property

# error

The error value that indicates the reason a promotional image failed to load.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var error: (any Error)? { get }

## Discussion

The `error` value is `nil` while the icon is loading, if the icon successfully
loads, or if you haven’t set up a promotional image for the in-app purchase in
App Store Connect. Use this value as a convenience to access the error value
in code that assumes you’ve set up a promotional image.

Enumeration Case

# ProductIconPhase.loading

The promotional image is in the process of loading.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case loading

## See Also

### Getting the promotional image's load phases

`case success(Image)`

The promotional image successfully loaded.

`case unavailable`

The promotional image isn’t available for download.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.success(_:)

The promotional image successfully loaded.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case success(Image)

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case unavailable`

The promotional image isn’t available for download.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.unavailable

The promotional image isn’t available for download.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case unavailable

## Discussion

You set up promotional images for in-app purchases in App Store Connect.

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case success(Image)`

The promotional image successfully loaded.

`case failure(any Error)`

The promotional image failed to load, with an error.

Enumeration Case

# ProductIconPhase.failure(_:)

The promotional image failed to load, with an error.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    case failure(any Error)

##  Parameters

`Error`

    

The reason that the promotional image failed to load.

## See Also

### Getting the promotional image's load phases

`case loading`

The promotional image is in the process of loading.

`case success(Image)`

The promotional image successfully loaded.

`case unavailable`

The promotional image isn’t available for download.

Instance Property

# promotionalIcon

The promotional image, if the loading task is successful.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var promotionalIcon: Image? { get }

## Discussion

This value is `nil` while the image is loading, or if the system can’t access
the promotional image for any reason. Use this value as a convenience to
access the image in code that doesn’t depend on the reason an image may not be
accessible.

For information about setting up promotional images, see Promote in-app
purchases.

Instance Property

# error

The error value that indicates the reason a promotional image failed to load.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var error: (any Error)? { get }

## Discussion

The `error` value is `nil` while the icon is loading, if the icon successfully
loads, or if you haven’t set up a promotional image for the in-app purchase in
App Store Connect. Use this value as a convenience to access the error value
in code that assumes you’ve set up a promotional image.

