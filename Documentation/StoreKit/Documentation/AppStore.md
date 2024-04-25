Type Property

# canMakePayments

A Boolean value that indicates whether the person can make purchases.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var canMakePayments: Bool { get }

## Discussion

Use `canMakePayments` to determine at runtime whether a person can authorize
payments. If your app is configured with entitlements for the External
Purchase APIs, `canMakePayments` informs your app at runtime whether it can
call the External Purchase APIs or use the StoreKit In-App Purchase API.

Important

Your app might need to alter its behavior or appearance when people aren’t
allowed to make purchases. For example, don't enable your user interface for
making in-app purchases when purchases are blocked.

If your app uses only StoreKit In-App Purchase APIs, and:

  * `canMakePayments` is `true`, someone can authorize purchases in the App Store.

  * `canMakePayments` is `false`, don't offer in-app purchases using StoreKit In-App Purchase APIs.

The following conditions can cause the value of `canMakePayments` to be
`false`:

  * A person sets the Content & Privacy Restrictions in Screen Time to block purchases. For more information, see Use parental controls on your child's iPhone, iPad, and iPod touch. 

  * The device has a mobile device management (MDM) profile that blocks purchases. For more information, see Device Management. 

  * StoreKit In-App Purchase APIs are unavailable because the app must use the External Purchase APIs instead. See the section below, Interpret this value in apps that use the External Purchase APIs, for more details.

### Interpret this value in apps that use the External Purchase APIs

If your app has the entitlements to use the External Purchase APIs, use
`canMakePayments` to determine at runtime whether to use the External Purchase
or StoreKit In-App Purchase API based on the operating system, as follows:

For apps built with an SDK starting with iOS 17.4, iPadOS 17.4, macOS 14.4,
Mac Catalyst 17.4, tvOS 17.4, watchOS 10.4, and Xcode 13.3, and:

  * `canMakePayments` is `false`, your app can use only External Purchase APIs. 

  * `canMakePayments` is `true`, your app can use only the StoreKit In-App Purchase APIs and can offer in-app purchases.

For apps built with the iOS 15.4 through 17.3 SDKs, or iPadOS 15.4 through
17.3 SDKs:

  * Your app must check `canMakePayments` before attempting to use External Purchase APIs.

  * If `canMakePayments` is `true`, your app may proceed to call External Purchase APIs. 

  * If `canMakePayments` is `false`, don't call External Purchase APIs.

For all apps:

  * Anytime `canMakePayments` is `false`, your app can't use StoreKit In-App Purchase for offering in-app purchases.

Note

The StoreKit APIs always enable your app to view existing transactions and
receive auto-renewable subscription renewals, so your app can support your
customer’s existing purchases made through the App Store.

Type Property

# deviceVerificationID

The device verification identifier to use to verify whether signed information
is valid for the current device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var deviceVerificationID: UUID? { get }

## Discussion

Use this property to verify whether an App Store-signed JSON Web Signature
(JWS) is valid for the current device. The JWS may be one of the following:

  * A `jwsRepresentation` representing a signed transaction

  * A `jwsRepresentation` representing a signed subscription renewal information 

  * A `jwsRepresentation` representing a signed app transaction.

To verify that the JWS is valid for the current device, follow these steps:

  1. Append the lowercased UUID string representation of this property, `deviceVerificationID`, after the lowercased UUID string representation of the device verification nonce. For a transaction, the nonce is `deviceVerificationNonce`. For subscription renewal information, the nonce is `deviceVerificationNonce`. For an app transaction, the nonce is `deviceVerificationNonce`.

  2. Compute the SHA-384 hash of the appended UUID strings.

  3. Verify that the SHA-384 digest is equal to the device verification property. For a transaction, the device verification property is `deviceVerification`. For subscription renewal information, the device verification property is `deviceVerification`. For an app transaction, the device verifcation property is `deviceVerification`.

Type Method

# showManageSubscriptions(in:)

