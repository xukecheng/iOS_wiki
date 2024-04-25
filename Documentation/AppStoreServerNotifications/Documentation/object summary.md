Type

# requestIdentifier

A string that contains a unique identifier for a subscription-renewal-date
extension request.

App Store Server Notifications 2.7+

    
    
    uuid requestIdentifier

## Discussion

You originally specify the `requestIdentifier` when you call Extend
Subscription Renewal Dates for All Active Subscribers in the App Store Server
API.

## See Also

### Data types

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

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

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# storefrontCountryCodes

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

App Store Server Notifications 2.7+

    
    
    [storefrontCountryCode] storefrontCountryCodes

## Discussion

If you provide a list of storefronts when you call the Extend Subscription
Renewal Dates for All Active Subscribers endpoint, the notification returns
only those storefronts. If you don’t use the `storefrontCountryCodes`, the
subscription-renewal-date extension applies to all storefronts.

For information about providing the list of storefronts, see
`MassExtendRenewalDateRequest`.

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# storefrontCountryCode

The three-letter code that represents the country or region associated with
the App Store storefront.

App Store Server Notifications 2.7+

    
    
    string storefrontCountryCode

## Discussion

This type uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# failedCount

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

App Store Server Notifications 2.7+

    
    
    int64 failedCount

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# succeededCount

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

App Store Server Notifications 2.7+

    
    
    int64 succeededCount

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

