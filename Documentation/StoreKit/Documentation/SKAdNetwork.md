Article

# Signing and providing ads

Advertise apps by signing and providing StoreKit-rendered ads, view-through
ads, or attributable web ads.

## Overview

SKAdNetwork supports several ways for ad networks to provide ads:

  * StoreKit-rendered ads, where StoreKit displays an App Store product page as the ad impression

  * View-through ads, where the ad network presents an ad in any format and reports the ad impression using the SKAdNetwork API

  * Attributable web ads, where the ad network presents an ad on a Safari web page using the SKAdNetwork for Web Ads API

To differentiate StoreKit-rendered ads from view-through ads, SKAdNetwork
defines a `fidelity-type` parameter, which you include in the ad signature,
and receive in the install-validation postback. Use a `fidelity-type` value of
`1` for StoreKit-rendered ads and attributable web ads, and `0` for view-
through ads. The following table compares the ad presentation options:

Ad presentation option| Description| Fidelity type| Availability  
---|---|---|---  
StoreKit-rendered ads| App Store product page that StoreKit renders| `1`| All
SKAdNetwork versions  
View-through ads| Custom, from the ad network| `0`| SKAdNetwork 2.2 and later  
Attributable web ads (SKAdNetwork for Web Ads)| Custom, from the ad network|
`1`| SKAdNetwork 4 and later  
  
For more information about availability and versions, see SKAdNetwork release
notes.

The `fidelity-type` can affect which ad receives attribution when the user
experiences multiple ad impressions. For more information about how `fidelity-
type` and the time of the ad impression affect attributions, see Receiving ad
attributions and postbacks.

Ad networks must cryptographically sign the ads. The signature contains
information that includes a campaign identifier. If ads result in conversions,
ad networks receive an install-validation postback that includes the campaign
identifier. For more information about the postback, see Verifying an install-
validation postback.

### Provide a StoreKit-rendered ad

Follow these steps to display a StoreKit-rendered ad in your app:

  1. Set Ad network install-validation keys with values that represent the ad impression.

  2. On the ad network’s server, generate the signature using those key values. Then, set the `SKStoreProductParameterAdNetworkAttributionSignature` key with the signature value. For information about generating the signature, see Generating the signature to validate StoreKit-rendered ads.

  3. Call `loadProduct(withParameters:completionBlock:)` using your ad network install-validation keys to load the ad.

  4. Present the ad in your app according to your app’s design. You can use either an `SKOverlay` or an `SKStoreProductViewController` to display a StoreKit-rendered ad. The `fidelity-type` value of a StoreKit-rendered ad is `1` in either case.

### Provide a view-through ad

Follow these steps to provide a view-through ad:

  1. Create an `SKAdImpression` instance and set its properties to represent the ad impression.

  2. On the ad network’s server, generate the signature based on those properties. Then set the `signature` property in the `SKAdImpression` instance to the generated signature. For more information, see Generating the signature to validate view-through ads.

  3. Call `startImpression(_:completionHandler:)` and then present your custom ad to the user according to your app’s design.

  4. Call `endImpression(_:completionHandler:)` when you finish presenting the ad.

### Provide an attributable web ad

Ad networks can sign attributable ads that websites can display in Safari. For
more information, see SKAdNetwork for Web Ads.

## See Also

### Essentials

Receiving ad attributions and postbacks

Learn about timeframes and priorities for ad impressions that result in ad
attributions, and how additional impressions qualify for postbacks.

Receiving postbacks in multiple conversion windows

Learn about the data that postbacks may contain in each conversion window.

SKAdNetwork release notes

Learn about the features in each SKAdNetwork version.

Article

# Receiving ad attributions and postbacks

Learn about timeframes and priorities for ad impressions that result in ad
attributions, and how additional impressions qualify for postbacks.

## Overview

Ad networks receive attributions in the form of install-validation postbacks.
Before an ad network can receive a postback, the following events need to
occur within limited time-windows:

  * Ad networks sign and present ads in the form of StoreKit-rendered ads, view-through ads, or attributable web ads. StoreKit records the ad impressions.

  * Users install the advertised app.

  * Users launch the app.

  * The app updates the conversion values when the user first launches the app, and continues to update it as needed.

If all these events occur within their respective time-windows, the ad
impression qualifies for an install-validation postback. The following table
shows the time-windows for the events:

Event| Time-window  
---|---  
The ad network presents a StoreKit-rendered ad.| The user has 30 days to
install the app.  
The ad network presents a view-through ad.| The user has 24 hours to install
the app.  
The user taps an attributable web ad.| The user has 30 days to install the
app.  
The user installs the app.| The user has 60 days to launch the app.  
The user launches the app and the app calls any conversion update method, such as `updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`, | The device has 60 days after the user installs the app to send the first conversion value update.  
The user launches the app and the app calls a conversion update method, such
as `updatePostbackConversionValue(_:completionHandler:)` for ads signed with
version 3 or earlier.| For ads signed with version 3 or earlier, the device
sends install-validation postbacks 0–24 hours after a 24-hour timer expires
following the final call to update the conversion value. The total delay from
the final conversion update to receiving the postback is 24–48 hours.  
  
The minimum elapsed time between an ad impression and the time the ad network
receives an install-validation postback is 24 to 48 hours. To reduce that time
to 5 to 10 minutes during testing, see Testing ad attributions with a
downloaded profile.

Devices send one or more postbacks depending on the SKAdNetwork and iOS
versions:

  * For ads signed with SKAdNetwork 1 through 2.2, devices send a single, winning postback.

  * Starting in iOS 14.6 for ads signed with version 3.0 or later, devices send a single winning postback, and up to five nonwinning postbacks.

  * Starting in iOS 15, devices also send a copy of the winning postback to the advertised app’s developer, if the developer opts in to receive it. 

  * Starting in iOS 16.1 for ads signed using SKAdNetwork 4, devices can send up to three postbacks for the winning ad attribution, in three conversion windows.

Time-windows for events apply equally to winning and nonwinning postbacks.

### Receive a winning postback

When multiple ad impressions qualify for install-validation postbacks, a
device sends the winning postback to the ad network based on the following
rules:

  * In versions 1 through 2.1, the attribution goes to the most recent ad impression.

  * Starting in version 2.2, the attribution goes to the most recent ad impression with the highest `fidelity-type` value. 

The ad presentation option defines the `fidelity-type` value:

  * StoreKit-rendered ads have the highest `fidelity-type` value of `1`.

  * View-through ads have a `fidelity-type` value of `0`. 

