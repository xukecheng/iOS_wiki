Enumeration Case

# StoreKitError.networkError(_:)

A network error occurred.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case networkError(URLError)

## See Also

### StoreKit Error Codes

`case systemError(any Error)`

A system error occurred.

`case userCancelled`

The user canceled.

`case notAvailableInStorefront`

The function isn’t available on devices configured for this storefront.

`case notEntitled`

The app doesn’t have the appropriate entitlements to use the functionality.

`case unknown`

An unknown error occurred.

Enumeration Case

# StoreKitError.systemError(_:)

A system error occurred.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case systemError(any Error)

## See Also

### StoreKit Error Codes

`case networkError(URLError)`

A network error occurred.

`case userCancelled`

The user canceled.

`case notAvailableInStorefront`

The function isn’t available on devices configured for this storefront.

`case notEntitled`

The app doesn’t have the appropriate entitlements to use the functionality.

`case unknown`

An unknown error occurred.

Enumeration Case

# StoreKitError.userCancelled

The user canceled.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case userCancelled

## See Also

### StoreKit Error Codes

`case networkError(URLError)`

A network error occurred.

`case systemError(any Error)`

A system error occurred.

`case notAvailableInStorefront`

The function isn’t available on devices configured for this storefront.

`case notEntitled`

The app doesn’t have the appropriate entitlements to use the functionality.

`case unknown`

An unknown error occurred.

Enumeration Case

# StoreKitError.notAvailableInStorefront

The function isn’t available on devices configured for this storefront.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case notAvailableInStorefront

## See Also

### StoreKit Error Codes

`case networkError(URLError)`

A network error occurred.

`case systemError(any Error)`

A system error occurred.

`case userCancelled`

The user canceled.

`case notEntitled`

The app doesn’t have the appropriate entitlements to use the functionality.

`case unknown`

An unknown error occurred.

Enumeration Case

# StoreKitError.notEntitled

The app doesn’t have the appropriate entitlements to use the functionality.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    case notEntitled

## See Also

### StoreKit Error Codes

`case networkError(URLError)`

A network error occurred.

`case systemError(any Error)`

A system error occurred.

`case userCancelled`

The user canceled.

`case notAvailableInStorefront`

The function isn’t available on devices configured for this storefront.

`case unknown`

An unknown error occurred.

Enumeration Case

# StoreKitError.unknown

An unknown error occurred.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case unknown

## See Also

### StoreKit Error Codes

`case networkError(URLError)`

A network error occurred.

`case systemError(any Error)`

A system error occurred.

`case userCancelled`

The user canceled.

`case notAvailableInStorefront`

The function isn’t available on devices configured for this storefront.

`case notEntitled`

The app doesn’t have the appropriate entitlements to use the functionality.

Instance Property

# localizedDescription

A string containing the localized description of the error.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var localizedDescription: String { get }

## See Also

### Error Descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A message describing the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

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

### Error Descriptions

`var localizedDescription: String`

A string containing the localized description of the error.

`var failureReason: String?`

A message describing the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# failureReason

A message describing the reason for the failure.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var failureReason: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Descriptions

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# helpAnchor

A localized message that provides additional information if the user requests
help.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.4+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var helpAnchor: String? { get }

## See Also

### Error Descriptions

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A message describing the reason for the failure.

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

### Error Descriptions

`var localizedDescription: String`

A string containing the localized description of the error.

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A message describing the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

