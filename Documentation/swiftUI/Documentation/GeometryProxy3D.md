Instance Method

# frame(in:)

The container view’s bounds rectangle converted to a defined coordinate space.

visionOS 1.0+

    
    
    func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> Rect3D

## See Also

### Accessing geometry characteristics

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# size

The size of the container view.

visionOS 1.0+

    
    
    var size: Size3D { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# safeAreaInsets

The safe area inset of the container view.

visionOS 1.0+

    
    
    var safeAreaInsets: EdgeInsets3D { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Subscript

# subscript(_:)

Resolves the value of an anchor to the container view.

visionOS 1.0+

    
    
    subscript<T>(anchor: Anchor<T>) -> T { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# transform(in:)

The container view’s 3D transform converted to a defined coordinate space.

visionOS 1.0+

    
    
    func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?

## Discussion

If the view doesn’t have a well-defined transform, such as if it’s affected by
a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