Indicate the `fidelity-type` when you generate the ad signature. Recorded ad
impressions with a `fidelity-type` of `1` always take precedence over those
with a `fidelity-type` of `0`. For example, if users see a StoreKit-rendered
ad followed by a view-through ad for the same app, the StoreKit-rendered ad
takes precedence over the view-through ad, despite the view-through ad being
more recent. The source app can display StoreKit-rendered ads using an
`SKOverlay` or `SKStoreProductViewController`; the `fidelity-type` value is
`1` in either case. For information about the fidelity of ads that an ad
network presents on a Safari web page using the SKAdNetwork for Web Ads API,
see `signature`.

In version 3 and later, the system indicates winning postbacks with a `did-
win` parameter of value `true`.

### Receive a nonwinning postback

Starting in iOS 14.6, devices can send multiple postbacks to ad networks that
sign ads using version 3 or later. The system indicates nonwinning postbacks
with a `did-win` parameter of value `false`. These postbacks don’t include
`conversion-value` or `source-app-id`.

Each ad network can receive only one install-validation postback, winning or
not winning. If you receive the winning postback, you don’t receive any
nonwinning postbacks even if your ads have multiple qualifying ad impressions.

Up to five ad networks receive one nonwinning postback each. The system orders
the recorded ad impressions using recency and `fidelity-type`, with the most
recent ad views and highest `fidelity-type` taking precedence. Devices send
nonwinning postbacks for the top five ad impressions from different ad
networks that qualify for ad attribution.

### Opt in to receive a copy of the winning postback

Starting in iOS 15, devices can send a copy of the winning install-validation
postback to the developer of the advertised app. Developers opt in to receive
the postback by specifying a server endpoint in their app’s `Info.plist` file.
For more information about opting in and specifying the endpoint, see
Configuring an advertised app.

The postback that developers receive is an exact copy of the winning install-
validation postback that the device sends to the ad network. The device sends
the postback to developers at the same time it sends the winning postback to
the ad network. To verify the postback, see Verifying an install-validation
postback.

### Limit view-through ad impressions

StoreKit records a maximum of 15 view-through ad impressions per source app
before discarding the oldest one. The recorded ad impressions may advertise
various products, and are each eligible to become pending attributions until
they expire (after 24 hours).

### Test ad impressions and postbacks

Use the StoreKit Test framework to validate your ad impressions and test your
postbacks by creating unit tests. For more information, see `SKAdTestSession`
and Testing and validating ad impression signatures and postbacks for
SKAdNetwork.

## See Also

### Essentials

Signing and providing ads

Advertise apps by signing and providing StoreKit-rendered ads, view-through
ads, or attributable web ads.

Receiving postbacks in multiple conversion windows

Learn about the data that postbacks may contain in each conversion window.

SKAdNetwork release notes

Learn about the features in each SKAdNetwork version.

Article

# Receiving postbacks in multiple conversion windows

Learn about the data that postbacks may contain in each conversion window.

## Overview

SKAdNetwork supports three conversion windows that may result in up to three
postbacks for a winning ad attribution. The conversion window begins when the
user first launches the app. The first conversion window spans days 0 to 2;
the second window spans days 3 to 7; and the third window spans days 8 to 35.
Apps can update conversion values during all three time-windows.

To be eligible to receive multiple postbacks, all participants need to meet
the following conditions:

  * The ad network needs to sign the ad using SKAdNetwork 4 or later.

  * The advertised app needs to call `updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)` or `updatePostbackConversionValue(_:coarseValue:completionHandler:)`to update the conversion values during each conversion window.

You may receive a single postback in the following cases:

  * If the app's postback data tier is Tier 0, the system sends only the first postback.

  * Nonwinning ad attributions receive only the first postback.

  * For ads signed using SKAdNetwork 3 or earlier, you receive only one winning postback.

### Lock conversion values to receive postbacks sooner

By default, the system waits until the end of a conversion window to get the
final conversion value. Apps can continue to update the conversion value until
the end of the conversion window. When the conversion window ends, the system
prepares the postback and sends it after a random delay, as the following
diagram shows:

The random delay is 24–48 hours for the first postback, and 24–144 hours for
the second and third postbacks.

The
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
method provides an option for you to lock in and finalize a conversion value
before the conversion window ends. You may choose to lock the conversion value
in any or all conversion windows. The diagram below shows an app that locks
the conversion value during the second conversion window:

After receiving a locked conversion value, the system immediately prepares the
postback and ignores any further conversion value updates in the same
conversion window. The system sends the postbacks after the same random delay
following the locked conversion: a 24–48-hour delay for the first postback,
and a 24–144-hour delay for the second and third postbacks. The system ignores
further updates to the conversion value for the remaining time in the same
conversion window.

Note

The earliest you may receive the first postback is unchanged from version 3 to
version 4: the total delay is 24–48 hours after the app updates its final
conversion value.

  * In version 3, the app finalizes the conversion value when a 24-hour timer expires after the last conversion value update. Then, the device sends the postback after a random 0–24 hour delay, making the earliest postback 24–48 hours after the app sets the final conversion value.

  * In version 4, the app may finalize the conversion value by locking it. Then, the device sends the postback after a random 24–48 hour delay.

As a result, both version 3 and 4 have a total delay of 24–48 hours to receive
the first postback after the app finalizes the conversion value.

### Receive the highest level of data that ensures crowd anonymity

To maintain users’ privacy and ensure crowd anonymity, the device may limit
the data that SKAdNetwork sends in postbacks. Apple determines a postback data
tier that it assigns to each app download. The following diagram depicts the
relationship between the tiers and relative crowd sizes. It's for illustrative
purposes only.

The postback data tier takes into account the crowd size associated with the
app or domain displaying the ad, the advertised app, and the hierarchical
source identifier the ad network provides. The system computes the postback
data tier for the two-, three-, and four-digit hierarchical source
identifiers. It selects the source identifier with the highest postback data
tier. If multiple source identifiers share the highest postback data tier, the
system selects the source identifier with the most digits. If the highest
postback data tier is Tier 1 or Tier 0, the system always selects the two-
digit source identifier.

The postback data tier affects the following fields in the postback, which may
be present or absent, or may contain a limited number of digits:

  * `source-identifier`, the hierarchical source identifier that may include two, three, or four digits

  * `conversion-value`, a fine-grained conversion value available only in the first postback

  * `coarse-conversion-value`, a coarse conversion value, which the system sends instead of the `conversion-value` in lower postback data tiers, and in the second and third postbacks

  * `source-app-id` for ads that display in apps, or `source-domain` for attributable web ads

