Initializer

# init(minimumDuration:)

Creates a long-press gesture with a minimum duration

tvOS 14.0+

    
    
    init(minimumDuration: Double = 0.5)

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

## See Also

### Creating a long press gesture

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Initializer

# init(minimumDuration:maximumDistance:)

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10
    )

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`maximumDistance`

    

The maximum distance that the fingers or cursor performing the long press can
move before the gesture fails.

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Instance Property

# minimumDuration

The minimum duration of the long press that must elapse before the gesture
succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var minimumDuration: Double

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Instance Property

# maximumDistance

The maximum distance that the long press can move before the gesture fails.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var maximumDistance: CGFloat { get set }

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

