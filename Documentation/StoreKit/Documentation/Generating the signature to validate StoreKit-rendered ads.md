Article

# Combining parameters to generate signatures for SKAdNetwork 2.2 and 3

Generate signatures to sign your ad with versions 2.2 and 3.

## Overview

To generate the signature, combine the required values of Ad network install-
validation keys for version 2, and include a `fidelity-type` value of `1` for
StoreKit-rendered ads.

Important

Lowercase the string representation of the nonce:
`SKStoreProductParameterAdNetworkNonce`. Failing to do so results in an
invalid signature. Only ads with valid signatures can get ad attributions.

For versions 2.2 and 3, combine the values into a UTF-8 string with an
invisible separator (`‘\u2063’`) between them, in the exact order the code
below shows:

## See Also

### Signatures for SKAdNetwork 1, 2, and 2.2–3

Combining parameters to generate a signature for SKAdNetwork 2

Generate signatures to sign your ad with version 2.

Combining parameters to generate a signature for SKAdNetwork 1

Generate signatures for apps compiled with earlier SDKs.

Article

# Combining parameters to generate a signature for SKAdNetwork 2

Generate signatures to sign your ad with version 2.

## Overview

To generate the signature, first combine the values of Ad network install-
validation keys for the version 2.

Important

Lowercase the string representation of the nonce:
`SKStoreProductParameterAdNetworkNonce`. Failing to do so results in an
invalid signature. Only ads with valid signatures can get ad attributions.

Strings for version 2 and earlier don’t include a `fidelity-type` parameter.
For version 2, combine the values into a UTF-8 string with an invisible
separator (`‘\u2063’`) between them, in the exact order shown:

**Listing 1**  Parameter values combined, in order, for version 2.

## See Also

### Signatures for SKAdNetwork 1, 2, and 2.2–3

Combining parameters to generate signatures for SKAdNetwork 2.2 and 3

Generate signatures to sign your ad with versions 2.2 and 3.

Combining parameters to generate a signature for SKAdNetwork 1

Generate signatures for apps compiled with earlier SDKs.

Article

# Combining parameters to generate a signature for SKAdNetwork 1

Generate signatures for apps compiled with earlier SDKs.

## Overview

Generate a signature using the parameters for version 1.0 if you compile your
app with an iOS SDK version from 11.3 through 13.7.

To generate the signature, first combine the values of Ad network install-
validation keys for the version 1.0.

The parameters required for a version 1.0 signature are:

`SKStoreProductParameterAdNetworkIdentifier`

    

Your ad network identifier that you registered with Apple. Shown as `ad-
network-id` in Listing 1.

`SKStoreProductParameterAdNetworkCampaignIdentifier`

    

A campaign number you provide. Shown as `campaign-id` in Listing 1.

`SKStoreProductParameterITunesItemIdentifier`

    

The App Store ID of the product to advertise. Shown as `itunes-item-id` in
Listing 1.

`SKStoreProductParameterAdNetworkNonce`

    

A unique `UUID` value that you provide for each ad impression. You must
lowercase the string representation of the nonce in the signature. Shown as
`nonce` in Listing 1.

`SKStoreProductParameterAdNetworkTimestamp`

    

A timestamp you generate near the time of the ad impression. Shown as
`timestamp` in Listing 1.

### Combine the parameters for version 1.0

Create the UTF-8 string for version 1.0 if you compile your app with an SDK
prior to iOS 14.

Important

You must use lowercase for the string representation of the nonce:
`SKStoreProductParameterAdNetworkNonce`.

Combine the values into a UTF-8 string with an invisible separator
(`‘\u2063’`) between them, in the exact order shown:

**Listing 1**  Parameter values combined, in order, for version 1.0.

Next, follow the instructions to sign the combined string, encode the
signature, and use the generated signature string as described in Generating
the signature to validate StoreKit-rendered ads.

## See Also

### Signatures for SKAdNetwork 1, 2, and 2.2–3

Combining parameters to generate signatures for SKAdNetwork 2.2 and 3

Generate signatures to sign your ad with versions 2.2 and 3.

Combining parameters to generate a signature for SKAdNetwork 2

Generate signatures to sign your ad with version 2.

