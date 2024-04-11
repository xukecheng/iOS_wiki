# KeyframeTimeline

Initializer

# init(initialValue:content:)

Creates a new instance using the initial value and content that you provide.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        @KeyframesBuilder<Value> content: () -> some Keyframes<Value>
    )

Instance Property

# duration

The duration of the content in seconds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var duration: TimeInterval { get }

Instance Method

# value(time:)

Returns the interpolated value at the given time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value(time: Double) -> Value

## See Also

### Getting an interpolated value

`func value(progress: Double) -> Value`

Returns the interpolated value at the given progress in the range zero to one.

Instance Method

# value(progress:)

Returns the interpolated value at the given progress in the range zero to one.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value(progress: Double) -> Value

## See Also

### Getting an interpolated value

`func value(time: Double) -> Value`

Returns the interpolated value at the given time.



# KeyframeTrackContentBuilder

Type Method

# buildArray(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildArray(_ components: [some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
    

## See Also

### Building keyframe track content

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildBlock()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildBlock() -> some KeyframeTrackContent<Value>
    

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildEither(first:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildEither<First, Second>(first component: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildEither(second:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildEither<First, Second>(second component: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildExpression(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildExpression<K>(_ expression: K) -> K where Value == K.Value, K : KeyframeTrackContent

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildPartialBlock(accumulated:next:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock(
        accumulated: some KeyframeTrackContent<Value>,
        next: some KeyframeTrackContent<Value>
    ) -> some KeyframeTrackContent<Value>
    

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Type Method

# buildPartialBlock(first:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func buildPartialBlock<K>(first: K) -> K where Value == K.Value, K : KeyframeTrackContent

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

Structure

# KeyframeTrackContentBuilder.Conditional

A conditional result from the result builder.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Conditional<ConditionalValue, First, Second> where ConditionalValue == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value

Available when `Value` conforms to `Animatable`.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`



# KeyframesBuilder

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



# KeyEquivalent

Type Property

# upArrow

Up Arrow (U+F700)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let upArrow: KeyEquivalent

## See Also

### Getting arrow keys

`static let downArrow: KeyEquivalent`

Down Arrow (U+F701)

`static let leftArrow: KeyEquivalent`

Left Arrow (U+F702)

`static let rightArrow: KeyEquivalent`

Right Arrow (U+F703)

Type Property

# downArrow

Down Arrow (U+F701)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let downArrow: KeyEquivalent

## See Also

### Getting arrow keys

`static let upArrow: KeyEquivalent`

Up Arrow (U+F700)

`static let leftArrow: KeyEquivalent`

Left Arrow (U+F702)

`static let rightArrow: KeyEquivalent`

Right Arrow (U+F703)

Type Property

# leftArrow

Left Arrow (U+F702)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let leftArrow: KeyEquivalent

## See Also

### Getting arrow keys

`static let upArrow: KeyEquivalent`

Up Arrow (U+F700)

`static let downArrow: KeyEquivalent`

Down Arrow (U+F701)

`static let rightArrow: KeyEquivalent`

Right Arrow (U+F703)

Type Property

# rightArrow

Right Arrow (U+F703)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let rightArrow: KeyEquivalent

## See Also

### Getting arrow keys

`static let upArrow: KeyEquivalent`

Up Arrow (U+F700)

`static let downArrow: KeyEquivalent`

Down Arrow (U+F701)

`static let leftArrow: KeyEquivalent`

Left Arrow (U+F702)

Type Property

# clear

Clear (U+F739)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let clear: KeyEquivalent

## See Also

### Getting other special keys

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# delete

Delete (U+0008)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let delete: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# deleteForward

Delete Forward (U+F728)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let deleteForward: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# end

End (U+F72B)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let end: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# escape

Escape (U+001B)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let escape: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# home

Home (U+F729)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let home: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# pageDown

Page Down (U+F72D)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let pageDown: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# pageUp

Page Up (U+F72C)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let pageUp: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# return

Return (U+000D)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let `return`: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# space

Space (U+0020)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let space: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let tab: KeyEquivalent`

Tab (U+0009)

Type Property

# tab

Tab (U+0009)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let tab: KeyEquivalent

## See Also

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

Initializer

# init(_:)

Creates a new key equivalent from the given character value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(_ character: Character)

## See Also

### Creating a key equivalent

`var character: Character`

The character value that the key equivalent represents.

Instance Property

# character

The character value that the key equivalent represents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var character: Character

## See Also

### Creating a key equivalent

`init(Character)`

Creates a new key equivalent from the given character value.



# KeyframeAnimator

Initializer

# init(initialValue:repeating:content:keyframes:)

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        repeating: Bool = true,
        @ViewBuilder content: @escaping (Value) -> Content,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> KeyframePath
    )

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`repeating`

    

Whether the keyframes are currently repeating. If false, the value at the
beginning of the keyframe timeline will be provided to the content closure.

`content`

    

A view builder closure that takes the interpolated value generated by the
keyframes as its single argument.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

## See Also

### Creating a phase animator

`init(initialValue: Value, trigger: some Equatable, content: (Value) ->
Content, keyframes: (Value) -> KeyframePath)`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

Initializer

# init(initialValue:trigger:content:keyframes:)

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (Value) -> Content,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> KeyframePath
    )

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`trigger`

    

A value to observe for changes.

`content`

    

A view builder closure that takes the interpolated value generated by the
keyframes as its single argument.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

If the trigger value changes while animating, the `keyframes` closure will be
called with the current interpolated value, and the keyframes that you return
define a new animation that replaces the old one. The previous velocity will
be preserved, so cubic or spring keyframes will maintain continuity from the
previous animation if they do not specify a custom initial velocity.

When a keyframe animation finishes, the animator will remain at the end value,
which becomes the initial value for the next animation.

## See Also

### Creating a phase animator

`init(initialValue: Value, repeating: Bool, content: (Value) -> Content,
keyframes: (Value) -> KeyframePath)`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.



# KeyframeTrack

Initializer

# init(content:)

Creates an instance that animates the entire value from the root of the key
path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(@KeyframeTrackContentBuilder<Root> content: () -> Content) where Root == Value

##  Parameters

`keyframes`

    

A keyframe collection builder closure containing the keyframes that control
the interpolation curve.

## See Also

### Creating a keyframe track

`init(WritableKeyPath<Root, Value>, content: () -> Content)`

Creates an instance that animates the property of the root value at the given
key path.

Initializer

# init(_:content:)

Creates an instance that animates the property of the root value at the given
key path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ keyPath: WritableKeyPath<Root, Value>,
        @KeyframeTrackContentBuilder<Value> content: () -> Content
    )

##  Parameters

`keyPath`

    

The property to animate.

`keyframes`

    

A keyframe collection builder closure containing the keyframes that control
the interpolation curve.

## See Also

### Creating a keyframe track

`init(content: () -> Content)`

Creates an instance that animates the entire value from the root of the key
path.



# KeyPress.Phases

Type Property

# down

The user pressed down on a key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let down: KeyPress.Phases

## See Also

### Getting the phases

`static let up: KeyPress.Phases`

The user released a key.

`static let `repeat`: KeyPress.Phases`

The user held a key down to issue a sequence of repeating events.

`static let all: KeyPress.Phases`

A value that matches all key press phases.

Type Property

# up

The user released a key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let up: KeyPress.Phases

## See Also

### Getting the phases

`static let down: KeyPress.Phases`

The user pressed down on a key.

`static let `repeat`: KeyPress.Phases`

The user held a key down to issue a sequence of repeating events.

`static let all: KeyPress.Phases`

A value that matches all key press phases.

Type Property

# repeat

The user held a key down to issue a sequence of repeating events.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let `repeat`: KeyPress.Phases

## See Also

### Getting the phases

`static let down: KeyPress.Phases`

The user pressed down on a key.

`static let up: KeyPress.Phases`

The user released a key.

`static let all: KeyPress.Phases`

A value that matches all key press phases.

Type Property

# all

A value that matches all key press phases.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let all: KeyPress.Phases

## See Also

### Getting the phases

`static let down: KeyPress.Phases`

The user pressed down on a key.

`static let up: KeyPress.Phases`

The user released a key.

`static let `repeat`: KeyPress.Phases`

The user held a key down to issue a sequence of repeating events.



# KeyPress.Result

Case

# KeyPress.Result.handled

The action consumed the event, preventing dispatch from continuing.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    case handled

## See Also

### Getting the result

`case ignored`

The action ignored the event, allowing dispatch to continue.

Case

# KeyPress.Result.ignored

The action ignored the event, allowing dispatch to continue.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    case ignored

## See Also

### Getting the result

`case handled`

The action consumed the event, preventing dispatch from continuing.



# Keyframes

Instance Property

# body

The composition of content that comprise the keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @KeyframesBuilder<Self.Value> var body: Self.Body { get }

**Required**

## See Also

### Creating a keyframe

`associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

Associated Type

# Body

The type of keyframes representing the body of this type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Body : Keyframes

**Required**

## Discussion

When you create a custom keyframes type, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

Associated Type

# Value

The type of value animated by this keyframes type

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Value = Self.Body.Value

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**



# KeyboardShortcut

Type Property

# cancelAction

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let cancelAction: KeyboardShortcut

## See Also

### Getting standard shortcuts

`static let defaultAction: KeyboardShortcut`

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

Type Property

# defaultAction

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let defaultAction: KeyboardShortcut

## Discussion

On macOS, the default button is designated with special coloration. If more
than one control is assigned this shortcut, only the first one is emphasized.

## See Also

### Getting standard shortcuts

`static let cancelAction: KeyboardShortcut`

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

Initializer

# init(_:modifiers:)

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    )

## Discussion

The localization configuration defaults to `automatic`.

## See Also

### Creating a shortcut

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

Instance Property

# key

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var key: KeyEquivalent

## See Also

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

Instance Property

# modifiers

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var modifiers: EventModifiers

## See Also

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

Initializer

# init(_:modifiers:localization:)

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    )

## Discussion

Use the `localization` parameter to specify a localization strategy for this
shortcut.

## See Also

### Creating a localized shortcut

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

Instance Property

# localization

The localization strategy to apply to this shortcut.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var localization: KeyboardShortcut.Localization

## See Also

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

Structure

# KeyboardShortcut.Localization

Options for how a keyboard shortcut participates in automatic localization.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct Localization

## Overview

A shortcut’s `key` that is defined on an US-English keyboard layout might not
be reachable on international layouts. For example the shortcut `⌘[` works
well for the US layout but is hard to reach for German users. On the German
keyboard layout, pressing `⌥5` will produce `[`, which causes the shortcut to
become `⌥⌘5`. If configured, which is the default behavior, automatic shortcut
remapping will convert it to `⌘Ö`.

In addition to that, some keyboard shortcuts carry information about
directionality. Right-aligning a block of text or seeking forward in context
of music playback are such examples. These kinds of shortcuts benefit from the
option `withoutMirroring` to tell the system that they won’t be flipped when
running in a right-to-left context.

## Topics

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.



# KeyboardShortcut.Localization

Type Property

# automatic

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let automatic: KeyboardShortcut.Localization

## Discussion

This is the default configuration.

## See Also

### Getting localization strategies

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

Type Property

# custom

Don’t use automatic shortcut remapping.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let custom: KeyboardShortcut.Localization

## Discussion

When you use this mode, you have to take care of international use-cases
separately.

## See Also

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

Type Property

# withoutMirroring

Don’t mirror shortcuts.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let withoutMirroring: KeyboardShortcut.Localization

## Discussion

Use this for shortcuts that always have a specific directionality, like
aligning something on the right.

Don’t use this option for navigational shortcuts like “Go Back” because
navigation is flipped in right-to-left contexts.

## See Also

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.



# KeyframeTrackContent

Instance Property

# body

The composition of content that comprise the keyframe track.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @KeyframeTrackContentBuilder<Self.Value> var body: Self.Body { get }

**Required**

## See Also

### Creating a keyframe

`associatedtype Body : KeyframeTrackContent`

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

Associated Type

# Body

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Body : KeyframeTrackContent

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

Associated Type

# Value

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Value : Animatable = Self.Body.Value

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Body : KeyframeTrackContent`

**Required**



# KeyPress

Instance Property

# key

The key equivalent value for the pressed key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let key: KeyEquivalent

## See Also

### Getting the keypress

`let characters: String`

The characters generated by the pressed key as if no modifier key applies.

`let modifiers: EventModifiers`

The set of modifier keys the user held in addition to the pressed key.

Instance Property

# characters

The characters generated by the pressed key as if no modifier key applies.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let characters: String

## See Also

### Getting the keypress

`let key: KeyEquivalent`

The key equivalent value for the pressed key.

`let modifiers: EventModifiers`

The set of modifier keys the user held in addition to the pressed key.

Instance Property

# modifiers

The set of modifier keys the user held in addition to the pressed key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let modifiers: EventModifiers

## See Also

### Getting the keypress

`let key: KeyEquivalent`

The key equivalent value for the pressed key.

`let characters: String`

The characters generated by the pressed key as if no modifier key applies.

Instance Property

# phase

The phase of the key-press event (`.down`, `.repeat`, or `.up`).

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let phase: KeyPress.Phases

## See Also

### Getting the phase of the keypress

`struct Phases`

Options for matching different phases of a key-press event.

Structure

# KeyPress.Phases

Options for matching different phases of a key-press event.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Phases

## Topics

### Getting the phases

`static let down: KeyPress.Phases`

The user pressed down on a key.

`static let up: KeyPress.Phases`

The user released a key.

`static let `repeat`: KeyPress.Phases`

The user held a key down to issue a sequence of repeating events.

`static let all: KeyPress.Phases`

A value that matches all key press phases.

## Relationships

### Conforms To

  * `CustomDebugStringConvertible`
  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Getting the phase of the keypress

`let phase: KeyPress.Phases`

The phase of the key-press event (`.down`, `.repeat`, or `.up`).

Enumeration

# KeyPress.Result

A result value returned from a key-press action that indicates whether the
action consumed the event.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    enum Result

## Topics

### Getting the result

`case handled`

The action consumed the event, preventing dispatch from continuing.

`case ignored`

The action ignored the event, allowing dispatch to continue.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`



