Initializer

# init(_:)

Creates a lightweight migration stage with the specified version checksums.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    convenience init(_ checksums: [String])

##  Parameters

`checksums`

    

The array of version checksums.

## Discussion

To determine an object model’s version checksum, use its `versionChecksum`
property. Alternatively, you can find the checksum in the versioned model’s
`VersionInfo.plist` file or in Xcode’s build log.

Instance Property

# versionChecksums

The array of version checksums.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var versionChecksums: [String] { get }

## Discussion

Core Data sets this property to the `checksums` parameter you specify when
creating the lightweight migration stage.

