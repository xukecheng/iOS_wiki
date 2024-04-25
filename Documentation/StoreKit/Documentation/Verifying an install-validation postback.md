Article

# Combining parameters for SKAdNetwork 3 postbacks

Recreate the byte array for version 3 postbacks that win and don’t win
attribution.

## Overview

Check your postback’s version, and use the version-specific instructions to
combine the parameters to validate the postback. The order of the parameters
depends on the version of the postback you receive.

To verify the signature, combine the postback parameter values in this order
for a version 3 postback:

  * `version`

  * `ad-network-id`

  * `campaign-id `

  * `app-id `

  * `transaction-id `

  * `redownload` (Use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.)

  * `source-app-id`

  * `fidelity-type`

  * `did-win`

Include `source-app-id` only if you receive it in the postback. Note that the
signature doesn’t include a conversion value, even if it’s present in the
postback. Postbacks that win the attribution have a `did-win` value of `true`.
Postbacks that don't win the attribution have a `did-win` value of `false`,
and don’t include `source-app-id`.

The following example of the UTF-8 string includes `source-app-id:`

The following example of the UTF-8 string doesn’t include `source-app-id:`

### Receive the winning postback with attribution

The following JSON example shows a version 3 install-validation postback the
device sends to an ad network that wins the attribution. This example contains
all possible parameters and a valid signature:

### Receive a nonwinning postback, without attribution

In iOS 14.6 and later, ad networks that sign ads with version 3 may receive a
postback for their qualifying ad impression that don't win the attribution.
Such postbacks have a `did-win` value of `false`, and don’t include `source-
app-id` or `conversion-value`.

The following example shows a version 3 postback for an ad that doesn't win
the attribution. This example contains all the parameters the system includes
in a nonwinning postback:

Up to five ad networks may receive a nonwinning postback. A single ad network
can receive at most one postback per advertised app, per conversion. For
example, if the device registers three qualifying ad impressions from your ad
network, you receive only one postback.

If your ad network wins the attribution, you only receive the winning
postback, even if the device registers other qualifying impressions for your
ad.

For more information about ad impressions qualifying for attribution, and
receiving winning or nonwinning postbacks, see Receiving ad attributions and
postbacks.

## See Also

### SKAdNetworks 3 and earlier postbacks

Combining parameters for previous SKAdNetwork postback versions

Recreate the byte array for versions 2.2 or earlier.

Article

# Combining parameters for previous SKAdNetwork postback versions

Recreate the byte array for versions 2.2 or earlier.

## Overview

Combine postback parameters to recreate a byte array that you use to verify
Apple’s signature. To recreate the byte array, create a UTF-8 string by
combining the parameter values in an exact order, with an invisible separator
(`‘\u2063’`) between them. You must combine the parameters in the exact orders
as show in the examples. For more information about the parameters and
verifying the signature, and an example using newer versions, see Verifying an
install-validation postback.

### Combine postback parameters for version 2.2

The following JSON shows an example of a version 2.2 install-validation
postback that contains all possible parameters and a valid signature:

To verify the signature, combine version 2.2 postback parameters in this
order:

  * `version`

  * `ad-network-id`

  * `campaign-id `

  * `app-id `

  * `transaction-id `

  * `redownload` Note: use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.

  * `source-app-id`

  * `fidelity-type`

Include `source-app-id` only if you received it in the postback. Note that the
signature never includes a conversion value, even if it’s present in the
postback.

The following is an example of the UTF-8 string for a postback with `source-
app-id `present in the postback:

The following is an example of the UTF-8 string for a postback without
`source-app-id`:

### Combine postback parameters for versions 2 and 2.1

Version 2 and 2.1 postbacks contain the following parameters. Combine their
values in this order:

  * `version`

  * `ad-network-id`

  * `campaign-id `

  * `app-id `

  * `transaction-id `

  * `redownload` Note: use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.

  * `source-app-id`

Include `source-app-id` only if you receive it in the postback. Note that the
signature never includes a conversion value, even if it’s present in the
postback.

The following is an example of the UTF-8 string for a postback with `source-
app-id `present in the postback:

The following is an example of the UTF-8 string for a postback without
`source-app-id`:

### Combine postback parameters for version 1

Version 1 postbacks contain the following parameters. Combine their values in
this order:

  * `ad-network-id`

  * `campaign-id`

  * `app-id`

  * `transaction-id`

The following is an example of the UTF-8 string for a version 1.0 postback:

## See Also

### SKAdNetworks 3 and earlier postbacks

Combining parameters for SKAdNetwork 3 postbacks

Recreate the byte array for version 3 postbacks that win and don’t win
attribution.

