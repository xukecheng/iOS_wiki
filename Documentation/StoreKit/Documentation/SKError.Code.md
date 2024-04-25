Enumeration Case

# SKError.Code.unknown

Error code indicating that an unknown or unexpected error occurred.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case unknown = 0

## Discussion

For more information about the underlying cause of the error, see the
`localizedDescription` property of the error object.

Retrying may resolve this error in some instances.

Enumeration Case

# SKError.Code.clientInvalid

Error code indicating that the client is not allowed to perform the attempted
action.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case clientInvalid = 1

Enumeration Case

# SKError.Code.paymentCancelled

Error code indicating that the user canceled a payment request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentCancelled = 2

Enumeration Case

# SKError.Code.paymentInvalid

Error code indicating that one of the payment parameters wasn’t recognized by
the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentInvalid = 3

Enumeration Case

# SKError.Code.paymentNotAllowed

Error code indicating that the user is not allowed to authorize payments.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentNotAllowed = 4

Enumeration Case

# SKError.Code.storeProductNotAvailable

Error code indicating that the requested product is not available in the
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case storeProductNotAvailable = 5

## Discussion

See `SKStorefront` for more information.

Enumeration Case

# SKError.Code.cloudServicePermissionDenied

Error code indicating that the user has not allowed access to Cloud service
information.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServicePermissionDenied = 6

Enumeration Case

# SKError.Code.cloudServiceNetworkConnectionFailed

Error code indicating that the device could not connect to the network.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServiceNetworkConnectionFailed = 7

Enumeration Case

# SKError.Code.cloudServiceRevoked

Error code indicating that the user has revoked permission to use this cloud
service.

iOS 10.3+  iPadOS 10.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 10.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServiceRevoked = 8

Enumeration Case

# SKError.Code.privacyAcknowledgementRequired

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case privacyAcknowledgementRequired = 9

Enumeration Case

# SKError.Code.unauthorizedRequestData

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case unauthorizedRequestData = 10

## Discussion

To use `requestData`, an app must have a required entitlement.

Enumeration Case

# SKError.Code.invalidOfferIdentifier

Error code indicating that the offer identifier is invalid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidOfferIdentifier = 11

## Discussion

The offer `identifier` is not valid. For example, you have not set up an offer
with that identifier in the App Store, or you have revoked the offer.

Enumeration Case

# SKError.Code.invalidOfferPrice

Error code indicating that the price you specified in App Store Connect is no
longer valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidOfferPrice = 14

## Discussion

An offer price can become invalid if you change the price of the base
subscription such that it is lower than the offer price. Offers must always
represent a discounted price.

Enumeration Case

# SKError.Code.invalidSignature

Error code indicating that the signature in a payment discount isn’t valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidSignature = 12

## Discussion

The `signature` is not valid.

Enumeration Case

# SKError.Code.missingOfferParams

Error code indicating that parameters are missing in a payment discount.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case missingOfferParams = 13

## Discussion

This error appears if all parameters of `SKPaymentDiscount` are not present.

Enumeration Case

# SKError.Code.ineligibleForOffer

An error code that indicates the user is ineligible for the subscription
offer.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case ineligibleForOffer = 18

Enumeration Case

# SKError.Code.overlayCancelled

An error code that indicates the cancellation of an overlay.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case overlayCancelled = 15

Enumeration Case

# SKError.Code.overlayInvalidConfiguration

An error code that indicates the overlay’s configuration is invalid.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    case overlayInvalidConfiguration = 16

Enumeration Case

# SKError.Code.overlayPresentedInBackgroundScene

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+  visionOS 1.0+

    
    
    case overlayPresentedInBackgroundScene = 20

Enumeration Case

# SKError.Code.overlayTimeout

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    case overlayTimeout = 17

Enumeration Case

# SKError.Code.unsupportedPlatform

An error code that indicates the current platform doesn’t support overlays.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    case unsupportedPlatform = 19

Enumeration Case

# SKError.Code.unknown

