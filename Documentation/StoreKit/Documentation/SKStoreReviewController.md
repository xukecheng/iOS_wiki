Type Method

# requestReview(in:)

Tells StoreKit to ask the user to rate or review the app, if appropriate,
using the specified scene.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    class func requestReview(in windowScene: UIWindowScene)

##  Parameters

`windowScene`

    

The window scene that StoreKit uses to present the rating and review request
interface.

## Discussion

When you call this method in your shipping app and the system displays a
rating and review request view, the system handles the entire process for you.
Although you normally call this method when it makes sense in the user
experience flow of your app, App Store policy governs the actual display of a
rating and review request view. When your app calls this API, StoreKit uses
the following criteria::

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

### Indicating an appropriate time for a review

`class func requestReview()`

Tells StoreKit to ask the user to rate or review your app, if appropriate.

Type Method

# requestReview()

Tells StoreKit to ask the user to rate or review your app, if appropriate.

iOS 10.3–14.0  Deprecated  iPadOS 10.3–14.0  Deprecated  macOS 10.14+  Mac
Catalyst 13.1–14.0  Deprecated

    
    
    class func requestReview()

Deprecated

For iOS, iPadOS, and apps built with Mac Catalyst, use `requestReview(in:)`
instead.

## Discussion

Although you normally call this method when it makes sense in the user
experience flow of your app, App Store policy governs the actual display of a
rating and review request view. Because this method may not present an alert,
it isn’t appropriate to call `requestReview()` or `requestReview(in:)` in
response to a button tap or other user action.

Note

When you call this method while your app is in development mode, a rating and
review request view is always displayed so you can test the user interface and
experience. However, this method has no effect when you call it in an app that
you distribute using TestFlight.

When you call this method in your shipping app and the system displays a
rating and review request view, the system handles the entire process for you.
In addition, you can continue to include a persistent link in the settings or
configuration screens of your app that links to your App Store product page.
To automatically open a page on which users can write a review in the App
Store, append the query parameter `action=write-review` to your product URL.

## See Also

### Indicating an appropriate time for a review

`class func requestReview(in: UIWindowScene)`

Tells StoreKit to ask the user to rate or review the app, if appropriate,
using the specified scene.

