Initializer

# init(url:)

Initializes the receiver with a URL for the store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    init(url: URL)

##  Parameters

`url`

    

Location for the store.

## Return Value

Initialized `NSPersistentStoreDescription` configured with the given URL.

Instance Property

# url

The URL that the store will use for its location.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var url: URL? { get set }

## See Also

### Configuring a Persistent Store Description

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# configuration

The name of the configuration used by this store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var configuration: String? { get set }

## Discussion

This displays the name of a configuration in the receiver's managed object
model that will be used by the new store. The configuration can be `nil`, in
which case no other configurations are allowed.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# timeout

The connection timeout for the associated store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var timeout: TimeInterval { get set }

## Discussion

This is a convenience method for setting the `NSPersistentStoreTimeoutOption`
on the associated store.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# type

The type of store this description represents.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var type: String { get set }

## Discussion

A string constant (such as `NSSQLiteStoreType`) that specifies the type of the
new store—see `NSPersistentStoreCoordinator`.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# isReadOnly

A flag that indicates whether this store will be read-only.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var isReadOnly: Bool { get set }

## Discussion

This is a convenience method for setting the `NSReadOnlyPersistentStoreOption`
on the associated store.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# shouldAddStoreAsynchronously

A flag that determines whether the store is added asynchronously.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var shouldAddStoreAsynchronously: Bool { get set }

## Discussion

By default, the store is added to the `NSPersistentStoreCoordinator`
synchronously on the calling thread. If this flag is set to `true`, the store
is added asynchronously on a background queue. The default for this flag is
`false`.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# shouldInferMappingModelAutomatically

A flag indicating whether a mapping model should be created automatically.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var shouldInferMappingModelAutomatically: Bool { get set }

## Discussion

If this flag is set to `true` and the value of the
`shouldMigrateStoreAutomatically` is `true`, the coordinator attempts to infer
a mapping model if none can be found. The default for this flag is `true`.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Property

# shouldMigrateStoreAutomatically

A flag indicating whether the associated persistent store should be migrated
automatically.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var shouldMigrateStoreAutomatically: Bool { get set }

## Discussion

If this is set to `false` and the store is out of sync, attempting to load the
store produces an error. If this is set to `true` and the store is out of
sync, attempting to load the store causes Core Data to attempt a migration.
This flag is set to `true` by default.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Method

# setOption(_:forKey:)

Sets an option on the store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func setOption(
        _ option: NSObject?,
        forKey key: String
    )

##  Parameters

`option`

    

The value to be set for an option on the store.

`key`

    

The key of the value to be set for an option on the store.

## Discussion

If a value was previously set for the given option, that value is replaced
with the given value. Note that the keys are case-sensitive. For a list of the
available options, see `NSPersistentStoreCoordinator`.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setValue(NSObject?, forPragmaNamed: String)`

Allows you to set pragmas for the SQLite store.

Instance Method

# setValue(_:forPragmaNamed:)

Allows you to set pragmas for the SQLite store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func setValue(
        _ value: NSObject?,
        forPragmaNamed name: String
    )

##  Parameters

`value`

    

The value of the pragma to be set.

`name`

    

The name of the pragma to be set.

## Discussion

Pragma options are for SQLite stores only. All pragma values must be specified
as `NSString`objects. The `fullfsync` and `synchronous` pragmas control the
tradeoff between write performance (write to disk speed and cache utilization)
and durability (data loss/corruption sensitivity to power interruption). For
more information on pragma settings, see http://sqlite.org/pragma.html.

## See Also

### Configuring a Persistent Store Description

`var url: URL?`

The URL that the store will use for its location.

`var configuration: String?`

The name of the configuration used by this store.

`var timeout: TimeInterval`

The connection timeout for the associated store.

`var type: String`

The type of store this description represents.

`var isReadOnly: Bool`

A flag that indicates whether this store will be read-only.

`var shouldAddStoreAsynchronously: Bool`

A flag that determines whether the store is added asynchronously.

`var shouldInferMappingModelAutomatically: Bool`

A flag indicating whether a mapping model should be created automatically.

`var shouldMigrateStoreAutomatically: Bool`

A flag indicating whether the associated persistent store should be migrated
automatically.

`func setOption(NSObject?, forKey: String)`

Sets an option on the store.

Instance Property

# options

A dictionary representation of the options set on the associated persistent
store.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var options: [String : NSObject] { get }

## Discussion

A dictionary containing key-value pairs that specify numerous settings for the
persistent store. For key definitions, see `NSPersistentStoreCoordinator`.

## See Also

### Accessing the Configuration Options

`var sqlitePragmas: [String : NSObject]`

The SQLite pragmas set for the associated persistent store. (read-only)

Instance Property

# sqlitePragmas

The SQLite pragmas set for the associated persistent store. (read-only)

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    var sqlitePragmas: [String : NSObject] { get }

## Discussion

This property contains all of the pragmas set on the associated persistent
store. This property is only relevant when the `type` is set to
`NSSQLiteStoreType`.

## See Also

### Accessing the Configuration Options

`var options: [String : NSObject]`

A dictionary representation of the options set on the associated persistent
store.

Instance Property

# cloudKitContainerOptions

Options that customize how this store description aligns with a CloudKit
database.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var cloudKitContainerOptions: NSPersistentCloudKitContainerOptions? { get set }

