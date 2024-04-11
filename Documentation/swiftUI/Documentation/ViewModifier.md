Instance Method

# body(content:)

Gets the current body of the caller.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    func body(content: Self.Content) -> Self.Body

**Required** Default implementation provided.

## Discussion

`content` is a proxy for the view that will have the modifier represented by
`Self` applied to it.

## Default Implementations

### ViewModifier Implementations

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

Available when `Body` is `Never`.

## See Also

### Creating a view modifier

`associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

Associated Type

# Body

The type of view representing the body.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`typealias Content`

The content view type passed to `body()`.

Type Alias

# ViewModifier.Content

The content view type passed to `body()`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Content

## See Also

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`associatedtype Body : View`

The type of view representing the body.

**Required**

Instance Method

# animation(_:)

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some ViewModifier
    

## See Also

### Adding animations to a view

`func concat<T>(T) -> ModifiedContent<Self, T>`

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

Instance Method

# concat(_:)

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func concat<T>(_ modifier: T) -> ModifiedContent<Self, T>

## See Also

### Adding animations to a view

`func animation(Animation?) -> some ViewModifier`

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

Instance Method

# transaction(_:)

Returns a new version of the modifier that will apply the transaction mutation
function `transform` to all transactions within the modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some ViewModifier
    

