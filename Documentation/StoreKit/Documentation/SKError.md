Instance Property

# errorCode

The error code that this instance represents.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 9.0+

    
    
    var errorCode: Int { get }

## See Also

### Error properties

`var errorUserInfo: [String : Any]`

An info dictionary for providing additional details about an error.

`var localizedDescription: String`

A string containing the localized description of the error.

`var code: Code`

`var userInfo: [String : Any]`

Instance Property

# errorUserInfo

An info dictionary for providing additional details about an error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 9.0+

    
    
    var errorUserInfo: [String : Any] { get }

## See Also

### Error properties

`var errorCode: Int`

The error code that this instance represents.

`var localizedDescription: String`

A string containing the localized description of the error.

`var code: Code`

`var userInfo: [String : Any]`

Instance Property

# localizedDescription

A string containing the localized description of the error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 9.0+

    
    
    var localizedDescription: String { get }

## See Also

### Error properties

`var errorCode: Int`

The error code that this instance represents.

`var errorUserInfo: [String : Any]`

An info dictionary for providing additional details about an error.

`var code: Code`

`var userInfo: [String : Any]`

Instance Property

# code

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.5+

    
    
    var code: Code { get }

## See Also

### Error properties

`var errorCode: Int`

The error code that this instance represents.

`var errorUserInfo: [String : Any]`

An info dictionary for providing additional details about an error.

`var localizedDescription: String`

A string containing the localized description of the error.

`var userInfo: [String : Any]`

Instance Property

# userInfo

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.5+

    
    
    var userInfo: [String : Any] { get }

## See Also

### Error properties

`var errorCode: Int`

The error code that this instance represents.

`var errorUserInfo: [String : Any]`

An info dictionary for providing additional details about an error.

`var localizedDescription: String`

A string containing the localized description of the error.

`var code: Code`

Type Property

# unknown

Error code indicating that an unknown or unexpected error occurred.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 8.0+

    
    
    static var unknown: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# clientInvalid

Error code indicating that the client is not allowed to perform the attempted
action.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 8.0+

    
    
    static var clientInvalid: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# paymentCancelled

Error code indicating that the user canceled a payment request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 8.0+

    
    
    static var paymentCancelled: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# paymentInvalid

Error code indicating that one of the payment parameters was not recognized by
the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 8.0+

    
    
    static var paymentInvalid: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# paymentNotAllowed

Error code indicating that the user is not allowed to authorize payments.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 8.0+

    
    
    static var paymentNotAllowed: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# storeProductNotAvailable

Error code indicating that the requested product is not available in the
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 9.0+

    
    
    static var storeProductNotAvailable: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# cloudServicePermissionDenied

Error code indicating that the user has not allowed access to Cloud service
information.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+  Xcode 7.3+

    
    
    static var cloudServicePermissionDenied: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# cloudServiceNetworkConnectionFailed

Error code indicating that the device could not connect to the network.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+  Xcode 7.3+

    
    
    static var cloudServiceNetworkConnectionFailed: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# cloudServiceRevoked

Error code indicating that the user has revoked permission to use this cloud
service.

iOS 10.3+  iPadOS 10.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 10.3+  watchOS
6.2+  visionOS 1.0+  Xcode 8.3+

    
    
    static var cloudServiceRevoked: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# privacyAcknowledgementRequired

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var privacyAcknowledgementRequired: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# unauthorizedRequestData

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var unauthorizedRequestData: SKError.Code { get }

## Discussion

To use `requestData`, an app must have a required entitlement.

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# invalidOfferIdentifier

Error code indicating that the offer identifier cannot be found or is not
active.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var invalidOfferIdentifier: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# invalidOfferPrice

Error code indicating that the price you specified in App Store Connect is no
longer valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var invalidOfferPrice: SKError.Code { get }

## Discussion

An offer price can become invalid if you change the price of the base
subscription such that it is lower than the offer price. Offers must always
represent a discounted price.

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# invalidSignature

Error code indicating that the signature in a payment discount is not valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var invalidSignature: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# missingOfferParams

Error code indicating that parameters are missing in a payment discount.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var missingOfferParams: SKError.Code { get }

## Discussion

This error appears if all parameters of `SKPaymentDiscount` are not present.

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# ineligibleForOffer

An error code that indicates the user is ineligible for the subscription
offer.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    static var ineligibleForOffer: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# overlayCancelled

