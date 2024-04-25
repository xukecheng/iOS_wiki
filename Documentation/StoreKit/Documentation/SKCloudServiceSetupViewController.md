Instance Property

# delegate

The cloud service view controller's delegate.

iOS 10.1+  iPadOS 10.1+  Mac Catalyst 13.1+

    
    
    weak var delegate: (any SKCloudServiceSetupViewControllerDelegate)? { get set }

## Discussion

You can identify a delegate to get informed when the cloud service setup view
controller is dismissed.

## See Also

### Setting a Delegate

`protocol SKCloudServiceSetupViewControllerDelegate`

A protocol that defines the methods a cloud service setup view controller can
use to get the status of the view, including when it is dismissed.

Article

# Offering Apple Music Subscription in Your App

Allow eligible users to subscribe to Apple Music library.

## Overview

With an Apple Music membership, users can play songs from the entire Apple
Music catalog or access their iCloud music library across all their devices.
You can offer users the option to sign up for an Apple Music subscription
directly from your app by following these steps:

  1. Request Apple Music Library access from the user.

  2. Determine if the user is eligible for an Apple Music subscription. 

  3. Present the sign-up subscription offer if the user is eligible.

### Request Apple Music Library Access

The user must grant permission before your app can access Apple Music library.
See Requesting Access to Apple Music Library for details. Use
`authorizationStatus()` to determine your app’s authorization status. If the
authorization status is `SKCloudServiceAuthorizationStatus.authorized`, your
app can check if the user is eligible for an Apple Music subscription offer.

Important

When the Music app is absent on the user’s device,
`load(options:completionHandler:)` fails to load.

### Determine if the User is Eligible for an Apple Music Subscription

After getting Apple Music access from the user, call
`requestCapabilities(completionHandler:)` on an instance of
`SKCloudServiceController` to query the user’s capabilities. Then, inspect the
`capabilities` parameter of this method to determine eligibility. See
Determining a User’s Apple Music Capabilities for details. A user has an
active subscription to Apple Music when `capabilities` contains
`musicCatalogPlayback`. A user is eligible for the offer when `capabilities`
doesn’t include `musicCatalogPlayback` but contains
`musicCatalogSubscriptionEligible`.

### Present the Offer to Subscribe for Apple Music

For users who are eligible for an Apple Music subscription, use the following
steps to allow users to sign up for it.

First, create a dictionary with an `action` key to `subscribe`:

If you have an iTunes Store affiliate account, you can add the
`affiliateToken` key to the dictionary to earn commision if the user
subscribes:

By default, the setup view is configured with the `messageIdentifier` key set
to `join`. Add `messageIdentifier` to the dictionary and set it to `addMusic`,
`connect`, or `playMusic` if you wish to change the default message that your
app shows to the user:

Next, create an `SKCloudServiceSetupViewController` object and set the view
controller class as its delegate:

Then, pass the dictionary to the `load(options:completionHandler:)` method of
the `SKCloudServiceSetupViewController` object. Finally, present the
`SKCloudServiceSetupViewController` object modally from your app:

## See Also

### Loading the Setup View

`func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler:
((Bool, (any Error)?) -> Void)?)`

Loads the cloud service setup view with the specified options.

`struct SKCloudServiceSetupOptionsKey`

Keys used to specify the types of setup options for a cloud service.

Instance Method

# load(options:completionHandler:)

Loads the cloud service setup view with the specified options.

iOS 10.1+  iPadOS 10.1+  Mac Catalyst 13.1+

    
    
    func load(
        options: [SKCloudServiceSetupOptionsKey : Any] = [:],
        completionHandler: ((Bool, (any Error)?) -> Void)? = nil
    )

##  Parameters

`options`

    

A key that identifies the type of setup the user needs to do. See
`SKCloudServiceSetupOptionsKey` for possible values.

`completionHandler`

    

A block that is called when the setup view has loaded. The block takes the
following parameters:

`result`

A Boolean value that indicates whether the view controller has loaded the view
and can be presented.

`error`

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

### Loading the Setup View

Offering Apple Music Subscription in Your App

Allow eligible users to subscribe to Apple Music library.

`struct SKCloudServiceSetupOptionsKey`

Keys used to specify the types of setup options for a cloud service.