The remaining postback data fields aren't dependent on the postback date tier
and appear in all postbacks, based on the SKAdNetwork version of the
postback.``

### Receive the first postback

The first conversion window ends two days after the user first launches the
app. The system prepares the postback after the conversion window ends, unless
you use a lock. If you use a lock, the system prepares the first postback when
the app calls
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
with the lock in an enabled state. The system then sends the postback after a
random 24–48-hour delay.

The postback data tier determines the data you receive in the first postback,
as follows:

For ads in Tier 3, the first postback contains:

  * `source-identifier`, the hierarchical source identifer with two, three, or four digits

  * `conversion-value`, the fine-grained conversion value, if the app provides one

  * `source-app-id` for ads that display in apps, or `source-domain` for attributable web ads

For ads in Tier 2, the first postback contains:

  * `source-identifier`, the hierarchical source identifer with two, three, or four digits

  * `conversion-value`, the fine-grained conversion value, if the app provides one

For ads in Tier 1, the first postback contains:

  * `source-identifier`, the hierarchical source identifer with two digits

  * `coarse-conversion-value`, a coarse value, if the app provides one

For ads in Tier 0, the first postback contains the `source-identifier`, the
hierarchical source identifer, with two digits.

### Receive the second and third postbacks

The second conversion window ends seven days after the user first launches the
app, and the third conversion window ends after 35 days. The system prepares
the second and third postbacks after their conversion windows end, and sends
them after a random 24–144-hour delay.

If you use a lock with the second or third conversion value updates, the
system prepares the postback when you call
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
with the lock in an enabled state. The system sends the postback after a
random 24–144-hour delay.

The postback data tier determines the data you receive in the postbacks, as
follows:

For ads in Tier 1, Tier 2, and Tier 3, the second and third postbacks contain:

  * `source-identifier`, the hierarchical source identifer with two digits

  * `coarse-conversion-value`, the coarse conversion value, if the app provides one

For ads in Tier 0, the system doesn’t send a second or third postback.

Ads signed with version 4 and later are eligible for second and third
postbacks after a winning ad impression. Ads signed with version 3 and earlier
are eligible for one winning postback.

## See Also

### Essentials

Signing and providing ads

Advertise apps by signing and providing StoreKit-rendered ads, view-through
ads, or attributable web ads.

Receiving ad attributions and postbacks

Learn about timeframes and priorities for ad impressions that result in ad
attributions, and how additional impressions qualify for postbacks.

SKAdNetwork release notes

Learn about the features in each SKAdNetwork version.

Article

# Registering an ad network

Use the install-validation APIs for your ad campaigns after registering your
ad network with Apple.

## Overview

Ad networks provide and cryptographically sign ads that are eligible for ad
attribution through SKAdNetwork. Ad networks need to register with Apple
before using the SKAdNetwork API.

To register your ad network, go to Ad Network ID Request Form, which prompts
you to sign in to Apple Developer and opens the request form.

When registering, you:

  * Receive your ad network ID.

  * Create an elliptic curve cryptographic key pair and share your public key with Apple for signature verification.

  * Provide a URL for receiving SKAdNetwork install-validation postback requests.

### Share your ad network ID with developers

The ad network ID is a unique lowercased identifier in the format of
“`example123.skadnetwork`”. Share your ad network ID with app developers who
display your ads. Developers need to include your ad network ID in their app’s
information property list to initiate the app install-validation process.

Important

Lowercase the ad network ID string; otherwise, the system doesn’t recognize it
as valid.

### Generate your private key

Ad networks use a private cryptographic key to generate a signature for each
ad that an app displays. During registration, ad networks create a public-
private key pair, and send the public key to Apple. The private key you create
uses an Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256v1
curve.

To create your private key, open Terminal and enter the following command:

    
    
    openssl ecparam -name prime256v1 -genkey -noout -out companyname_skadnetwork_private_key.pem
    

In the command, replace `companyname` with the name of your company. For
example, the name of the private key file for a company named _Example_ is
`example_skadnetwork_private_key.pem`.

Important

Secure your private keys as you do other credentials, such as passwords. Don’t
share your private keys, store keys in a code repository, or include keys in
client-side code. Share only your public key.

### Generate and share your public key

Next, you create a public key from the private key you created in the previous
section. The public key is a PEM-encoded PKCS#8 EC key that uses the
prime256v1 curve. In Terminal, enter the following command, again replacing
`companyname` with the name of your company:

    
    
    openssl ec -in companyname_skadnetwork_private_key.pem -pubout -out companyname_skadnetwork_public_key.pem
    

This command creates the file `companyname_skadnetwork_public_key.pem`, which
contains your public key. Run this command any time to generate a copy of your
public key file.

Send your public key file to Apple when you register your ad network.

## See Also

### Registering ad networks and configuring apps

Configuring a source app

Set up a source app to participate in ad campaigns.

Configuring an advertised app

Prepare an advertised app to participate in ad campaigns.

`property list key SKAdNetworkItems`

An array of dictionaries containing a list of ad network IDs.

`property list key NSAdvertisingAttributionReportEndpoint`

The URL where Private Click Measurement and SKAdNetwork send attribution
information.

Article

# Configuring a source app

Set up a source app to participate in ad campaigns.

## Overview

A _source app_ is an app that participates in ad campaigns by displaying ads
that an ad network signs. To participate in install validation, the source app
needs to include ad network IDs in its `Info.plist` file. Ad networks are
responsible for publishing or providing their ad network IDs to developers.

Only ads from ad networks that have an entry in the app’s `Info.plist` file
are eligible for install validation. To work with multiple ad networks,
include each of the ad network IDs in the source app’s `Info.plist` file, as
follows:

  1. Select `Info.plist` in the Project navigator in Xcode.

  2. Click the Add button (+) beside a key in the property list editor and press Return.

  3. Type the key name `SKAdNetworkItems`.

  4. Choose Array from the pop-up menu in the Type column.

Create an array that contains one dictionary for each allowed ad network,
using the single key `SKAdNetworkIdentifier`. The string value for the key is
the ad network ID.

Important

Lowercase the ad network ID string; otherwise, the system doesn’t recognize it
as valid.

The following example shows an array with two dictionaries that represent the
example ad network IDs `example100.skadnetwork` and `example200.skadnetwork`:

    
    
    <array>
        <dict>
            <key>SKAdNetworkIdentifier</key>
            <string>example100.skadnetwork</string>
        </dict>
        <dict>   
             <key>SKAdNetworkIdentifier</key>
             <string>example200.skadnetwork</string>
        </dict>
    </array>
    
    
    

