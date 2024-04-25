Global Variable

# SKStoreProductParameterAdNetworkSourceIdentifier

A four-digit integer that ad networks define to represent the ad campaign.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  tvOS 16.1+

    
    
    let SKStoreProductParameterAdNetworkSourceIdentifier: String

## Discussion

This key is available for ad impressions that use SKAdNetwork 4 and later. The
`SKStoreProductParameterAdNetworkSourceIdentifier`, also known as the
_hierarchical source identifier_ , replaces and extends the campaign
identifier value, `SKStoreProductParameterAdNetworkCampaignIdentifier`.

Ad networks and developers define the meaning of the hierarchical source
identifier. This string represents an integer of up to four digits. You can
encode information about your advertisement in each set of digits; you may
receive two, three, or all four digits of the `sourceIdentifier` in the first
winning postback, depending on the ad impression’s postback data tier. For
more information about the value you may get in the postback, see Receiving
postbacks in multiple conversion windows.

Global Variable

# SKStoreProductParameterAdNetworkVersion

The key that represents the version of the ad network API.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+

    
    
    let SKStoreProductParameterAdNetworkVersion: String

## Discussion

The value for this key is an `NSString`. Set this key to version number
"`4.0`", "`3.0`", "`2.2"`, `“2.1"`, or `"2.0"`. Use the highest available
version whenever possible. For version availability, see SKAdNetwork release
notes.

Ad networks use this key and the other Ad network install-validation keys when
signing ads. For more information, see Generating the signature to validate
StoreKit-rendered ads.

## See Also

### Required keys for SKAdNetwork 2 and later

`let SKStoreProductParameterAdNetworkSourceAppStoreIdentifier: String`

The key that represents the App Store ID of the app that displays the ad.

Global Variable

# SKStoreProductParameterAdNetworkSourceAppStoreIdentifier

The key that represents the App Store ID of the app that displays the ad.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+

    
    
    let SKStoreProductParameterAdNetworkSourceAppStoreIdentifier: String

## Discussion

The value for this key is an `NSNumber`. Provide the App Store item identifier
of the app that’s displaying the ad.

During testing, if you’re using a development-signed build to display the ads
and not an app from App Store, use `0` as the item identifier.

## See Also

### Required keys for SKAdNetwork 2 and later

`let SKStoreProductParameterAdNetworkVersion: String`

The key that represents the version of the ad network API.

Global Variable

# SKStoreProductParameterAdNetworkIdentifier

The key that represents the advertising network’s unique identifier.

iOS 11.3+  iPadOS 11.3+  Mac Catalyst 13.1+  tvOS 11.3+

    
    
    let SKStoreProductParameterAdNetworkIdentifier: String

## Discussion

The value for this key is an `NSString`.

Ad networks obtain an ad network identifier during registration. Ad networks
are responsible for sharing their ad network IDs with participating app
developers. Apps that display ads and need to initiate the app install
validation process must include the ad network ID in their `Info.plist`. For
more information see Registering an ad network and `Configuring Apps`.

## See Also

### Required keys

`let SKStoreProductParameterAdNetworkCampaignIdentifier: String`

The key that represents the advertising network’s campaign.

`let SKStoreProductParameterAdNetworkTimestamp: String`

The key that represents the UNIX time, in milliseconds, of the ad impression.

`let SKStoreProductParameterAdNetworkNonce: String`

The key that represents a random value to use for added security.

`let SKStoreProductParameterAdNetworkAttributionSignature: String`

The key that represents the advertising network’s cryptographic signature to
use for install validation.

Global Variable

# SKStoreProductParameterAdNetworkCampaignIdentifier

The key that represents the advertising network’s campaign.

iOS 11.3+  iPadOS 11.3+  Mac Catalyst 13.1+  tvOS 11.3+

    
    
    let SKStoreProductParameterAdNetworkCampaignIdentifier: String

## Discussion

