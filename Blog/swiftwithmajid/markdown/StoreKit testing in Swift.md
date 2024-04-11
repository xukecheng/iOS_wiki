##  StoreKit testing in Swift

09 Jan 2024

The second iteration of the StoreKit framework was the most significant change
in my apps during the last few years. The recent version of the StoreKit
framework has fully adopted Swift language features like _async_ and _await_ .
This week, we will talk about the StoreKitTest framework, which is not a part
of StoreKit 2 but is tightly coupled with it.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The StoreKitTest framework allows us to write tests for in-app product
purchasing, refunding, and restoring features. You can cover almost every
aspect of the in-app purchase with tests using the StoreKitTest framework.
Before starting, you should create a StoreKit Configuration File.

> To learn more about the basics of the StoreKit 2, take a look at my [
> “Mastering StoreKit 2” ](/2023/08/01/mastering-storekit2/) post.

The StoreKitTest framework provides us with the _SKTestSession_ type. Using an
instance of the _SKTestSession_ type, we can purchase in-app products, manage
transactions, refund and expire subscriptions, etc.

Let’s start by creating a test case for our StoreKit-related features. I
usually have a type called _SettingsStore_ , which defines user configuration
and handles in-app purchases. We will cover the in-app purchase management
part of the _SettingsStore_ with tests by using the StoreKitTest framework.

    
    
    @MainActor final class StoreKitTests: XCTestCase {
        func testProductPurchase() async throws {
            let session = try SKTestSession(configurationFileNamed: "SugarBot Food Calorie Counter")
            session.disableDialogs = true
            session.clearTransactions()
        }
    }
    

As you can see in the example above, we initialize an instance of the
_SKTestSession_ type. Then, we call the _clearTransactions_ function to remove
all the transactions we may have stored from the previous launches. We also
turn off dialogs to automate the purchase confirmation flow easily.

Now, we can use our _SettingsStore_ type to purchase products and process
subscription status. The _SKTestSession_ type also allows us to buy a product
that simulates the purchase outside the app. For example, it might be a
purchased product with family sharing enabled.

    
    
    @MainActor final class StoreKitTests: XCTestCase {
        var store: SettingsStore!
        
        override func setUp() {
            store = SettingsStore()
        }
        
        func testProductPurchase() async throws {
            let session = try SKTestSession(configurationFileNamed: "SugarBot Food Calorie Counter")
            session.disableDialogs = true
            session.clearTransactions()
            
            try await session.buyProduct(identifier: "annual")
            
            guard let product = try await Product.products(for: ["annual"]).first else {
                return XCTFail("Can't load products...")
            }
            
            let status = try await product.subscription?.status ?? []
            await store.processSubscriptionStatus(status)
            
            XCTAssertFalse(store.activeSubscriptions.isEmpty)
        }
    }
    

As you can see in the example above, we use the _buyProduct_ function on an
instance of the _SKTestSession_ type to simulate a purchase. We can also use
the _expireSubscription_ function of the _SKTestSession_ type to expire
ongoing subscriptions and verify how our app processes this data.

    
    
    @MainActor final class StoreKitTests: XCTestCase {
        var store: SettingsStore!
        
        override func setUp() {
            store = SettingsStore()
        }
        
        func testExpiredProduct() async throws {
            let session = try SKTestSession(configurationFileNamed: "SugarBot Food Calorie Counter")
            session.disableDialogs = true
            session.clearTransactions()
            
            let transaction = try await session.buyProduct(identifier: "annual")
            
            let activeProducts = try await Product.products(for: ["annual"])
            let activeStatus = try await activeProducts.first?.subscription?.status ?? []
            await store.processSubscriptionStatus(activeStatus)
            
            XCTAssertFalse(store.activeSubscriptions.isEmpty)
            
            try session.expireSubscription(productIdentifier: "annual")
            
            let expiredProducts = try await Product.products(for: ["annual"])
            let expiredStatus = try await expiredProducts.first?.subscription?.status ?? []
            await store.processSubscriptionStatus(expiredStatus)
            
            XCTAssertTrue(store.activeSubscriptions.isEmpty)
        }
    }
    

The _SKTestSession_ type also allows us to simulate product refunds using the
_refundTransaction_ function. Another exciting option is to test how the app
reacts to transaction updates.

    
    
    let transaction = try await session.buyProduct(identifier: "annual")
    // verify purchase ...
    try session.refundTransaction(identifier: UInt(transaction.id))
    // verify refund ...
    

You can also use the _askToBuyEnabled_ property to enable the ask-to-buy
feature and then use the _approveAskToBuyTransaction_ or
_declineAskToBuyTransaction_ functions to approve or decline purchases. In
this case, the transaction should change from pending to successful.

    
    
    session.askToBuyEnabled = true
    
    await store.purchase("annual")
    // verify purchase ...
    
    let declined = store.pendingTrancations.first?.id ?? 0
    try session.declineAskToBuyTransaction(identifier: UInt(declined.id))
    // verify purchase ...
    
    await store.purchase("annual")
    // verify purchase ...
    
    let approved = store.pendingTrancations.first?.id ?? 0
    try session.approveAskToBuyTransaction(identifier: UInt(approved.id))
    // verify purchase ...
    

As you can see in the example above, we use an instance of the SKTestSession
type to simulate ask-to-buy and verify the behavior of our app while the
purchase is approved or declined.

This week, we learned how to use the StoreKitTest framework to verify how our
app handles in-app purchases and user flows like refunds, ask-to-buy, and
subscription expiration. I hope you enjoy the post. Feel free to follow me on
[ Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

  1. [ Mastering StoreKit 2 ](/2023/08/01/mastering-storekit2/)
  2. [ Mastering StoreKit 2. ProductView and StoreView in SwiftUI. ](/2023/08/08/mastering-storekit2-productview-in-swiftui/)
  3. [ Mastering StoreKit 2. SubscriptionStoreView in SwiftUI ](/2023/08/23/mastering-storekit2-subscriptionstoreview-in-swiftui/)
  4. [ Mastering StoreKit 2. SwiftUI view modifiers. ](/2023/08/29/mastering-storekit2-swiftui-view-modifiers/)
  5. StoreKit testing in Swift 

