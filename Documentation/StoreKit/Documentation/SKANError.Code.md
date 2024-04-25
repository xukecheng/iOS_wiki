Enumeration Case

# SKANError.Code.adNetworkIdMissing

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case adNetworkIdMissing = 2

## Discussion

The value you specify for your ad network identifier in your ad impresion must
match the value in the `Info.plist`. ``An app that participates in ad
campaigns by displaying ads must include the ad network identifiers in its
`Info.plist`. For more information, see Configuring a source app.

## See Also

### Error Codes

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionMissingRequiredValue

A required value is missing from a view-through ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionMissingRequiredValue = 0

## Discussion

Check that your instance of `SKAdImpression` provides all of the required
values.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionNotFound

The system can’t find the ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionNotFound = 4

## Discussion

This error may occur if an app calls `endImpression(_:completionHandler:)`
before calling `startImpression(_:completionHandler:)`.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionTooShort

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionTooShort = 11

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidAdvertisedAppId

The App Store ID of the advertised app is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidAdvertisedAppId = 8

## Discussion

Ad networks provide an advertised app identifier when signing an ad
impression. If you’re providing a StoreKit-rendered ad, check that the value
you set for `SKStoreProductParameterITunesItemIdentifier` in
`loadProduct(withParameters:completionBlock:)` is a valid app identifer. If
you’re providing a view-through ad, check the value of
`advertisedAppStoreItemIdentifier`.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidCampaignId

The campaign identifier that you provided is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidCampaignId = 5

## Discussion

Check that the campaign identifier is a valid value. For more information, see
`SKStoreProductParameterAdNetworkCampaignIdentifier` for StoreKit-rendered
ads, and `adCampaignIdentifier` for view-through ads.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidConversionValue

The conversion value is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidConversionValue = 6

## Discussion

Apps provide a conversion value when calling
`updatePostbackConversionValue(_:completionHandler:)` or
`updateConversionValue(_:)`. Check that the conversion value you provide is
within the allowed range.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidSourceAppId

The App Store ID of the app displaying the ad is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidSourceAppId = 7

## Discussion

Check that the value you provide for
`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier` or
`sourceAppStoreItemIdentifier` is correct and matches the App Store ID of the
app that’s displaying the ad.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidVersion

The SKAdNetwork version number is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidVersion = 9

## Discussion

Ad networks provide an SKAdNetwork version number when preparing an ad
impression, in `SKStoreProductParameterAdNetworkVersion` or `version`. Check
that the version number is valid and that you follow the version-specific
instructions to generate a signature. For more information about versions, see
SKAdNetwork release notes.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.mismatchedSourceAppId

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case mismatchedSourceAppId = 3

## Discussion

Check that the `sourceAppStoreItemIdentifier` you provide in the
`SKAdImpression` object matches the app identifier of the app displaying the
ad.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.unknown

An unknown error occurred.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case unknown = 10

## Discussion

If this error appears, continue processing the ad; an ad impression may
succeed despite this error.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.unsupported

Your app attempted to use functionality that isn’t supported in the specified
version.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case unsupported = 1

## Discussion

For information about supported features by version number, see SKAdNetwork
release notes. For example, to provide view-through ads, use SKAdNetwork
version 2.2 or later.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

Enumeration Case

# SKANError.Code.adNetworkIdMissing

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case adNetworkIdMissing = 2

## Discussion

The value you specify for your ad network identifier in your ad impresion must
match the value in the `Info.plist`. ``An app that participates in ad
campaigns by displaying ads must include the ad network identifiers in its
`Info.plist`. For more information, see Configuring a source app.

## See Also

### Error Codes

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionMissingRequiredValue

A required value is missing from a view-through ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionMissingRequiredValue = 0

## Discussion

Check that your instance of `SKAdImpression` provides all of the required
values.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionNotFound

The system can’t find the ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionNotFound = 4

## Discussion

This error may occur if an app calls `endImpression(_:completionHandler:)`
before calling `startImpression(_:completionHandler:)`.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.impressionTooShort

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case impressionTooShort = 11

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidAdvertisedAppId

The App Store ID of the advertised app is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidAdvertisedAppId = 8

## Discussion

Ad networks provide an advertised app identifier when signing an ad
impression. If you’re providing a StoreKit-rendered ad, check that the value
you set for `SKStoreProductParameterITunesItemIdentifier` in
`loadProduct(withParameters:completionBlock:)` is a valid app identifer. If
you’re providing a view-through ad, check the value of
`advertisedAppStoreItemIdentifier`.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidCampaignId

The campaign identifier that you provided is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidCampaignId = 5

## Discussion

Check that the campaign identifier is a valid value. For more information, see
`SKStoreProductParameterAdNetworkCampaignIdentifier` for StoreKit-rendered
ads, and `adCampaignIdentifier` for view-through ads.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidConversionValue

The conversion value is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidConversionValue = 6

## Discussion

Apps provide a conversion value when calling
`updatePostbackConversionValue(_:completionHandler:)` or
`updateConversionValue(_:)`. Check that the conversion value you provide is
within the allowed range.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidSourceAppId

The App Store ID of the app displaying the ad is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidSourceAppId = 7

## Discussion

Check that the value you provide for
`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier` or
`sourceAppStoreItemIdentifier` is correct and matches the App Store ID of the
app that’s displaying the ad.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.invalidVersion

The SKAdNetwork version number is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case invalidVersion = 9

## Discussion

Ad networks provide an SKAdNetwork version number when preparing an ad
impression, in `SKStoreProductParameterAdNetworkVersion` or `version`. Check
that the version number is valid and that you follow the version-specific
instructions to generate a signature. For more information about versions, see
SKAdNetwork release notes.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.mismatchedSourceAppId

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case mismatchedSourceAppId = 3

## Discussion

Check that the `sourceAppStoreItemIdentifier` you provide in the
`SKAdImpression` object matches the app identifier of the app displaying the
ad.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case unknown`

An unknown error occurred.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.unknown

An unknown error occurred.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case unknown = 10

## Discussion

If this error appears, continue processing the ad; an ad impression may
succeed despite this error.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unsupported`

Your app attempted to use functionality that isn’t supported in the specified
version.

Enumeration Case

# SKANError.Code.unsupported

Your app attempted to use functionality that isn’t supported in the specified
version.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    case unsupported = 1

## Discussion

For information about supported features by version number, see SKAdNetwork
release notes. For example, to provide view-through ads, use SKAdNetwork
version 2.2 or later.

## See Also

### Error Codes

`case adNetworkIdMissing`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`case impressionMissingRequiredValue`

A required value is missing from a view-through ad impression.

`case impressionNotFound`

The system can’t find the ad impression.

`case impressionTooShort`

`case invalidAdvertisedAppId`

The App Store ID of the advertised app is invalid.

`case invalidCampaignId`

The campaign identifier that you provided is invalid.

`case invalidConversionValue`

The conversion value is invalid.

`case invalidSourceAppId`

The App Store ID of the app displaying the ad is invalid.

`case invalidVersion`

The SKAdNetwork version number is invalid.

`case mismatchedSourceAppId`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`case unknown`

An unknown error occurred.

