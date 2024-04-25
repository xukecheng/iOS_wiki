Type Property

# canPresent

A Boolean value that indicates whether the app can successfully present the
notice sheet to inform people about external purchases.

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 15.3+

    
    
    static var canPresent: Bool { get async }

## Discussion

Check this property, as shown below, to determine whether your app can
successfully call `presentNoticeSheet()` to inform people before showing
external purchases:

Check the value of this property again whenever the App Store storefront
changes by using the `updates` asynchronous sequence of `Storefront`.

This property is `true` if all the following conditions are met:

  * The current App Store storefront allows external purchase, and the person is eligible to make external purchases.

  * Your app configures the `com.apple.developer.storekit.external-purchase` entitlement.

  * Your app configures the country code for the current App Store storefront in `SKExternalPurchase`.

Otherwise, this property is `false`.

When this property is `false`, check `canMakePayments` to determine whether
your app can offer in-app purchases using the StoreKit In-App Purchase APIs.
For more information, see `canMakePayments`.

## See Also

### Offering an external purchase

`static func presentNoticeSheet() -> ExternalPurchase.NoticeResult`

Presents a notice sheet from Apple that informs people before showing external
purchases and determines whether your app can present external purchases.

`enum ExternalPurchase.NoticeResult`

The options available to people while viewing the external purchase notice
sheet.

`property list key SKExternalPurchase`

A string array of country codes that indicates your app supports external
purchases.

Type Method

# presentNoticeSheet()

Presents a notice sheet from Apple that informs people before showing external
purchases and determines whether your app can present external purchases.

iOS 15.4+  iPadOS 15.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 13.3+

    
    
    static func presentNoticeSheet() async throws -> ExternalPurchase.NoticeResult

## Return Value

This returns `ExternalPurchase.NoticeResult`.

## Discussion

This method is only available to apps with the
`com.apple.developer.storekit.external-purchase` entitlement. For more
information, see `ExternalPurchase`.

Call this method each time your app is ready to present an external purchase.
To use this method, follow these steps:

  1. Call `canPresent`. If it’s `false`, don’t call `presentNoticeSheet()` and don’t show external purchases.

  2. If `canPresent` is `true`, display buttons or other user-interface elements to enable deliberate user interaction. Then, in response to a deliberate user interaction such as tapping a button, call `presentNoticeSheet()` as shown below:

3\. If the result is
`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`
your app can show external purchases. Otherwise, you must not show external
purchases.

Important

Record and use the token from the result to report to Apple the customer’s
external purchases. For more information on reporting, see External Purchase
Server API.

This method throws a `StoreKitError` in any of the following conditions:

  * Your app doesn’t have the `com.apple.developer.storekit.external-purchase` entitlement.

  * Your app doesn’t have external purchases configured for the current App Store storefront; see `SKExternalPurchase` and `Storefront`.

  * The current App Store storefront doesn’t support external purchases. 

  * The person is ineligible to make external purchases.

  * A network or system error occurs.

This method also throws a `StoreKitError` if its functionality is unavailable
for the following reasons:

  * Your app is built with Mac Catalyst and you compile with an SDK earlier than iOS 17.4 or iPadOS 17.4.

  * Your app is a compatible iPad or iPhone app running in macOS or visionOS and uses an SDK earlier than iOS 17.4 or iPadOS 17.4.

For apps compiled with SDKs earlier than iOS 17.4 or iPadOS 17.4, your app can
show external purchases if the result is
`ExternalPurchase.NoticeResult.continued`.

## See Also

### Offering an external purchase

`static var canPresent: Bool`

A Boolean value that indicates whether the app can successfully present the
notice sheet to inform people about external purchases.

`enum ExternalPurchase.NoticeResult`

The options available to people while viewing the external purchase notice
sheet.

`property list key SKExternalPurchase`

A string array of country codes that indicates your app supports external
purchases.

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

