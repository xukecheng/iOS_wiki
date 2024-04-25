Type Property

# shared

Gets the App Store-signed app transaction information for the app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static var shared: VerificationResult<AppTransaction> { get async throws }

## Discussion

Use this property to get a `VerificationResult` that contains the App Store-
signed app transaction information for your app, including the first time the
app launches. StoreKit automatically keeps the app transaction up-to-date.

This property throws an error if the `AppTransaction` isn't available or if
the user isn't authenticated with the App Store. Getting an `AppTransaction`
may require network connectivity.

The following example shows how to get the `AppTransaction`.

If your app fails to get an `AppTransaction` by accessing the `shared`
property, see `refresh()`.

Instance Property

# environment

The server environment that signs the app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`struct AppStore.Environment`

Constants that represent the App Store server environment.

Instance Property

# bundleID

The bundle identifier that the app transaction applies to.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let bundleID: String

## Discussion

The `bundleID` is the bundle identifier string that you entered in Xcode. For
more information, see What is a bundle ID?

## See Also

### Getting app and version info

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appVersion

The app version that the app transaction applies to.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appVersion: String

## Discussion

This value is the version string you entered in Xcode. This value is a
machine-readable string composed of one to three period-separated integers,
such as `10.4.1`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# originalAppVersion

The app version that the user originally purchased from the App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let originalAppVersion: String

## Discussion

Use this value to determine which app version the user first purchased or
downloaded. This value is comparable to the `appVersion` value.

The `originalAppVersion` remains constant and doesn't change when the user
upgrades the app. The string value contains the original value of the
`CFBundleShortVersionString` for apps running in macOS, and the original value
of the `CFBundleVersion` for apps running on all other platforms.

For more information about using the `originalAppVersion`, see Supporting
business model changes by using the app transaction.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appID

The unique identifier the App Store uses to identify the app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appID: UInt64?

## Discussion

The App Store assigns this value. This value is the app's Apple ID in App
Store Connect. In the `sandbox` and `xcode` environments, this value is `nil`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appVersionID

The number that the App Store uses to uniquely identify the version of the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appVersionID: UInt64?

## Discussion

The App Store assigns this value. In the `sandbox` and `xcode` environments,
this value is `nil`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

Instance Property

# originalPurchaseDate

The date the user originally purchased the app from the App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let originalPurchaseDate: Date

## Discussion

The original purchase date remains the same, even if the user deletes and
reinstalls the app.

## See Also

### Getting purchase dates

`let preorderDate: Date?`

The date the customer placed an order for the app before it’s available in the
App Store.

Instance Property

# preorderDate

The date the customer placed an order for the app before it’s available in the
App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let preorderDate: Date?

## Discussion

This date is present if your app is available for preorder and the customer
places an order before your app is available in the App Store. When your app
becomes available, the App Store fulfills the customer’s order. The
`preorderDate` remains the same.

Use this date to recognize customers who place preorders.

For more infomation about preorders, see Offering Your Apps for Pre-Order.

## See Also

### Getting purchase dates

`let originalPurchaseDate: Date`

The date the user originally purchased the app from the App Store.

Instance Property

# deviceVerification

The device verification value to use to verify whether the app transaction
belongs to the device.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying the app transaction

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS app transaction.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying the app transaction

`let deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS app transaction.

Instance Property

# signedDate

The date that the App Store signed the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the app
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying the app transaction

`let deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the app transaction information.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information contained in the `jsonRepresentation` is the same information
as contained in the properties of the same instance of an `AppTransaction`.

Type Method

# refresh()

Gets the App Store-signed app transaction information from the App Store
server.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func refresh() async throws -> VerificationResult<AppTransaction>

## Return Value

Returns a `VerificationResult` with a single `AppTransaction`.

## Discussion

This method queries the App Store server to refresh the app transaction
information. This method returns a `VerificationResult` that contains the App
Store-signed app transaction information for your app.

Important

Calling `refresh()` displays a system prompt that asks users to authenticate
with their App Store credentials. Call this function only in response to an
explicit user action, like tapping or clicking a button.

Use this method to get an `AppTransaction` in the following cases:

  * The `shared` property throws an error.

  * The `shared` property returns an unverified (`VerificationResult.unverified(_:_:)` ) result.

This method throws an error if the user cancels the authentication prompt, if
there’s no network connectivity, or if the call fails to update the app
transaction.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: AppTransaction, rhs: AppTransaction) -> Bool

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

### Comparing and hashing app transactions

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (lhs: AppTransaction, rhs: AppTransaction) -> Bool

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# debugDescription

A string represenation of the instance, suitable for debugging.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Type Property

# shared

Gets the App Store-signed app transaction information for the app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static var shared: VerificationResult<AppTransaction> { get async throws }

## Discussion

Use this property to get a `VerificationResult` that contains the App Store-
signed app transaction information for your app, including the first time the
app launches. StoreKit automatically keeps the app transaction up-to-date.

This property throws an error if the `AppTransaction` isn't available or if
the user isn't authenticated with the App Store. Getting an `AppTransaction`
may require network connectivity.

