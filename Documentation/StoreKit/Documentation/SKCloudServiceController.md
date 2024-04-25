Article

# Requesting Access to Apple Music Library

Prompt the user to authorize access to Apple Music library.

StoreKit  Bundle Resources

## Overview

Your app must obtain permission from the user before accessing Apple Music
Library.

### Provide a Purpose String in Info.plist

Provide a purpose string or usage description that describes how your app
intends to use the user’s iCloud Music library or Apple Music catalog. Add the
`NSAppleMusicUsageDescription` key to your app’s Info.plist. Set its value to
a string that explains why your app needs access to Apple Music library. The
system displays the string to the user when prompting them for authorization.

Important

This key is required for apps that access the user’s music library. Apps crash
when the key is absent.

See Requesting access to protected resources for more details.

### Request Authorization

The user determines whether apps can play items from the Apple Music catalog
or add tracks to their iCloud Music library. They can grant or deny access
when your app requests authorization. Because the user can change your app’s
authorization status in Settings > Privacy > Media and Apple Music, be sure to
call `SKCloudServiceController`’s `authorizationStatus()` before attempting to
access their Apple Music library.

If the authorization status i`s
``SKCloudServiceAuthorizationStatus.notDetermined`, call
`SKCloudServiceController`’s `requestAuthorization(_:)` to prompt the user for
access.

The system remembers the user’s answer so that subsequent calls to
`requestAuthorization(_:)` don’t prompt them again.

## See Also

### Getting Authorization to Access the Music Library

`class func authorizationStatus() -> SKCloudServiceAuthorizationStatus`

Returns the type of authorization the user has set for accessing the music
library on the device.

`class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)`

Asks the user for permission to access the music library on the device.

`enum SKCloudServiceAuthorizationStatus`

Constants that indicate the type of authorization the user has set for
accessing the music library.

Type Method

# authorizationStatus()

Returns the type of authorization the user has set for accessing the music
library on the device.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    class func authorizationStatus() -> SKCloudServiceAuthorizationStatus

## Return Value

The type of authorization for music library access. See
`SKCloudServiceAuthorizationStatus` for a list of possible values.

## Discussion

Use the authorization status to determine in what ways you can access the
user’s music library.

## See Also

### Getting Authorization to Access the Music Library

Requesting Access to Apple Music Library

Prompt the user to authorize access to Apple Music library.

`class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)`

Asks the user for permission to access the music library on the device.

`enum SKCloudServiceAuthorizationStatus`

Constants that indicate the type of authorization the user has set for
accessing the music library.

### Related Documentation

In-App Purchase Programming Guide

Type Method

# requestAuthorization(_:)

Asks the user for permission to access the music library on the device.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    class func requestAuthorization(_ completionHandler: @escaping (SKCloudServiceAuthorizationStatus) -> Void)

##  Parameters

`handler`

    

A block that is called when authorization is granted or denied by the user.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For example:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

You can use this method to ask the user for permission to play Apple Music
tracks or to add tracks to the music library.

## See Also

### Getting Authorization to Access the Music Library

Requesting Access to Apple Music Library

Prompt the user to authorize access to Apple Music library.

`class func authorizationStatus() -> SKCloudServiceAuthorizationStatus`

Returns the type of authorization the user has set for accessing the music
library on the device.

`enum SKCloudServiceAuthorizationStatus`

Constants that indicate the type of authorization the user has set for
accessing the music library.

Article

# Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

## Overview

After you request the user’s permission to access their Apple Music library
(see Requesting Access to Apple Music Library), you confirm that authorization
and then identify Apple Music capabilities on the user’s device.

### Confirm Whether the User Authorized Access to Apple Music Library

Use `SKCloudServiceController`’s `authorizationStatus()` to check whether the
user has authorized access to Apple Music Library. If the authorization status
is `SKCloudServiceAuthorizationStatus.notDetermined`, call
`SKCloudServiceController`’s `requestAuthorization(_:)` to prompt the user for
access.

If the authorization status is `SKCloudServiceAuthorizationStatus.authorized`,
your app can proceed to determine which Apple Music capabilities
(`musicCatalogPlayback`, `musicCatalogSubscriptionEligible`, or
`addToCloudMusicLibrary`) are available on the user’s device.

