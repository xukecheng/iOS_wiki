Initializer

# init(configuration:)

Creates an overlay you use to recommend another app on the App Store.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(configuration: SKOverlay.Configuration)

##  Parameters

`configuration`

    

The object that represents the overlay’s attributes; for example, its position
on the screen.

## Discussion

Pass an `SKOverlay.AppConfiguration` as the `configuration` parameter if you
want to display the overlay in an app. To recommend an App Clip’s
corresponding app, pass an `SKOverlay.AppClipConfiguration` object to the
initializer. For more information, see Recommending your app to App Clip
users.

## See Also

### Creating an overlay

`var configuration: SKOverlay.Configuration`

An overlay’s attributes; for example, its position on the screen.

`class SKOverlay.AppConfiguration`

An object that represents the attributes of an overlay you use to recommend
another app on the App Store.

`class SKOverlay.AppClipConfiguration`

An object that represents the attributes of an overlay you use to recommend an
App Clip’s corresponding full app.

`class SKOverlay.Configuration`

The abstract superclass for all classes that represent an overlay’s
attributes.

Instance Property

# configuration

An overlay’s attributes; for example, its position on the screen.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @NSCopying
    var configuration: SKOverlay.Configuration { get }

## See Also

### Creating an overlay

`init(configuration: SKOverlay.Configuration)`

Creates an overlay you use to recommend another app on the App Store.

`class SKOverlay.AppConfiguration`

An object that represents the attributes of an overlay you use to recommend
another app on the App Store.

`class SKOverlay.AppClipConfiguration`

An object that represents the attributes of an overlay you use to recommend an
App Clip’s corresponding full app.

`class SKOverlay.Configuration`

The abstract superclass for all classes that represent an overlay’s
attributes.

Class

# SKOverlay.Configuration

The abstract superclass for all classes that represent an overlay’s
attributes.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    class Configuration : NSObject

## Relationships

### Inherits From

  * `NSObject`

## See Also

### Creating an overlay

`init(configuration: SKOverlay.Configuration)`

Creates an overlay you use to recommend another app on the App Store.

`var configuration: SKOverlay.Configuration`

An overlay’s attributes; for example, its position on the screen.

`class SKOverlay.AppConfiguration`

An object that represents the attributes of an overlay you use to recommend
another app on the App Store.

`class SKOverlay.AppClipConfiguration`

An object that represents the attributes of an overlay you use to recommend an
App Clip’s corresponding full app.

Instance Method

# present(in:)

Presents an overlay in a window scene.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    func present(in scene: UIWindowScene)

##  Parameters

`scene`

    

The window scene used to display the overlay.

Type Method

# dismiss(in:)

Dismisses an App Store overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    class func dismiss(in scene: UIWindowScene)

##  Parameters

`scene`

    

The window scene used to display the overlay.

Instance Property

# delegate

The overlay’s delegate.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    weak var delegate: (any SKOverlayDelegate)? { get set }

## See Also

### Setting a delegate

`protocol SKOverlayDelegate`

Methods for responding to the overlay’s appearance, dismissal, or failure to
load.

