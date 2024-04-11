Instance Method

# bounds(of:)

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func bounds(of coordinateSpace: NamedCoordinateSpace) -> CGRect?

## See Also

### Accessing geometry characteristics

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# frame(in:)

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func frame(in coordinateSpace: CoordinateSpace) -> CGRect

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# frame(in:)

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> CGRect

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# size

The size of the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var size: CGSize { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# safeAreaInsets

The safe area inset of the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var safeAreaInsets: EdgeInsets { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Subscript

# subscript(_:)

Resolves the value of an anchor to the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<T>(anchor: Anchor<T>) -> T { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# transform(in:)

The container view’s 3D transform converted to a defined coordinate space.

visionOS 1.0+

    
    
    func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?

## Discussion

If the view doesn’t have a well defined transform, such as if it is affected
by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

