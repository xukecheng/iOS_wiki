##  UI Testing in Swift with XCTest framework

18 Mar 2021

I’m not going to talk about the importance of testing in general, but I want
to talk about UI testing. One obvious benefit of UI testing over Unit Testing
is the opportunity to write UI tests even when you have a smelling and deeply
coupled codebase. This week we will learn how to write UI tests both for
SwiftUI and UIKit-based projects.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

UI test is a programmatic way to verify that the particular user flow works
correctly in your app. For example, you can write a UI test to mimic user
behavior while adding a product to the shopping cart and checkout.

Xcode provides us XCTest framework that we use to write both unit and UI
tests. XCTest utilize Accessibility APIs to access controls in your view
hierarchy and interact with them. As you might know, UIKit and SwiftUI provide
accessibility support out of the box. That’s why you can easily use the XCTest
framework to write UI tests for your apps written in UIKit or SwiftUI.

> To learn more about accessibility support in UIKit, take a look at my [
> “Make your app accessible for everyone” ](/2018/07/09/make-your-app-
> accessible-for-everyone/) post.

Let’s start writing our first UI test for a simple view that displays a
message.

    
    
    struct ContentView: View {
        var body: some View {
            Text("Hello World!")
        }
    }
    

To create a new UI testing target, go to the Xcode menu _File - > New ->
Target -> UI Testing bundle _ . Now we can write our first UI test.

    
    
    import XCTest
    
    final class UITests: XCTestCase {
        var app: XCUIApplication!
    
        override func setUp() {
            continueAfterFailure = false
            app = XCUIApplication()
            app.launchArguments = ["testing"]
            app.launch()
        }
        
        func testWelcomeMessage() {
            XCTAssertTrue(app.staticTexts["Hello World!"].exists)
        }
    }
    

To write a UI test, we have to create a Swift class that extends _XCTestCase_
. Xcode runs every method that starts with the word **test** as a separate
test. As you can see in the example above, we override the _setUp_ method.
Xcode runs this method before every test in the test case. It is an excellent
place for an initial setup for every test.

Here we run the app from scratch before every UI test to keep them consistent
over multiple runs. XCTest provides us the _XCUIApplication_ class as a proxy
for the application specified by the “Target Application” target setting. We
can access and interact with our app via the instance of the _XCUIApplication_
class.

In our simple test, we verify that our app displays a static text with a
particular message.

####  Queries

_XCUIApplication_ provides a lot of properties to query view hierarchy. You
can access buttons, labels, tables, sliders, switches, and other views living
in your view hierarchy. The main requirement to access a view is enabled
accessibility. By default, accessibility support is enabled for any view.

    
    
    let email = app.textFields["email"]
    let pwd = app.secureTextFields["password"]
    let message = app.staticTexts["Hello World!"]
    let loginButton = app.buttons["login"]
    

As you can see, we can access all the needed views by using subscript syntax.
We pass a string to find a control in the view hierarchy. Xcode tries to find
the view matching accessibility label or accessibility identifier.

> To learn more about accessibility support in SwiftUI, take a look at my [
> “Accessibility in SwiftUI” ](/2019/09/10/accessibility-in-swiftui/) post.

Labels, buttons, and switches use titles as accessibility labels out of the
box. But you still need to set accessibility identifiers for views like
_UITableView_ and _UICollectionView_ manually.

    
    
    // UIKit
    let tableView = UITableView()
    tableView.accessibilityIdentifier = "newsList"
    
    // SwiftUI
    List {
        Text("news item")
    }.accessibilityIdentifier("newsList")
    

To learn more about query properties of _XCUIApplication_ , take a look at the
documentation for the _XCUIElementTypeQueryProvider_ protocol.

####  Actions

XCTest framework provides us a lot of functions for interacting with views.
You can easily tap, double-tap, swipe, pinch and rotate views.

    
    
    app.switches["rememberMe"].tap()
    app.buttons["login"].doubleTap()
    app.buttons["logout"].twoFingerTap()
    

To learn more about the actions that XCTest provides us, take a look at the
documentation for the _XCUIElement_ class.

####  Advanced example

Now we can interact with our app using the XCTest framework. Let’s write a
more interesting test that verifies login flow. Assume that you have a login
view written in SwiftUI. It might look like this:

    
    
    struct LoginView: View {
        @ObservedObject var viewModel: ViewModel
    
        var body: some View {
            Form {
                Section {
                    TextField("email", text: $viewModel.email)
                        .textContentType(.emailAddress)
                        .accessibilityLabel("email")
                    SecureField("password", text: $viewModel.password)
                        .textContentType(.password)
                        .accessibilityLabel("password")
                    Toggle("rememberMe", isOn: $viewModel.rememberMe)
                        .accessibilityIdentifier("rememberMe")
                }
    
                Button("login", action: viewModel.login)
            }
        }
    }
    
    struct ContentView: View {
        @StateObject var viewModel = ViewModel()
    
        var body: some View {
            if viewModel.isAuthorized {
                Text("Hello World!")
            } else {
                LoginView(viewModel: viewModel)
            }
        }
    }
    

Here we have the _ContentView_ that presents _LoginView_ and replace it with
the message as soon as the user logged in.

    
    
    import XCTest
    
    final class UITests: XCTestCase {
        var app: XCUIApplication!
    
        override func setUp() {
            continueAfterFailure = false
            app = XCUIApplication()
            app.launchArguments = ["testing"]
            app.launch()
        }
    
        func testLoginFlow() {
            let email = app.textFields["email"]
            email.tap()
            email.typeText("cmecid@gmail.com")
    
            let pwd = app.secureTextFields["password"]
            pwd.tap()
            pwd.typeText("pwd")
    
            app.switches["rememberMe"].tap()
            app.buttons["login"].doubleTap()
            app.buttons["login"].twoFingerTap()
    
            let message = app.staticTexts["Hello World!"]
            XCTAssertTrue(message.waitForExistence(timeout: 5))
        }
    }
    

In the example above, we have the test that verifies the login flow. Please
note that we use the _waitForExistence_ function here. It waits for a
particular timeout and returns **false** if the element doesn’t appear. On the
other hand, it returns **true** as soon as the element appears on the screen.

####  Performance

UI tests run slower than unit tests because they needs to run the whole app.
That’s why we usually try to write as many unit tests as we can and cover the
essential user flows with UI tests. But still, there is a way to improve
performance by disabling animations while running UI tests.

    
    
    final class AppDelegate: NSObject, UIApplicationDelegate {
        func applicationDidFinishLaunching(_ application: UIApplication) {
            if CommandLine.arguments.contains("testing") {
                // clear your app state before running UI tests here.
                UIView.setAnimationsEnabled(false)
            }
        }
    }
    

Here we check if the app runs under the UI test using command-line arguments.
In the previous examples, we set the launch arguments while running UI tests,
and this is how we can check arguments and prepare our app for UI tests. For
instance, we can reset the app state by removing user defaults, keychain data,
and cleaning the local database.

####  Conclusion

UI tests is an excellent way to verify the most crucial user flows in your
app. XCTest framework provides a very nice and simple API that we can utilize
to write complex tests straightforwardly. You can write your first UI test
without any refactoring just by interacting with your app user interface.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this article.
Thanks for reading, and see you next week!

