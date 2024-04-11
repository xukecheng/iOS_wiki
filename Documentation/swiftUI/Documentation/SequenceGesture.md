Initializer

# init(_:_:)

Creates a sequence gesture with two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ first: First,
        _ second: Second
    )

##  Parameters

`first`

    

The first gesture of the sequence.

`second`

    

The second gesture of the sequence.

## See Also

### Creating the gesture

`var first: First`

The first gesture in a sequence of two gestures.

`var second: Second`

The second gesture in a sequence of two gestures.

Instance Property

# first

The first gesture in a sequence of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var first: First

## See Also

### Creating the gesture

`init(First, Second)`

Creates a sequence gesture with two gestures.

`var second: Second`

The second gesture in a sequence of two gestures.

Instance Property

# second

The second gesture in a sequence of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var second: Second

## See Also

### Creating the gesture

`init(First, Second)`

Creates a sequence gesture with two gestures.

`var first: First`

The first gesture in a sequence of two gestures.

Enumeration

# SequenceGesture.Value

The value of a sequence gesture that helps to detect whether the first gesture
succeeded, so the second gesture can start.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Value

## Topics

### Getting gesture values

`case first(First.Value)`

The first gesture hasn’t ended.

`case second(First.Value, Second.Value?)`

The first gesture has ended.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