### Create a Cloud Service Controller and Its Handler to Fetch Capabilities

First, create an `SKCloudServiceController` object:

Then call its `requestCapabilities(completionHandler:)` method to fetch the
current Apple Music capabilities, as described in the sections that follow.

### Check for the Capability to Play Apple Music Content

If you want your app to play Apple Music content, check whether `capabilities
`includes `musicCatalogPlayback`:

### Check for the Subscription-Eligible Capability

A user is eligible for an Apple Music subscription offer when `capabilities`
doesn’t include `musicCatalogPlayback` but contains
`musicCatalogSubscriptionEligible`. If you want your app to present the user
with an offer to subscribe to Apple Music, check `capabilities` for these
features:

You can present the offer using `SKCloudServiceSetupViewController`.

### Check for the Capability to Add Songs to the User’s iCloud Music Library

If you want your app to add tracks to the user’s iCloud music library, check
whether `capabilities `includes `addToCloudMusicLibrary`:

## See Also

### Determining Capabilities

`func requestUserToken(forDeveloperToken: String, completionHandler: (String?,
(any Error)?) -> Void)`

Returns a user token that you use to access personalized Apple Music content.

`func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the country code for the storefront associated with a user's iTunes
account.

`func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any
Error)?) -> Void)`

Gets the current capabilities associated with the music library on the device.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the device’s storefront identifier.

`func requestPersonalizationToken(forClientToken: String,
withCompletionHandler: (String?, (any Error)?) -> Void)`Deprecated

Instance Method

# requestUserToken(forDeveloperToken:completionHandler:)

Returns a user token that you use to access personalized Apple Music content.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
7.0+

    
    
    func requestUserToken(
        forDeveloperToken developerToken: String,
        completionHandler: @escaping (String?, (any Error)?) -> Void
    )

##  Parameters

`developerToken`

    

A signed and encrypted JWT token used to authenticate the developer in Apple
Music API requests.

`completionHandler`

    

A completion block that includes the following parameters:

userToken

    

A token that identifies the user.

error

    

The error that occurred, if any.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Use this method with your developer token to get a token that authenticates
the user in personalized Apple Music API requests. Note that personalized
requests return user-specific data. Errors 401 and 403 only occur when
requesting a music user token. They do not occur for any of the other Apple
Music API requests.

## See Also

### Determining Capabilities

Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

`func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the country code for the storefront associated with a user's iTunes
account.

`func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any
Error)?) -> Void)`

Gets the current capabilities associated with the music library on the device.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the device’s storefront identifier.

`func requestPersonalizationToken(forClientToken: String,
withCompletionHandler: (String?, (any Error)?) -> Void)`Deprecated

Instance Method

# requestStorefrontCountryCode(completionHandler:)

Gets the country code for the storefront associated with a user's iTunes
account.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+

    
    
    func requestStorefrontCountryCode(completionHandler: @escaping (String?, (any Error)?) -> Void)

##  Parameters

`completionHandler`

    

A block that is called when the storefront country code is returned. The block
takes the following parameters:

storefrontCountryCode

    

The country code of a specific storefront.

error

    

An error value that indicates the reason for failure. See `SKError.Code` for
possible error values.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

You need to get the appropriate storefront country code before you specify a
product as each country or region contains different products.

## See Also

### Determining Capabilities

Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

`func requestUserToken(forDeveloperToken: String, completionHandler: (String?,
(any Error)?) -> Void)`

Returns a user token that you use to access personalized Apple Music content.

`func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any
Error)?) -> Void)`

Gets the current capabilities associated with the music library on the device.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the device’s storefront identifier.

`func requestPersonalizationToken(forClientToken: String,
withCompletionHandler: (String?, (any Error)?) -> Void)`Deprecated

Instance Method

# requestCapabilities(completionHandler:)

Gets the current capabilities associated with the music library on the device.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    func requestCapabilities(completionHandler: @escaping (SKCloudServiceCapability, (any Error)?) -> Void)

##  Parameters

`completionHandler`

    

A block that is called when the device’s current capabilities are determined.
The block takes the following parameters:

capabilities

    

Flags that indicate the device’s capabilities. For possible values, see
`SKCloudServiceCapability`.

error

    

