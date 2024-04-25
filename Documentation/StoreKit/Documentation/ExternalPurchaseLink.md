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

Type Property

# eligibleURLs

An array of external purchase links for the current storefront that the app
configured and from which it chooses.

iOS 17.5+ Beta iPadOS 17.5+ Beta macOS 14.5+ Beta Mac Catalyst 17.5+ Beta tvOS
17.5+ Beta watchOS 10.5+ Beta visionOS 1.2+ Beta Xcode 15.3+

    
    
    static var eligibleURLs: [URL]? { get async }

## Discussion

Use this property if your app configures the `SKExternalPurchaseMultiLink`
property list key.

Use the `eligibleURLs` to get the array of external purchase links for the
current storefront that your app has configured in the
`SKExternalPurchaseMultiLink` property list key. Your app can select from any
of the eligible URLs. Call `open(url:)` with the URL you choose.

The `eligibleURLs` array is `nil` if any of the following is true:

  * The current App Store storefront doesn't allow external purchase or the person isn't eligible to make external purchases.

  * Your app doesn't configure the `com.apple.developer.storekit.external-purchase-link` entitlement.

  * Your app doesn’t configure any links for the current storefront in the `SKExternalPurchaseMultiLink` property list key

If this value is `nil` and your app also configures the
`SKExternalPurchaseLink` property list key, check `canOpen` to determine
whether your app can continue to provide an external purchase link.

Otherwise, if this value is `nil`, check `canMakePayments` to determine
whether your app can offer in-app purchases using the StoreKit In-App Purchase
APIs. For more information, see `canMakePayments`.

## See Also

### Getting multiple external purchase links

`property list key SKExternalPurchaseMultiLink`

A dictionary that contains an array of URLs to websites where people using
your app can make external purchases.

Beta

`static func open(url: URL)`

Presents a continuation sheet that enables people to choose whether your app
shows the indicated URL link for external purchases.

Beta Software

This documentation contains preliminary information about an API or technology
in development. This information is subject to change, and software
implemented according to this documentation should be tested with final
operating system software.

Learn more about using Apple's beta software

Type Method

# open(url:)

Presents a continuation sheet that enables people to choose whether your app
shows the indicated URL link for external purchases.

iOS 17.5+ Beta iPadOS 17.5+ Beta macOS 14.5+ Beta Mac Catalyst 17.5+ Beta tvOS
17.5+ Beta watchOS 10.5+ Beta visionOS 1.2+ Beta Xcode 15.3+

    
    
    static func open(url: URL) async throws

##  Parameters

`url`

    

An eligible external purchase link that you select from the `eligibleURLs`
array.

## Discussion

Call this method if your app configures the `SKExternalPurchaseMultiLink`
property list key to attempt to open the eligible external purchase link,
`url`. Call this asynchronous method as shown below:

To use this method, follow these steps:

  1. Check the `eligibleURLs` array. If the array contains one or more links, your app can display the user-interface controls to enable deliberate user interaction before offering an external purchase link. 

  2. Select one of the eligible links.

  3. In response to deliberate user interaction, such as tapping a button, call `open(url:)` with the link you select. 

The system displays the continuation sheet that enables the user to choose
whether to continue to view the external purchase link. This asynchronous
method returns before the system presents the continuation sheet, and can
throw an error.

If the person chooses to continue, this method opens the link that you provide
in the `url` parameter, and appends an external purchase token and the app’s
bundleID to the URL. For example, StoreKit opens the following link on the
default browser if your destination URL is `https://site.example.com`:

    
    
    https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example
    

Important

Record and use the external purchase token to report the customer’s external
purchases to Apple. For more information, see External Purchase Server API.

### Handle errors

This method throws a `StoreKitError` if any of the following are true:

  * Your app doesn’t have the `com.apple.developer.storekit.external-purchase-link` entitlement.

  * You haven’t configured external purchase links for the current App Store storefront in the `SKExternalPurchaseMultiLink` property list key.

  * The current App Store storefront doesn’t support external purchases.

  * The person is ineligible to make external purchases.

  * A network or system error occurs.