For more information about property lists, see Edit property lists.

## See Also

### Registering ad networks and configuring apps

Registering an ad network

Use the install-validation APIs for your ad campaigns after registering your
ad network with Apple.

Configuring an advertised app

Prepare an advertised app to participate in ad campaigns.

`property list key SKAdNetworkItems`

An array of dictionaries containing a list of ad network IDs.

`property list key NSAdvertisingAttributionReportEndpoint`

The URL where Private Click Measurement and SKAdNetwork send attribution
information.

Article

# Configuring an advertised app

Prepare an advertised app to participate in ad campaigns.

## Overview

An _advertised app_ is an app a user installs after viewing an ad that an ad
network signs. The advertised app doesn’t require any configuration to
participate in install validation. However, to register ad attributions, the
app needs to call one of the methods that update conversion values when the
app first launches. Those methods are:
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`,
`updatePostbackConversionValue(_:coarseValue:completionHandler:)`, and
`updatePostbackConversionValue(_:completionHandler:)`.

Developers opt in to get copies of winning install-validation postbacks.

### Configure your app to receive copies of winning install-validation
postbacks

To opt in to receive copies of winning install-validation postbacks for your
advertised app, add the `NSAdvertisingAttributionReportEndpoint` key in your
app’s `Info.plist` file, and configure your server to receive the postbacks.

To add the key in your app’s `Info.plist` file:

  1. Select `Info.plist` in the Project navigator in Xcode.

  2. Click the Add button (+) beside a key in the property list editor and press Return.

  3. Type the key name `NSAdvertisingAttributionReportEndpoint`.

  4. Choose String from the pop-up menu in the Type column.

  5. Type a valid URL in the format of `“https://example.com”` that contains your domain name in place of `example.com`.

For more information about editing property lists, see Edit property lists.

The system uses the registrable part of the domain name you provide in the
key, and ignores any subdomains. Using your domain name, the system generates
a _well-known path_ and sends postbacks to that URL. To receive postbacks,
your domain needs to have a valid SSL certificate. Configure your server to
accept HTTPS POST messages at the following well-known path:

`https://example.com/.well-known/skadnetwork/report-attribution/`

Replace `example.com` with your domain name.

For more information about receiving postbacks, see Receiving ad attributions
and postbacks.

## See Also

### Registering ad networks and configuring apps

Registering an ad network

Use the install-validation APIs for your ad campaigns after registering your
ad network with Apple.

Configuring a source app

Set up a source app to participate in ad campaigns.

`property list key SKAdNetworkItems`

An array of dictionaries containing a list of ad network IDs.

`property list key NSAdvertisingAttributionReportEndpoint`

The URL where Private Click Measurement and SKAdNetwork send attribution
information.

Property List Key

# SKAdNetworkItems

An array of dictionaries containing a list of ad network IDs.

iOS 11.3+  iPadOS 11.3+

##  Details

Type

    

array of dictionaries

## Discussion

Apps that display ads and initiate install-validation information to share
with ad networks need to include the ad network IDs in this key.

Each dictionary contains one `SKAdNetworkIdentifier`. Provide one dictionary
for each ad network that you work with.

Important

Ad network IDs are case-sensitive and are in lowercase.

For more information, see Configuring a source app.

## Topics

### Ad network identifiers

`property list key SKAdNetworkIdentifier`

A string that contains an ad network ID.

## See Also

### Registering ad networks and configuring apps

Registering an ad network

Use the install-validation APIs for your ad campaigns after registering your
ad network with Apple.

Configuring a source app

Set up a source app to participate in ad campaigns.

Configuring an advertised app

Prepare an advertised app to participate in ad campaigns.

`property list key NSAdvertisingAttributionReportEndpoint`

The URL where Private Click Measurement and SKAdNetwork send attribution
information.

Property List Key

# NSAdvertisingAttributionReportEndpoint

The URL where Private Click Measurement and SKAdNetwork send attribution
information.

iOS 14.5+  iPadOS 14.5+  visionOS 1.0+

##  Details

Type

    

string

## Discussion

This key is a string that contains a valid URL containing your domain name.
Provide a string in the format `“https://example.com”`, where you replace
`example` with your domain name. Include this key in your app for the
following two uses:

  * To specify where the system sends event attribution data it receives from launched websites that support Private Click Measurement (PCM). PCM won’t work if your app doesn’t include this key. 

  * To specify where the system sends a copy of the winning install-validation postback to the advertised app’s developer, for apps that are advertised using the `SKAdNetwork` API. Including this key is optional. 

The system sends postbacks to a well-known URL it generates using the domain
name you provide in the key. To receive the postbacks, configure your server
to receive HTTPS POST messages at the following endpoints:

  * To receive PCM event attribution data: `https://example.com/.well-known/private-click-measurement/report-attribution/`

  * To receive SKAdNetwork install-validation postbacks: `https://example.com/.well-known/skadnetwork/report-attribution/`

Replace `example.com` with your domain name. The system uses only the
registrable part of the domain name, and ignores any subdomains.

For more information about PCM and setting up a server to receive event
attribution data, see Introducing Private Click Measurement. For more
information about configuring an advertised app to enable its developer to
receive postbacks, see Configuring an advertised app and `SKAdNetwork`.

Note

Mac apps built with Mac Catalyst don’t support PCM.

## See Also

### Private Click Measurement (PCM)

`class UIEventAttributionView`

An overlay view that verifies user interaction for Web AdAttributionKit.

`class UIEventAttribution`

An object that contains event attribution information for Web
AdAttributionKit.

Article

# Generating the signature to validate view-through ads

Initiate install validation by displaying a view-through ad with signed
parameters.

## Overview

Install validation informs an ad network when users install and launch an app
they purchase after viewing an ad. Ad networks provide an ad with
cryptographically signed information that includes their ad network ID. If the
ad results in a conversion, the customer’s device sends install-validation
postbacks. For information about attribution-winning and nonwinning postbacks,
see Receiving ad attributions and postbacks.

Starting in iOS 14.5 with SKAdNetwork 2.2, ad networks can present view-
through ads to provide custom ads using any media.

Note

These instructions are for signing view-through ads. If you’re presenting a
StoreKit-rendered ad, see Generating the signature to validate StoreKit-
rendered ads.

To provide a view-through ad and initiate a validation, the app calls
`startImpression(_:completionHandler:)`, presents the ad, and then calls
`endImpression(_:completionHandler:)`. The ad network needs to generate the
`signature` in the `SKAdImpression` instance that both methods share.

