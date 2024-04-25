Property List Key

# com.apple.developer.storekit.external-purchase

A Boolean value that indicates whether your app can offer external purchases.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+

##  Details

Type

    

boolean

## Discussion

Qualifying apps may offer external purchases within the app. To offer external
purchases in your app, complete a request for this entitlement. For more
information about qualifying apps and to request this entitlement, see:

  * Distributing apps using alternative payment providers in the European Union

  * Distributing dating apps in the Netherlands

  * Distributing apps using a third-party payment provider in South Korea

If your account receives this entitlement, which is also known as the StoreKit
External Purchase entitlement, add it to your app by opening the project’s
.`entitlements` file in Xcode. Then add the following key and set the
corresponding value to `true`:

    
    
    <plist>
    <dict>
        <key>com.apple.developer.storekit.external-purchase</key>
        <true/>
    </dict>
    </plist>
    

For more information, see External Purchase.

## See Also

### StoreKit

`com.apple.developer.storekit.external-link.account`

A Boolean value that indicates whether your app can link to an external
website for account creation or management.

`com.apple.developer.storekit.external-purchase-link`

A Boolean value that indicates whether your app can include a link that
directs people to a website to make an external purchase.

Property List Key

# SKExternalPurchase

A string array of country codes that indicates your app supports external
purchases.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.0+

##  Details

Type

    

array of strings

## Discussion

Use this information property list key if your app has the
`com.apple.developer.storekit.external-purchase` entitlement.

To the array, add a string containing the lowercased ISO 3166-1 alpha-2
country code for each country where your app supports external purchases. The
following code example shows a property list entry with two strings, for the
Netherlands (`nl`) and Italy (`it`):

    
    
    <plist>
    <dict>
        <key>SKExternalPurchase</key>
        <array>
            <string>nl</string>
            <string>it</string>
        </array>
    </dict>
    </plist>
    

