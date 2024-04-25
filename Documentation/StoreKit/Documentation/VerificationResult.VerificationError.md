Instance Property

# localizedDescription

A string containing the localized description of the error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var localizedDescription: String { get }

## See Also

### Error Description

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# errorDescription

A description of the error, suitable for debugging.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var errorDescription: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# failureReason

A localized message describing the reason for the failure.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var failureReason: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# helpAnchor

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.4+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var helpAnchor: String? { get }

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# recoverySuggestion

A message containing a suggestion for recovering from the error.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var recoverySuggestion: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

Enumeration Case

# VerificationResult.VerificationError.invalidCertificateChain

An error indicating that the certificate chain is invalid.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidCertificateChain

## Discussion

This error may occur if one or more certificates in the certiificate chain are
expired or from an untrusted source.

## See Also

### Error Codes

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidDeviceVerification

An error that indicates the signed value wasn’t generated for the current
device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidDeviceVerification

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidEncoding

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidEncoding

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidSignature

An error that indicates that the signature didn’t match the header and
payload.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidSignature

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.missingRequiredProperties

An error that indicates the header or payload are missing information that’s
required to verify the signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case missingRequiredProperties

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.revokedCertificate

An error that indicates the certificate chain includes a revoked certificate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case revokedCertificate

## Discussion

In some cases, this error may resolve if you try again later.

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: VerificationResult<SignedType>.VerificationError, rhs: VerificationResult<SignedType>.VerificationError) -> Bool

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

### Error Comparisons

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: VerificationResult<SignedType>.VerificationError, b: VerificationResult<SignedType>.VerificationError) -> Bool

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# localizedDescription

A string containing the localized description of the error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var localizedDescription: String { get }

## See Also

### Error Description

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# errorDescription

A description of the error, suitable for debugging.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var errorDescription: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# failureReason

A localized message describing the reason for the failure.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var failureReason: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# helpAnchor

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.4+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var helpAnchor: String? { get }

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# recoverySuggestion

A message containing a suggestion for recovering from the error.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var recoverySuggestion: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Description

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

Enumeration Case

# VerificationResult.VerificationError.invalidCertificateChain

An error indicating that the certificate chain is invalid.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidCertificateChain

## Discussion

This error may occur if one or more certificates in the certiificate chain are
expired or from an untrusted source.

## See Also

### Error Codes

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidDeviceVerification

An error that indicates the signed value wasn’t generated for the current
device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidDeviceVerification

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidEncoding

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidEncoding

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.invalidSignature

An error that indicates that the signature didn’t match the header and
payload.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case invalidSignature

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.missingRequiredProperties

An error that indicates the header or payload are missing information that’s
required to verify the signature.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case missingRequiredProperties

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case revokedCertificate`

An error that indicates the certificate chain includes a revoked certificate.

Enumeration Case

# VerificationResult.VerificationError.revokedCertificate

An error that indicates the certificate chain includes a revoked certificate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case revokedCertificate

## Discussion

In some cases, this error may resolve if you try again later.

## See Also

### Error Codes

`case invalidCertificateChain`

An error indicating that the certificate chain is invalid.

`case invalidDeviceVerification`

An error that indicates the signed value wasn’t generated for the current
device.

`case invalidEncoding`

An error that indicates the signature, certificate chain, or other part of
value uses invalid encoding.

`case invalidSignature`

An error that indicates that the signature didn’t match the header and
payload.

`case missingRequiredProperties`

An error that indicates the header or payload are missing information that’s
required to verify the signature.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: VerificationResult<SignedType>.VerificationError, rhs: VerificationResult<SignedType>.VerificationError) -> Bool

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

### Error Comparisons

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: VerificationResult<SignedType>.VerificationError, b: VerificationResult<SignedType>.VerificationError) -> Bool

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (VerificationResult<SignedType>.VerificationError,
VerificationResult<SignedType>.VerificationError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