Ad networks generate the signature on their server using their ad network ID
and the PKCS#8 private key they establish when registering to use the API. For
more information, see Registering an ad network.

### Create an ad impression instance

Create an instance of `SKAdImpression` to set the properties for the ad
impression. These properties contain the same values you use to generate the
signature.

The following table maps the parameters you use in the signature string to
their equivalent `SKAdImpression` properties, as the code example demonstrates
in the Combine parameter values section below:

Signature parameter| Equivalent properties  
---|---  
`version`| `version`. For view-through ads, use version 2.2 and later.  
`ad-network-id`| `adNetworkIdentifier`  
`campaign-id`| `adCampaignIdentifier` for version 3 or earlier. For version 4
and later, the `sourceIdentifier` replaces this parameter.  
`source-identifier`| `sourceIdentifier` for version 4 and later. This
parameter replaces the `adCampaignIdentifier` parameter.  
`itunes-item-id`| `advertisedAppStoreItemIdentifier`  
`nonce`| `adImpressionIdentifier`  
`source-app-id`| `sourceAppStoreItemIdentifier`  
`fidelity-type`| An additional parameter in the signature that isn't part of
`SKAdImpression`. Required for version 2.2 and later signatures. For view-
through ads, use a fidelity type value of `0`.  
`timestamp`| `timestamp`  
  
### Combine parameter values

The order and content of the signature parameters depends on the `version` of
the signature you're creating. Choose one of the parameter combinations below,
based on your `version`.

To generate a signature for version 4 or later, combine the signature
parameter values into a UTF-8 string with an invisible separator (`‘\u2063’`)
between them, in the exact order the code below shows:

    
    
    version + '\u2063' + ad-network-id + '\u2063' + source-identifier + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + timestamp
    
    
    

To generate a signature for versions 2.2 and 3, combine the signature
parameter values into a UTF-8 string with an invisible separator (`‘\u2063’`)
between them, in the exact order the code below shows:

    
    
    version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + timestamp
    
    
    

Use the most recent version available in the SDK whenever possible. For
information about availability, see SKAdNetwork release notes.

### Sign the combined string

Sign the combined UTF-8 string with the following key and algorithm:

  * Your PKCS#8 private key.

  * The Elliptic Curve Digital Signature Algorithm (ECDSA) with a SHA-256 hash. 

The resulting Digital Encoding Rules (DER)-formatted binary value is the
signature.

### Encode the signature

Encode the binary signature you generate into a Base64 string. The result is
your ad network attribution signature, `signature`, to use for view-through
ads. The signature string should resemble the following:

    
    
    MEQCIEQlmZRNfYzKBSE8QnhLTIHZZZWCFgZpRqRxHss65KoFAiAJgJKjdrWdkLUOCCjuEx2RmFS7daRzSVZRVZ8RyMyUXg==
    

For more information about Base64 encoding, see
`base64EncodedString(options:)`.

### Use the generated signature string

After you generate the signature, you have all the required values for your
`SKAdImpression` instance and can use it to call
`startImpression(_:completionHandler:)`. Present your view-through ad, and
then call `endImpression(_:completionHandler:)` using the same
`SKAdImpression` instance.

## See Also

### Signing view-through ads

`class SKAdImpression`

A class that defines an ad impression for a view-through ad.

`class func startImpression(SKAdImpression, completionHandler: (((any Error)?)
-> Void)?)`

Indicates that your app is presenting a view-through ad to the user.

`class func endImpression(SKAdImpression, completionHandler: (((any Error)?)
-> Void)?)`

Indicates that your app is no longer presenting a view-through ad to the user.

Type Method

# startImpression(_:completionHandler:)

Indicates that your app is presenting a view-through ad to the user.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    class func startImpression(
        _ impression: SKAdImpression,
        completionHandler completion: (((any Error)?) -> Void)? = nil
    )

##  Parameters

`impression`

    

An instance of `SKAdImpression` with the properties set for the view-through
ad that you’re presenting.

`completion`

    

The callback handler you provide to handle any tasks relevant to the start of
the ad impression.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Call this method when you start presenting the view-through ad to the user. If
you call `startImpression(_:completionHandler:)` more than once for the same
advertised app before calling `endImpression(_:completionHandler:)`, the
latest impression overwrites the earlier impression.

Call `endImpression(_:completionHandler:)` when the impression ends and is no
longer visible to the user.

Note

To ensure that SKAdNetwork records the impression, call
`endImpression(_:completionHandler:)` after the impression ends, regardless of
whether `startImpression(_:completionHandler:)` returns an error in the
completion handler.

## See Also

### Signing view-through ads

Generating the signature to validate view-through ads

Initiate install validation by displaying a view-through ad with signed
parameters.

`class SKAdImpression`

A class that defines an ad impression for a view-through ad.

`class func endImpression(SKAdImpression, completionHandler: (((any Error)?)
-> Void)?)`

Indicates that your app is no longer presenting a view-through ad to the user.

Type Method

# endImpression(_:completionHandler:)

Indicates that your app is no longer presenting a view-through ad to the user.

iOS 14.5+  iPadOS 14.5+  Mac Catalyst 14.5+

    
    
    class func endImpression(
        _ impression: SKAdImpression,
        completionHandler completion: (((any Error)?) -> Void)? = nil
    )

##  Parameters

`impression`

    

An instance of `SKAdImpression` with the properties set for the view-through
ad that you presented. This must be the same instance you provide in
`startImpression(_:completionHandler:)`.

`completion`

    

The callback handler you provide to handle any tasks relevant to concluding
the ad impression.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Call this method when you end the presentation of a view-through ad and it’s
no longer visible to the user. To help ensure it’s a valid impression,
StoreKit only records the impression if the ad displays for a minimum amount
of time. That minimum is 2 seconds on devices running iOS 15.4 and iPadOS 15.4
and later, and 3 seconds on devices running earlier versions of iOS and
iPadOS. If the app displays the ad for fewer than the minimum number of
seconds, StoreKit doesn’t record the ad impression for attribution.

Note

To ensure that SKAdNetwork records the impression, call
`endImpression(_:completionHandler:)` after the impression ends, regardless of
whether `startImpression(_:completionHandler:)` returns an error in the
completion handler.

StoreKit records a maximum of 15 view-through ad impressions per source app
for various products before discarding the oldest-recorded impression.

For more information about ad impressions and attributions, see Receiving ad
attributions and postbacks.

## See Also

### Signing view-through ads

Generating the signature to validate view-through ads

Initiate install validation by displaying a view-through ad with signed
parameters.