An error value that indicates the reason for failure. Possible values are
`SKError.Code.unknown`, `SKError.Code.cloudServicePermissionDenied`, and
`SKError.Code.cloudServiceNetworkConnectionFailed`.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

## See Also

### Determining Capabilities

Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

`func requestUserToken(forDeveloperToken: String, completionHandler: (String?,
(any Error)?) -> Void)`

Returns a user token that you use to access personalized Apple Music content.

`func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the country code for the storefront associated with a user's iTunes
account.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the device’s storefront identifier.

`func requestPersonalizationToken(forClientToken: String,
withCompletionHandler: (String?, (any Error)?) -> Void)`Deprecated

Instance Method

# requestStorefrontIdentifier(completionHandler:)

Gets the device’s storefront identifier.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    func requestStorefrontIdentifier(completionHandler: @escaping (String?, (any Error)?) -> Void)

##  Parameters

`completionHandler`

    

A block that is called when the storefront ID is returned. The block takes the
following parameters:

storefrontIdentifier

    

The identifier of a specific storefront.

error

    

An error value that indicates the reason for failure. Possible values are
`SKError.Code.unknown`, `SKError.Code.cloudServicePermissionDenied`, and
`SKError.Code.cloudServiceNetworkConnectionFailed`.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

You need to get the appropriate storefront before you specify a product,
because product identifiers are meaningful within the context of a store.

## See Also

### Determining Capabilities

Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

`func requestUserToken(forDeveloperToken: String, completionHandler: (String?,
(any Error)?) -> Void)`

Returns a user token that you use to access personalized Apple Music content.

`func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the country code for the storefront associated with a user's iTunes
account.

`func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any
Error)?) -> Void)`

Gets the current capabilities associated with the music library on the device.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestPersonalizationToken(forClientToken: String,
withCompletionHandler: (String?, (any Error)?) -> Void)`Deprecated

Instance Method

# requestPersonalizationToken(forClientToken:withCompletionHandler:)

iOS 10.3–11.0  Deprecated  iPadOS 10.3–11.0  Deprecated  tvOS 10.3–11.0
Deprecated

    
    
    func requestPersonalizationToken(
        forClientToken clientToken: String,
        withCompletionHandler completionHandler: @escaping (String?, (any Error)?) -> Void
    )

## See Also

### Determining Capabilities

Determining a User’s Apple Music Capabilities

Determine which Apple Music capabilities are available on a user’s device.

`func requestUserToken(forDeveloperToken: String, completionHandler: (String?,
(any Error)?) -> Void)`

Returns a user token that you use to access personalized Apple Music content.

`func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the country code for the storefront associated with a user's iTunes
account.

`func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any
Error)?) -> Void)`

Gets the current capabilities associated with the music library on the device.

`struct SKCloudServiceCapability`

Constants that specify the current capabilities of the user’s music library on
the device.

`func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?)
-> Void)`

Gets the device’s storefront identifier.

Type Property

# SKStorefrontIdentifierDidChange

A notification name for indicating a change in the storefront identifier
associated with the device.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    static let SKStorefrontIdentifierDidChange: NSNotification.Name

## See Also

### StoreKit

`static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name`

A notification name for indicating a change in the capabilities associated
with the music library on the device.

`static let SKStorefrontCountryCodeDidChange: NSNotification.Name`

A notification name for indicating a change in the storefront country or
region code associated with the device.

Type Property

# SKCloudServiceCapabilitiesDidChange

A notification name for indicating a change in the capabilities associated
with the music library on the device.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name

## See Also

### StoreKit

`static let SKStorefrontIdentifierDidChange: NSNotification.Name`

A notification name for indicating a change in the storefront identifier
associated with the device.

`static let SKStorefrontCountryCodeDidChange: NSNotification.Name`

A notification name for indicating a change in the storefront country or
region code associated with the device.

Type Property

# SKStorefrontCountryCodeDidChange

A notification name for indicating a change in the storefront country or
region code associated with the device.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
7.0+

    
    
    static let SKStorefrontCountryCodeDidChange: NSNotification.Name

## See Also

### StoreKit

`static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name`

A notification name for indicating a change in the capabilities associated
with the music library on the device.

`static let SKStorefrontIdentifierDidChange: NSNotification.Name`

A notification name for indicating a change in the storefront identifier
associated with the device.

