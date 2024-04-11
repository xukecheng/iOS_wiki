Type Method

# point(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func point(_ p: CGPoint) -> Anchor<Value>.Source

Available when `Value` is `CGPoint`.

## See Also

### Getting point anchor sources

`static func unitPoint(UnitPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

Type Method

# unitPoint(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func unitPoint(_ p: UnitPoint) -> Anchor<Value>.Source

Available when `Value` is `CGPoint`.

## See Also

### Getting point anchor sources

`static func point(CGPoint) -> Anchor<Value>.Source`

Available when `Value` is `CGPoint`.

Type Method

# rect(_:)

Returns an anchor source rect defined by `r` in the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func rect(_ r: CGRect) -> Anchor<Value>.Source

Available when `Value` is `CGRect`.

## See Also

### Getting rectangle anchor sources

`static var bounds: Anchor<CGRect>.Source`

An anchor source rect defined as the entire bounding rect of the current view.

Available when `Value` is `CGRect`.

Type Property

# bounds

An anchor source rect defined as the entire bounding rect of the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bounds: Anchor<CGRect>.Source { get }

Available when `Value` is `CGRect`.

## See Also

### Getting rectangle anchor sources

`static func rect(CGRect) -> Anchor<Value>.Source`

Returns an anchor source rect defined by `r` in the current view.

Available when `Value` is `CGRect`.

Type Property

# topLeading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var topLeading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# top

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var top: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var topTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# topTrailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var topTrailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting top anchor sources

`static var topLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var top: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# leading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var leading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# center

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var center: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var trailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# trailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var trailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting middle anchor sources

`static var leading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var center: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottomTrailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottomTrailing: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottom

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottom: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottomLeading: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Type Property

# bottomLeading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bottomLeading: Anchor<CGPoint>.Source { get }

Available when `Value` is `CGPoint`.

## See Also

### Getting bottom anchor sources

`static var bottomTrailing: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

`static var bottom: Anchor<CGPoint>.Source`

Available when `Value` is `CGPoint`.

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ anchor: Anchor<T>.Source?) where Value == T?

## See Also

### Creating an anchor source

`init<T>([Anchor<T>.Source])`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ array: [Anchor<T>.Source]) where Value == [T]

## See Also

### Creating an anchor source

`init<T>(Anchor<T>.Source?)`