For more information about App Store storefronts, see `Storefront`.

## See Also

### Getting multiple external purchase links

`property list key SKExternalPurchaseMultiLink`

A dictionary that contains an array of URLs to websites where people using
your app can make external purchases.

Beta

`static var eligibleURLs: [URL]?`

An array of external purchase links for the current storefront that the app
configured and from which it chooses.

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

Type Property

# canOpen

A Boolean value that indicates whether the app can successfully open the
configured external purchase link in the current App Store storefront.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    static var canOpen: Bool { get async }

## Discussion

Use this method if your app configures the `SKExternalPurchaseLink` property
list key.

Check this property, as shown below, to determine whether your app can
successfully call `open()`.

If the result is `true`, configure any user-interface controls that enable
people to open the external purchase link. You configure that link in the
`SKExternalPurchaseLink` property list key in the `Info.plist` file. There’s
no need to call `canOpen` again, unless the App Store storefront changes. For
more information about the App Store storefront, see `Storefront`.

This property is `true` if all the following conditions are met:

  * The current App Store storefront allows external purchase and the person is eligible to make external purchases.

  * Your app configures the `com.apple.developer.storekit.external-purchase-link` entitlement.

  * Your app configures a link for the current App Store storefront in `SKExternalPurchaseLink`.

Otherwise, this property is `false`.

When this property is `false`, check `canMakePayments` to determine whether
your app can offer in-app purchases using the StoreKit In-App Purchase APIs.
For more information, see `canMakePayments`.

## See Also

### Getting a single external purchase link

`property list key SKExternalPurchaseLink`

A dictionary that contains URLs to websites where people using your app can
make external purchases, for supported regions.

`static func open()`

Presents a continuation sheet that enables people to choose whether your app
shows its link for external purchases.

Type Method

# open()

Presents a continuation sheet that enables people to choose whether your app
shows its link for external purchases.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    static func open() async throws

## Discussion

Use this method if your app configures the `SKExternalPurchaseLink` property
list key.

Call this asynchronous method to have the system attempt to open the external
purchase link, as shown below:

To use this method, follow these steps:

  1. Call `canOpen` to determine whether to display a button or other user-interface controls that enable you to call `open()`. If it returns `true`, your app can display the user-interface controls to enable deliberate user interaction.

  2. In response to deliberate user interaction, such as tapping a button, call `open()`. The system displays the continuation sheet that enables the user to choose whether to continue to view your app’s external purchase URL. This asynchronous method returns before the system presents the continuation sheet, and throws an error if `canOpen` is `false`.

If the person chooses to continue, this method opens the current storefront’s
destination URL that you configure in the `SKExternalPurchaseLink` property
list key and appends an external purchase token and the app's bundleID to the
URL. For example, StoreKit opens the following URL on the default browser if
your destination URL is `https://site.example.com`:

    
    
    https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example
    
    
    

Important

Record and use the external purchase token to report the customer’s external
purchases to Apple. For more information, see External Purchase Server API.

### Handle errors

This method throws a `StoreKitError` if any of the following are true:

  * Your app doesn’t have the `com.apple.developer.storekit.external-purchase-link` entitlement.

  * You haven’t configured external purchases for the current App Store storefront in `SKExternalPurchaseLink`.

  * The current App Store storefront doesn’t support external purchases.

  * The person is ineligible to make external purchases.

  * A network or system error occurs.

For more information about App Store storefronts, see `Storefront`.

## See Also

### Getting a single external purchase link

`property list key SKExternalPurchaseLink`

A dictionary that contains URLs to websites where people using your app can
make external purchases, for supported regions.

`static var canOpen: Bool`

A Boolean value that indicates whether the app can successfully open the
configured external purchase link in the current App Store storefront.

