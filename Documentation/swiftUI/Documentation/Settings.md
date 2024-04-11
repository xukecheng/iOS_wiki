Initializer

# init(content:)

Creates a scene that presents an interface for viewing and modifying an app’s
preferences.

macOS 11.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

A view that represents the content of the scene.

## Discussion

Use `Settings(content:)` to add a preferences scene when you declare your app
using the `App` protocol.

The example below shows the view content for the settings scene added to the
SwiftUI app delegate:

When you use an `App` declaration for multiple platforms, compile the settings
scene only in macOS, as shown in the example above.

