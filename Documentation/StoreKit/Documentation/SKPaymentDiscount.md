Initializer

# init(identifier:keyIdentifier:nonce:signature:timestamp:)

Initializes the payment discount with a signature and the parameters used by
the signature.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    init(
        identifier: String,
        keyIdentifier: String,
        nonce: UUID,
        signature: String,
        timestamp: NSNumber
    )

Instance Property

# identifier

A string used to uniquely identify a discount offer for a product.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var identifier: String { get }

## Discussion

You set up offers and their identifiers in App Store Connect. If the
`identifier` is not valid, an `SKError.Code.invalidOfferIdentifier` error can
result.

## See Also

### Identifying the Discount

`var keyIdentifier: String`

A string that identifies the key used to generate the signature.

Instance Property

# keyIdentifier

A string that identifies the key used to generate the signature.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var keyIdentifier: String { get }

## Discussion

You generate and download keys from App Store Connect. See the “KEY ID” column
in App Store Connect to use as the `keyIdentifier`.

## See Also

### Identifying the Discount

`var identifier: String`

A string used to uniquely identify a discount offer for a product.

Instance Property

# nonce

A universally unique ID (UUID) value that you define.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var nonce: UUID { get }

## Discussion

Your server generates a unique `nonce` when it creates the `signature` string
for the payment discount. The string representation of the `nonce` must be
lowercase.

You can use a `nonce` one time; generate a new one for every buy request.

## See Also

### Validating the Discount

`var signature: String`

A string representing the properties of a specific promotional offer,
cryptographically signed.

`var timestamp: NSNumber`

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

Instance Property

# signature

A string representing the properties of a specific promotional offer,
cryptographically signed.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var signature: String { get }

## Discussion

The `signature` is a string signed with your private key that represents the
properties of a specific promotional offer. To keep your private key secure,
generate the `signature` on a server.

Generate the `signature` using the Elliptic Curve Digital Signature Algorithm
(ECDSA) with SHA 256. For more information, see Generating a signature for
promotional offers.

## See Also

### Validating the Discount

`var nonce: UUID`

A universally unique ID (UUID) value that you define.

`var timestamp: NSNumber`

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

Instance Property

# timestamp

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    @NSCopying
    var timestamp: NSNumber { get }

## Discussion

The `timestamp` keeps the payment discount active for 24 hours.

## See Also

### Validating the Discount

`var nonce: UUID`

A universally unique ID (UUID) value that you define.

`var signature: String`

A string representing the properties of a specific promotional offer,
cryptographically signed.

Initializer

# init(identifier:keyIdentifier:nonce:signature:timestamp:)

Initializes the payment discount with a signature and the parameters used by
the signature.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    init(
        identifier: String,
        keyIdentifier: String,
        nonce: UUID,
        signature: String,
        timestamp: NSNumber
    )

Instance Property

# identifier

A string used to uniquely identify a discount offer for a product.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var identifier: String { get }

## Discussion

You set up offers and their identifiers in App Store Connect. If the
`identifier` is not valid, an `SKError.Code.invalidOfferIdentifier` error can
result.

## See Also

### Identifying the Discount

`var keyIdentifier: String`

A string that identifies the key used to generate the signature.

Instance Property

# keyIdentifier

A string that identifies the key used to generate the signature.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var keyIdentifier: String { get }

## Discussion

You generate and download keys from App Store Connect. See the “KEY ID” column
in App Store Connect to use as the `keyIdentifier`.

## See Also

### Identifying the Discount

`var identifier: String`

A string used to uniquely identify a discount offer for a product.

Instance Property

# nonce

A universally unique ID (UUID) value that you define.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var nonce: UUID { get }

## Discussion

Your server generates a unique `nonce` when it creates the `signature` string
for the payment discount. The string representation of the `nonce` must be
lowercase.

You can use a `nonce` one time; generate a new one for every buy request.

## See Also

### Validating the Discount

`var signature: String`

A string representing the properties of a specific promotional offer,
cryptographically signed.

`var timestamp: NSNumber`

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

Instance Property

# signature

A string representing the properties of a specific promotional offer,
cryptographically signed.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var signature: String { get }

## Discussion

The `signature` is a string signed with your private key that represents the
properties of a specific promotional offer. To keep your private key secure,
generate the `signature` on a server.

Generate the `signature` using the Elliptic Curve Digital Signature Algorithm
(ECDSA) with SHA 256. For more information, see Generating a signature for
promotional offers.

## See Also

### Validating the Discount

`var nonce: UUID`

A universally unique ID (UUID) value that you define.

`var timestamp: NSNumber`

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

Instance Property

# timestamp

The date and time of the signature's creation in milliseconds, formatted in
Unix epoch time.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    @NSCopying
    var timestamp: NSNumber { get }

## Discussion

The `timestamp` keeps the payment discount active for 24 hours.

## See Also

### Validating the Discount

`var nonce: UUID`

A universally unique ID (UUID) value that you define.

`var signature: String`

A string representing the properties of a specific promotional offer,
cryptographically signed.