Error code indicating that an unknown or unexpected error occurred.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case unknown = 0

## Discussion

For more information about the underlying cause of the error, see the
`localizedDescription` property of the error object.

Retrying may resolve this error in some instances.

Enumeration Case

# SKError.Code.clientInvalid

Error code indicating that the client is not allowed to perform the attempted
action.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case clientInvalid = 1

Enumeration Case

# SKError.Code.paymentCancelled

Error code indicating that the user canceled a payment request.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentCancelled = 2

Enumeration Case

# SKError.Code.paymentInvalid

Error code indicating that one of the payment parameters wasn’t recognized by
the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentInvalid = 3

Enumeration Case

# SKError.Code.paymentNotAllowed

Error code indicating that the user is not allowed to authorize payments.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case paymentNotAllowed = 4

Enumeration Case

# SKError.Code.storeProductNotAvailable

Error code indicating that the requested product is not available in the
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case storeProductNotAvailable = 5

## Discussion

See `SKStorefront` for more information.

Enumeration Case

# SKError.Code.cloudServicePermissionDenied

Error code indicating that the user has not allowed access to Cloud service
information.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServicePermissionDenied = 6

Enumeration Case

# SKError.Code.cloudServiceNetworkConnectionFailed

Error code indicating that the device could not connect to the network.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 9.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServiceNetworkConnectionFailed = 7

Enumeration Case

# SKError.Code.cloudServiceRevoked

Error code indicating that the user has revoked permission to use this cloud
service.

iOS 10.3+  iPadOS 10.3+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 10.3+  watchOS
6.2+  visionOS 1.0+

    
    
    case cloudServiceRevoked = 8

Enumeration Case

# SKError.Code.privacyAcknowledgementRequired

Error code indicating that the user has not yet acknowledged Apple’s privacy
policy for Apple Music.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case privacyAcknowledgementRequired = 9

Enumeration Case

# SKError.Code.unauthorizedRequestData

Error code indicating that the app is attempting to use a property for which
it does not have the required entitlement.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case unauthorizedRequestData = 10

## Discussion

To use `requestData`, an app must have a required entitlement.

Enumeration Case

# SKError.Code.invalidOfferIdentifier

Error code indicating that the offer identifier is invalid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidOfferIdentifier = 11

## Discussion

The offer `identifier` is not valid. For example, you have not set up an offer
with that identifier in the App Store, or you have revoked the offer.

Enumeration Case

# SKError.Code.invalidOfferPrice

Error code indicating that the price you specified in App Store Connect is no
longer valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidOfferPrice = 14

## Discussion

An offer price can become invalid if you change the price of the base
subscription such that it is lower than the offer price. Offers must always
represent a discounted price.

Enumeration Case

# SKError.Code.invalidSignature

Error code indicating that the signature in a payment discount isn’t valid.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case invalidSignature = 12

## Discussion

The `signature` is not valid.

Enumeration Case

# SKError.Code.missingOfferParams

Error code indicating that parameters are missing in a payment discount.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case missingOfferParams = 13

## Discussion

This error appears if all parameters of `SKPaymentDiscount` are not present.

Enumeration Case

# SKError.Code.ineligibleForOffer

An error code that indicates the user is ineligible for the subscription
offer.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case ineligibleForOffer = 18

Enumeration Case

# SKError.Code.overlayCancelled

An error code that indicates the cancellation of an overlay.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    case overlayCancelled = 15

Enumeration Case

# SKError.Code.overlayInvalidConfiguration

An error code that indicates the overlay’s configuration is invalid.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    case overlayInvalidConfiguration = 16

Enumeration Case

# SKError.Code.overlayPresentedInBackgroundScene

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+  visionOS 1.0+

    
    
    case overlayPresentedInBackgroundScene = 20

Enumeration Case

# SKError.Code.overlayTimeout

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    case overlayTimeout = 17

Enumeration Case

# SKError.Code.unsupportedPlatform

An error code that indicates the current platform doesn’t support overlays.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    case unsupportedPlatform = 19