The value for this key is an `NSNumber`. Ad networks determine their own
campaign identifiers, which must be an integer `>=1` and `<=100`.

Use `SKStoreProductParameterAdNetworkSourceIdentifier` instead of this value
to generate version 4 and later signatures.

## See Also

### Required keys

`let SKStoreProductParameterAdNetworkIdentifier: String`

The key that represents the advertising network’s unique identifier.

`let SKStoreProductParameterAdNetworkTimestamp: String`

The key that represents the UNIX time, in milliseconds, of the ad impression.

`let SKStoreProductParameterAdNetworkNonce: String`

The key that represents a random value to use for added security.

`let SKStoreProductParameterAdNetworkAttributionSignature: String`

The key that represents the advertising network’s cryptographic signature to
use for install validation.

Global Variable

# SKStoreProductParameterAdNetworkTimestamp

The key that represents the UNIX time, in milliseconds, of the ad impression.

iOS 11.3+  iPadOS 11.3+  Mac Catalyst 13.1+  tvOS 11.3+

    
    
    let SKStoreProductParameterAdNetworkTimestamp: String

## Discussion

The value for this key is an `NSNumber`. Ad networks generate the timestamp,
represented as UNIX time in milliseconds, at the time you’re preparing to
serve the ad.

## See Also

### Required keys

`let SKStoreProductParameterAdNetworkIdentifier: String`

The key that represents the advertising network’s unique identifier.

`let SKStoreProductParameterAdNetworkCampaignIdentifier: String`

The key that represents the advertising network’s campaign.

`let SKStoreProductParameterAdNetworkNonce: String`

The key that represents a random value to use for added security.

`let SKStoreProductParameterAdNetworkAttributionSignature: String`

The key that represents the advertising network’s cryptographic signature to
use for install validation.

Global Variable

# SKStoreProductParameterAdNetworkNonce

The key that represents a random value to use for added security.

iOS 11.3+  iPadOS 11.3+  Mac Catalyst 13.1+  tvOS 11.3+

    
    
    let SKStoreProductParameterAdNetworkNonce: String

## Discussion

The value for this key is an `NSUUID`. Ad networks generate a random value for
this key at the time of the ad impression.

Important

When you generate the signature value
(`SKStoreProductParameterAdNetworkAttributionSignature`), you must sign the
nonce as an all-lowercase UUID string representation.

## See Also

### Required keys

`let SKStoreProductParameterAdNetworkIdentifier: String`

The key that represents the advertising network’s unique identifier.

`let SKStoreProductParameterAdNetworkCampaignIdentifier: String`

The key that represents the advertising network’s campaign.

`let SKStoreProductParameterAdNetworkTimestamp: String`

The key that represents the UNIX time, in milliseconds, of the ad impression.

`let SKStoreProductParameterAdNetworkAttributionSignature: String`

The key that represents the advertising network’s cryptographic signature to
use for install validation.

Global Variable

# SKStoreProductParameterAdNetworkAttributionSignature

The key that represents the advertising network’s cryptographic signature to
use for install validation.

iOS 11.3+  iPadOS 11.3+  Mac Catalyst 13.1+  tvOS 11.3+

    
    
    let SKStoreProductParameterAdNetworkAttributionSignature: String

## Discussion

The value for this key is an `NSString`. The ad network creates the
cryptographic signature, used to sign ads. For instructions on generating this
value, see Generating the signature to validate StoreKit-rendered ads.

## See Also

### Required keys

`let SKStoreProductParameterAdNetworkIdentifier: String`

The key that represents the advertising network’s unique identifier.

`let SKStoreProductParameterAdNetworkCampaignIdentifier: String`

The key that represents the advertising network’s campaign.

`let SKStoreProductParameterAdNetworkTimestamp: String`

The key that represents the UNIX time, in milliseconds, of the ad impression.

`let SKStoreProductParameterAdNetworkNonce: String`

The key that represents a random value to use for added security.

