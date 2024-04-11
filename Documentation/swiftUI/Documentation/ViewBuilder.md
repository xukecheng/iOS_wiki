Type Method

# buildBlock()

Builds an empty view from a block containing no statements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock() -> EmptyView

## See Also

### Building content

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:)

Passes a single view written as a child view through unmodified.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> Content where Content : View

## Discussion

An example of a single view written as a child view is `{ Text("Hello") }`.

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock<each Content>(_ content: repeat each Content) -> TupleView<(repeat each Content)> where repeat each Content : View

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : View

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

Type Method

# buildEither(first:)

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : View, FalseContent : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildEither(second:)

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : View, FalseContent : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildIf(_:)

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildIf<Content>(_ content: Content?) -> Content? where Content : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildLimitedAvailability(_:)

Processes view content for a conditional compiler-control statement that
performs an availability check.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

