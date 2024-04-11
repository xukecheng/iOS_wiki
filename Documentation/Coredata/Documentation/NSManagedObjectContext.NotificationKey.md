Enumeration Case

# NSManagedObjectContext.NotificationKey.deletedObjectIDs

A key for the set of deleted object identifiers.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    case deletedObjectIDs

Enumeration Case

# NSManagedObjectContext.NotificationKey.deletedObjects

A key for the context’s set of deleted objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case deletedObjects

Enumeration Case

# NSManagedObjectContext.NotificationKey.insertedObjectIDs

A key for the set of inserted object identifiers.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    case insertedObjectIDs

Enumeration Case

# NSManagedObjectContext.NotificationKey.insertedObjects

A key for the context’s set of inserted objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case insertedObjects

Enumeration Case

# NSManagedObjectContext.NotificationKey.invalidatedAllObjects

A key for the context’s set of all invalidated objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case invalidatedAllObjects

Enumeration Case

# NSManagedObjectContext.NotificationKey.invalidatedObjectIDs

A key for the set of invalidated object identifiers.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    case invalidatedObjectIDs

Enumeration Case

# NSManagedObjectContext.NotificationKey.invalidatedObjects

A key for the context’s set of invalidated objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case invalidatedObjects

Enumeration Case

# NSManagedObjectContext.NotificationKey.queryGeneration

A key for the token that indicates which generation of the persistent store
Core Data is accessing

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case queryGeneration

Enumeration Case

# NSManagedObjectContext.NotificationKey.refreshedObjectIDs

A key for the set of refreshed object identifiers.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    case refreshedObjectIDs

Enumeration Case

# NSManagedObjectContext.NotificationKey.refreshedObjects

A key for the context’s set of refreshed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case refreshedObjects

Enumeration Case

# NSManagedObjectContext.NotificationKey.updatedObjectIDs

A key for the set of updated object identifiers.

iOS 10.3+  iPadOS 10.3+  macOS 10.12+  Mac Catalyst 14.0+  tvOS 10.2+  watchOS
3.2+  visionOS 1.0+  Xcode 12.0+

    
    
    case updatedObjectIDs

Enumeration Case

# NSManagedObjectContext.NotificationKey.updatedObjects

A key for the context’s set of updated objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    case updatedObjects

Initializer

# init(rawValue:)

Creates a notification key using the specified raw value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    init?(rawValue: String)

##  Parameters

`rawValue`

    

The raw string value of the key.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating and Comparing Keys

`var rawValue: String`

The raw string value of the key.

`typealias NSManagedObjectContext.NotificationKey.RawValue`

The raw type of notification key values.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the
specified hasher.

`var hashValue: Int`

The hash value.

Instance Property

# rawValue

The raw string value of the key.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 14.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 12.0+

    
    
    var rawValue: String { get }

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating and Comparing Keys

`init?(rawValue: String)`

Creates a notification key using the specified raw value.

`typealias NSManagedObjectContext.NotificationKey.RawValue`

The raw type of notification key values.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the
specified hasher.

`var hashValue: Int`

The hash value.

Type Alias

# NSManagedObjectContext.NotificationKey.RawValue

The raw type of notification key values.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    typealias NSManagedObjectContext.NotificationKey.RawValue = String

## See Also

### Creating and Comparing Keys

`init?(rawValue: String)`

Creates a notification key using the specified raw value.

`var rawValue: String`

The raw string value of the key.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the
specified hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the
specified hasher.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Creating and Comparing Keys

`init?(rawValue: String)`

Creates a notification key using the specified raw value.

`var rawValue: String`

The raw string value of the key.

`typealias NSManagedObjectContext.NotificationKey.RawValue`

The raw type of notification key values.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    var hashValue: Int { get }

## See Also

### Creating and Comparing Keys

`init?(rawValue: String)`

Creates a notification key using the specified raw value.

`var rawValue: String`

The raw string value of the key.

`typealias NSManagedObjectContext.NotificationKey.RawValue`

The raw type of notification key values.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the
specified hasher.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    static func != (lhs: NSManagedObjectContext.NotificationKey, rhs: NSManagedObjectContext.NotificationKey) -> Bool

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

