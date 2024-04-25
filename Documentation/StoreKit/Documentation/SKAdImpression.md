Instance Property

# signature

The advertising network’s cryptographic signature for the ad impression.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var signature: String { get set }

## Discussion

The ad network creates a cryptographic signature that it uses to sign ads. For
instructions on generating this value, see Generating the signature to
validate view-through ads.

Initializer

#
init(sourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:)

Creates an ad impression object using the supplied values.

iOS 16.0+  iPadOS 16.0+

    
    
    init(
        sourceAppStoreItemIdentifier: NSNumber,
        advertisedAppStoreItemIdentifier: NSNumber,
        adNetworkIdentifier: String,
        adCampaignIdentifier: NSNumber,
        adImpressionIdentifier: String,
        timestamp: NSNumber,
        signature: String,
        version: String
    )

## See Also

### Creating a signature

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# version

The version of the SKAdNetwork API.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var version: String { get set }

## Discussion

Set this instance property to the SKAdNetwork version you’re using to sign the
view-through ad impression. View-through ads are available starting in version
2.2. For more information about versions and availability, see SKAdNetwork
release notes.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adNetworkIdentifier

A string that represents the advertising network’s unique identifier.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adNetworkIdentifier: String { get set }

## Discussion

Set this property to your ad network ID.

Ad networks obtain an ad network identifier during registration. Ad networks
must share their ad network identifiers with participating app developers.
Apps that display ads must include the ad network ID in their `Info.plist` to
initiate the app install validation process. For more information about
acquiring your ad network ID, see Registering an ad network.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# sourceIdentifier

A four-digit integer that ad networks define to represent the ad campaign.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    var sourceIdentifier: NSNumber { get set }

## Discussion

The `sourceIdentifier` key is available for ad impressions that use
SKAdNetwork 4 and later. The `sourceIdentifier`, also known as the
_hierarchical source identifier_ , replaces and extends the campaign
identifier value, `adCampaignIdentifier`.

Ad networks and developers define the meaning of the hierarchical source
identifier. This integer can have up to four digits. You can encode
information about your advertisement in each set of digits; you may receive
two, three, or all four digits of the `sourceIdentifier` in the first winning
postback, depending on the ad impression’s postback data tier. For more
information about the value you may get in the postback, see Receiving
postbacks in multiple conversion windows.

Note

An install-validation postback represents this integer as a string in its
`source-identifier` parameter. For more details about the parameters of an
install-validation postback, see Identifying the parameters in install-
validation postbacks.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adCampaignIdentifier

A number that represents the advertising network’s campaign.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adCampaignIdentifier: NSNumber { get set }

## Discussion

Ad networks set their own campaign identifiers, which must be an integer `>=1`
and `<=100.`

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# advertisedAppStoreItemIdentifier

The App Store ID of the app that the ad impression advertises.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var advertisedAppStoreItemIdentifier: NSNumber { get set }

## Discussion

Set this property to the App Store item identifier of the app that you’re
advertising.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adImpressionIdentifier

A random value to use for added security.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adImpressionIdentifier: String { get set }

## Discussion

Ad networks set the value of this property to a random value (nonce) at the
time of the ad impression.

Important

When you generate `signature`, which is the signature value, you must sign the
`adImpressionIdentifier` as an all-lowercase UUID string representation.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# sourceAppStoreItemIdentifier

The App Store ID of the app that displays the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var sourceAppStoreItemIdentifier: NSNumber { get set }

## Discussion

Set this property to the App Store item identifier of the app that’s
displaying the ad.

If you’re using a development-signed build to display the ads and not an app
from App Store during testing, use `0` as the item identifier.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# timestamp

A number that represents the UNIX time, in milliseconds, of the ad impression.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var timestamp: NSNumber { get set }

## Discussion

Ad networks generate the timestamp, represented as UNIX time in milliseconds,
at the time you begin to serve the ad to users.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

Instance Property

# adType

The type of the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adType: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adDescription: String?`

A human-readable description of the ad.

`var adPurchaserName: String?`

The name of the entity that purchased the ad.

Instance Property

# adDescription

A human-readable description of the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adDescription: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adType: String?`

The type of the ad.

`var adPurchaserName: String?`

The name of the entity that purchased the ad.

Instance Property

# adPurchaserName