Presents the App Store sheet for managing subscriptions.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @MainActor
    static func showManageSubscriptions(in scene: UIWindowScene) async throws

##  Parameters

`scene`

    

The `UIWindowScene` that the system displays the sheet on.

## Discussion

Use this function to display the manage subscriptions sheet within your app.
Consider adding a manage subscriptions option to your app. For design guidance
on supporting this functionality, see Human Interface Guidelines > In-App
Purchase > Helping People Manage Their Subscriptions.

The `showManageSubscriptions(in:)` function presents a manage subscription
sheet that’s the same as what customers can view in their account settings in
the App Store app or by choosing Settings > Apple ID > Subscriptions on an iOS
or iPadOS device. The sheet displays the customer’s currently active
subscription for your app and the options to view, upgrade, downgrade, or
cancel their subscription.

If you’re using SwiftUI, call the `manageSubscriptionsSheet(isPresented:)`view
modifier.

Avoid showing the user interface for this feature in Mac apps built with Mac
Catalyst and on iOS apps running on Mac computers with Apple silicon because
this sheet isn’t supported in macOS.

  * In Mac apps built with Mac Catalyst, enclose the code in a compilation conditional block that uses the `targetEnvironment(): `platform condition. For more information on Mac Catalyst, see Creating a Mac version of your iPad app. 

  * For iOS apps running on Apple silicon, if `isiOSAppOnMac` is `true,` avoid showing the user interface for this feature.

### Test managing subscriptions

Test the managing subscriptions functionality in the sandbox environment and
StoreKit testing in Xcode. For more information about testing, see Testing at
all stages of development with Xcode and the sandbox and Setting up StoreKit
Testing in Xcode.

## See Also

### Managing subscriptions

`static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID:
String)`

Presents the App Store sheet for managing subscriptions for a subscription
group.

Type Method

# showManageSubscriptions(in:subscriptionGroupID:)

Presents the App Store sheet for managing subscriptions for a subscription
group.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+  Xcode 15.0+

    
    
    @MainActor
    static func showManageSubscriptions(
        in scene: UIWindowScene,
        subscriptionGroupID: String
    ) async throws

##  Parameters

`scene`

    

The `UIWindowScene` that the system displays the sheet on.

`subscriptionGroupID`

    

The subscription group identifier that the subscription belongs to.

## See Also

### Managing subscriptions

`static func showManageSubscriptions(in: UIWindowScene)`

Presents the App Store sheet for managing subscriptions.

Type Method

# requestReview(in:)

Tells StoreKit to request an App Store rating or review from the user, if
appropriate, using the specified scene.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @MainActor
    static func requestReview(in scene: UIWindowScene)

##  Parameters

`scene`

    

The `UIWindowScene` that StoreKit uses to present the rating and review
request interface.

## Discussion

When you call this method in your shipping app and the system displays a
rating and review request view, the system handles the entire process for you.
Although you normally call this method when it makes sense in the user
experience flow of your app, App Store policy governs the actual display of a
rating and review request view. When your app calls this API, StoreKit uses
the following criteria:

  * If the person hasn’t rated or reviewed your app on this device, StoreKit displays the ratings and review request a maximum of three times within a 365-day period.

  * If the person has rated or reviewed your app on this device, StoreKit displays the ratings and review request if the app version is new, and if more than 365 days have passed since the person’s previous review.

Note

Because this method may not present an alert, don’t call `requestReview()` or
`requestReview(in:)` in response to a button tap or other user action.

It’s up to your app to decide on the best timing for requesting reviews. For
design guidance, see Human Interface Guidelines > Ratings and reviews.

### Test review requests

When your app calls this method while it’s in development mode, StoreKit
always displays the rating and review request view, so you can test the user
interface and experience. However, this method has no effect in apps that you
distribute for beta testing using TestFlight.

### Provide a persistent link to your product page (optional)

