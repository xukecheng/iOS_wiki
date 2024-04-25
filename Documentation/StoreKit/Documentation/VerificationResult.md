Enumeration Case

# VerificationResult.verified(_:)

The associated value passed StoreKit automatic verification checks.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case verified(SignedType)

## Discussion

The associated value in this case is the App Store-signed value.

## See Also

### Getting the verification results

`case unverified(SignedType,
VerificationResult<SignedType>.VerificationError)`

The associated value failed StoreKit automatic verification checks.

`var payloadValue: SignedType`

The verified value of the signed type that StoreKit confirms as verified.

`var unsafePayloadValue: SignedType`

The associated value of the verification result that StoreKit doesn’t confirm
as verified.

`enum VerificationResult.VerificationError`

Error cases for StoreKit JWS verification.

Enumeration Case

# VerificationResult.unverified(_:_:)

The associated value failed StoreKit automatic verification checks.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case unverified(SignedType, VerificationResult<SignedType>.VerificationError)

## Discussion

The first associated value in this case is the App Store-signed value. The
second associated value provides the reason why the verification failed.

## See Also

### Getting the verification results

`case verified(SignedType)`

The associated value passed StoreKit automatic verification checks.

`var payloadValue: SignedType`

The verified value of the signed type that StoreKit confirms as verified.

`var unsafePayloadValue: SignedType`

The associated value of the verification result that StoreKit doesn’t confirm
as verified.

`enum VerificationResult.VerificationError`

Error cases for StoreKit JWS verification.

Instance Property

# payloadValue

The verified value of the signed type that StoreKit confirms as verified.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var payloadValue: SignedType { get throws }

## Discussion

This property represents the value of a payload in a JSON Web Signature (JWS)
value that passed StoreKit verification.

This property throws an error if the JWS value containing the payload doesn’t
pass StoreKit’s verification and is therefore _unverified_. To access the
payload of an unverified JWS value, get the associated value of the
verification result, or use the `unsafePayloadValue` property.

## See Also

### Getting the verification results

`case verified(SignedType)`

The associated value passed StoreKit automatic verification checks.

`case unverified(SignedType,
VerificationResult<SignedType>.VerificationError)`

The associated value failed StoreKit automatic verification checks.

`var unsafePayloadValue: SignedType`

The associated value of the verification result that StoreKit doesn’t confirm
as verified.

`enum VerificationResult.VerificationError`

Error cases for StoreKit JWS verification.

Instance Property

# unsafePayloadValue

The associated value of the verification result that StoreKit doesn’t confirm
as verified.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var unsafePayloadValue: SignedType { get }

## Discussion

This property represents the value of a payload in a JSON Web Signature (JWS)
value that’s not confirmed to have passed StoreKit verification.

Use the `unsafePayloadValue` for debugging purposes or other situations where
the integrity of the data is unimportant. This property ignores any
verification errors. To get a payload that passed verification, or to check
for verification errors, use the `payloadValue` property instead.

Important

Don’t trust the integrity of the values you receive from the
`unsafePayloadValue` property. This property contains data regardless of the
verification result, and contains data even if StoreKit’s verification fails.

To determine if the JWS value fails verification, perform a verification on
the `jwsRepresentation` property for subscription renewal information, the
`jwsRepresentation` property for transactions, or the `jwsRepresentation`
property for app transactions.

## See Also

### Getting the verification results

`case verified(SignedType)`

The associated value passed StoreKit automatic verification checks.

`case unverified(SignedType,
VerificationResult<SignedType>.VerificationError)`

The associated value failed StoreKit automatic verification checks.

`var payloadValue: SignedType`

The verified value of the signed type that StoreKit confirms as verified.

`enum VerificationResult.VerificationError`

Error cases for StoreKit JWS verification.

Instance Property

# jwsRepresentation

The transaction signed by the App Store, in JWS compact serialization format.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jwsRepresentation: String { get }

Available when `SignedType` is `Transaction`.

## Discussion

