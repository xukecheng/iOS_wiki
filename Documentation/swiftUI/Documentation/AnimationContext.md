Instance Property

# state

The current state of a custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var state: AnimationState<Value>

## Discussion

An instance of `CustomAnimation` uses this property to read and write state
values as the animation runs.

An alternative to using the `state` property in a custom animation is to
create an `AnimationStateKey` type and extend `AnimationContext` with a custom
property that returns the state as a custom type. For example, the following
code creates a state key named `PausableState`. It’s convenient to store state
values in the key type, so the `PausableState` structure includes properties
for the stored state values `paused` and `pauseTime`.

To provide access the pausable state, the following code extends
`AnimationContext` to include the `pausableState` property. This property
returns an instance of the custom `PausableState` structure stored in `state`,
and it can also store a new `PausableState` instance in `state`.

Now a custom animation can use the `pausableState` property instead of the
`state` property as a convenient way to read and write state values as the
animation runs.

Instance Property

# environment

The current environment of the view that created the custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var environment: EnvironmentValues { get }

## Discussion

An instance of `CustomAnimation` uses this property to read environment values
from the view that created the animation. To learn more about environment
values including how to define custom environment values, see
`EnvironmentValues`.

Instance Method

# withState(_:)

Creates a new context from another one with a state that you provide.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func withState<T>(_ state: AnimationState<T>) -> AnimationContext<T> where T : VectorArithmetic

##  Parameters

`state`

    

The initial state for the new context.

## Return Value

A new context that contains the specified state.

## Discussion

Use this method to create a new context that contains the state that you
provide and view environment values from the original context.

Instance Property

# isLogicallyComplete

Set this to `true` to indicate that an animation is logically complete.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isLogicallyComplete: Bool

## Discussion

This controls when AnimationCompletionCriteria.logicallyComplete completion
callbacks are fired. This should be set to `true` at most once in the life of
an animation, changing back to `false` later will be ignored. If this is never
set to `true`, the behavior is equivalent to if this had been set to `true`
just as the animation finished (by returning `nil`).