An error code that indicates the cancellation of an overlay.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 14.0+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+  Xcode 10.2+

    
    
    static var overlayCancelled: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# overlayInvalidConfiguration

An error code that indicates the overlay’s configuration is invalid.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.2+  visionOS 1.0+  Xcode 12.0+

    
    
    static var overlayInvalidConfiguration: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# overlayPresentedInBackgroundScene

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+  visionOS 1.0+  Xcode 12.5+

    
    
    static var overlayPresentedInBackgroundScene: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# overlayTimeout

An error code that indicates the timing out of an overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.2+  visionOS 1.0+  Xcode 12.0+

    
    
    static var overlayTimeout: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var unsupportedPlatform: SKError.Code`

An error code that indicates the current platform doesn’t support overlays.

Type Property

# unsupportedPlatform

An error code that indicates the current platform doesn’t support overlays.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.2+  watchOS 7.0+
visionOS 1.0+  Xcode 12.0+

    
    
    static var unsupportedPlatform: SKError.Code { get }

## See Also

### Error codes

`enum SKError.Code`

Error codes for StoreKit errors.

`static var unknown: SKError.Code`

Error code indicating that an unknown or unexpected error occurred.

`static var clientInvalid: SKError.Code`

Error code indicating that the client is not allowed to perform the attempted
action.

`static var paymentCancelled: SKError.Code`

Error code indicating that the user canceled a payment request.

`static var paymentInvalid: SKError.Code`

Error code indicating that one of the payment parameters was not recognized by
the App Store.

`static var paymentNotAllowed: SKError.Code`

Error code indicating that the user is not allowed to authorize payments.

`static var storeProductNotAvailable: SKError.Code`

Error code indicating that the requested product is not available in the
store.

`static var cloudServicePermissionDenied: SKError.Code`

Error code indicating that the user has not allowed access to Cloud service
information.

`static var cloudServiceNetworkConnectionFailed: SKError.Code`

Error code indicating that the device could not connect to the network.

`static var cloudServiceRevoked: SKError.Code`

Error code indicating that the user has revoked permission to use this cloud
service.

`static var privacyAcknowledgementRequired: SKError.Code`

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

`static var unauthorizedRequestData: SKError.Code`

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

`static var invalidOfferIdentifier: SKError.Code`

Error code indicating that the offer identifier cannot be found or is not
active.

`static var invalidOfferPrice: SKError.Code`

Error code indicating that the price you specified in App Store Connect is no
longer valid.

`static var invalidSignature: SKError.Code`

Error code indicating that the signature in a payment discount is not valid.

`static var missingOfferParams: SKError.Code`

Error code indicating that parameters are missing in a payment discount.

`static var ineligibleForOffer: SKError.Code`

An error code that indicates the user is ineligible for the subscription
offer.

`static var overlayCancelled: SKError.Code`

An error code that indicates the cancellation of an overlay.

`static var overlayInvalidConfiguration: SKError.Code`

An error code that indicates the overlay’s configuration is invalid.

`static var overlayPresentedInBackgroundScene: SKError.Code`

`static var overlayTimeout: SKError.Code`

An error code that indicates the timing out of an overlay.

Type Property

# errorDomain

Gets the error domain that identifies an error as a StoreKit error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 9.0+

    
    
    static var errorDomain: String { get }

## See Also

### Error domain

`let SKErrorDomain: String`

The error domain name for StoreKit errors.

Global Variable

# SKErrorDomain

The error domain name for StoreKit errors.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKErrorDomain: String

## See Also

### Errors

Handling errors

Determine the underlying cause of errors that result from StoreKit requests.

`enum SKError.Code`

Error codes for StoreKit errors.

`struct SKError`

StoreKit error descriptions, codes, and domains.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+  Xcode 9.3+

    
    
    static func != (lhs: SKError, rhs: SKError) -> Bool

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

### Error code comparisons and hash

`static func == (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 7.1+

    
    
    static func == (lhs: SKError, rhs: SKError) -> Bool

## See Also

### Error code comparisons and hash

`static func != (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.5+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Error code comparisons and hash

`static func != (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.5+

    
    
    var hashValue: Int { get }

## See Also

### Error code comparisons and hash

`static func != (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SKError, SKError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Initializer

# init(_:userInfo:)

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 14.5+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.5+

    
    
    init(
        _ code: Code,
        userInfo: [String : Any] = [:]
    )

