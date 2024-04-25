Initializer

# init(rawValue:)

Initializes a cloud service setup options key based on the provided raw value.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.0+  tvOS 9.0+  visionOS
1.0+  Xcode 7.1+

    
    
    init(rawValue: String)

Type Property

# action

A key that specifies the action for a setup entry point.

iOS 10.1+  iPadOS 10.1+  Mac Catalyst 13.1+  tvOS 10.0+

    
    
    static let action: SKCloudServiceSetupOptionsKey

## See Also

### Indicating Setup Options

`struct SKCloudServiceSetupAction`

A string used to specify the type of setup action to offer for a cloud
service.

`static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store item that the user is trying to access
through the service.

`static let affiliateToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate token.

`static let campaignToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate campaign token.

`static let messageIdentifier: SKCloudServiceSetupOptionsKey`

A key that is used to select the main message presented to the user for this
setup view.

`struct SKCloudServiceSetupMessageIdentifier`

Identifiers for the available messages the setup view can present to the user.

Type Property

# iTunesItemIdentifier

A key that specifies the iTunes Store item that the user is trying to access
through the service.

iOS 10.1+  iPadOS 10.1+  Mac Catalyst 13.1+  tvOS 10.0+

    
    
    static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey

## Discussion

The only iTunes Store items that are supported are song, video, playlist, and
album.

## See Also

### Indicating Setup Options

`static let action: SKCloudServiceSetupOptionsKey`

A key that specifies the action for a setup entry point.

`struct SKCloudServiceSetupAction`

A string used to specify the type of setup action to offer for a cloud
service.

`static let affiliateToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate token.

`static let campaignToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate campaign token.

`static let messageIdentifier: SKCloudServiceSetupOptionsKey`

A key that is used to select the main message presented to the user for this
setup view.

`struct SKCloudServiceSetupMessageIdentifier`

Identifiers for the available messages the setup view can present to the user.

Type Property

# affiliateToken

A key that specifies the iTunes Store affiliate token.

iOS 10.3+  iPadOS 10.3+  Mac Catalyst 13.1+  tvOS 10.2+

    
    
    static let affiliateToken: SKCloudServiceSetupOptionsKey

## See Also

### Indicating Setup Options

`static let action: SKCloudServiceSetupOptionsKey`

A key that specifies the action for a setup entry point.

`struct SKCloudServiceSetupAction`

A string used to specify the type of setup action to offer for a cloud
service.

`static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store item that the user is trying to access
through the service.

`static let campaignToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate campaign token.

`static let messageIdentifier: SKCloudServiceSetupOptionsKey`

A key that is used to select the main message presented to the user for this
setup view.

`struct SKCloudServiceSetupMessageIdentifier`

Identifiers for the available messages the setup view can present to the user.

Type Property

# campaignToken

A key that specifies the iTunes Store affiliate campaign token.

iOS 10.3+  iPadOS 10.3+  Mac Catalyst 13.1+  tvOS 10.2+

    
    
    static let campaignToken: SKCloudServiceSetupOptionsKey

## See Also

### Indicating Setup Options

`static let action: SKCloudServiceSetupOptionsKey`

A key that specifies the action for a setup entry point.

`struct SKCloudServiceSetupAction`

A string used to specify the type of setup action to offer for a cloud
service.

`static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store item that the user is trying to access
through the service.

`static let affiliateToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate token.

`static let messageIdentifier: SKCloudServiceSetupOptionsKey`

A key that is used to select the main message presented to the user for this
setup view.

`struct SKCloudServiceSetupMessageIdentifier`

Identifiers for the available messages the setup view can present to the user.

Type Property

# messageIdentifier

A key that is used to select the main message presented to the user for this
setup view.

iOS 11.0+  iPadOS 11.0+  Mac Catalyst 13.1+  tvOS 11.0+

    
    
    static let messageIdentifier: SKCloudServiceSetupOptionsKey

## Discussion

If this key is missing, the setup view is configured as if it is using the
`join` key by default.

## See Also

### Indicating Setup Options

`static let action: SKCloudServiceSetupOptionsKey`

A key that specifies the action for a setup entry point.

`struct SKCloudServiceSetupAction`

A string used to specify the type of setup action to offer for a cloud
service.

`static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store item that the user is trying to access
through the service.

`static let affiliateToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate token.

`static let campaignToken: SKCloudServiceSetupOptionsKey`

A key that specifies the iTunes Store affiliate campaign token.

`struct SKCloudServiceSetupMessageIdentifier`

Identifiers for the available messages the setup view can present to the user.

