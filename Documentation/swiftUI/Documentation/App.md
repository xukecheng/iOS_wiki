Instance Property

# body

The content and behavior of the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @SceneBuilder @MainActor
    var body: Self.Body { get }

**Required**

## Discussion

For any app that you create, provide a computed `body` property that defines
your app’s scenes, which are instances that conform to the `Scene` protocol.
For example, you can create a simple app with a single scene containing a
single view:

Swift infers the app’s `Body` associated type based on the scene provided by
the `body` property.

## See Also

### Implementing an app

`associatedtype Body : Scene`

The type of scene representing the content of the app.

**Required**

Associated Type

# Body

The type of scene representing the content of the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : Scene

**Required**

## Discussion

When you create a custom app, Swift infers this type from your implementation
of the required `body` property.

## See Also

### Implementing an app

`var body: Self.Body`

The content and behavior of the app.

**Required**

Initializer

# init()

Creates an instance of the app using the body that you define for its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    init()

**Required**

## Discussion

Swift synthesizes a default initializer for structures that don’t provide one.
You typically rely on the default initializer for your app.

## See Also

### Running an app

`static func main()`

Initializes and runs the app.

Type Method

# main()

Initializes and runs the app.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    static func main()

## Discussion

If you precede your `App` conformer’s declaration with the @main attribute,
the system calls the conformer’s `main()` method to launch the app. SwiftUI
provides a default implementation of the method that manages the launch
process in a platform-appropriate way.

## See Also

### Running an app

`init()`

Creates an instance of the app using the body that you define for its content.

**Required**