`class SKAdImpression`

A class that defines an ad impression for a view-through ad.

`class func startImpression(SKAdImpression, completionHandler: (((any Error)?)
-> Void)?)`

Indicates that your app is presenting a view-through ad to the user.

Type Method

# updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)

Updates the fine and coarse conversion values and indicates whether to send
the postback before the conversion window ends, and calls a completion handler
if the update fails.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    class func updatePostbackConversionValue(
        _ fineValue: Int,
        coarseValue: SKAdNetwork.CoarseConversionValue,
        lockWindow: Bool,
        completionHandler completion: (((any Error)?) -> Void)? = nil
    )

##  Parameters

`fineValue`

    

An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the
meaning of the fine conversion value.

`coarseValue`

    

An `SKAdNetwork.CoarseConversionValue` value of `low`, `medium`, or `high`.
The app or the ad network defines the meaning of the coarse conversion value.

`lockWindow`

    

A Boolean value that indicates whether to send the postback before the
conversion window ends. Use `true` to tell the system to send the postback
without waiting for the end of the conversion window. The default value is
`false`.

`completion`

    

An optional completion handler you provide to catch and handle any errors this
method encounters when you update a conversion value. Set this value to `nil`
if you don’t provide a handler.

## Return Value

This method returns `SKANError.Code.invalidConversionValue` if the `fineValue`
is outside of the allowed range.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Call this method when the user first launches an app to register the app
installation, and again to update conversion values as the user engages with
the app. It’s up to your app to decide what the conversion values signify in
your app, both the `fineValue` and the `coarseValue`.

This method supports ads signed with any verison of SKAdNetwork, and you can
use it instead of calling
`updatePostbackConversionValue(_:completionHandler:)` and
`updatePostbackConversionValue(_:coarseValue:completionHandler:)`. The system
automatically determines the method’s behavior based on the ad’s version, as
the following sections describe — the app doesn’t need to know the ad version.
To take advantage of the multiple postbacks available starting in version 4,
use this method or
`updatePostbackConversionValue(_:coarseValue:completionHandler:)`.

Important

The system ignores calls to this method if the `fineValue` is outside of the
valid range. Valid conversion updates your app sends before or after an
invalid conversion remain available.

### Update conversion values for ads signed with SKAdNetwork 4 or later

For ads that ad networks sign using version 4 or later, calling this method
behaves as follows:

  * Both the `fineValue` and `coarseValue` represent conversion values. The method ignores the `fineValue` after the first conversion window.

  * Setting the `lockWindow` parameter to `true` indicates a final update for the conversion value for the current conversion window. The system ignores additional calls to update the conversion value until the end of the conversion window.

  * Setting the `lockWindow` parameter to `false` continues updating the conversion value throughout the conversion window.

For information about the data you may receive in postbacks, see Receiving
postbacks in multiple conversion windows.

### Update conversion values for ads signed with SKAdNetwork 3 or earlier

For ads that ad networks sign using version 3 or earlier, calling this method
behaves as follows:

  * The `fineValue` represents the conversion value. 

  * The method ignores the `coarseValue` and `lockWindow` parameters.

  * There’s a single conversion period that ends after a rolling 24-hour timer expires. The 24-hour timer restarts each time the app calls this method with a valid conversion value greater than the previous value. When the timer expires, the conversion value is final and subsequent calls to this method have no effect.

  * The device sends the postback 0–24 hours after the timer expires. 

  * The postback contains the final conversion value only if the postback data tier contains the value.

For more information about SKAdNetwork versions, see SKAdNetwork release
notes.

## See Also

### Providing conversion information

`class func updatePostbackConversionValue(Int, coarseValue:
SKAdNetwork.CoarseConversionValue, completionHandler: (((any Error)?) ->
Void)?)`

Updates the fine and coarse conversion values, and calls a completion handler
if the update fails.

`struct SKAdNetwork.CoarseConversionValue`

Coarse values to use for updating conversion values.

`class func updatePostbackConversionValue(Int, completionHandler: (((any
Error)?) -> Void)?)`

Verifies the first launch of an advertised app and, on subsequent calls,
updates the conversion value or calls a completion handler if the update
fails.

Type Method

# updatePostbackConversionValue(_:coarseValue:completionHandler:)

Updates the fine and coarse conversion values, and calls a completion handler
if the update fails.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    class func updatePostbackConversionValue(
        _ fineValue: Int,
        coarseValue: SKAdNetwork.CoarseConversionValue,
        completionHandler completion: (((any Error)?) -> Void)? = nil
    )

##  Parameters

`fineValue`

    

An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the
meaning of the conversion value.

`coarseValue`

    

An `SKAdNetwork.CoarseConversionValue` value. The app or the ad network
defines the meaning of this value.

`completion`

    

An optional completion handler you provide to catch and handle any errors this
method encounters when you update a conversion value. Set this value to `nil`
if you don’t provide a handler.

## Return Value

This method returns `SKANError.Code.invalidConversionValue` if the `fineValue`
is outside of the allowed range.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Call this method when the user first launches an app to register the app
installation, and optionally again, to update conversion values as the user
engages with the app.

This method is identical to calling
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
with the `lockWindow` parameter set to `false`.

Important

The system ignores calls to this method if the `fineValue` is outside of the
valid range. Valid conversion updates your app sends before or after an
invalid conversion remain available.

## See Also

### Providing conversion information

`class func updatePostbackConversionValue(Int, coarseValue:
SKAdNetwork.CoarseConversionValue, lockWindow: Bool, completionHandler: (((any
Error)?) -> Void)?)`

Updates the fine and coarse conversion values and indicates whether to send
the postback before the conversion window ends, and calls a completion handler
if the update fails.

`struct SKAdNetwork.CoarseConversionValue`

Coarse values to use for updating conversion values.

`class func updatePostbackConversionValue(Int, completionHandler: (((any
Error)?) -> Void)?)`

Verifies the first launch of an advertised app and, on subsequent calls,
updates the conversion value or calls a completion handler if the update
fails.

Type Method

# updatePostbackConversionValue(_:completionHandler:)

Verifies the first launch of an advertised app and, on subsequent calls,
updates the conversion value or calls a completion handler if the update
fails.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+

    
    
    class func updatePostbackConversionValue(
        _ conversionValue: Int,
        completionHandler completion: (((any Error)?) -> Void)? = nil
    )

##  Parameters

`conversionValue`

    

An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the
meaning of the conversion value. For ad impressions signed with SKAdNetwork 3
or earlier, you need to increase the `conversionValue` each time you call this
method. For ad impressions signed with SKAdNetwork 4 or later, you may use any
valid `conversionValue` each time you call this method.

