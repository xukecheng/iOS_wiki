Instance Property

# body

The content and behavior of the gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## See Also

### Implementing a custom gesture

`associatedtype Body : Gesture`

The type of gesture representing the body of `Self`.

**Required**

Associated Type

# Body

The type of gesture representing the body of `Self`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : Gesture

**Required**

## See Also

### Implementing a custom gesture

`var body: Self.Body`

The content and behavior of the gesture.

**Required**

Instance Method

# updating(_:body:)

Updates the provided gesture state property as the gesture’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func updating<State>(
        _ state: GestureState<State>,
        body: @escaping (Self.Value, inout State, inout Transaction) -> Void
    ) -> GestureStateGesture<Self, State>

##  Parameters

`state`

    

A binding to a view’s `GestureState` property.

`body`

    

The callback that SwiftUI invokes as the gesture’s value changes. Its
`currentState` parameter is the updated state of the gesture. The
`gestureState` parameter is the previous state of the gesture, and the
`transaction` is the context of the gesture.

## Return Value

A version of the gesture that updates the provided `state` as the originating
gesture’s value changes and that resets the `state` to its initial value when
the user or the system ends or cancels the gesture.

## Discussion

Use this callback to update transient UI state as described in Adding
interactivity with gestures.

## See Also

### Performing the gesture

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Instance Method

# onChanged(_:)

Adds an action to perform when the gesture’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onChanged(_ action: @escaping (Self.Value) -> Void) -> _ChangedGesture<Self>

Available when `Value` conforms to `Equatable`.

##  Parameters

`action`

    

The action to perform when this gesture’s value changes. The `action`
closure’s parameter contains the gesture’s new value.

## Return Value

A gesture that triggers `action` when this gesture’s value changes.

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Instance Method

# onEnded(_:)

Adds an action to perform when the gesture ends.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onEnded(_ action: @escaping (Self.Value) -> Void) -> _EndedGesture<Self>

##  Parameters

`action`

    

The action to perform when this gesture ends. The `action` closure’s parameter
contains the final value of the gesture.

## Return Value

A gesture that triggers `action` when the gesture ends.

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Associated Type

# Value

The type representing the gesture’s value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

Instance Method

# simultaneously(with:)

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func simultaneously<Other>(with other: Other) -> SimultaneousGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture that you want to combine with your gesture to create a new, combined
gesture.

## Return Value

A gesture with two simultaneous gestures.

## See Also

### Composing gestures

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

Instance Method

# sequenced(before:)

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sequenced<Other>(before other: Other) -> SequenceGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture you want to combine with another gesture to create a new, sequenced
gesture.

## Return Value

A gesture that’s a sequence of two gestures.

## See Also

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

Instance Method

# exclusively(before:)

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func exclusively<Other>(before other: Other) -> ExclusiveGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture you combine with your gesture, to create a new, combined gesture.

## Return Value

A gesture that’s the result of combining two gestures where only one of them
can succeed. SwiftUI gives precedence to the first gesture.

## See Also

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

Instance Method

# modifiers(_:)

Combines a gesture with keyboard modifiers.

macOS 10.15+

    
    
    func modifiers(_ modifiers: EventModifiers) -> _ModifiersGesture<Self>

##  Parameters

`modifiers`

    

A set of flags that correspond to the modifier keys that the user needs to
hold down.

## Return Value

A new gesture that combines a gesture with keyboard modifiers.

## Discussion

The gesture receives updates while the user presses the modifier keys that
correspond to the given modifiers option set.

Instance Method

# map(_:)

Returns a gesture that’s the result of mapping the given closure over the
gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func map<T>(_ body: @escaping (Self.Value) -> T) -> _MapGesture<Self, T>

Instance Method

# handActivationBehavior(_:)

Customizes the activation behavior for a gesture when driven by hand or hand-
like input.

visionOS 1.0+

    
    
    func handActivationBehavior(_ behavior: HandActivationBehavior) -> some Gesture<Self.Value>
    

##  Parameters

`behavior`

    

The hand activation behavior to use for the gesture.

## Return Value

A new gesture with a preference to activate with the provided behavior.

## Discussion

Use `automatic` to allow a gesture to activate with default system behaviors.
Use `pinch` when a gesture should only trigger when the hand is pinched.

For example, in a 3D chess application, a `DragGesture` that enables movement
of the pieces could use the pinch behavior to ensure that piece movement is
only possible when a hand is pinched in order to avoid pushing the piece
around by only touching it:

Instance Method

# targetedToAnyEntity()

Require this gesture to target an entity.

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
    

## Return Value

A `RealityCoordinateSpaceConvertible`value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

Instance Method

# targetedToEntity(_:)

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToEntity(_ entity: Entity) -> some Gesture<EntityTargetValue<Self.Value>>
    

##  Parameters

`entity`

    

The entity the gesture should target.

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

Instance Method

# targetedToEntity(where:)

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToEntity(where query: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
    

##  Parameters

`query`

    

a `QueryPredicate<Entity>` to filter which entity the gesture should target

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

