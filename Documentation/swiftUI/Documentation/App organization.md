Protocol

# App

A type that represents the structure and behavior of an app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol App

## Overview

Create an app by declaring a structure that conforms to the `App` protocol.
Implement the required `body` computed property to define the app’s content:

Precede the structure’s declaration with the @main attribute to indicate that
your custom `App` protocol conformer provides the entry point into your app.
The protocol provides a default implementation of the `main()` method that the
system calls to launch your app. You can have exactly one entry point among
all of your app’s files.

Compose the app’s body from instances that conform to the `Scene` protocol.
Each scene contains the root view of a view hierarchy and has a life cycle
managed by the system. SwiftUI provides some concrete scene types to handle
common scenarios, like for displaying documents or settings. You can also
create custom scenes.

You can declare state in your app to share across all of its scenes. For
example, you can use the `StateObject` attribute to initialize a data model,
and then provide that model on a view input as an `ObservedObject` or through
the environment as an `EnvironmentObject` to scenes in the app:

## Topics

### Implementing an app

`var body: Self.Body`

The content and behavior of the app.

**Required**

` associatedtype Body : Scene`

The type of scene representing the content of the app.

**Required**

### Running an app

`init()`

Creates an instance of the app using the body that you define for its content.

**Required**

` static func main()`

Initializes and runs the app.

## See Also

### Creating an app

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Backyard Birds: Building an app with SwiftData and widgets

Create an app with persistent data, interactive widgets, and an all new in-app
purchase experience.

Food Truck: Building a SwiftUI multiplatform app

Create a single codebase and app target for Mac, iPad, and iPhone.

Fruta: Building a Feature-Rich App with SwiftUI

Create a shared codebase to build a multiplatform app that offers widgets and
an App Clip.

Property List Key

# UILaunchScreen

The user interface to show while an app launches.

iOS 14.0+  iPadOS 14.0+

##  Details

Type

    

dictionary

## Discussion

You use this key to define the launch screen that the system displays while
your app launches. If you need to provide different launch screens in response
to being launched by different URL schemes, use `UILaunchScreens` instead.

Note

Use this key to configure the user interface during app launch in a way that
doesn’t rely on storyboards. If you prefer to use storyboards, use
`UILaunchStoryboardName` instead.

## Topics

### Main Interface

`property list key UIColorName`

The name of a color to use as the background color on the launch screen.

`property list key UIImageName`

The name of an image to display during app launch.

`property list key UIImageRespectsSafeAreaInsets`

A Boolean that specifies whether the launch image should respect the safe area
insets.

### Border Elements

`property list key UINavigationBar`

Navigation bar visibility and configuration during launch.

`property list key UITabBar`

Tab bar visibility and configuration during launch.

`property list key UIToolbar`

Toolbar visibility and configuration during launch.

## See Also

### Launch interface

`property list key UILaunchScreens`

The user interfaces to show while an app launches in response to different URL
schemes.

`property list key UILaunchStoryboardName`

The filename of the storyboard from which to generate the app’s launch image.

**Name:** Launch screen interface file base name

`property list key UILaunchStoryboards`

The launch storyboard to use to generate a launch image when your app opens
from a supported scheme.

`property list key LSUIPresentationMode`

The initial user-interface mode for the app.

**Name:** Application UI Presentation Mode

`property list key UILaunchToFullScreenByDefaultOnMac`

A Boolean value that indicates whether to launch your iPad app in full-screen
mode when running on a Mac.

Property List Key

# UILaunchScreens

The user interfaces to show while an app launches in response to different URL
schemes.

iOS 14.0+  iPadOS 14.0+

##  Details

Type

    

dictionary

## Discussion

You use this key if your app supports launching in response to one or more URL
schemes, and if you want to provide different launch screens for different
launch triggers. If you need only one launch screen, use `UILaunchScreen`
instead.

To define launch screens, create an array of dictionaries, each similar to the
one you might provide for `UILaunchScreen`, but with an added
`UILaunchScreenIdentifier` key that uniquely identifies the screen. Store the
array as the value for the `UILaunchScreenDefinitions` key.

To map from URL schemes to a launch screens, create a dictionary of schemes
and identifiers, and store it as the value for the
`UIURLToLaunchScreenAssociations` key. Additionally, indicate a default launch
screen by setting a value for the `UIDefaultLaunchScreen` key.

Note

Use this key to configure the user interface during app launch in a way that
doesn’t rely on storyboards. If you prefer to use storyboards to define the
launch screen, use the `UILaunchStoryboards` key instead.

## Topics

### Launch Screen Definitions

`property list key UILaunchScreenDefinitions`

A collection of launch screen configuration dictionaries.

### Associations

`property list key UIURLToLaunchScreenAssociations`

The mapping of URL schemes to launch screen configurations.

`property list key UIDefaultLaunchScreen`

The default launch screen configuration.

## See Also

### Launch interface

`property list key UILaunchScreen`

The user interface to show while an app launches.

`property list key UILaunchStoryboardName`

