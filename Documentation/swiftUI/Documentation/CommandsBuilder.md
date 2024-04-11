Type Method

# buildBlock()

Builds an empty command set from a block containing no statements.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock() -> EmptyCommands

## See Also

### Building content

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:)

Passes a single command group written as a child group through modified.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C>(_ content: C) -> C where C : Commands

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> some Commands where C0 : Commands, C1 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
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
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands, C8 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
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
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands, C8 : Commands, C9 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

Type Method

# buildEither(first:)

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where T : Commands, F : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildEither(second:)

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where T : Commands, F : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildIf(_:)

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildIf<C>(_ content: C?) -> C? where C : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildLimitedAvailability(_:)

Processes commands for a conditional compiler-control statement that performs
an availability check.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildLimitedAvailability<C>(_ content: C) -> some Commands where C : Commands
    

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

