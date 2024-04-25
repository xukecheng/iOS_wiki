Initializer

# init(id:)

Creates the payment method binding for eligible apps and users.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    init(id: String) async throws

##  Parameters

`id`

    

The in-app binding identifier that your server receives from the Apple server
when your server initiates payment method binding.

## Discussion

This method succeeds if the app is entitled to use this API, the `id` is valid
and unexpired, and the user is eligible. Otherwise, it throws an error. See
`PaymentMethodBinding.PaymentMethodBindingError` and
`StoreKitError.userCancelled` for the error information.

This method determines if the user is eligible, and requires that they're
signed in to the App Store.

Important

This method may display a system prompt that asks users to sign in with their
Apple ID. Call this method only after an explicit user action, like tapping or
clicking a button.

Note that it's possible that the system determines a user isn't eligible after
it prompts for authentication.

Instance Property

# id

The in-app binding identifier.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    let id: String

## Discussion

This identifier is the in-app binding identifier that your server receives
from the Apple server when your server initiates payment method binding.

## Relationships

### From Protocol

  * `Identifiable`

## See Also

### Creating and identifying bindings

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `PaymentMethodBinding` conforms to `AnyObject`.

`typealias PaymentMethodBinding.ID`

A type that represents the identifier of a payment account binding.

Instance Property

# id

The stable identity of the entity associated with this instance.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 11.0+

    
    
    var id: ObjectIdentifier { get }

Available when `PaymentMethodBinding` conforms to `AnyObject`.

## Discussion

Note

This documentation comment was inherited from `Identifiable`.

## See Also

### Creating and identifying bindings

`let id: String`

The in-app binding identifier.

`typealias PaymentMethodBinding.ID`

A type that represents the identifier of a payment account binding.

Type Alias

# PaymentMethodBinding.ID

A type that represents the identifier of a payment account binding.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    typealias PaymentMethodBinding.ID = String

## See Also

### Creating and identifying bindings

`let id: String`

The in-app binding identifier.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `PaymentMethodBinding` conforms to `AnyObject`.

Instance Method

# bind()

Asks the user to confirm whether to add the payment method to their Apple
payment methods.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    func bind() async throws

## Discussion

Important

This method displays a system prompt that asks users to authenticate with
their Apple ID. Call this method only after an explicit user action, like
tapping or clicking a button.

This method displays an Apple sheet that asks the user to confirm whether to
add the payment method associated with the in-app binding ID (`id`). If the
user confirms adding the payment method, it becomes the user’s primary payment
method for media purchases and subscriptions from Apple.

The binding succeeds if this method doesn’t throw an error.

This method throws an error in any of the following conditions:

  * The user cancels the sheet and doesn’t confirm the payment method update.

  * The in-app binding ID (`id`) is invalid or expired.

  * The user isn’t eligible.

  * The app isn’t entitled to use this API.

For more information about the errors, see
`PaymentMethodBinding.PaymentMethodBindingError` and
`StoreKitError.userCancelled`.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func != (lhs: PaymentMethodBinding, rhs: PaymentMethodBinding) -> Bool

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

### Comparing and hashing bindings

`static func == (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func == (a: PaymentMethodBinding, b: PaymentMethodBinding) -> Bool

## See Also

### Comparing and hashing bindings

`static func != (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

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

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing bindings

`static func != (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing bindings

`static func != (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (PaymentMethodBinding, PaymentMethodBinding) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