The filename of the storyboard from which to generate the app’s launch image.

**Name:** Launch screen interface file base name

`property list key UILaunchStoryboards`

The launch storyboard to use to generate a launch image when your app opens
from a supported scheme.

`property list key LSUIPresentationMode`

The initial user-interface mode for the app.

**Name:** Application UI Presentation Mode

`property list key UILaunchToFullScreenByDefaultOnMac`

A Boolean value that indicates whether to launch your iPad app in full-screen
mode when running on a Mac.

Structure

# UIApplicationDelegateAdaptor

A property wrapper type that you use to create a UIKit app delegate.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct UIApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : UIApplicationDelegate

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle,
define a type that conforms to the `UIApplicationDelegate` protocol, and
implement the delegate methods that you need. For example, you can implement
the `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method
to handle remote notification registration:

Then use the `UIApplicationDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given app. If you declare it more than once,
SwiftUI generates a runtime error.

If your app delegate conforms to the `ObservableObject` protocol, as in the
example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your app
using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an app’s life cycle events without using an app delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like
`application(_:didFinishLaunchingWithOptions:)`.

### Scene delegates

Some iOS apps define a `UIWindowSceneDelegate` to handle scene-based events,
like app shortcuts:

You can provide this kind of delegate to a SwiftUI app by returning the scene
delegate’s type from the `application(_:configurationForConnecting:options:)`
method inside your app delegate:

When you configure the `UISceneConfiguration` instance, you only need to
indicate the delegate class, and not a scene class or storyboard. SwiftUI
creates and manages the delegate instance, and sends it any relevant delegate
callbacks.

As with the app delegate, if you make your scene delegate an observable
object, SwiftUI automatically puts it in the `Environment`, from where you can
access it with the `EnvironmentObject` property wrapper, and create bindings
to its published properties.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`var wrappedValue: DelegateType`

The underlying app delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting iOS and iPadOS

UILaunchScreen

The user interface to show while an app launches.

UILaunchScreens

The user interfaces to show while an app launches in response to different URL
schemes.

Structure

# NSApplicationDelegateAdaptor

A property wrapper type that you use to create an AppKit app delegate.

macOS 11.0+

    
    
    @MainActor @propertyWrapper
    struct NSApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : NSApplicationDelegate

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle,
define a type that conforms to the `NSApplicationDelegate` protocol, and
implement the delegate methods that you need. For example, you can implement
the `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method
to handle remote notification registration:

Then use the `NSApplicationDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given app. If you declare it more than once,
SwiftUI generates a runtime error.

If your app delegate conforms to the `ObservableObject` protocol, as in the
example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your app
using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an app’s life cycle events without using an app delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like `applicationDidFinishLaunching(_:)`.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor.

`init(DelegateType.Type)`

Creates an AppKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `Observable`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`NSApplicationDelegate`, and `DelegateType` conforms to `ObservableObject`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

Structure

# WKApplicationDelegateAdaptor

A property wrapper that is used in `App` to provide a delegate from WatchKit.

watchOS 7.0+

    
    
    @MainActor @propertyWrapper
    struct WKApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKApplicationDelegate

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting watchOS

`struct WKExtensionDelegateAdaptor`

A property wrapper type that you use to create a WatchKit extension delegate.

Structure

# WKExtensionDelegateAdaptor

A property wrapper type that you use to create a WatchKit extension delegate.

watchOS 7.0+

    
    
    @MainActor @propertyWrapper
    struct WKExtensionDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKExtensionDelegate

## Overview

To handle extension delegate callbacks in an extension that uses the SwiftUI
life cycle, define a type that conforms to the `WKExtensionDelegate` protocol,
and implement the delegate methods that you need. For example, you can
implement the `didRegisterForRemoteNotifications(withDeviceToken:)` method to
handle remote notification registration:

Then use the `WKExtensionDelegateAdaptor` property wrapper inside your `App`
declaration to tell SwiftUI about the delegate type:

SwiftUI instantiates the delegate and calls the delegate’s methods in response
to life cycle events. Define the delegate adaptor only in your `App`
declaration, and only once for a given extension. If you declare it more than
once, SwiftUI generates a runtime error.

If your extension delegate conforms to the `ObservableObject` protocol, as in
the example above, then SwiftUI puts the delegate it creates into the
`Environment`. You can access the delegate from any scene or view in your
extension using the `EnvironmentObject` property wrapper:

This enables you to use the dollar sign (`$`) prefix to get a binding to
published properties that you declare in the delegate. For more information,
see `projectedValue`.

Important

Manage an externsion’s life cycle events without using a delegate whenever
possible. For example, prefer to handle changes in `ScenePhase` instead of
relying on delegate callbacks, like `applicationDidFinishLaunching()`.

## Topics

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`var wrappedValue: DelegateType`

The underlying delegate.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Targeting watchOS

`struct WKApplicationDelegateAdaptor`

A property wrapper that is used in `App` to provide a delegate from WatchKit.