`completion`

    

An optional completion handler you provide to catch and handle any errors this
method encounters when you update a conversion value. Set this value to `nil`
if you don’t provide a handler.

## Return Value

Invalid conversion values cause the method to fail and return error
`SKANError.Code.invalidConversionValue`.

## Discussion

Concurrency Note

You can call this method from synchronous code using a completion handler, as
shown on this page, or you can call it as an asynchronous method that has the
following declaration:

For information about concurrency and asynchronous code in Swift, see Calling
Objective-C APIs Asynchronously.

Note

Consider using
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
instead of this method for newer implementations.

Apps call this method to update conversion values as people engage with the
app. It’s up to the app or ad network to define the conversion value’s
meaning. Call this method immediately when the user first launches the app to
confirm the app’s launch. Call this method again, as needed, to reflect the
person’s engagement with the app.

The final conversion value appears in the postback if sending the data meets
Apple’s privacy threshold. Only postbacks that win the ad attribution can
contain a conversion value. Nonwinning postbacks don’t contain conversion
values. For more information, see Receiving ad attributions and postbacks.

The way this method behaves depends on the ad’s version, as described in the
following sections. Ad networks determine an ad’s version when they sign the
ad. For more information about signing ads, see Signing and providing ads.

### Update the conversion value for version 3 ads and earlier

If the ad network signs the winning ad with version 3 or earlier, calling this
method behaves as follows:

  * Apps may call this method repeatedly before a rolling 24-hour timer expires.

  * The 24-hour timer restarts each time the app calls this method with a valid `conversionValue` that’s greater than the previous value. 

  * When the timer expires, the conversion value is final and subsequent calls to `updatePostbackConversionValue(_:completionHandler:)` have no effect.

  * The device sends the postback to the ad network’s URL within 0 to 24 hours after the timer expires. The postback contains the final conversion value only if sending the data meets Apple’s privacy threshold.

### Update the conversion value for version 4 ads and later

Note

This method supports ads signed with version 4 and later, however, it doesn’t
provide advanced features, such as multiple postbacks and coarse conversion
values, available starting in version 4. To get those advanced features for
ads signed with version 4 and later, use
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
instead of this method.

If the ad network signs the winning ad with version 4 or later, calling this
method behaves as follows:

  * Apps may call this method repeatedly within the first conversion window.

  * Provide any `conversionValue` within the valid range; the `conversionValue` doesn’t need to increase with each call.

  * This method is available only during the first conversion window. Use `updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)` to update conversion values in the subsequent conversion windows.

  * When the first conversion window closes, the system sends the postback within 0 to 24 hours. The postback contains the final conversion value only if sending the data meets Apple’s privacy threshold.

## See Also

### Providing conversion information

`class func updatePostbackConversionValue(Int, coarseValue:
SKAdNetwork.CoarseConversionValue, lockWindow: Bool, completionHandler: (((any
Error)?) -> Void)?)`

Updates the fine and coarse conversion values and indicates whether to send
the postback before the conversion window ends, and calls a completion handler
if the update fails.

`class func updatePostbackConversionValue(Int, coarseValue:
SKAdNetwork.CoarseConversionValue, completionHandler: (((any Error)?) ->
Void)?)`

Updates the fine and coarse conversion values, and calls a completion handler
if the update fails.

`struct SKAdNetwork.CoarseConversionValue`

Coarse values to use for updating conversion values.

Article

# Identifying the parameters in install-validation postbacks

Learn about the postback parameters in all SKAdNetwork versions.

## Overview

The following list describes all the possible parameters you may get in a
postback, and their version availability. To verify that Apple signed the
postback, see Verifying an install-validation postback.

`version`

    

Version 2 and later. The SKAdNetwork version that matches
`SKStoreProductParameterAdNetworkVersion` or `version`. For more information
about versions, see SKAdNetwork release notes.

`ad-network-id`

    

Version 1 and later. Your ad network ID, which matches the value you provide
for `SKStoreProductParameterAdNetworkIdentifier` or `adNetworkIdentifier`.

`attribution-signature`

    

Version 2 and later. Apple’s attribution signature that you verify.

`app-id`

    

Version 1 and later. The App Store app ID of the advertised app.

`source-identifier`

    

Version 4 and later. The hierarchical source identifier that replaces the
`campaign-id`. This string represents two, three, or four digits of the
original value the ad network supplies in
`SKStoreProductParameterAdNetworkSourceIdentifier` or `sourceIdentifier`.

`campaign-id`

    

Versions 1–3. The campaign identifer you provide when displaying the ad, which
matches `SKStoreProductParameterAdNetworkCampaignIdentifier` or
`adCampaignIdentifier`. Version 4 and later ads use `source-identifer`
instead.

`source-app-id`

    

Version 2 and later. The App Store app ID of the app that displays the ad. The
`source-app-id` value matches
`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier` or
`sourceAppStoreItemIdentifier`.

Note: The `source-app-id` only appears in the postback if providing the
parameter meets Apple’s privacy threshold.

`source-domain`

    

Version 4 and later, for web ads only. For more information, see SKAdNetwork
for Web Ads.

`conversion-value`

    

Version 2 and later. An unsigned 6-bit value that the installed app sets by
calling a method to update the conversion value, such as
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`.
The `conversion-value` only appears in the postback if the installed app
provides it, and if providing the parameter meets Apple’s privacy threshold.

Note: The signature doesn’t include the `conversion-value`. Postbacks may
contain either `conversion-value` or `coarse-conversion-value`, not both.

`coarse-conversion-value`

    

Version 4 and later. Possible values are the strings `"low"`, `"medium"`, and
`"high"`. The installed app sets this value by calling a method to update
conversion values, such as
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`.

Note: The signature doesn’t include the `coarse-conversion-value`. Postbacks
may contain either `conversion-value` or `coarse-conversion-value`, not both.

`did-win`

    

Version 3 and later. A Boolean value that’s `true` if the ad network wins the
attribution, and `false` if the postback represents a qualifying ad impression
that doesn't win the attribution.

`fidelity-type`

    

Version 2.2 and later. A value of `0` indicates a view-through ad
presentation; a value of `1` indicates a StoreKit-rendered ad or an
SKAdNetwork-attributed web ad.

`postback-sequence-index`

    

Version 4 and later. The possible integer values of `0`, `1`, and `2` signify
the order of postbacks that result from the three conversion windows. For more
information, see Receiving postbacks in multiple conversion windows.