Use this value to perform your own JWS verification on your server, or on the
device.

## See Also

### Getting properties for transactions

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# deviceVerification

The device verification value to use to verify whether the transaction belongs
to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var deviceVerification: Data { get }

Available when `SignedType` is `Transaction`.

## Discussion

For more information about using the `deviceVerification` value, see
`deviceVerification`.

This value is identical to the `deviceVerification` value in `Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var deviceVerificationNonce: UUID { get }

Available when `SignedType` is `Transaction`.

## Discussion

Use the lowercased nonce when computing the `deviceVerification` value.

This value is identical to the `deviceVerificationNonce` value in
`Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# signedDate

The date that the App Store signed the JWS transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signedDate: Date { get }

Available when `SignedType` is `Transaction`.

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# headerData

The header component of the JWS transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var headerData: Data { get }

Available when `SignedType` is `Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# payloadData

The payload component of the JWS transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var payloadData: Data { get }

Available when `SignedType` is `Transaction`.

## Discussion

This value is the same as the `jsonRepresentation` in `Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# signedData

The transaction data covered by the signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signedData: Data { get }

Available when `SignedType` is `Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# signatureData

The signature component of the JWS transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signatureData: Data { get }

Available when `SignedType` is `Transaction`.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Transaction`.

Instance Property

# signature

The signature component of the JSON web signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signature: P256.Signing.ECDSASignature { get }

Available when `SignedType` is `Transaction`.

## Discussion

Use this `signature` with Apple CryptoKit if you verify the signature on the
device.

## See Also

### Getting properties for transactions

`var jwsRepresentation: String`

The transaction signed by the App Store, in JWS compact serialization format.

Available when `SignedType` is `Transaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the transaction belongs
to the device.

Available when `SignedType` is `Transaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Transaction`.

`var signedDate: Date`

The date that the App Store signed the JWS transaction.

Available when `SignedType` is `Transaction`.

`var headerData: Data`

The header component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var payloadData: Data`

The payload component of the JWS transaction.

Available when `SignedType` is `Transaction`.

`var signedData: Data`

The transaction data covered by the signature.

Available when `SignedType` is `Transaction`.

`var signatureData: Data`

The signature component of the JWS transaction.

Available when `SignedType` is `Transaction`.

Instance Property

