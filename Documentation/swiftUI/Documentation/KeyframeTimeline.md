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

