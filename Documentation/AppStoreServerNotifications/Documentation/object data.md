Type

# appAppleId

The unique identifier of an app in the App Store.

App Store Server Notifications 2.0+

    
    
    int64 appAppleId

## See Also

### App metadata and environment

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# bundleVersion

The version of the build that identifies an iteration of the bundle.

App Store Server Notifications 2.0+

    
    
    string bundleVersion

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# environment

The server environment, either sandbox or production.

App Store Server Notifications 2.0+

    
    
    string environment

##  Possible Values

`Sandbox`

    

Indicates that the notification applies to testing in the sandbox environment.

`Production`

    

Indicates that the notification applies to the production environment.

## Discussion

You receive notifications in the sandbox environment when you opt in to
receive notifications in the sandbox environment and test your app in the
sandbox environment. TestFlight also uses the sandbox environment to send
notifications. To opt in to receive notifications, see Enter a URL for App
Store Server Notifications. For more information about testing, see Testing at
all stages of development with Xcode and the sandbox, and Beta Testing Made
Simple with TestFlight.

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# status

The status of an auto-renewable subscription at the time the App Store signs
the notification.

App Store Server Notifications 2.8+

    
    
    int32 status

##  Possible Values

`1`

    

The auto-renewable subscription is active.

`2`

    

The auto-renewable subscription is expired.

`3`

    

The auto-renewable subscription is in a billing retry period.

`4`

    

The auto-renewable subscription is in a Billing Grace Period.

`5`

    

The auto-renewable subscription is revoked.

## Discussion

This status value is current as of the `signedDate` in the decoded payload,
`responseBodyV2DecodedPayload`.

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

Type

# JWSRenewalInfo

Subscription renewal information signed by the App Store, in JSON Web
Signature (JWS) format.

App Store Server Notifications 2.0+

    
    
    string JWSRenewalInfo

## Discussion

The `JWSRenewalInfo` type is a string of three Base64 URL-encoded components,
separated by a period. The string contains the JWS representation of the
subscription renewal information, signed by the App Store according to the
JSON Web Signature (JWS) IETF RFC 7515 specification.

The three components in the string are a header, a payload, and a signature,
in that order.

To read the subscription renewal information, Base64 URL-decode the payload.
Use a `JWSRenewalInfoDecodedPayload` object to read the payload information.

To read the header, Base64 URL-decode it and use a `JWSDecodedHeader` object
to access the information. Use the information in the header to verify the
signature.

## See Also

### JWS transaction and renewal info

`object JWSRenewalInfoDecodedPayload`

A decoded payload containing subscription renewal information for an auto-
renewable subscription.

`type JWSTransaction`

Transaction information signed by the App Store, in JSON Web Signature (JWS)
format.

`object JWSTransactionDecodedPayload`

A decoded payload that contains transaction information.

Type

# JWSTransaction

Transaction information signed by the App Store, in JSON Web Signature (JWS)
format.

App Store Server Notifications 2.0+

    
    
    string JWSTransaction

## Discussion

The `JWSTransaction` type is a string of three Base64 URL-encoded components,
separated by a period. The string contains the JWS representation of the
transaction information, signed by the App Store according to the JSON Web
Signature (JWS) IETF RFC 7515 specification.

The three components of the string are a header, a payload, and a signature,
in that order.

To read the transaction information, Base64 URL-decode the payload. Use a
`JWSTransactionDecodedPayload` object to read the payload information.

To read the header, decode it and use a `JWSDecodedHeader` object to access
the information. Use the information in the header to verify the signature.

## See Also

### JWS transaction and renewal info

`type JWSRenewalInfo`

Subscription renewal information signed by the App Store, in JSON Web
Signature (JWS) format.

`object JWSRenewalInfoDecodedPayload`

A decoded payload containing subscription renewal information for an auto-
renewable subscription.

`object JWSTransactionDecodedPayload`

A decoded payload that contains transaction information.

Type

# consumptionRequestReason

The customer-provided reason for a refund request.

App Store Server Notifications 2.11+

    
    
    string consumptionRequestReason

##  Possible Values

`UNINTENDED_PURCHASE`

    

The customer didn't intend to make the in-app purchase.

`FULFILLMENT_ISSUE`

    

The customer had issues with receiving or using the in-app purchase.

`UNSATISFIED_WITH_PURCHASE`

    

The customer wasn't satisfied with the in-app purchase.

`LEGAL`

    

The customer requested a refund based on a legal reason.

`OTHER`

    

The customer requested a refund for other reasons.

## Discussion

When a customer initiates a refund request for a consumable in-app purchase or
auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST`
`notificationType` to your server. The notification includes the
`consumptionRequestReason` in the `data` object.

