Case

# ScenePhase.active

The scene is in the foreground and interactive.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case active

## Discussion

An active scene isn’t necessarily front-most. For example, a macOS window
might be active even if it doesn’t currently have focus. Nevertheless, all
scenes should operate normally in this phase.

An app or custom scene in this phase contains at least one active scene
instance.

## See Also

### Getting scene phases

`case inactive`

The scene is in the foreground but should pause its work.

`case background`

The scene isn’t currently visible in the UI.

Case

# ScenePhase.inactive

The scene is in the foreground but should pause its work.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case inactive

## Discussion

A scene in this phase doesn’t receive events and should pause timers and free
any unnecessary resources. The scene might be completely hidden in the user
interface or otherwise unavailable to the user. In macOS, scenes only pass
through this phase temporarily on their way to the `ScenePhase.background`
phase.

An app or custom scene in this phase contains no scene instances in the
`ScenePhase.active` phase.

## See Also

### Getting scene phases

`case active`

The scene is in the foreground and interactive.

`case background`

The scene isn’t currently visible in the UI.

Case

# ScenePhase.background

The scene isn’t currently visible in the UI.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case background

## Discussion

Do as little as possible in a scene that’s in the `background` phase. The
`background` phase can precede termination, so do any cleanup work immediately
upon entering this state. For example, close any open files and network
connections. However, a scene can also return to the `ScenePhase.active` phase
from the background.

Expect an app that enters the `background` phase to terminate.

## See Also

### Getting scene phases

`case active`

The scene is in the foreground and interactive.

`case inactive`

The scene is in the foreground but should pause its work.