Your customers can review your app at any time on the App Store. To make it
easier for people to leave reviews, you may include a persistent link to your
App Store product page in your app’s settings or configuration screens. Append
the query parameter `action=write-review` to your product page URL to
automatically open the App Store page where users can write a review.

## See Also

### Requesting reviews

`struct RequestReviewAction`

An instance that tells StoreKit to request an App Store rating or review, if
appropriate.

`static func requestReview(in: NSViewController)`

Tells StoreKit to request an App Store rating or review from the user, if
appropriate, using the specified view controller.

Type Method

# requestReview(in:)

Tells StoreKit to request an App Store rating or review from the user, if
appropriate, using the specified view controller.

macOS 13.0+  Xcode 14.0+

    
    
    @MainActor
    static func requestReview(in controller: NSViewController)

##  Parameters

`controller`

    

The `NSViewController` that StoreKit uses to present the rating and review
request interface.

## Discussion

When you call this method in your shipping app and the system displays a
rating and review request view, the system handles the entire process for you.
Although you normally call this method when it makes sense in the user
experience flow of your app, App Store policy governs the actual display of a
rating and review request view. When your app calls this API, StoreKit uses
the following criteria:

  * If the person hasn’t rated or reviewed your app on this device, StoreKit displays the ratings and review request a maximum of three times within a 365-day period.

  * If the person has rated or reviewed your app on this device, StoreKit displays the ratings and review request if the app version is new, and if more than 365 days have passed since the person’s previous review.

Note

Because this method may not present an alert, don’t call `requestReview(in:)`
in response to a button tap or other user action.

It’s up to your app to decide on the best timing for requesting reviews. For
design guidance, see Human Interface Guidelines > Ratings and reviews.

### Test review requests

When your app calls this method while it’s in development mode, StoreKit
always displays the rating and review request view, so you can test the user
interface and experience. However, this method has no effect in apps that you
distribute for beta testing using TestFlight.

### Provide a persistent link to your product page (optional)

Your customers can review your app at any time on the App Store. To make it
easier for people to leave reviews, you may include a persistent link to your
App Store product page in your app’s settings or configuration screens. Append
the query parameter `action=write-review` to your product page URL to
automatically open the App Store page where users can write a review.

## See Also

### Requesting reviews

`struct RequestReviewAction`

An instance that tells StoreKit to request an App Store rating or review, if
appropriate.

`static func requestReview(in: UIWindowScene)`

Tells StoreKit to request an App Store rating or review from the user, if
appropriate, using the specified scene.

Article

# Supporting subscription offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

## Overview

To help you acquire, retain, and win back subscribers, you can use offer
codes. Offer codes are alphanumeric codes that provide subscriptions at a
discount or for free for a specific duration. Configure the offers and create
offer codes in App Store Connect, and distribute them to your customers.
Customers can redeem offer codes in the App Store, using offer code redemption
URLs, or in your app if you’ve implemented one of the following APIs:

  * `offerCodeRedemption(isPresented:onCompletion:)` or `presentOfferCodeRedeemSheet(in:)`, which are available in iOS 16 and later and iPadOS 16 and later

  * `presentCodeRedemptionSheet()`, which is available in iOS 14 and later and iPadOS 14 and later

When customers redeem a valid offer code, your app receives a successful
transaction. If customers redeem offer codes in the App Store and don’t have
your app installed, they’re prompted to download it as part of the redemption
flow. Successfully redeeming an offer code entitles the customer to the auto-
renewable subscription, the same as a purchase does. Your app needs to provide
service for the product.

### Set up offer codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. You can
have up to 10 active offers per subscription, and create codes for a maximum
of 1,000,000 redemptions per app, per quarter. There are two types of offer
codes: one-time use codes, and custom codes. The offer code redemption APIs
support both.

Download the offer codes from App Store Connect to distribute them to your
customers. For more information on creating and distributing offer codes, and
to learn which type of offer code may work for your campaign, see Set up offer
codes.

### Redeem offer codes in your app

