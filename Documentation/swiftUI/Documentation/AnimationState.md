Initializer

# init()

Create an empty state container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()

## Discussion

You don’t typically create an instance of `AnimationState` directly. Instead,
the `AnimationContext` provides the animation state to an instance of
`CustomAnimation`.

Instance Subscript

# subscript(_:)

Accesses the state for a custom key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : AnimationStateKey { get set }

## Overview

Create a custom animation state value by defining a key that conforms to the
`AnimationStateKey` protocol and provide the `defaultValue` for the key. Also
include properties to read and write state values that your `CustomAnimation`
uses. For example, the following code defines a key named `PausableState` that
has two state values, `paused` and `pauseTime`:

Use that key with the subscript operator of the `AnimationState` structure to
get and set a value for the key. For more convenient access to the key value,
extend `AnimationContext` with a computed property that gets and sets the
key’s value.

To access the state values in a `CustomAnimation`, call the custom computed
property, then read and write the state values that the custom
`AnimationStateKey` provides.

