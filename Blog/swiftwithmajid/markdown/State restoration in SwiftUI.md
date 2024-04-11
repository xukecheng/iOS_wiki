##  State restoration in SwiftUI

10 Mar 2022

We always want to provide a great user experience in our apps. The system can
shut down your app when the user leaves it and when the user relaunches your
app, the system creates it from scratch, and the current state of your app is
lost. This is a bad user experience. To avoid this kind of situation, we
should provide a state restoration mechanism. This week we will learn how to
implement state restoration in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  SceneStorage property wrapper

_State_ and _StateObject_ property wrappers are great tools to hold a view
state in runtime. The only problem is the ability to restore its value after
app relaunch. SwiftUI sets the initial values to _State_ and _StateObject_
whenever it recreates a view holding these property wrappers.

> To learn more about property wrappers in SwiftUI, take a look at my [
> “Understanding Property Wrappers in SwiftUI” ](/2019/06/12/understanding-
> property-wrappers-in-swiftui/) post.

Fortunately, SwiftUI provides us with the _SceneStorage_ property wrapper
allowing us to store values in the memory allocated by the current scene. It
means every scene has private storage that other scenes can’t access. The
system is entirely responsible for managing per-scene storage, and you don’t
have access to the data without the _SceneStorage_ property wrapper.

    
    
    struct RootView: View {
        @SceneStorage("selectedTab")
        private var selectedTab = 0
    
        var body: some View {
            TabView(selection: $selectedTab) {
                NavigationView {
                    TimerView()
                }
                .tabItem {
                    Image(systemName: "timer")
                    Text("timer")
                }
                .tag(0)
    
                NavigationView {
                    InsightsContainerView()
                        .navigationTitle("Insights")
                }
                .tabItem {
                    Image(systemName: "chart.bar")
                    Text("insights")
                }
                .tag(1)
            }
        }
    }
    

As you can see in the example above, we use the _SceneStorage_ property
wrapper to hold the tab selection. When the system relaunches the app, it also
restores the value of _SceneStorage_ property wrappers. The _SceneStorage_
property wrapper is an excellent tool for storing tab selection, active
navigation links, sheet presentation conditions, etc.

    
    
    struct RootView: View {
        @EnvironmentObject var store: Store<AppState, AppAction>
        
        @SceneStorage("bloodPressureFormShown")
        private var bloodPressureFormShown = false
        
        @SceneStorage("selectedTab")
        private var selectedTab = 0
    
        var body: some View {
            TabView(selection: $selectedTab) {
                NavigationView {
                    SummaryContainerView()
                        .navigationBarTitle("today")
                        .sheet(isPresented: $bloodPressureFormShown) {
                            AddBloodPressureView()
                        }
                    }
                    .tabItem {
                        Image(systemName: "heart")
                        Text("today")
                    }.tag(0)
                    
                    NavigationView {
                        SettingsView()
                    }
                    .tabItem {
                        Image(systemName: "gear")
                        Text("Settings")
                    }.tag(1)
                }
            }
        }
    }
    

Remember that the system doesn’t guarantee when and how often the data
persists. Make sure you don’t use _SceneStorage_ property wrapper with
sensitive data. _SceneStorage_ is not a replacement for the _State_ and
_StateObject_ property wrappers. It is designed to operate in pair with them.

> To learn more about scene management in SwiftUI, take a look at my [
> “Managing scenes in SwiftUI” ](/2020/08/26/managing-scenes-in-swiftui/)
> post.

####  User Activity

_UserActivity_ type is another option to provide a state restoration. It
allows us to mark a particular feature with unique data that the system
preserves across launches. For example, you can mark a purchase flow in the
e-commerce app with the purchased item identifier and any additional
information you need.

Whenever the system relaunches the app, it passes the instance of
_UserActivity_ type with the data populated previously. SwiftUI provides a few
view modifiers to populate and handle user activities in the app. Let’s take a
quick look at how we can use these view modifiers.

    
    
    struct PurchaseView: View {
        static let userActivity = "com.aaplab.app.purchase"
        let product: Product
    
        @State private var isPurchaseLinkActivated = false
    
        var body: some View {
            VStack {
                Text(product.title)
                NavigationLink(isActive: $isPurchaseLinkActivated) {
                        CheckoutView(product: product)
                    } label: {
                        Label("Go to checkout", systemImage: "creditcard")
                    }
            }
            .userActivity(
                PurchaseView.userActivity,
                isActive: isPurchaseLinkActivated
            ) { userActivity in
                userActivity.title = "Purchase \(product.title)"
                userActivity.userInfo = ["id": product.id]
            }
        }
    }
    

In the example above, we enable user activity when the user presses: “Go to
checkout” button. The system recognizes the user activity and stores it.
Whenever the system relaunches the app, it provides an instance of
_UserActivity_ type that we can grab and handle to continue the user flow.

    
    
    struct CommerceApp: App {
        var body: some Scene {
            WindowGroup {
                RootView()
                    .onContinueUserActivity(PurchaseView.userActivity) { userActivity in
                        if let id = userActivity.userInfo?["id"] {
                            // mutate the state of the app and navigate to the purchase view
                        }
                    }
            }
        }
    }
    

Here we use the _onContinueUserActivity_ view modifier to extract the instance
of _UserActivity_ type if it is available and navigate to the particular
screen.

####  Conclusion

State restoration is the key feature to implement a fluid user experience.
SwiftUI provides us with all the needed APIs to implement it quickly without
too many lines of code. I hope you enjoy the post. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

