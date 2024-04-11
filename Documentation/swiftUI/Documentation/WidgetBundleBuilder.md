Type Method

# buildBlock()

Builds an empty Widget from a block containing no statements, `{ }`.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock() -> some Widget
    

## See Also

### Bundling widgets

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:)

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> some Widget where Content : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> some Widget where C0 : Widget, C1 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget, C8 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget, C8 : Widget, C9 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildLimitedAvailability(_:)

Processes widget content for a conditional compiler-control statement that
performs an availability check.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildLimitedAvailability(_ widget: some Widget) -> any Widget & _LimitedAvailabilityWidgetMarker

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildOptional(_:)

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildOptional(_ widget: (any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget
    

## Discussion

Conditional statements in a `WidgetBundleBuilder` can contain an `if`
statement but not an `else` statement, and the condition can only perform a
compiler check for availability, like in the following code:

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

