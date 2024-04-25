Property List Key

# com.apple.developer.storekit.external-link.account

A Boolean value that indicates whether your app can link to an external
website for account creation or management.

iOS 15.4+  iPadOS 15.4+  tvOS 16.4+

##  Details

Type

    

boolean

## Discussion

If your developer account has this entitlement, add it to your app by opening
the project’s entitlements file in Xcode. Add the following key and set the
corresponding value to `true`:

    
    
    <plist>
    <dict>
        <key>com.apple.developer.storekit.external-link.account</key>
        <true/>
    </dict>
    </plist>
    

## See Also

### StoreKit

`com.apple.developer.storekit.external-purchase`

A Boolean value that indicates whether your app can offer external purchases.

`com.apple.developer.storekit.external-purchase-link`

A Boolean value that indicates whether your app can include a link that
directs people to a website to make an external purchase.

Property List Key

# SKExternalLinkAccount

A dictionary that contains localized URLs to an external website for account
creation or management.

iOS 15.4+  iPadOS 15.4+  tvOS 16.4+

##  Details

Type

    

dictionary

## Properties

`Any Key`

`string`

A dictionary with keys that are lowercase ISO 3166-1 alpha-2 country codes and
values that are URLs. The dictionary must contain a key with the string `*`
that maps to a default URL.

## Discussion

Use this information property list key if your app has the
`com.apple.developer.storekit.external-link.account` entitlement. The
following shows a property list with a default URL and a specific URL for the
`jp` locale:

    
    
    <plist>
    <dict>
        <key>SKExternalLinkAccount</key>
        <dict>
            <key>*</key>
            <string>https://example.com</string>
            <key>jp</key>
            <string>https://example.com/jp</string>
        </dict>
    </dict>
    </plist>
    

## See Also

### External accounts

`com.apple.developer.storekit.external-link.account`

A Boolean value that indicates whether your app can link to an external
website for account creation or management.

`enum ExternalLinkAccount`

Enables qualifying apps to link to an external website for account creation or
management.

