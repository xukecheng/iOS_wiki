Initializer

# init(rawValue:)

Initializes a cloud service capability with the provided raw value.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+  Xcode 7.1+

    
    
    init(rawValue: UInt)

Type Property

# musicCatalogPlayback

The device allows playback of Apple Music catalog tracks.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    static var musicCatalogPlayback: SKCloudServiceCapability { get }

## See Also

### Identifying Cloud Service Capabilities

`static var musicCatalogSubscriptionEligible: SKCloudServiceCapability`

The device allows subscription to the Apple Music catalog.

`static var addToCloudMusicLibrary: SKCloudServiceCapability`

The device allows tracks to be added to the user’s music library.

Type Property

# musicCatalogSubscriptionEligible

The device allows subscription to the Apple Music catalog.

iOS 10.1+  iPadOS 10.1+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 10.1+  watchOS
7.0+

    
    
    static var musicCatalogSubscriptionEligible: SKCloudServiceCapability { get }

## See Also

### Identifying Cloud Service Capabilities

`static var musicCatalogPlayback: SKCloudServiceCapability`

The device allows playback of Apple Music catalog tracks.

`static var addToCloudMusicLibrary: SKCloudServiceCapability`

The device allows tracks to be added to the user’s music library.

Type Property

# addToCloudMusicLibrary

The device allows tracks to be added to the user’s music library.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.3+  watchOS
7.0+

    
    
    static var addToCloudMusicLibrary: SKCloudServiceCapability { get }

## See Also

### Identifying Cloud Service Capabilities

`static var musicCatalogPlayback: SKCloudServiceCapability`

The device allows playback of Apple Music catalog tracks.

`static var musicCatalogSubscriptionEligible: SKCloudServiceCapability`

The device allows subscription to the Apple Music catalog.

