Case

# AsyncImagePhase.empty

No image is loaded.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case empty

## See Also

### Getting load phases

`case success(Image)`

An image succesfully loaded.

`case failure(any Error)`

An image failed to load with an error.

Case

# AsyncImagePhase.success(_:)

An image succesfully loaded.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case success(Image)

## See Also

### Getting load phases

`case empty`

No image is loaded.

`case failure(any Error)`

An image failed to load with an error.

Case

# AsyncImagePhase.failure(_:)

An image failed to load with an error.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case failure(any Error)

## See Also

### Getting load phases

`case empty`

No image is loaded.

`case success(Image)`

An image succesfully loaded.

Instance Property

# image

The loaded image, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var image: Image? { get }

## Discussion

If this value isn’t `nil`, the image load operation has finished, and you can
use the image to update the view. You can use the image directly, or you can
modify it in some way. For example, you can add a
`resizable(capInsets:resizingMode:)` modifier to make the image resizable.

Instance Property

# error

The error that occurred when attempting to load an image, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var error: (any Error)? { get }

