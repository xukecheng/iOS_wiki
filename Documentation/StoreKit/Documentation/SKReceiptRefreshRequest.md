Initializer

# init(receiptProperties:)

Creates a receipt refresh request with optional properties.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    init(receiptProperties properties: [String : Any]?)

##  Parameters

`properties`

    

In the test environment, the properties that the new receipt is to have. For
keys, see Receipt Properties and Keys.

In the production environment, set this parameter to `nil`.

## Return Value

The initialized request.

## Discussion

In the sandbox environment, you can initialize a receipt with any combination
of properties to test the state transitions related to Volume Purchase Plan
receipts. Set the `properties` when you call this initializer.

Instance Property

# receiptProperties

The properties of the receipt.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var receiptProperties: [String : Any]? { get }

## Discussion

Receipt properties include `SKReceiptPropertyIsExpired`,
`SKReceiptPropertyIsRevoked`, and `SKReceiptPropertyIsVolumePurchase`.

## See Also

### Receipt Properties and Keys

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsExpired

A key with a value that indicates whether the receipt is in an expired state.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsExpired: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is in an expired state.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsRevoked

A key with a value that indicates whether the receipt is in a revoked state.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsRevoked: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is in a revoked state.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsVolumePurchase

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsVolumePurchase: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is a Volume Purchase Plan
receipt.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

Initializer

# init(receiptProperties:)

Creates a receipt refresh request with optional properties.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    init(receiptProperties properties: [String : Any]?)

##  Parameters

`properties`

    

In the test environment, the properties that the new receipt is to have. For
keys, see Receipt Properties and Keys.

In the production environment, set this parameter to `nil`.

## Return Value

The initialized request.

## Discussion

In the sandbox environment, you can initialize a receipt with any combination
of properties to test the state transitions related to Volume Purchase Plan
receipts. Set the `properties` when you call this initializer.

Instance Property

# receiptProperties

The properties of the receipt.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var receiptProperties: [String : Any]? { get }

## Discussion

Receipt properties include `SKReceiptPropertyIsExpired`,
`SKReceiptPropertyIsRevoked`, and `SKReceiptPropertyIsVolumePurchase`.

## See Also

### Receipt Properties and Keys

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsExpired

A key with a value that indicates whether the receipt is in an expired state.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsExpired: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is in an expired state.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsRevoked

A key with a value that indicates whether the receipt is in a revoked state.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsRevoked: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is in a revoked state.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsVolumePurchase: String`

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

Global Variable

# SKReceiptPropertyIsVolumePurchase

A key with a value that indicates whether the receipt is a Volume Purchase
Plan receipt.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKReceiptPropertyIsVolumePurchase: String

## Discussion

This key’s value is an instance of `NSNumber` that the system interprets as a
Boolean value that indicates whether the receipt is a Volume Purchase Plan
receipt.

## See Also

### Receipt Properties and Keys

`var receiptProperties: [String : Any]?`

The properties of the receipt.

`let SKReceiptPropertyIsExpired: String`

A key with a value that indicates whether the receipt is in an expired state.

`let SKReceiptPropertyIsRevoked: String`

A key with a value that indicates whether the receipt is in a revoked state.

