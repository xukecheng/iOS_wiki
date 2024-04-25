Type Property

# errorDomain

A string containing the error domain for SKAdNetwork errors.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var errorDomain: String { get }

Instance Property

# code

The error code.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var code: Code { get }

## See Also

### Getting Error Properties

`var errorCode: Int`

The integer error code.

`var userInfo: [String : Any]`

The user information dictionary associated with the error.

`var errorUserInfo: [String : Any]`

The error user information dictionary associated with the error.

`var localizedDescription: String`

A string containing the localized description of the error.

Instance Property

# errorCode

The integer error code.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var errorCode: Int { get }

## See Also

### Getting Error Properties

`var code: Code`

The error code.

`var userInfo: [String : Any]`

The user information dictionary associated with the error.

`var errorUserInfo: [String : Any]`

The error user information dictionary associated with the error.

`var localizedDescription: String`

A string containing the localized description of the error.

Instance Property

# userInfo

The user information dictionary associated with the error.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var userInfo: [String : Any] { get }

## See Also

### Getting Error Properties

`var code: Code`

The error code.

`var errorCode: Int`

The integer error code.

`var errorUserInfo: [String : Any]`

The error user information dictionary associated with the error.

`var localizedDescription: String`

A string containing the localized description of the error.

Instance Property

# errorUserInfo

The error user information dictionary associated with the error.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var errorUserInfo: [String : Any] { get }

## See Also

### Getting Error Properties

`var code: Code`

The error code.

`var errorCode: Int`

The integer error code.

`var userInfo: [String : Any]`

The user information dictionary associated with the error.

`var localizedDescription: String`

A string containing the localized description of the error.

Instance Property

# localizedDescription

A string containing the localized description of the error.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

## See Also

### Getting Error Properties

`var code: Code`

The error code.

`var errorCode: Int`

The integer error code.

`var userInfo: [String : Any]`

The user information dictionary associated with the error.

`var errorUserInfo: [String : Any]`

The error user information dictionary associated with the error.

Type Property

# adNetworkIdMissing

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var adNetworkIdMissing: SKANError.Code { get }

## Discussion

The value you specify for your ad network identifier in your ad impresion must
match the value in the `Info.plist`. ``An app that participates in ad
campaigns by displaying ads must include the ad network identifiers in its
`Info.plist`. For more information, see Configuring a source app.

## See Also

### Getting Error Codes

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# impressionMissingRequiredValue

A required value is missing from a view-through ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var impressionMissingRequiredValue: SKANError.Code { get }

## Discussion

Check that your instance of `SKAdImpression` provides all of the required
values.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# impressionNotFound

The system can’t find the ad impression.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var impressionNotFound: SKANError.Code { get }

## Discussion

This error may occur if an app calls `endImpression(_:completionHandler:)`
before calling `startImpression(_:completionHandler:)`.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# impressionTooShort

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var impressionTooShort: SKANError.Code { get }

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# invalidAdvertisedAppId

The App Store ID of the advertised app is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var invalidAdvertisedAppId: SKANError.Code { get }

## Discussion

Ad networks provide an advertised app identifier when signing an ad
impression. If you’re providing a StoreKit-rendered ad, check that the value
you set for `SKStoreProductParameterITunesItemIdentifier` in
`loadProduct(withParameters:completionBlock:)` is a valid app identifer. If
you’re providing a view-through ad, check the value of
`advertisedAppStoreItemIdentifier`.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# invalidCampaignId

The campaign identifier that you provided is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var invalidCampaignId: SKANError.Code { get }

## Discussion

Check that the campaign identifier is a valid value. For more information, see
`SKStoreProductParameterAdNetworkCampaignIdentifier` for StoreKit-rendered
ads, and `adCampaignIdentifier` for view-through ads.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# invalidConversionValue

The conversion value is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var invalidConversionValue: SKANError.Code { get }

## Discussion

Apps provide a conversion value when calling
`updatePostbackConversionValue(_:completionHandler:)` or
`updateConversionValue(_:)`. Check that the conversion value you provide is
within the allowed range.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# invalidSourceAppId

The App Store ID of the app displaying the ad is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var invalidSourceAppId: SKANError.Code { get }

## Discussion

Check that the value you provide for
`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier` or
`sourceAppStoreItemIdentifier` is correct and matches the App Store ID of the
app that’s displaying the ad.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# invalidVersion

The SKAdNetwork version number is invalid.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var invalidVersion: SKANError.Code { get }

## Discussion

Ad networks provide an SKAdNetwork version number when preparing an ad
impression, in `SKStoreProductParameterAdNetworkVersion` or `version`. Check
that the version number is valid and that you follow the version-specific
instructions to generate a signature. For more information about versions, see
SKAdNetwork release notes.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# mismatchedSourceAppId

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var mismatchedSourceAppId: SKANError.Code { get }

## Discussion

Check that the `sourceAppStoreItemIdentifier` you provide in the
`SKAdImpression` object matches the app identifier of the app displaying the
ad.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var unknown: SKANError.Code`

An unknown error occurred.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# unknown

An unknown error occurred.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var unknown: SKANError.Code { get }

## Discussion

If this error appears, continue processing the ad; an ad impression may
succeed despite this error.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unsupported: SKANError.Code`

Your app attempted to use functionality that isn’t supported in the specified
version.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Type Property

# unsupported

Your app attempted to use functionality that isn’t supported in the specified
version.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static var unsupported: SKANError.Code { get }

## Discussion

For information about supported features by version number, see SKAdNetwork
release notes. For example, to provide view-through ads, use SKAdNetwork
version 2.2 or later.

## See Also

### Getting Error Codes

`static var adNetworkIdMissing: SKANError.Code`

The ad network identifier in the ad impression doesn’t match the value in the
information property list.

`static var impressionMissingRequiredValue: SKANError.Code`

A required value is missing from a view-through ad impression.

`static var impressionNotFound: SKANError.Code`

The system can’t find the ad impression.

`static var impressionTooShort: SKANError.Code`

`static var invalidAdvertisedAppId: SKANError.Code`

The App Store ID of the advertised app is invalid.

`static var invalidCampaignId: SKANError.Code`

The campaign identifier that you provided is invalid.

`static var invalidConversionValue: SKANError.Code`

The conversion value is invalid.

`static var invalidSourceAppId: SKANError.Code`

The App Store ID of the app displaying the ad is invalid.

`static var invalidVersion: SKANError.Code`

The SKAdNetwork version number is invalid.

`static var mismatchedSourceAppId: SKANError.Code`

The source app identifier in the ad impression doesn’t match the app
identifier in the source app.

`static var unknown: SKANError.Code`

An unknown error occurred.

`enum SKANError.Code`

Constants that indicate the type of error for an ad network attribution
operation.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.4+  iPadOS 15.4+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static func != (lhs: SKANError, rhs: SKANError) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and Hashing Errors

`static func == (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    static func == (lhs: SKANError, rhs: SKANError) -> Bool

## See Also

### Comparing and Hashing Errors

`static func != (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and Hashing Errors

`static func != (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and Hashing Errors

`static func != (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (SKANError, SKANError) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Initializer

# init(_:userInfo:)

Initializes an error structure with a code and custom data.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 13.3+

    
    
    init(
        _ code: Code,
        userInfo: [String : Any] = [:]
    )

##  Parameters

`code`

    

The error code.

`userInfo`

    

The dictionary of additional information to pass with the error.

