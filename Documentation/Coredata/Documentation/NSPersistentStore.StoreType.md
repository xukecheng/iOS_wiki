Type Property

# binary

A store that reads from and writes to a persistent binary file.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let binary: NSPersistentStore.StoreType

## Discussion

A binary store is atomic, which means Core Data reads and writes the file in
its entirety. This behavior is different from a `sqlite` store, which you can
partially modify.

## See Also

### Store Types

`static let inMemory: NSPersistentStore.StoreType`

An ephemeral store that reads from and writes to memory only.

`static let sqlite: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent SQLite database.

`static let xml: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent XML file.

Type Property

# inMemory

An ephemeral store that reads from and writes to memory only.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let inMemory: NSPersistentStore.StoreType

## See Also

### Store Types

`static let binary: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent binary file.

`static let sqlite: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent SQLite database.

`static let xml: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent XML file.

Type Property

# sqlite

A store that reads from and writes to a persistent SQLite database.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let sqlite: NSPersistentStore.StoreType

## See Also

### Store Types

`static let binary: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent binary file.

`static let inMemory: NSPersistentStore.StoreType`

An ephemeral store that reads from and writes to memory only.

`static let xml: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent XML file.

Type Property

# xml

A store that reads from and writes to a persistent XML file.

macOS 12.0+  Xcode 13.0+

    
    
    static let xml: NSPersistentStore.StoreType

## Discussion

An XML store is atomic, which means Core Data reads and writes the file in its
entirety. This behavior is different from a `sqlite` store, which you can
partially modify.

## See Also

### Store Types

`static let binary: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent binary file.

`static let inMemory: NSPersistentStore.StoreType`

An ephemeral store that reads from and writes to memory only.

`static let sqlite: NSPersistentStore.StoreType`

A store that reads from and writes to a persistent SQLite database.

Initializer

# init(rawValue:)

Creates a store type using the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that represents the store type.

## Relationships

### From Protocol

  * `RawRepresentable`

Instance Property

# rawValue

The store type’s cardinal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting a Store Type’s Raw Value

`typealias NSPersistentStore.StoreType.RawValue`

The type the conforming type uses to represent its values.

Type Alias

# NSPersistentStore.StoreType.RawValue

The type the conforming type uses to represent its values.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias NSPersistentStore.StoreType.RawValue = String

## See Also

### Getting a Store Type’s Raw Value

`var rawValue: String`

The store type’s cardinal value.

Instance Property

# hashValue

The store type’s computed hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Hashing a Store Type

`func hash(into: inout Hasher)`

Hashes the components of the store type using the provided hasher.

Instance Method

# hash(into:)

Hashes the components of the store type using the provided hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining components of this store type.

## See Also

### Hashing a Store Type

`var hashValue: Int`

The store type’s computed hash value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: NSPersistentStore.StoreType, rhs: NSPersistentStore.StoreType) -> Bool

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

