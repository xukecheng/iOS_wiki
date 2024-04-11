Initializer

# init(base:state:body:)

Creates a new gesture that’s the result of an ongoing gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        base: Base,
        state: GestureState<State>,
        body: @escaping (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void
    )

##  Parameters

`base`

    

The originating gesture.

`state`

    

The wrapped value of a `GestureState` property.

`body`

    

The callback that SwiftUI invokes as the gesture’s value changes.

## See Also

### Creating an in-progress gesture

`var base: Base`

The originating gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

Instance Property

# base

The originating gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var base: Base

## See Also

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

Instance Property

# state

A value that changes as the user performs the gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var state: GestureState<State>

## See Also

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var base: Base`

The originating gesture.

Instance Property

# body

The updating gesture containing the originating gesture’s value, the updated
state of the gesture, and a transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void

