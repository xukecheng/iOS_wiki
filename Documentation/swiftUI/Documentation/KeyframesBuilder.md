Type Method

# buildArray(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildArray(_ components: [some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
    

## See Also

### Building keyframes

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildBlock()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildBlock() -> some Keyframes<Value>
    

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildBlock()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildBlock() -> some KeyframeTrackContent<Value> where Value : Animatable
    

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildEither(first:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildEither<First, Second>(first component: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildEither(second:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildEither<First, Second>(second component: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildExpression(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildExpression<K>(_ expression: K) -> K where Value == K.Value, K : KeyframeTrackContent

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildExpression(_:)

Keyframes

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ expression: Content) -> Content where Value == Content.Value, Content : Keyframes

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildFinalResult(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildFinalResult<Content>(_ component: Content) -> KeyframeTrack<Value, Value, Content> where Value == Content.Value, Content : KeyframeTrackContent

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildFinalResult(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildFinalResult<Content>(_ component: Content) -> Content where Value == Content.Value, Content : Keyframes

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildPartialBlock(accumulated:next:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock(
        accumulated: some KeyframeTrackContent<Value>,
        next: some KeyframeTrackContent<Value>
    ) -> some KeyframeTrackContent<Value>
    

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildPartialBlock(accumulated:next:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock(
        accumulated: some Keyframes<Value>,
        next: some Keyframes<Value>
    ) -> some Keyframes<Value>
    

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildPartialBlock(first:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock<Content>(first: Content) -> Content where Value == Content.Value, Content : Keyframes

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

Type Method

# buildPartialBlock(first:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock<K>(first: K) -> K where Value == K.Value, K : KeyframeTrackContent

## See Also

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

