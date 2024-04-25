Global Variable

# SKStoreProductParameterITunesItemIdentifier

The key representing the iTunes identifier for the item you want the store to
display when the view controller is presented.

iOS 6.0+  iPadOS 6.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.0+

    
    
    let SKStoreProductParameterITunesItemIdentifier: String

## Discussion

The value for this key, an iTunes item identifier, is an instance of
`NSNumber`.

To find a product’s iTunes identifier, go to linkmaker.itunes.apple.com and
search for the product, then locate the iTunes identifier in the link URL. For
example, the iTunes identifier for the iBooks app is 364709193.

Global Variable

# SKStoreProductParameterProductIdentifier

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 11.0+

    
    
    let SKStoreProductParameterProductIdentifier: String

## Discussion

The value for this key is an instance of `NSString`.

When your app uses an `SKStoreProductViewController` to render an app page for
another app, you can optionally choose to highlight an in-app purchase by
displaying it at the top of the store page. Set
`SKStoreProductParameterProductIdentifier` to the identifier of the product
you want displayed at the top of the page.

The product indicated by the identifier must be set up as a promoted product
in the App Store, otherwise the identifier is ignored. See Promoting In-App
Purchases.

Note

Use the same product identifiers as used in the `productIdentifier` variable
in the `SKProduct` class.

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterAdvertisingPartnerToken: String`

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterAffiliateToken: String`

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterCampaignToken: String`

The key representing an App Analytics campaign.

`let SKStoreProductParameterProviderToken: String`

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

`let SKStoreProductParameterCustomProductPageIdentifier: String`

Global Variable

# SKStoreProductParameterAdvertisingPartnerToken

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

iOS 9.3+  iPadOS 9.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.2+

    
    
    let SKStoreProductParameterAdvertisingPartnerToken: String

## Discussion

The value for this key is an instance of `NSString`.

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterProductIdentifier: String`

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

`let SKStoreProductParameterAffiliateToken: String`

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterCampaignToken: String`

The key representing an App Analytics campaign.

`let SKStoreProductParameterProviderToken: String`

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

`let SKStoreProductParameterCustomProductPageIdentifier: String`

Global Variable

# SKStoreProductParameterAffiliateToken

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

iOS 8.0+  iPadOS 8.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.0+

    
    
    let SKStoreProductParameterAffiliateToken: String

## Discussion

The value for this key is an instance of `NSString`.

You receive an affiliate identifier when you sign up for the Affiliate
Program. The affiliate associated with this view controller is paid a
commission for any items purchased using the controller.

Learn more about the Affiliate Program at https://apple.com/itunes/affiliates.

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterProductIdentifier: String`

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

`let SKStoreProductParameterAdvertisingPartnerToken: String`

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterCampaignToken: String`

The key representing an App Analytics campaign.

`let SKStoreProductParameterProviderToken: String`

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

`let SKStoreProductParameterCustomProductPageIdentifier: String`

Global Variable

# SKStoreProductParameterCampaignToken

The key representing an App Analytics campaign.

iOS 8.0+  iPadOS 8.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.0+

    
    
    let SKStoreProductParameterCampaignToken: String

## Discussion

The value for this key is an instance of `NSString`, containing any 40-byte
string.

This token allows you to track the effectiveness of your Affiliate Program
link and your App Analytics campaign.

For more information about the Affiliate Program, see the Affiliate Program at
https://apple.com/itunes/affiliates. For more information about App Store
Connect Analytics, see App Store Connect Developer Guide.

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterProductIdentifier: String`

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

`let SKStoreProductParameterAdvertisingPartnerToken: String`

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterAffiliateToken: String`

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterProviderToken: String`

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

`let SKStoreProductParameterCustomProductPageIdentifier: String`

Global Variable

# SKStoreProductParameterProviderToken

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

iOS 8.3+  iPadOS 8.3+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 9.0+

    
    
    let SKStoreProductParameterProviderToken: String

## Discussion

The value for this key is an instance of `NSString`.

Use your own provider token when cross promoting your own apps. This token
lets you track the effectiveness of the cross promotion effort separate from
any affiliate campaign that shares the same campaign token.

When promoting apps for other developers, use their provider token instead. In
this case, the token lets the developer track the effectiveness of your App
Analytics campaign for their apps.

The key must be used in combination with your campaign token,
`SKStoreProductParameterCampaignToken`. For more information, see App Store
Connect Developer Guide.

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterProductIdentifier: String`

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

`let SKStoreProductParameterAdvertisingPartnerToken: String`

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterAffiliateToken: String`

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterCampaignToken: String`

The key representing an App Analytics campaign.

`let SKStoreProductParameterCustomProductPageIdentifier: String`

Global Variable

# SKStoreProductParameterCustomProductPageIdentifier

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+

    
    
    let SKStoreProductParameterCustomProductPageIdentifier: String

## See Also

### Affiliate and Analytics Keys

`let SKStoreProductParameterProductIdentifier: String`

The key representing the product identifier for the promoted product you want
the store to display at the top of the page.

`let SKStoreProductParameterAdvertisingPartnerToken: String`

The key representing the advertising partner you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterAffiliateToken: String`

The key representing the affiliate identifier you wish to use for any purchase
made through the view controller.

`let SKStoreProductParameterCampaignToken: String`

The key representing an App Analytics campaign.

`let SKStoreProductParameterProviderToken: String`

The key representing the provider token for the developer that created the app
specified by the `SKStoreProductParameterITunesItemIdentifier` key.

