##  Mastering StoreKit 2

01 Aug 2023

StoreKit provides us with an opportunity to make revenue from our apps. It
allows us to set up the purchase flow for in-app purchases and subscriptions.
StoreKit 2 introduces a modern Swift-based API to build type-safe in-app
purchases. This week we will start the series of posts about StoreKit 2.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

First, we must configure our project by adding in-app purchases in the
projects’ “Signing & Capabilities” tab. Next, we should create a StoreKit
configuration file to test in-app purchases without a network connection with
the App Store. Go to File -> New -> File and choose “StoreKit Configuration
File”.

You can create a local-only configuration file and populate it with test
subscriptions and in-app purchases. Another option is to fetch the list of
subscriptions and in-app purchases from the App Store Connect by enabling the
“Sync this file with an app in App Store Connect” checkbox.

The final step is to run your app with the predefined StoreKit configuration
file. You need to edit the scheme of your project, and in the options tab of
the run section, choose your StoreKit configuration file. Now you have a
fully-configured project allowing us to test in-app purchases in the Xcode.

Let’s start building our paywall feature by introducing the _Store_ type to
handle all the logic related to in-app purchases.

    
    
    import StoreKit
    
    @MainActor final class Store: ObservableObject {
        @Published private(set) var products: [Product] = []
        
        init() {}
        
        func fetchProducts() async {
            do {
                products = try await Product.products(
                    for: [
                        "123456789", "987654321"
                    ]
                )
            } catch {
                products = []
            }
        }
    }
    

As you can see in the example above, we define the _Store_ type fetching and
storing the list of products we will display on the paywall screen. The
StoreKit 2 framework provides the _Product_ type encapsulating all the logic
around an in-app purchase. The _Product_ type has a static function called
_products_ that we can use to fetch the list of products by providing a
collection of identifiers.

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        
        var body: some View {
            VStack {
                if store.products.isEmpty {
                    ProgressView()
                } else {
                    ForEach(store.products, id: \.id) { product in
                        Button {
                            Task {
                                try await store.purchase(product)
                            }
                        } label: {
                            VStack {
                                Text(verbatim: product.displayName)
                                    .font(.headline)
                                Text(verbatim: product.displayPrice)
                            }
                        }
                        .buttonStyle(.borderedProminent)
                    }
                }
            }
            .task {
                await store.fetchProducts()
            }
        }
    }
    

We use our _Store_ type to fetch and display the list of available in-app
purchases. An instance of the _Product_ type contains all information we need
to show, like the title, description, and price of an in-app purchase.

The _Product_ type also has the _purchase_ function that we can use to start
an in-app purchase flow for a particular product. It returns an instance of
the _PurchaseResult_ enum defining three cases: _success_ , _pending_ , and
_userCancelled_ .

    
    
    @MainActor final class Store: ObservableObject {
        // ...
        
        @Published private(set) var activeTransactions: Set<StoreKit.Transaction> = []
        
        func purchase(_ product: Product) async throws {
            let result = try await product.purchase()
            switch result {
            case .success(let verificationResult):
                if let transaction = try? verificationResult.payloadValue {
                    activeTransactions.insert(transaction)
                    await transaction.finish()
                }
            case .userCancelled:
                break
            case .pending:
                break
            @unknown default:
                break
            }
        }
    }
    

Whenever the purchase result is in the success state, it provides an
associated value of type _Transaction_ defining the successful transaction.
StoreKit wraps the transaction in the _VerificationResult_ type allowing us to
validate that transaction is correctly signed and comes from the App Store.

The _VerificationResult_ type used by StoreKit 2 to verify that the data is
valid and signed by the App Store. It provides us the _payloadValue_
calculated property that we can use to unwrap the signed data or throw an
error if the data is not correctly signed.

As soon as you retrieve the transaction, you should unlock the feature user
purchased and call the _finish_ function on the particular transaction.
Remember, you should always finish the transaction only after unlocking the
purchased feature.

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        
        var body: some View {
            VStack {
                Text("Purchased items: \(store.activeTransactions.count)")
                
                if store.products.isEmpty {
                    ProgressView()
                } else {
                    if store.activeTransactions.isEmpty {
                        ForEach(store.products, id: \.id) { product in
                            Button {
                                Task {
                                    try await store.purchase(product)
                                }
                            } label: {
                                VStack {
                                    Text(verbatim: product.displayName)
                                        .font(.headline)
                                    Text(verbatim: product.displayPrice)
                                }
                            }
                            .buttonStyle(.borderedProminent)
                        }
                    }
                }
            }
            .task {
                await store.fetchProducts()
            }
        }
    }
    

The purchase becomes pending whenever the ask to buy is enabled. In this case,
the transaction arrives later, only after approval by the parent. You should
observe the _Transaction.updates_ stream to handle this kind of transaction.
We must start monitoring this stream as soon as the app launches to never miss
a transaction.

    
    
    @MainActor final class Store: ObservableObject {
        @Published private(set) var activeTransactions: Set<StoreKit.Transaction> = []
        private var updates: Task<Void, Never>?
        
        // ...
        
        init() {
            updates = Task {
                for await update in StoreKit.Transaction.updates {
                    if let transaction = try? update.payloadValue {
                        await fetchActiveTransactions()
                        await transaction.finish()
                    }
                }
            }
        }
        
        deinit {
            updates?.cancel()
        }
    }
    

StoreKit 2 provides an easy way to fetch all active subscriptions and
purchased products. The _currentEntitlements_ property on _Transaction_ type
lists all the active subscriptions and not refunded products.

    
    
    @MainActor final class Store: ObservableObject {
        @Published private(set) var activeTransactions: Set<StoreKit.Transaction> = []
        // ...
        
        func fetchActiveTransactions() async {
            var activeTransactions: Set<StoreKit.Transaction> = []
            
            for await entitlement in StoreKit.Transaction.currentEntitlements {
                if let transaction = try? entitlement.payloadValue {
                    activeTransactions.insert(transaction)
                }
            }
            
            self.activeTransactions = activeTransactions
        }
    }
    

We can use the _currentEntitlements_ property to fetch all the active
purchases on every app launch or more often. By actively monitoring the
_currentEntitlements_ property we eliminate need for restoring purchases
because the _currentEntitlements_ always contains the latest list of active
subscriptions and non-consumable purchases even if they purchased on another
device.

    
    
    @main
    struct MyApp: App {
        @Environment(\.scenePhase) private var scenePhase
        @StateObject private var store = Store()
        
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .environmentObject(store)
                    .task(id: scenePhase) {
                        if scenePhase == .active {
                            await store.fetchActiveTransactions()
                        }
                    }
            }
        }
    }
    

Today we started the series of posts about StoreKit 2. As you can see, it is
really easy to use and it handle a bunch of use-cases out of the box for you.
I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

  1. Mastering StoreKit 2 
  2. [ Mastering StoreKit 2. ProductView and StoreView in SwiftUI. ](/2023/08/08/mastering-storekit2-productview-in-swiftui/)
  3. [ Mastering StoreKit 2. SubscriptionStoreView in SwiftUI ](/2023/08/23/mastering-storekit2-subscriptionstoreview-in-swiftui/)
  4. [ Mastering StoreKit 2. SwiftUI view modifiers. ](/2023/08/29/mastering-storekit2-swiftui-view-modifiers/)
  5. [ StoreKit testing in Swift ](/2024/01/09/storekit-testing-in-swift/)

