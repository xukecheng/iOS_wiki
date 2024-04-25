Article

# SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

## Overview

Use `“4.0”` as the version number when signing ads for this version.

You’re eligible to receive a version 4 postback if all participants meet the
following conditions:

  * The ad network generates an ad signature for version 4.

  * For ads that appear in an app, the app is built with iOS 16.1 SDK or later. For web ads, the ad appears in Safari 16.1 or later. 

  * The advertised app is App Store-signed and is running on a device with iOS 16.1 or later. 

Advertised apps built with iOS 16.1 SDK or later can register up to three
conversions that result in postbacks for the winning ad impression. Apps built
with earlier SDKs can register only one conversion, resulting in one winning
postback.

### New features

  * **Multiple postbacks.** SKAdNetwork now supports multiple conversions in three conversion windows. When you call the new methods `updatePostbackConversionValue(_:coarseValue:completionHandler:)` and `updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`, the app can update conversion values in three separate conversion windows. The app may send up to three postbacks for the winning ad attribution. 

You can lock a conversion during a conversion window to receive the postback
sooner by calling
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
and setting the lock to `true`. Otherwise, the system sends postbacks after
the conversion window closes. For more information about postback timing, see
Receiving ad attributions and postbacks. For more information about multiple
postbacks, see Receiving postbacks in multiple conversion windows.

  * **Coarse conversion values.** The conversion value that you send can include both a fine-grained value and a coarse-grained value. For information about coarse conversion values, see `SKAdNetwork.CoarseConversionValue`. You provide the fine and coarse conversion values in the new methods `updatePostbackConversionValue(_:coarseValue:completionHandler:)` and `updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`.

  * **Hierarchical source identifiers.** Ad networks can now provide hierarchical source identifiers when they sign an ad, which replaces and expands on campaign identifiers. The source identifer is a four-digit integer, which you indicate in `sourceIdentifier` for view-through ads and in `SKStoreProductParameterAdNetworkSourceIdentifier` for StoreKit-rendered ads. Winning postbacks contain two, three, or four digits of the source identifier, depending on the ad impression’s privacy threshold tier. 

  * **Attributed ads on the web.** SKAdNetwork for Web Ads supports attributed ads that you initiate on Safari web pages.

## See Also

### SKAdNetwork versions

SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

Article

# SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

## Overview

Use `“3.0”` as the version number when signing ads for this version.

You’re eligible to receive a version 3.0 postback if all three of the
following conditions are met:

  * The source app generates a signature for version 3.0.

  * The source app is built with iOS 14.6 SDK or later.

  * The advertised app is App Store-signed and is running on a device with iOS 14.6 or later.

### New features

New features include:

  * Devices can now send install-validation postbacks to multiple ad networks that sign their ads using version 3.0. One ad network receives a postback with a `did-win` parameter value of `true` for the ad impression that wins the ad attribution. Up to five other ad networks receive a postback with a `did-win` parameter value of `false` if their ad impressions qualified for, but didn’t win, the attribution.

For more information about signing ads with version 3.0, see Signing and
providing ads. For more information about your ad’s eligibility to receive an
attribution or a non-winning postback, see Receiving ad attributions and
postbacks. For details about the postback, see Verifying an install-validation
postback.

## See Also

### SKAdNetwork versions

SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

Article

# SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

## Overview

Use `“2.2”` as the version number when signing ads for this version.

Ad networks are eligible to receive a version 2.2 postback if all three of the
following conditions are met:

  * The source app generates a signature for version 2.2.

  * The source app is built with iOS 14.5 SDK or later.

  * The advertised app is App Store-signed and running on a device with iOS 14.5 or later.

### New features

New features include:

  * You can now create view-through ads using the new APIs `SKAdImpression` , `startImpression(_:completionHandler:)`, and `endImpression(_:completionHandler:)`. 

  * You can now indicate whether an ad is a view-through ad or a StoreKit-rendered ad by using the new `fidelity-type` parameter. The `fidelity-type` value is `0` for view-through ads, and `1` for StoreKit-rendered ads. You include this parameter when you sign an ad, and receive it in the postback.

For more information about view-through ads and` fidelity-type`, see Signing
and providing ads and Generating the signature to validate view-through ads.
For more information about the postback, see Verifying an install-validation
postback.

## See Also

### SKAdNetwork versions

SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

Article

# SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

## Overview

Use `“2.1”` as the version number when signing ads for this version.

Ad networks are eligible to receive a version 2.1 postback if all three of the
following conditions are met:

  * The source app generates a signature for version 2.1.

  * The source app is built with the iOS 14 SDK or later.

  * The advertised app is App Store-signed and running on a device with iOS 14 or later.

### New features

New features include:

  * SKAdNetwork now signs install-validation postbacks using Apple’s NIST P-256 public key. For more information, see Verifying an install-validation postback.

## See Also

### SKAdNetwork versions

SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

Article

# SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

## Overview

Use `“2.0”` as the version number when signing ads for this version.

Ad networks are eligible to receive a version 2.0 postback if all three of the
following conditions are met:

  * The source app generates a signature for version 2.0.

  * The source app is built with the iOS 14 SDK or later.

  * The advertised app is App Store-signed and running on a device with iOS 14 or later.

When verifying an install-validation postback for version 2.0, use the
following Apple P-192 public key:

    
    
    MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEMyHD625uvsmGq4C43cQ9BnfN2xslVT5V1nOmAMP6qaRRUll3PB1JYmgSm+62sosG
    

For more information, see Verifying an install-validation postback.

### New features

New features include:

  * The advertised app can now provide conversion values. For more information, see `updateConversionValue(_:)`.

  * The install-validation postback now contains additional parameters, including the version number, conversion value, source app ID, and redownload value. For more information, see Verifying an install-validation postback.

## See Also

### SKAdNetwork versions

SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

Article

# SKAdNetwork 1 release notes

A version of SKAdNetwork available in iOS 11.3 and later.

## Overview

You’re eligible to receive a version 1.0 postback when any of these conditions
are met:

  * The source app uses iOS 13.7 SDK or earlier.

  * The advertised app is App Store-signed and running on a device with iOS 14 or earlier.

The original install-validation postback doesn’t include a version number. For
more information, see Combining parameters for previous SKAdNetwork postback
versions.

When verifying an install-validation postback for version 1.0, use the
following Apple P-192 public key:

    
    
    MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEMyHD625uvsmGq4C43cQ9BnfN2xslVT5V1nOmAMP6qaRRUll3PB1JYmgSm+62sosG
    

For more information, see Verifying an install-validation postback.

### New features

This is the original version of SKAdNetwork.

## See Also

### SKAdNetwork versions

SKAdNetwork 4 release notes

A version of SKAdNetwork available in iOS 16.1 and later.

SKAdNetwork 3 release notes

A version of SKAdNetwork available in iOS 14.6 and later.

SKAdNetwork 2.2 release notes

A version of SKAdNetwork available in iOS 14.5 and later.

SKAdNetwork 2.1 release notes

A version of SKAdNetwork available in iOS 14 and later.

SKAdNetwork 2 release notes

A version of SKAdNetwork available in iOS 14 and later.