Use valid country codes for the following allowed countries or regions:

  * In the European Union: Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`) 

  * South Korea (`kr`)

For more information, see External Purchase.

## See Also

### Offering external purchases

`enum ExternalPurchase`

Enables qualifying apps to offer external purchases within the app.

`com.apple.developer.storekit.external-purchase`

A Boolean value that indicates whether your app can offer external purchases.

Property List Key

# com.apple.developer.storekit.external-purchase-link

A Boolean value that indicates whether your app can include a link that
directs people to a website to make an external purchase.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+

##  Details

Type

    

boolean

## Discussion

The `com.apple.developer.storekit.external-purchase-link` entitlement enables
qualifying apps to include a link that directs people using the app to a
website to make an external purchase. For more information about qualifying
apps and to request this entitlement, see:

  * Distributing apps using alternative payment providers in the European Union

  * Distributing dating apps in the Netherlands

  * Distributing apps in Russia that provide an external purchase link

  * Distributing apps in the U.S. that provide an external purchase link

  * Distributing music streaming apps in the EEA that provide an external purchase link

If your account receives this entitlement, which is also known as the StoreKit
External Purchase Link entitlement, you can add it to your app by opening the
project’s `.entitlements` file in Xcode. Then add the following key and set
the corresponding value to `true`:

    
    
    <plist>
    <dict>
        <key>com.apple.developer.storekit.external-purchase-link</key>
        <true/>
    </dict>
    </plist>
    

For more information, see External Purchase.

## See Also

### StoreKit

`com.apple.developer.storekit.external-link.account`

A Boolean value that indicates whether your app can link to an external
website for account creation or management.

`com.apple.developer.storekit.external-purchase`

A Boolean value that indicates whether your app can offer external purchases.

Property List Key

# SKExternalPurchaseMultiLink

A dictionary that contains an array of URLs to websites where people using
your app can make external purchases.

iOS 17.5+ Beta iPadOS 17.5+ Beta macOS 14.5+ Beta Mac Catalyst 17.5+ Beta tvOS
17.5+ Beta watchOS 10.5+ Beta visionOS 1.2+ Beta

##  Details

Type

    

dictionary

## Properties

`Any Key`

`[string]`

A dictionary with a key that is the lowercased ISO 3166-1 alpha-2 country
code, and an array of strings that represent valid destination URLs.

Valid country codes include those for the European Union: Austria (`at`),
Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia
(`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany
(`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia
(`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`),
Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia
(`si`), Spain (`es`), Sweden (`se`); and Iceland (`is`), Norway (`no`), Russia
(`ru`), and United States (`us`).

## Discussion

Use this information property list key if your app has the
`com.apple.developer.storekit.external-purchase-link` entitlement.

Include a key entry for each country code where your app supports an external
purchase link. Provide from one to five destination URLs (links to your
website) for your app to choose from for each country code.

Note

You can provide up to five links if your app qualifies for the StoreKit
External Purchase Link entitlement as described in Distributing music
streaming apps in the EEA that provide an external purchase link.  Otherwise,
provide one link for each country code.

Your app accesses these URLs through the `eligibleURLs` array in the
`ExternalPurchaseLink` object, and uses the link you select with the
`open(url:)` method in the `ExternalPurchaseLink` object.

Important

At all times, the destination URLs that you provide in the property list key
must match the values in your app binary that you submit to App Review.

Make sure each destination URL meets all of the following conditions:

  * Uses the HTTPS scheme

  * Forms a valid, absolute URL

  * Contains no query parameters

  * Contains 1,000 or fewer ASCII characters

The following code example shows a property list entry with keys for several
country codes, and links for each entry:

    
    
    <key>SKExternalPurchaseMultiLink</key>
    <dict>
        <key>es</key>
        <array>
            <string>https://www.example.com/es1</string>
            <string>https://www.example.com/new-user-es</string>
            <string>https://www.example.com/seasonal-sale-es</string>
            <string>https://www.example.com/es2</string>
            <string>https://www.example.com/es3</string>
        </array>
        <key>fr</key>
        <array>
            <string>https://www.example.com/fr</string>
            <string>https://www.example.com/global-sale</string>
            <string>https://www.example.com/new-user-fr</string>
        </array>
        <key>it</key>
        <array>
            <string>https://www.example.com/global-sale</string>
        </array>
    </dict>
    

The order of the links is not significant.

For more information, see External Purchase and `ExternalPurchaseLink`.

### Provide up to the maximum number of links

The following country codes have a maximum of five links for apps that qualify
for the StoreKit External Purchase Link entitlement as described in
Distributing music streaming apps in the EEA that provide an external purchase
link: Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus
(`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France
(`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy
(`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`),
Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia
(`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`), Iceland (`is`), Norway
(`no`). Otherwise, the maximum is one link, for valid country codes.

Count the total number of unique links you provide for each country code by
adding together the number of links you provide in the
`SKExternalPurchaseMultiLink` and `SKExternalPurchaseLink` property list keys.

For example, if a country code has a maximum of five links and you provide
five unique links in the `SKExternalPurchaseMultiLink` key, then specify one
of the same five links in the `SKExternalPurchaseLink` key to avoid exceeding
the maximum allowed links. If a country code has a maximum of one link, the
`SKExternalPurchaseMultiLink` and `SKExternalPurchaseLink` keys need to
specify the same link.

Beta Software

This documentation contains preliminary information about an API or technology
in development. This information is subject to change, and software
implemented according to this documentation should be tested with final
operating system software.

Learn more about using Apple's beta software

Property List Key

# SKExternalPurchaseLink

A dictionary that contains URLs to websites where people using your app can
make external purchases, for supported regions.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.0+

##  Details

Type

    

dictionary

## Properties

`Any Key`

`string`

A dictionary with a key that is the lowercased ISO 3166-1 alpha-2 country
code, and a string that contains a valid destination URL.

Valid country codes include those for the European Union: Austria (`at`),
Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia
(`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany
(`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia
(`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`),
Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia
(`si`), Spain (`es`), Sweden (`se`); and Iceland (`is`), Norway (`no`), Russia
(`ru`), and United States (`us`).

## Discussion

Use this information property list key if your app has the
`com.apple.developer.storekit.external-purchase-link` entitlement and your app
has a minimum OS version prior to iOS 17.5, macOS 14.5, watchOS 10.5, tvOS
17.5, or visionOS 1.2. Otherwise, use the `SKExternalPurchaseMultiLink`
property list key to provide multiple URLs for country codes that allow
multiple links.

Include one key entry for each country code where your app supports an
external purchase link. Provide a destination URL (link to your website) for
your app to open when the country code in the key matches the device’s App
Store storefront. If you support multiple country codes, you may provide the
same or different destination URLs for each country code.

Important

At all times, the destination URLs that you provide in the property list key
must match the values in your app binary that you submit to App Review.

Make sure the destination URL meets all of the following conditions:

  * Uses the HTTPS scheme

  * Forms a valid, absolute URL

  * Contains no query parameters

  * Contains 1,000 or fewer ASCII characters.

The following code example shows a property list entry with a single country
code key, for the Netherlands (`nl`). Replace the string
"`https://example.com`" below with your link:

    
    
    <plist>
    <dict>
        <key>SKExternalPurchaseLink</key>
        <dict>
            <key>nl</key>
            <string>https://example.com</string>
        </dict>
    </dict>
    </plist>
    

The following code example shows a property list entry with keys for more than
one country code. Replace the “`https://example.com`“ strings with your links:

    
    
    <plist>
    <dict>
        <key>SKExternalPurchaseLink</key>
        <dict>
            <key>at</key>
            <string>https://ex1.example.com</string>
            <key>nl</key>
            <string>https://ex2.example.com</string>
            <key>it</key>
            <string>https://ex2.example.com</string>
        </dict>
    </dict>
    </plist>
    

For more information, see External Purchase.

## See Also

### Offering external purchase links

`enum ExternalPurchaseLink`

Enables qualifying apps to offer external purchase links.

`com.apple.developer.storekit.external-purchase-link`

A Boolean value that indicates whether your app can include a link that
directs people to a website to make an external purchase.

`property list key SKExternalPurchaseMultiLink`

A dictionary that contains an array of URLs to websites where people using
your app can make external purchases.

Beta

Article

# Receiving and decoding external purchase tokens

Receive tokens for external purchases that you use to report transactions to
Apple.

## Overview

An _external purchase token_ is a unique string that your app or website
receives when your app’s customer chooses to view your external purchase
offerings. You receive external purchase tokens in two ways: within your app,
or appended to your website URL for link out, as follows:

  * In your app, the API returns the token when your app calls `presentNoticeSheet()` and the response is `ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`.

  * For link out, when your app calls `open()`, the API appends the token to the current storefront’s destination URL that you configure in the `SKExternalPurchaseLink` property list key.

Decode the token to obtain its `externalPurchaseId`, which you use to report
the tokens and associated transactions to Apple using the Send External
Purchase Report endpoint of the External Purchase Server API.

### Decode external purchase tokens

The token your app or website’s server receives is a string that is Base64URL-
encoded JSON. Decode the token using Base64URL decoding to read the JSON,
which contains the following fields:

  * The `appAppleId` and `bundleId`, which uniquely identify the app to which the token applies

  * The `tokenCreationDate`, which is the UNIX time, in milliseconds, when the system created the token

  * The `externalPurchaseId`, which is a unique value the system created to identify the token

The `externalPurchaseId` field is required by the Send External Purchase
Report endpoint when you report tokens and transactions. To get the
`externalPurchaseId`, follow these steps:

  * Decode the token string using Base64URL decoding. For example, if the token string is:

`ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9`

Then, the token’s value after Base64URL decoding is the following JSON:

    
    
    {  
      "appAppleId":1234567890,  
      "bundleId":"com.example",  
      "tokenCreationDate":1706169600000,
      "externalPurchaseId":"00000000-0000-0000-0000-000000000000"
    }
    

  * Use the value of the `externalPurchaseId` property to identify the token when you call the Send External Purchase Report endpoint.

### Recognize tokens from the testing environment

The External Purchase API returns external purchase tokens that are specific
to the app’s environment: production or sandbox. You can recognize a token for
the sandbox environment by its `externalPurchaseId` property, which always
begins with "`SANDBOX`".

The following example is an external purchase token that the system created in
the sandbox environment. The sandbox token string is:

`ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiU0FOREJPWF8wMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiCn0K`

The token’s JSON content after Base64URL decoding is:

    
    
    {
        "appAppleId":1234567890,
        "bundleId":"com.example",
        "tokenCreationDate":1706169600000,
        "externalPurchaseId":"SANDBOX_00000000-0000-0000-0000-000000000000"
    }
    

The `externalPurchaseId` includes the "`SANDBOX`" prefix in the testing
environment.