`redownload`

    

Version 2 and later. A Boolean value of `true` indicates that a device with
the customer’s Apple ID previously installed the app.

`transaction-id`

    

Version 1 and later. A unique value for this validation; use it to deduplicate
install-validation postbacks.

To ensure crowd anonymity, Apple assigns a postback data tier to app
downloads. The postback data tier determines whether certain parameters appear
in the postback, as well as the number of digits in the hierarchical source
identifer. The following postback parameters are subject to the postback data
tier:

  * `source-identifier` (affects the number of digits the postback returns)

  * `coarse-conversion-value`

  * `conversion-value`

  * `source-app-id`

  * `source-domain`

For more information about receiving postbacks, see Receiving postbacks in
multiple conversion windows.

## See Also

### Verifying postbacks

Verifying an install-validation postback

Ensure the validity of a postback you receive after an ad conversion by
verifying its cryptographic signature.

Article

# Testing ad attributions with a downloaded profile

Reduce the time-window for ad attributions and inspect postbacks using a proxy
during testing.

## Overview

You can reduce the time window for receiving ad attribution postbacks by
installing an SKAdNetwork testing profile on your test device.

Important

To download the latest profile, see the AdAttributionKit article on Testing ad
attributions with a downloaded profile. This profile is compatible with both
AdAttributionKit and SKAdNetwork.

For information about installing profiles, see Install a configuration profile
on your iPhone or iPad. You can install this profile on devices running iOS or
iPadOS 14 or later.

With this profile, the installed app has five minutes to update the conversion
value after initially registering. The device sends the postback within
another five minutes after the rolling five-minute timer for conversion
updates expires. Using this profile reduces the conversion value update and
postback window from 24–48 hours to 5–10 minutes.

This testing profile expires two weeks after you install it on the device. To
continue testing, download the latest profile and reinstall it.

### Log in with an Apple ID to test ad attributions

To test ad attributions, you must log in to the device with a production Apple
ID. SKAdNetwork doesn’t support Sandbox Apple IDs.

### Inspect postbacks using an HTTP proxy

On devices running iOS 14.7 and later with this profile installed, the system
can send SKAdNetwork postbacks through an HTTP proxy that you configure. By
using an HTTP proxy, you can monitor the HTTP traffic between your device and
the network, including SKAdNetwork postbacks.

To configure the HTTP proxy, do the following on a testing device:

  1. Go to Settings > Wi-Fi and select the Wi-Fi network you're connected to. 

  2. Under the HTTP Proxy heading, select Configure Proxy.

  3. Select Manual to configure the Server, Port, and Authentication settings for your proxy, or select Automatic to provide a URL for your proxy.

  4. Tap Save.

With the profile installed, the SKAdNetwork postbacks that the device sends
now go through the proxy you configured.

## See Also

### Testing ad attributions and postbacks

Testing and validating ad impression signatures and postbacks for SKAdNetwork

Validate your ad impressions and test your postbacks by creating unit tests
using the StoreKit Test framework.

Type Method

# registerAppForAdNetworkAttribution()

Verifies the first launch of an app installed as a result of an ad.

iOS 11.3–15.4  Deprecated  iPadOS 11.3–15.4  Deprecated  Mac Catalyst
13.1–15.4  Deprecated

    
    
    class func registerAppForAdNetworkAttribution()

Deprecated

Use
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
instead.

## Discussion

Apps that an ad network campaign advertise call this method or
`updateConversionValue(_:)` when the app first launches. Both methods generate
an install notification, which is the cryptographically signed data that
validates that a user installed and launched this app as a result of an ad.

In iOS 15.4 and earlier, the first call to
`registerAppForAdNetworkAttribution()` generates the notification if the
device has attribution data for that app, and starts a 24-hour timer.
Subsequent calls to this method have no effect, unless the ad already has a
conversion value set, in which case calling
`registerAppForAdNetworkAttribution()` resets the conversion value to `0`. You
may, however, call `updateConversionValue(_:)` to provide an updated
conversion value and restart the timer.

The device sends one or more install notifications to ad network postback URLs
within 0-24 hours after the timer expires. For more information about
attribution-winning and non-winning postbacks, see Receiving ad attributions
and postbacks.

Ad networks must verify the postback after receiving it. For more information,
see Verifying an install-validation postback.

## See Also

### Deprecated

`class func updateConversionValue(Int)`

Updates the conversion value and verifies the first launch of an app installed
as a result of an ad.

Deprecated

Type Method

# updateConversionValue(_:)

Updates the conversion value and verifies the first launch of an app installed
as a result of an ad.

iOS 14.0–15.4  Deprecated  iPadOS 14.0–15.4  Deprecated  Mac Catalyst
14.0–15.4  Deprecated

    
    
    class func updateConversionValue(_ conversionValue: Int)

Deprecated

Use
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
instead.

##  Parameters

`conversionValue`

    

An unsigned 6-bit value (`>=0` and `<=63`). The app or the ad network
determines the meaning of the value. The default value is `0`.

## Discussion

Apps that ad networks advertise call `updateConversionValue(_:)` or
`registerAppForAdNetworkAttribution()` when the app first launches, to
register the attribution.

Important

Provide a valid conversion value within the range of `>=0` and `<=63` when
calling `updateConversionValue(_:)` to register the attribution. Invalid
conversion values cause the method to fail, and the conversion to fail to
register.

Apps may call `updateConversionValue(_:)` again within a rolling 24-hour
period to update the conversion value. Calling this method serves two
purposes:

  * It registers the attribution by generating an install notification — the cryptographically signed data that confirms that a user installed and launched this app as a result of an ad.

  * It enables the app to provide and update a conversion value.

Conversion values are a 6-bit value that the ad network or the app defines.
The app decides when to update the value, which it can do any number of times
before a rolling 24-hour timer expires. The 24-hour timer restarts each time
the app calls this method with a valid conversion value greater than the
previous value. When the timer expires, the conversion value is final and
subsequent calls to `updateConversionValue(_:)` have no effect.

The device sends the install notification postback to the ad network’s URL
within 0-24 hours after the timer expires. The postback only contains the
final conversion value if sending the data meets Apple’s privacy threshold.
Only postbacks with an ad attribution can contain a conversion value; non-
winning postbacks don't include a conversion value. For more information, see
Receiving ad attributions and postbacks.

Ad networks must verify the postback after receiving it. See Verifying an
install-validation postback for more information.

## See Also

### Deprecated

`class func registerAppForAdNetworkAttribution()`

Verifies the first launch of an app installed as a result of an ad.

Deprecated

