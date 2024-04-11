Type Property

# identity

A transition that returns the input view, unmodified, as the output view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let identity: AnyTransition

## See Also

### Getting built-in transitions

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# move(edge:)

Returns a transition that moves the view away, towards the specified edge of
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func move(edge: Edge) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# offset(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func offset(_ offset: CGSize) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# offset(x:y:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# opacity

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let opacity: AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# push(from:)

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func push(from edge: Edge) -> AnyTransition

##  Parameters

`edge`

    

the edge from which the view will be animated in.

## Return Value

A transition that animates a view by moving and fading it.

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# scale

Returns a transition that scales the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var scale: AnyTransition { get }

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Method

# scale(scale:anchor:)

Returns a transition that scales the view by the specified amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func scale(
        scale: CGFloat,
        anchor: UnitPoint = .center
    ) -> AnyTransition

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Type Property

# slide

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var slide: AnyTransition { get }

## Discussion

See Also

`AnyTransition.move(edge:)`

## See Also

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

Instance Method

# animation(_:)

Attaches an animation to this transition.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> AnyTransition

## See Also

### Combining and configuring transitions

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

Type Method

# asymmetric(insertion:removal:)

Provides a composite transition that uses a different transition for insertion
versus removal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func asymmetric(
        insertion: AnyTransition,
        removal: AnyTransition
    ) -> AnyTransition

## See Also

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

Instance Method

# combined(with:)

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func combined(with other: AnyTransition) -> AnyTransition

## See Also

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

Initializer

# init(_:)

Create an instance that type-erases `transition`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<T>(_ transition: T) where T : Transition

## See Also

### Creating a custom transition

`static func modifier<E>(active: E, identity: E) -> AnyTransition`

Returns a transition defined between an active modifier and an identity
modifier.

Type Method

# modifier(active:identity:)

Returns a transition defined between an active modifier and an identity
modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func modifier<E>(
        active: E,
        identity: E
    ) -> AnyTransition where E : ViewModifier

## See Also

### Creating a custom transition

`init<T>(T)`

Create an instance that type-erases `transition`.