The following example shows how to get the `AppTransaction`.

    
    
    do {
        let verificationResult = try await AppTransaction.shared
    
    
        switch verificationResult {
        case .verified(let appTransaction):
            // StoreKit verified that the user purchased this app and
            // the properties in the AppTransaction instance.
            // Add your code here.
        case .unverified(let appTransaction, let verificationError):
            // The app transaction didn't pass StoreKit's verification.        
            // Handle unverified app transaction information according
            // to your business model.
            // Add your code here.
        }
    }
    catch {
      // Handle errors.
    }
    
    
    

If your app fails to get an `AppTransaction` by accessing the `shared`
property, see `refresh()`.

Instance Property

# environment

The server environment that signs the app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`struct AppStore.Environment`

Constants that represent the App Store server environment.

Instance Property

# bundleID

The bundle identifier that the app transaction applies to.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let bundleID: String

## Discussion

The `bundleID` is the bundle identifier string that you entered in Xcode. For
more information, see What is a bundle ID?

## See Also

### Getting app and version info

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appVersion

The app version that the app transaction applies to.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appVersion: String

## Discussion

This value is the version string you entered in Xcode. This value is a
machine-readable string composed of one to three period-separated integers,
such as `10.4.1`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# originalAppVersion

The app version that the user originally purchased from the App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let originalAppVersion: String

## Discussion

Use this value to determine which app version the user first purchased or
downloaded. This value is comparable to the `appVersion` value.

The `originalAppVersion` remains constant and doesn't change when the user
upgrades the app. The string value contains the original value of the
`CFBundleShortVersionString` for apps running in macOS, and the original value
of the `CFBundleVersion` for apps running on all other platforms.

For more information about using the `originalAppVersion`, see Supporting
business model changes by using the app transaction.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appID

The unique identifier the App Store uses to identify the app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appID: UInt64?

## Discussion

The App Store assigns this value. This value is the app's Apple ID in App
Store Connect. In the `sandbox` and `xcode` environments, this value is `nil`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appVersionID: UInt64?`

The number that the App Store uses to uniquely identify the version of the
app.

Instance Property

# appVersionID

The number that the App Store uses to uniquely identify the version of the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let appVersionID: UInt64?

## Discussion

The App Store assigns this value. In the `sandbox` and `xcode` environments,
this value is `nil`.

## See Also

### Getting app and version info

`let bundleID: String`

The bundle identifier that the app transaction applies to.

`let appVersion: String`

The app version that the app transaction applies to.

`let originalAppVersion: String`

The app version that the user originally purchased from the App Store.

`let appID: UInt64?`

The unique identifier the App Store uses to identify the app.

Instance Property

# originalPurchaseDate

The date the user originally purchased the app from the App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let originalPurchaseDate: Date

## Discussion

The original purchase date remains the same, even if the user deletes and
reinstalls the app.

## See Also

### Getting purchase dates

`let preorderDate: Date?`

The date the customer placed an order for the app before it’s available in the
App Store.

Instance Property

# preorderDate

The date the customer placed an order for the app before it’s available in the
App Store.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let preorderDate: Date?

## Discussion

This date is present if your app is available for preorder and the customer
places an order before your app is available in the App Store. When your app
becomes available, the App Store fulfills the customer’s order. The
`preorderDate` remains the same.

Use this date to recognize customers who place preorders.

For more infomation about preorders, see Offering Your Apps for Pre-Order.

## See Also

### Getting purchase dates

`let originalPurchaseDate: Date`

The date the user originally purchased the app from the App Store.

Instance Property

# deviceVerification

The device verification value to use to verify whether the app transaction
belongs to the device.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying the app transaction

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS app transaction.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying the app transaction

`let deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS app transaction.

Instance Property

# signedDate

The date that the App Store signed the JWS app transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the app
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying the app transaction

`let deviceVerification: Data`

The device verification value to use to verify whether the app transaction
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the app transaction information.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information contained in the `jsonRepresentation` is the same information
as contained in the properties of the same instance of an `AppTransaction`.

Type Method

# refresh()

Gets the App Store-signed app transaction information from the App Store
server.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func refresh() async throws -> VerificationResult<AppTransaction>

## Return Value

Returns a `VerificationResult` with a single `AppTransaction`.

## Discussion

This method queries the App Store server to refresh the app transaction
information. This method returns a `VerificationResult` that contains the App
Store-signed app transaction information for your app.

Important

Calling `refresh()` displays a system prompt that asks users to authenticate
with their App Store credentials. Call this function only in response to an
explicit user action, like tapping or clicking a button.

Use this method to get an `AppTransaction` in the following cases:

  * The `shared` property throws an error.

  * The `shared` property returns an unverified (`VerificationResult.unverified(_:_:)` ) result.

This method throws an error if the user cancels the authentication prompt, if
there’s no network connectivity, or if the call fails to update the app
transaction.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: AppTransaction, rhs: AppTransaction) -> Bool

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

### Comparing and hashing app transactions

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (lhs: AppTransaction, rhs: AppTransaction) -> Bool

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing app transactions

`static func != (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (AppTransaction, AppTransaction) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# debugDescription

A string represenation of the instance, suitable for debugging.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

