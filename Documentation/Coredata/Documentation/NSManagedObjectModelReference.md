Initializer

# init(model:versionChecksum:)

Creates an object model reference for the specified model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        model: NSManagedObjectModel,
        versionChecksum: String
    )

##  Parameters

`model`

    

The managed object model.

`versionChecksum`

    

The checksum of the object model’s version.

## Discussion

To determine an object model’s version checksum, use its `versionChecksum`
property. Alternatively, you can find the checksum in the versioned model’s
`VersionInfo.plist` file or in Xcode’s build log.

## See Also

### Creating a reference

`init(fileURL: URL, versionChecksum: String)`

Creates an object model reference for the model at the specified file URL.

`init(name: String, in: Bundle?, versionChecksum: String)`

Creates an object model reference for the named model in the specified bundle.

`init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum:
String)`

Creates an object model reference with the entities corresponding to the
specified entity version hashes.

Initializer

# init(fileURL:versionChecksum:)

Creates an object model reference for the model at the specified file URL.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        fileURL: URL,
        versionChecksum: String
    )

##  Parameters

`fileURL`

    

The on-disk location of the managed object model.

`versionChecksum`

    

The checksum of the object model’s version.

## Discussion

To determine an object model’s version checksum, use its `versionChecksum`
property. Alternatively, you can find the checksum in the versioned model’s
`VersionInfo.plist` file or in Xcode’s build log.

## See Also

### Creating a reference

`init(model: NSManagedObjectModel, versionChecksum: String)`

Creates an object model reference for the specified model.

`init(name: String, in: Bundle?, versionChecksum: String)`

Creates an object model reference for the named model in the specified bundle.

`init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum:
String)`

Creates an object model reference with the entities corresponding to the
specified entity version hashes.

Initializer

# init(name:in:versionChecksum:)

Creates an object model reference for the named model in the specified bundle.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        name modelName: String,
        in bundle: Bundle?,
        versionChecksum: String
    )

##  Parameters

`modelName`

    

The name of the managed object model in the specified bundle.

`bundle`

    

The bundle to search.

`versionChecksum`

    

The checksum of the object model’s version.

## Discussion

To determine an object model’s version checksum, use its `versionChecksum`
property. Alternatively, you can find the checksum in the versioned model’s
`VersionInfo.plist` file or in Xcode’s build log.

## See Also

### Creating a reference

`init(model: NSManagedObjectModel, versionChecksum: String)`

Creates an object model reference for the specified model.

`init(fileURL: URL, versionChecksum: String)`

Creates an object model reference for the model at the specified file URL.

`init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum:
String)`

Creates an object model reference with the entities corresponding to the
specified entity version hashes.

Initializer

# init(entityVersionHashes:in:versionChecksum:)

Creates an object model reference with the entities corresponding to the
specified entity version hashes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        entityVersionHashes versionHash: [AnyHashable : Any],
        in bundle: Bundle?,
        versionChecksum: String
    )

##  Parameters

`versionHash`

    

The dictionary of entity names and their corresponding version hashes.

`bundle`

    

The bundle to search.

`versionChecksum`

    

The checksum of the object model’s version.

## Discussion

To determine an object model’s version checksum, use its `versionChecksum`
property. Alternatively, you can find the checksum in the versioned model’s
`VersionInfo.plist` file or in Xcode’s build log.

## See Also

### Creating a reference

`init(model: NSManagedObjectModel, versionChecksum: String)`

Creates an object model reference for the specified model.

`init(fileURL: URL, versionChecksum: String)`

Creates an object model reference for the model at the specified file URL.

`init(name: String, in: Bundle?, versionChecksum: String)`

Creates an object model reference for the named model in the specified bundle.

Instance Property

# resolvedModel

The resolved object model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var resolvedModel: NSManagedObjectModel { get }

## See Also

### Resolving the model object

`var versionChecksum: String`

The version checksum of the resolved model.

Instance Property

# versionChecksum

The version checksum of the resolved model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var versionChecksum: String { get }

## See Also

### Resolving the model object

`var resolvedModel: NSManagedObjectModel`

The resolved object model.

