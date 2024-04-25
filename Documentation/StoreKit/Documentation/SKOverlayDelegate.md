Instance Method

# storeOverlayWillStartPresentation(_:transitionContext:)

Indicates that the platform presents an overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    optional func storeOverlayWillStartPresentation(
        _ overlay: SKOverlay,
        transitionContext: SKOverlay.TransitionContext
    )

##  Parameters

`overlay`

    

An overlay object that’s about to appear.

`transitionContext`

    

A context you can use to animate changes to UI components as the overlay
appears.

## Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main
thread. For example, make a `UIImageView` disappear by animating the change of
its opacity to 0% as shown in the following code:

## See Also

### Responding to the Overlay’s Appearance and Disappearance

`func storeOverlayDidFinishPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform finished presenting an overlay.

`func storeOverlayWillStartDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform dismisses an overlay.

`func storeOverlayDidFinishDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that platform finished dismissing an overlay.

`class SKOverlay.TransitionContext`

A context object you can use to animate UI changes while the platform presents
or dismisses an overlay.

Instance Method

# storeOverlayDidFinishPresentation(_:transitionContext:)

Indicates that the platform finished presenting an overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    optional func storeOverlayDidFinishPresentation(
        _ overlay: SKOverlay,
        transitionContext: SKOverlay.TransitionContext
    )

##  Parameters

`overlay`

    

The overlay object that appears.

`transitionContext`

    

A context you can use to animate changes to UI components after the overlay
appears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance

`func storeOverlayWillStartPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform presents an overlay.

`func storeOverlayWillStartDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform dismisses an overlay.

`func storeOverlayDidFinishDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that platform finished dismissing an overlay.

`class SKOverlay.TransitionContext`

A context object you can use to animate UI changes while the platform presents
or dismisses an overlay.

Instance Method

# storeOverlayWillStartDismissal(_:transitionContext:)

Indicates that the platform dismisses an overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    optional func storeOverlayWillStartDismissal(
        _ overlay: SKOverlay,
        transitionContext: SKOverlay.TransitionContext
    )

##  Parameters

`overlay`

    

An overlay object that’s about to disappear.

`transitionContext`

    

The context you can use to animate changes to UI components when the overlay
disappears.

## Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main
thread. For example, make a `UIImageView` appear by animating the change of
its opacity to 100%`,` as shown in the following code:

## See Also

### Responding to the Overlay’s Appearance and Disappearance

`func storeOverlayWillStartPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform presents an overlay.

`func storeOverlayDidFinishPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform finished presenting an overlay.

`func storeOverlayDidFinishDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that platform finished dismissing an overlay.

`class SKOverlay.TransitionContext`

A context object you can use to animate UI changes while the platform presents
or dismisses an overlay.

Instance Method

# storeOverlayDidFinishDismissal(_:transitionContext:)

Indicates that platform finished dismissing an overlay.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    optional func storeOverlayDidFinishDismissal(
        _ overlay: SKOverlay,
        transitionContext: SKOverlay.TransitionContext
    )

##  Parameters

`overlay`

    

An app banner object that disappeared.

`transitionContext`

    

The context you can use to animate changes to UI components when the overlay
disappears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance

`func storeOverlayWillStartPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform presents an overlay.

`func storeOverlayDidFinishPresentation(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform finished presenting an overlay.

`func storeOverlayWillStartDismissal(SKOverlay, transitionContext:
SKOverlay.TransitionContext)`

Indicates that the platform dismisses an overlay.

`class SKOverlay.TransitionContext`

A context object you can use to animate UI changes while the platform presents
or dismisses an overlay.

Instance Method

# storeOverlayDidFailToLoad(_:error:)

Indicates that an overlay failed to load.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    optional func storeOverlayDidFailToLoad(
        _ overlay: SKOverlay,
        error: any Error
    )

##  Parameters

`overlay`

    

An overlay object that failed to load.

`error`

    

An indication of why the overlay failed to load.

## Discussion

Common cases for a failure when loading an overlay are:

  * Using invalid iTunes identifiers.

  * Trying to present an overlay for media that’s not an app.

  * Trying to present an overlay from an app extension or the simulator.