The name of the entity that purchased the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adPurchaserName: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adType: String?`

The type of the ad.

`var adDescription: String?`

A human-readable description of the ad.

Instance Property

# signature

The advertising network’s cryptographic signature for the ad impression.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var signature: String { get set }

## Discussion

The ad network creates a cryptographic signature that it uses to sign ads. For
instructions on generating this value, see Generating the signature to
validate view-through ads.

Initializer

#
init(sourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:)

Creates an ad impression object using the supplied values.

iOS 16.0+  iPadOS 16.0+

    
    
    init(
        sourceAppStoreItemIdentifier: NSNumber,
        advertisedAppStoreItemIdentifier: NSNumber,
        adNetworkIdentifier: String,
        adCampaignIdentifier: NSNumber,
        adImpressionIdentifier: String,
        timestamp: NSNumber,
        signature: String,
        version: String
    )

## See Also

### Creating a signature

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# version

The version of the SKAdNetwork API.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var version: String { get set }

## Discussion

Set this instance property to the SKAdNetwork version you’re using to sign the
view-through ad impression. View-through ads are available starting in version
2.2. For more information about versions and availability, see SKAdNetwork
release notes.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adNetworkIdentifier

A string that represents the advertising network’s unique identifier.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adNetworkIdentifier: String { get set }

## Discussion

Set this property to your ad network ID.

Ad networks obtain an ad network identifier during registration. Ad networks
must share their ad network identifiers with participating app developers.
Apps that display ads must include the ad network ID in their `Info.plist` to
initiate the app install validation process. For more information about
acquiring your ad network ID, see Registering an ad network.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# sourceIdentifier

A four-digit integer that ad networks define to represent the ad campaign.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    var sourceIdentifier: NSNumber { get set }

## Discussion

The `sourceIdentifier` key is available for ad impressions that use
SKAdNetwork 4 and later. The `sourceIdentifier`, also known as the
_hierarchical source identifier_ , replaces and extends the campaign
identifier value, `adCampaignIdentifier`.

Ad networks and developers define the meaning of the hierarchical source
identifier. This integer can have up to four digits. You can encode
information about your advertisement in each set of digits; you may receive
two, three, or all four digits of the `sourceIdentifier` in the first winning
postback, depending on the ad impression’s postback data tier. For more
information about the value you may get in the postback, see Receiving
postbacks in multiple conversion windows.

Note

An install-validation postback represents this integer as a string in its
`source-identifier` parameter. For more details about the parameters of an
install-validation postback, see Identifying the parameters in install-
validation postbacks.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adCampaignIdentifier

A number that represents the advertising network’s campaign.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adCampaignIdentifier: NSNumber { get set }

## Discussion

Ad networks set their own campaign identifiers, which must be an integer `>=1`
and `<=100.`

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# advertisedAppStoreItemIdentifier

The App Store ID of the app that the ad impression advertises.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var advertisedAppStoreItemIdentifier: NSNumber { get set }

## Discussion

Set this property to the App Store item identifier of the app that you’re
advertising.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# adImpressionIdentifier

A random value to use for added security.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adImpressionIdentifier: String { get set }

## Discussion

Ad networks set the value of this property to a random value (nonce) at the
time of the ad impression.

Important

When you generate `signature`, which is the signature value, you must sign the
`adImpressionIdentifier` as an all-lowercase UUID string representation.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# sourceAppStoreItemIdentifier

The App Store ID of the app that displays the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var sourceAppStoreItemIdentifier: NSNumber { get set }

## Discussion

Set this property to the App Store item identifier of the app that’s
displaying the ad.

If you’re using a development-signed build to display the ads and not an app
from App Store during testing, use `0` as the item identifier.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var timestamp: NSNumber`

A number that represents the UNIX time, in milliseconds, of the ad impression.

Instance Property

# timestamp

A number that represents the UNIX time, in milliseconds, of the ad impression.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var timestamp: NSNumber { get set }

## Discussion

Ad networks generate the timestamp, represented as UNIX time in milliseconds,
at the time you begin to serve the ad to users.

## See Also

### Creating a signature

`init(sourceAppStoreItemIdentifier: NSNumber,
advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String,
adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp:
NSNumber, signature: String, version: String)`

Creates an ad impression object using the supplied values.

`var version: String`

The version of the SKAdNetwork API.

`var adNetworkIdentifier: String`

A string that represents the advertising network’s unique identifier.

`var sourceIdentifier: NSNumber`

A four-digit integer that ad networks define to represent the ad campaign.

`var adCampaignIdentifier: NSNumber`

A number that represents the advertising network’s campaign.

`var advertisedAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that the ad impression advertises.

`var adImpressionIdentifier: String`

A random value to use for added security.

`var sourceAppStoreItemIdentifier: NSNumber`

The App Store ID of the app that displays the ad.

Instance Property

# adType

The type of the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adType: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adDescription: String?`

A human-readable description of the ad.

`var adPurchaserName: String?`

The name of the entity that purchased the ad.

Instance Property

# adDescription

A human-readable description of the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adDescription: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adType: String?`

The type of the ad.

`var adPurchaserName: String?`

The name of the entity that purchased the ad.

Instance Property

# adPurchaserName

The name of the entity that purchased the ad.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    var adPurchaserName: String? { get set }

## Discussion

This property is not used.

## See Also

### Describing ads

`var adType: String?`

The type of the ad.

`var adDescription: String?`

A human-readable description of the ad.

