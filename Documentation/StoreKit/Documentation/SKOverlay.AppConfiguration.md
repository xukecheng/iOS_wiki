Initializer

# init(appIdentifier:position:)

Creates an object that represents the attributes of an overlay you use to
recommend another app on the App Store.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        appIdentifier: String,
        position: SKOverlay.Position
    )

##  Parameters

`appIdentifier`

    

The iTunes identifier of the recommended app.

`position`

    

The position of the overlay on the screen.

## See Also

### Creating an App Configuration

`var appIdentifier: String`

The iTunes identifier of the recommended app.

`var position: SKOverlay.Position`

The position of the overlay on the screen.

`enum SKOverlay.Position`

Constants that identify the position of an overlay on the screen.

Instance Property

# appIdentifier

The iTunes identifier of the recommended app.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var appIdentifier: String { get set }

## See Also

### Creating an App Configuration

`init(appIdentifier: String, position: SKOverlay.Position)`

Creates an object that represents the attributes of an overlay you use to
recommend another app on the App Store.

`var position: SKOverlay.Position`

The position of the overlay on the screen.

`enum SKOverlay.Position`

Constants that identify the position of an overlay on the screen.

Instance Property

# position

The position of the overlay on the screen.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var position: SKOverlay.Position { get set }

## See Also

### Creating an App Configuration

`init(appIdentifier: String, position: SKOverlay.Position)`

Creates an object that represents the attributes of an overlay you use to
recommend another app on the App Store.

`var appIdentifier: String`

The iTunes identifier of the recommended app.

`enum SKOverlay.Position`

Constants that identify the position of an overlay on the screen.

Instance Property

# userDismissible

A Boolean value that indicates whether the user can dismiss the overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var userDismissible: Bool { get set }

Instance Property

# campaignToken

A token you use to represent an ad campaign and measure its effectiveness.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var campaignToken: String? { get set }

## Discussion

A campaign token is a 40-byte string that represents an ad campaign. By
setting the `campaignToken`, you can measure the effectiveness of an Apple
Services Performance Partners Program link or an App Store Connect Analytics
campaign.

For more information, see Apple Services Performance Partners Program and App
Store Connect.

## See Also

### Verifying Advertising Campaigns

`var providerToken: String?`

A token that represents the provider of an app promotion campaign, and that
you use to measure the campaign’s effectiveness.

`func setAdditionalValue(Any?, forKey: String)`

Sets an additional value for a key; for example, a value for measuring the
effectiveness of an ad campaign.

`func additionalValue(forKey: String) -> Any?`

Returns the object associated with the key.

Instance Property

# providerToken

A token that represents the provider of an app promotion campaign, and that
you use to measure the campaign’s effectiveness.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var providerToken: String? { get set }

## Discussion

When you set a provider token, you must also set the `campaignToken`.

When promoting your own apps, set your own provider token using
`providerToken`. This allows you to track a promotion’s effectiveness
independently from any affiliate campaign that shares the same campaign token.

When promoting apps by other developers, set `providerToken` using their
provider token. This allows those developers to track the effectiveness of
your App Store Connect Analytics campaign.

## See Also

### Verifying Advertising Campaigns

`var campaignToken: String?`

A token you use to represent an ad campaign and measure its effectiveness.

`func setAdditionalValue(Any?, forKey: String)`

Sets an additional value for a key; for example, a value for measuring the
effectiveness of an ad campaign.

`func additionalValue(forKey: String) -> Any?`

Returns the object associated with the key.

Instance Method

# setAdditionalValue(_:forKey:)

Sets an additional value for a key; for example, a value for measuring the
effectiveness of an ad campaign.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func setAdditionalValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The value to associate with the `key`.

`key`

    

The string that identifies an additional value.

## Discussion

Set additional values to verify and associate an app installation with an ad
campaign. For more information, see `SKAdNetwork`.

## See Also

### Verifying Advertising Campaigns

`var campaignToken: String?`

A token you use to represent an ad campaign and measure its effectiveness.

`var providerToken: String?`

A token that represents the provider of an app promotion campaign, and that
you use to measure the campaign’s effectiveness.

`func additionalValue(forKey: String) -> Any?`

Returns the object associated with the key.

Instance Method

# additionalValue(forKey:)

Returns the object associated with the key.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func additionalValue(forKey key: String) -> Any?

##  Parameters

`key`

    

The string that identifies an additional value.

## Return Value

The associated value of the key.

## Discussion

Additional values are values you use to verify and associate an app
installation with an ad campaign. For more information, see `SKAdNetwork`.

## See Also

### Verifying Advertising Campaigns

`var campaignToken: String?`

A token you use to represent an ad campaign and measure its effectiveness.

`var providerToken: String?`

A token that represents the provider of an app promotion campaign, and that
you use to measure the campaign’s effectiveness.

`func setAdditionalValue(Any?, forKey: String)`

Sets an additional value for a key; for example, a value for measuring the
effectiveness of an ad campaign.

Instance Property

# latestReleaseID

The release ID of the latest version of your app as displayed in App Store
Connect.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var latestReleaseID: String? { get set }

Instance Property

# customProductPageIdentifier

An optional identifier for an app’s custom product page.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var customProductPageIdentifier: String? { get set }

## Discussion

The identifier, referred to as the product variant identifier, identifies
specific variant product pages from App Store Connect for your app.

Instance Method

# setAdImpression(_:)

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    func setAdImpression(_ impression: SKAdImpression)

Instance Property

# appImpression

AdAttributionKit  StoreKit  iOS 17.4+  iPadOS 17.4+  Xcode 15.3+

    
    
    var appImpression: AppImpression? { get set }

