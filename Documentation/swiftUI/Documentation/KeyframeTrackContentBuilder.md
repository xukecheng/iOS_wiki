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