# jwsRepresentation

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jwsRepresentation: String { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

Use this value to perform your own JWS verification on your server, or on the
device.

## See Also

### Getting properties for subscription renewal info

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# deviceVerification

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var deviceVerification: Data { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

For more information about using the device verification value, see
`deviceVerification`.

This value is identical to the `deviceVerification` value in
`Product.SubscriptionInfo.RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var deviceVerificationNonce: UUID { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

Use the lowercased nonce when computing the `deviceVerification` value.

This value is identical to the `deviceVerificationNonce` value in
`Product.SubscriptionInfo.RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# signedDate

The date that the App Store signed the JWS subscription renewal info.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signedDate: Date { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# headerData

The header component of the JWS subscription renewal info.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var headerData: Data { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# payloadData

The payload component of the JWS subscription renewal info.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var payloadData: Data { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

This value is the same as the `jsonRepresentation` in
`Product.SubscriptionInfo.RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# signedData

The subscription renewal info data covered by the signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signedData: Data { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# signatureData

The signature component of the JWS subscription renewal info.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signatureData: Data { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# signature

The signature component of the JSON web signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var signature: P256.Signing.ECDSASignature { get }

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

## Discussion

Use this `signature` with Apple CryptoKit if you verify the signature on the
device.

## See Also

### Getting properties for subscription renewal info

`var jwsRepresentation: String`

The subscription renewal information signed by the App Store, in JWS compact
serialization format.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerification: Data`

The device verification value to use to verify whether the subscription
renewal info belongs to the device.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedDate: Date`

The date that the App Store signed the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var headerData: Data`

The header component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var payloadData: Data`

The payload component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signedData: Data`

The subscription renewal info data covered by the signature.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

`var signatureData: Data`

The signature component of the JWS subscription renewal info.

Available when `SignedType` is `Product``.``SubscriptionInfo``.``RenewalInfo`.

Instance Property

# jwsRepresentation

The app transaction signed by the App Store, in JWS compact serialization
format.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var jwsRepresentation: String { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

Use this value to perform your own JWS verification on your server or on the
device.

## See Also

### Getting properties for app transactions

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# deviceVerification

The device verification value to use to verify whether the app transaction
belongs to the device.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var deviceVerification: Data { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

For more information about using the device verification value, see
`deviceVerification`.

This value is identical to the `deviceVerification` value in `AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var deviceVerificationNonce: UUID { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

Use the lowercased nonce when computing the `deviceVerification` value.

This value is identical to the `deviceVerificationNonce` value in
`AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# signedDate

The date that the App Store signed the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var signedDate: Date { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# headerData

The header component of the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var headerData: Data { get }

Available when `SignedType` is `AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# payloadData

The payload component of the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var payloadData: Data { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

This value is the same as the `jsonRepresentation` in `AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# signedData

The app transaction data covered by the signature.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var signedData: Data { get }

Available when `SignedType` is `AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# signatureData

The signature component of the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var signatureData: Data { get }

Available when `SignedType` is `AppTransaction`.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signature: P256.Signing.ECDSASignature`

The signature component of the JSON web signature.

Available when `SignedType` is `AppTransaction`.

Instance Property

# signature

The signature component of the JSON web signature.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var signature: P256.Signing.ECDSASignature { get }

Available when `SignedType` is `AppTransaction`.

## Discussion

Use this `signature` with Apple CryptoKit if you verify the signature on the
device.

## See Also

### Getting properties for app transactions

`var jwsRepresentation: String`

The app transaction signed by the App Store, in JWS compact serialization
format.

Available when `SignedType` is `AppTransaction`.

`var deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

Available when `SignedType` is `AppTransaction`.

`var deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Available when `SignedType` is `AppTransaction`.

`var signedDate: Date`

The date that the App Store signed the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var headerData: Data`

The header component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var payloadData: Data`

The payload component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

`var signedData: Data`

The app transaction data covered by the signature.

Available when `SignedType` is `AppTransaction`.

`var signatureData: Data`

The signature component of the JWS app transaction.

Available when `SignedType` is `AppTransaction`.

Instance Property

# debugDescription

A description of the verification result that’s suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

Available when `SignedType` conforms to `CustomDebugStringConvertible`.

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: VerificationResult<SignedType>, rhs: VerificationResult<SignedType>) -> Bool

Available when `SignedType` conforms to `Equatable`.

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

### Comparing and hashing verification results

`static func == (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Available when `SignedType` conforms to `Equatable`.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Available when `SignedType` conforms to `Hashable`.

`var hashValue: Int`

The hash value.

Available when `SignedType` conforms to `Hashable`.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: VerificationResult<SignedType>, b: VerificationResult<SignedType>) -> Bool

Available when `SignedType` conforms to `Equatable`.

## See Also

### Comparing and hashing verification results

`static func != (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Available when `SignedType` conforms to `Equatable`.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Available when `SignedType` conforms to `Hashable`.

`var hashValue: Int`

The hash value.

Available when `SignedType` conforms to `Hashable`.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

Available when `SignedType` conforms to `Hashable`.

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing verification results

`static func != (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Available when `SignedType` conforms to `Equatable`.

`static func == (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Available when `SignedType` conforms to `Equatable`.

`var hashValue: Int`

The hash value.

Available when `SignedType` conforms to `Hashable`.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

Available when `SignedType` conforms to `Hashable`.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing verification results

`static func != (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Available when `SignedType` conforms to `Equatable`.

`static func == (VerificationResult<SignedType>,
VerificationResult<SignedType>) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Available when `SignedType` conforms to `Equatable`.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Available when `SignedType` conforms to `Hashable`.