To display the system sheet for customers to redeem offer codes within your
app, call one of the redemption APIs, depending on your app’s UI
implementation:

  * Call `offerCodeRedemption(isPresented:onCompletion:)` if your app uses SwiftUI.

  * Call `presentOfferCodeRedeemSheet(in:)` if your app uses UIKit.

  * Call `presentCodeRedemptionSheet()` for apps running on devices prior to iOS 16 and iPadOS 16.

The redemption sheet takes care of the redemption flow, including alerting
users about invalid entries, as appropriate. Invalid entries may include, for
example, expired offer codes, invalid codes, or codes that would result in a
subscription downgrade.

Including the redemption sheet in your app is recommended, but optional. For
more guidance on supporting offer code redemption within your app, see Human
Interface Guidelines > In-app purchase.

### Support offer codes redeemed outside of your app

Customers may redeem offer codes outside your app, by entering the offer code
in the App Store, or by using a redemption URL. To handle offer codes — and
other transactions that can occur outside of your app — your app needs to use
`updates` on `Transaction` to receive new transactions while the app is
running. Create a `Task` to iterate through the transactions from the listener
as soon as your app launches. For more information and sample code, see
`updates`.

When the app launches, it needs to check `all` or `currentEntitlements` on
`Transaction` to get any transactions that may have occurred while the app
wasn’t running. Process the transactions to ensure your app provides service
for all products it’s entitled to.

### Identify subscriptions purchased with offer codes

When customers successfully redeem subscription offer codes, the transaction
or subscription renewal information contain fields that identify the offer and
its offer type. Find the offer code details in the transaction information, in
your app and on your server, as follows.

In your app, use the following StoreKit APIs to locate the offer code
information:

  * See the `Transaction` properties `offerID` and `offerType`. An offer type value of `code` indicates the customer redeemed an offer code.

  * Some offer code redemptions may apply to an auto-renewable subscription’s next renewal period, for example, if the customer is already subscribed. In this case, see the `Product.SubscriptionInfo.RenewalInfo` properties `offerID` and `offerType`. An offer type value of `code` indicates the customer redeemed an offer code.

On your server, use the following server-side APIs to locate offer code
information:

  * In the App Store Server API, when you call endpoints such as Get Transaction History, Get All Subscription Statuses, and others, the response contains the signed transaction, `JWSTransaction`. In its decoded payload, `JWSTransactionDecodedPayload`, look for the fields `offerIdentifier` and `offerType`. An `offerType` value of `3` indicates the customer redeemed an offer code.

  * The App Store Server Notifications V2 sends a notification with an `OFFER_REDEEMED` `notificationType` when someone redeems an offer code. The decoded payloads `JWSTransactionDecodedPayload` and `JWSRenewalInfoDecodedPayload` contain the fields `offerIdentifier` and `offerType`. An `offerType` value of `3` indicates the customer redeemed an offer code.

### Provide subscription service to new and existing customers

When you acquire new customers with an offer code, they already have an auto-
renewable subscription when they open your app for the first time. In addition
to providing subscription service, you may need to update your backend
system’s records. Your app follows these steps:

  1. When the app launches, check `all` or `currentEntitlements` on `Transaction` to get all transactions or current entitlements, respectively. StoreKit automatically validates the transactions, and returns verified results in `VerificationResult.verified(_:)`. To perform your own validation, use the `jwsRepresentation` property.

  2. To determine if a subscription results from an offer code redemption, check the `offerID` and `offerType` properties on the subscription’s `Transaction`. 

  3. Provide the subscription service based on the offer and call `finish()` on `Transaction`. 

  4. Guide new customers through your new-user experience, as needed. Update your backend system’s records.

When an existing customer redeems an offer code within your app, the
transaction comes in through the `updates` sequence on `Transaction`. Process
the transaction as usual, providing service based on the offer, and call
`finish()`.

Type Method

# presentOfferCodeRedeemSheet(in:)

