Initializer

# init(containerIdentifier:)

Initializes container options using the given CloudKit container identifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(containerIdentifier: String)

## See Also

### Creating Container Options

`var containerIdentifier: String`

The identifier of the CloudKit container associated with a given store
description.

`var databaseScope: CKDatabase.Scope`

The database scope — public, private, or shared — to use for a specified store
in a persistent CloudKit container.

Instance Property

# containerIdentifier

The identifier of the CloudKit container associated with a given store
description.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var containerIdentifier: String { get }

## See Also

### Creating Container Options

`init(containerIdentifier: String)`

Initializes container options using the given CloudKit container identifier.

`var databaseScope: CKDatabase.Scope`

The database scope — public, private, or shared — to use for a specified store
in a persistent CloudKit container.

Instance Property

# databaseScope

The database scope — public, private, or shared — to use for a specified store
in a persistent CloudKit container.

Core Data  CloudKit  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+
tvOS 14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    var databaseScope: CKDatabase.Scope { get set }

## See Also

### Creating Container Options

`init(containerIdentifier: String)`

Initializes container options using the given CloudKit container identifier.

`var containerIdentifier: String`

The identifier of the CloudKit container associated with a given store
description.

