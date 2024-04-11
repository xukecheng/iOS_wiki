Type Property

# mainQueue

A concurrency type where the context performs its tasks on the main queue.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let mainQueue: NSManagedObjectContext.ConcurrencyType

## See Also

### Concurrency Types

`static let privateQueue: NSManagedObjectContext.ConcurrencyType`

A concurrency type where the context performs its tasks on a private queue.

Type Property

# privateQueue

A concurrency type where the context performs its tasks on a private queue.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let privateQueue: NSManagedObjectContext.ConcurrencyType

## See Also

### Concurrency Types

`static let mainQueue: NSManagedObjectContext.ConcurrencyType`

A concurrency type where the context performs its tasks on the main queue.

Initializer

# init(rawValue:)

Creates a concurrency type using the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: NSManagedObjectContextConcurrencyType)

##  Parameters

`rawValue`

    

The raw concurrency type. For possible values, see
`NSManagedObjectContextConcurrencyType`.

## Relationships

### From Protocol

  * `RawRepresentable`

Instance Property

# rawValue

The concurrency type’s cardinal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var rawValue: NSManagedObjectContextConcurrencyType

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting a Concurrency Type’s Raw Value

`typealias NSManagedObjectContext.ConcurrencyType.RawValue`

The type the conforming type uses to represent its values.

Type Alias

# NSManagedObjectContext.ConcurrencyType.RawValue

The type the conforming type uses to represent its values.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias NSManagedObjectContext.ConcurrencyType.RawValue = NSManagedObjectContextConcurrencyType

## See Also

### Getting a Concurrency Type’s Raw Value

`var rawValue: NSManagedObjectContextConcurrencyType`

The concurrency type’s cardinal value.

Instance Property

# hashValue

The concurrency type’s computed hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Hashing a Concurrency Type

`func hash(into: inout Hasher)`

Hashes the components of the concurrency type using the provided hasher.

Instance Method

# hash(into:)

Hashes the components of the concurrency type using the provided hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining components of this concurrency type.

## See Also

### Hashing a Concurrency Type

`var hashValue: Int`

The concurrency type’s computed hash value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: NSManagedObjectContext.ConcurrencyType, rhs: NSManagedObjectContext.ConcurrencyType) -> Bool

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

