Type Property

# blurReplace

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var blurReplace: BlurReplaceTransition { get }

Available when `Self` is `BlurReplaceTransition`.

## See Also

### Getting built-in transitions

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# blurReplace(_:)

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func blurReplace(_ config: BlurReplaceTransition.Configuration = .downUp) -> Self

Available when `Self` is `BlurReplaceTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Property

# identity

A transition that returns the input view, unmodified, as the output view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var identity: IdentityTransition { get }

Available when `Self` is `IdentityTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# move(edge:)

Returns a transition that moves the view away, towards the specified edge of
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func move(edge: Edge) -> Self

Available when `Self` is `MoveTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# offset(_:)

Returns a transition that offset the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func offset(_ offset: CGSize) -> Self

Available when `Self` is `OffsetTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# offset(x:y:)

Returns a transition that offset the view by the specified x and y values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> Self

Available when `Self` is `OffsetTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Property

# opacity

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var opacity: OpacityTransition { get }

Available when `Self` is `OpacityTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# push(from:)

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func push(from edge: Edge) -> Self

Available when `Self` is `PushTransition`.

##  Parameters

`edge`

    

the edge from which the view will be animated in.

## Return Value

A transition that animates a view by moving and fading it.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Property

# scale

Returns a transition that scales the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scale: ScaleTransition { get }

Available when `Self` is `ScaleTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# scale(_:anchor:)

Returns a transition that scales the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func scale(
        _ scale: Double,
        anchor: UnitPoint = .center
    ) -> Self

Available when `Self` is `ScaleTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Property

# slide

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var slide: SlideTransition { get }

Available when `Self` is `SlideTransition`.

## Discussion

See Also

`AnyTransition.move(edge:)`

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Property

# symbolEffect

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var symbolEffect: SymbolEffectTransition { get }

Available when `Self` is `SymbolEffectTransition`.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

Type Method

# symbolEffect(_:options:)

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default
    ) -> SymbolEffectTransition where T : SymbolEffect, T : TransitionSymbolEffect

Available when `Self` is `SymbolEffectTransition`.

##  Parameters

`effect`

    

the symbol effect value.

## Return Value

a new transition.

## See Also

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

Instance Method

# animation(_:)

Attaches an animation to this transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some Transition
    

## See Also

### Configuring a transition

`static var properties: TransitionProperties`

Returns the properties this transition type has.

**Required** Default implementation provided.

Type Property

# properties

Returns the properties this transition type has.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var properties: TransitionProperties { get }

**Required** Default implementation provided.

## Discussion

Defaults to `TransitionProperties()`.

## Default Implementations

### Transition Implementations

`static var properties: TransitionProperties`

Returns the properties this transition type has.

## See Also

### Configuring a transition

`func animation(Animation?) -> some Transition`

Attaches an animation to this transition.

Instance Method

# apply(content:phase:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func apply<V>(
        content: V,
        phase: TransitionPhase
    ) -> some View where V : View
    

## See Also

### Using a transition

`func combined<T>(with: T) -> some Transition`

Instance Method

# combined(with:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func combined<T>(with other: T) -> some Transition where T : Transition
    

## See Also

### Using a transition

`func apply<V>(content: V, phase: TransitionPhase) -> some View`

Instance Method

# body(content:phase:)

Gets the current body of the caller.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func body(
        content: Self.Content,
        phase: TransitionPhase
    ) -> Self.Body

**Required**

## Discussion

`content` is a proxy for the view that will have the modifier represented by
`Self` applied to it.

## See Also

### Creating a custom transition

`associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

Associated Type

# Body

The type of view representing the body.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating a custom transition

`func body(content: Self.Content, phase: TransitionPhase) -> Self.Body`

Gets the current body of the caller.

**Required**

` typealias Content`

The content view type passed to `body()`.

Type Alias

# Transition.Content

The content view type passed to `body()`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    typealias Content = PlaceholderContentView<Self>

## See Also

### Creating a custom transition

`func body(content: Self.Content, phase: TransitionPhase) -> Self.Body`

Gets the current body of the caller.

**Required**

` associatedtype Body : View`

The type of view representing the body.

**Required**

Structure

# BlurReplaceTransition

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct BlurReplaceTransition

## Topics

### Creating the transition

`init(configuration: BlurReplaceTransition.Configuration)`

Creates a new transition.

`var configuration: BlurReplaceTransition.Configuration`

The transition configuration.

`struct Configuration`

Configuration properties for a transition.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# IdentityTransition

A transition that returns the input view, unmodified, as the output view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct IdentityTransition

## Topics

### Creating the transition

`init()`

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# MoveTransition

Returns a transition that moves the view away, towards the specified edge of
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct MoveTransition

## Topics

### Creating the transition

`init(edge: Edge)`

Creates a transition that moves the view away, towards the specified edge of
the view.

`var edge: Edge`

The edge to move the view towards.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# OffsetTransition

Returns a transition that offset the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct OffsetTransition

## Topics

### Creating the transition

`init(CGSize)`

Creates a transition that offset the view by the specified amount.

`var offset: CGSize`

The amount to offset the view by.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# OpacityTransition

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct OpacityTransition

## Topics

### Creating the transition

`init()`

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# PushTransition

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PushTransition

## Topics

### Creating the transition

`init(edge: Edge)`

Creates a transition that animates a view by moving and fading it.

`var edge: Edge`

The edge from which the view will be animated in.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# ScaleTransition

Returns a transition that scales the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ScaleTransition

## Topics

### Creating the transition

`init(Double, anchor: UnitPoint)`

Creates a transition that scales the view by the specified amount.

`var anchor: UnitPoint`

The anchor point to scale the view around.

`var scale: Double`

The amount to scale the view by.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Structure

# SlideTransition

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SlideTransition

## Overview

See Also

`MoveTransition`

## Topics

### Creating the transition

`init()`

## Relationships

### Conforms To

  * `Transition`

## See Also

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