Displays a sheet in the window scene that enables users to redeem a
subscription offer code that you configure in App Store Connect.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @MainActor
    static func presentOfferCodeRedeemSheet(in scene: UIWindowScene) async throws

##  Parameters

`scene`

    

The `UIWindowScene` that StoreKit uses to display the offer code redemption
sheet.

## Discussion

The `presentOfferCodeRedeemSheet(in:)` method displays a system sheet in the
window scene, where customers can enter and redeem subscription offer codes.
If you generate subscription offer codes in App Store Connect, call this
function to enable users to redeem the offer. To display the sheet using
SwiftUI, see `offerCodeRedemption(isPresented:onCompletion:)`.

Important

Set up subscription offer codes in App Store Connect before calling this API.
Customers can only redeem these offers in your app through the redemption
sheet; don’t use a custom UI.

For more information on offer codes, see Supporting subscription offer codes
in your app.

When customers redeem an offer code, StoreKit emits the resulting transaction
in `updates`. Set up a transaction listener as soon as your app launches to
receive new transactions while the app is running. For more information, see
`updates`.

In Mac apps built with Mac Catalyst, this method throws a
`StoreKitError.unknown` error.

## See Also

### Presenting the offer code redemption sheet

Supporting subscription offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: @MainActor
(Result<Void, any Error>) -> Void) -> View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

Instance Method

# offerCodeRedemption(isPresented:onCompletion:)

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 17.0+  visionOS 1.0+
Xcode 14.0+

    
    
    func offerCodeRedemption(
        isPresented: Binding<Bool>,
        onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }
    ) -> some View

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether the system displays the
sheet. You set the Boolean value to `true` to cause the system to display the
sheet. The system sets it to `false` when it dismisses the sheet.

`onCompletion`

    

A closure that returns the result of the presentation.

In Mac apps built with Mac Catalyst, the completion handler returns a failure
with an error.

## Discussion

The `offerCodeRedemption(isPresented:onCompletion:)` method displays a system
sheet where customers can enter and redeem subscription offer codes. If you
generate subscription offer codes in App Store Connect, call this function to
enable users to redeem the offer. To display the sheet using UIKit, see
`presentOfferCodeRedeemSheet(in:)`.

Important

Set up subscription offer codes in App Store Connect before calling this API.
Customers can only redeem these offers in your app through the redemption
sheet; don’t use a custom UI.

For more information, see Supporting subscription offer codes in your app.

The following code example shows a view that displays the offer code
redemption sheet upon a button press:

When customers redeem an offer code, StoreKit emits the resulting transaction
in `updates`. Set up a transaction listener as soon as your app launches to
receive new transactions while the app is running. For more information, see
`updates`.

In Mac apps built with Mac Catalyst, the completion handler returns a failure
with an error.

## See Also

### Presenting the offer code redemption sheet

Supporting subscription offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

`static func presentOfferCodeRedeemSheet(in: UIWindowScene)`

Displays a sheet in the window scene that enables users to redeem a
subscription offer code that you configure in App Store Connect.

Type Method

# sync()

Synchronizes your app’s transaction information and subscription status with
information from the App Store.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func sync() async throws

## Discussion

Include some mechanism in your app, such as a Restore Purchases button, to let
users restore their in-app purchases. In rare cases when a user suspects the
app isn’t showing all the transactions, call `sync()`. By calling `sync()`,
you force the app to obtain transaction information and subscription status
from the App Store.

Important

Calling `sync()`displays a system prompt that asks users to authenticate with
their App Store credentials. Call this function only in response to an
explicit user action, like tapping or clicking a button.

In regular operations, there’s no need to call `sync()`. StoreKit
automatically keeps up to date transaction information and subscription status
available to your app. When users reinstall your app or download it on a new
device, the app automatically has all transactions available to it upon
initial launch. There’s no need for users to ask your app to restore
transactions — your app can immediately get the current entitlements using
`currentEntitlements` and transaction history using `all`. For more
information about transactions, see `Transaction`.

