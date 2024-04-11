Initializer

# init(_:_:)

Creates a gesture with two gestures that can receive updates or succeed
independently of each other.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ first: First,
        _ second: Second
    )

##  Parameters

`first`

    

The first of two gestures that can happen simultaneously.

`second`

    

The second of two gestures that can happen simultaneously.

## See Also

### Creating the gesture

`var first: First`

The first of two gestures that can happen simultaneously.

`var second: Second`

The second of two gestures that can happen simultaneously.

Instance Property

# first

The first of two gestures that can happen simultaneously.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var first: First

## See Also

### Creating the gesture

`init(First, Second)`

Creates a gesture with two gestures that can receive updates or succeed
independently of each other.

`var second: Second`

The second of two gestures that can happen simultaneously.

Instance Property

# second

The second of two gestures that can happen simultaneously.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var second: Second

## See Also

### Creating the gesture

`init(First, Second)`

Creates a gesture with two gestures that can receive updates or succeed
independently of each other.

`var first: First`

The first of two gestures that can happen simultaneously.

Structure

# SimultaneousGesture.Value

The value of a simultaneous gesture that indicates which of its two gestures
receives events.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Value

## Topics

### Getting gesture values

`var first: First.Value?`

The value of the first gesture.

`var second: Second.Value?`

The value of the second gesture.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

