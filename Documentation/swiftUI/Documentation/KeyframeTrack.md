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

