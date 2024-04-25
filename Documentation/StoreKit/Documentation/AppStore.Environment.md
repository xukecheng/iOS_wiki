Type Property

# production

A value that indicates the production server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let production: AppStore.Environment

## See Also

### Getting the environment value

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# sandbox

A value that indicates the sandbox server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let sandbox: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# xcode

A value that indicates the StoreKit Testing in Xcode environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let xcode: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

Instance Property

# rawValue

The underlying string value that describes the environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting the raw value

`typealias AppStore.Environment.RawValue`

A string type that represents the raw value of an App Store environment.

Type Alias

# AppStore.Environment.RawValue

A string type that represents the raw value of an App Store environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias AppStore.Environment.RawValue = String

## See Also

### Getting the raw value

`let rawValue: String`

The underlying string value that describes the environment.

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

The raw value to use for the new instance.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: AppStore.Environment, rhs: AppStore.Environment) -> Bool

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

### Comparing and hashing the environment value

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

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# production

A value that indicates the production server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let production: AppStore.Environment

## See Also

### Getting the environment value

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# sandbox

A value that indicates the sandbox server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let sandbox: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# xcode

A value that indicates the StoreKit Testing in Xcode environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let xcode: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

Instance Property

# rawValue

The underlying string value that describes the environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting the raw value

`typealias AppStore.Environment.RawValue`

A string type that represents the raw value of an App Store environment.

Type Alias

# AppStore.Environment.RawValue

A string type that represents the raw value of an App Store environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias AppStore.Environment.RawValue = String

## See Also

### Getting the raw value

`let rawValue: String`

The underlying string value that describes the environment.

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

The raw value to use for the new instance.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: AppStore.Environment, rhs: AppStore.Environment) -> Bool

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

### Comparing and hashing the environment value

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

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# production

A value that indicates the production server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let production: AppStore.Environment

## See Also

### Getting the environment value

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# sandbox

A value that indicates the sandbox server environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let sandbox: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let xcode: AppStore.Environment`

A value that indicates the StoreKit Testing in Xcode environment.

Type Property

# xcode

A value that indicates the StoreKit Testing in Xcode environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static let xcode: AppStore.Environment

## See Also

### Getting the environment value

`static let production: AppStore.Environment`

A value that indicates the production server environment.

`static let sandbox: AppStore.Environment`

A value that indicates the sandbox server environment.

Instance Property

# rawValue

The underlying string value that describes the environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting the raw value

`typealias AppStore.Environment.RawValue`

A string type that represents the raw value of an App Store environment.

Type Alias

# AppStore.Environment.RawValue

A string type that represents the raw value of an App Store environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias AppStore.Environment.RawValue = String

## See Also

### Getting the raw value

`let rawValue: String`

The underlying string value that describes the environment.

Initializer

# init(rawValue:)

Creates a new instance with the specified raw value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

The raw value to use for the new instance.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: AppStore.Environment, rhs: AppStore.Environment) -> Bool

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

### Comparing and hashing the environment value

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

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing the environment value

`static func != (AppStore.Environment, AppStore.Environment) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

