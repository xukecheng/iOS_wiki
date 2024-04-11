Initializer

# init(_:_:)

Creates a gesture from two gestures where only one of them succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ first: First,
        _ second: Second
    )

##  Parameters

`first`

    

The first of two gestures. This gesture has precedence over the other gesture.

`second`

    

The second of two gestures.

## See Also

### Creating the gesture

`var first: First`

The first of two gestures.

`var second: Second`

The second of two gestures.

Instance Property

# first

The first of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var first: First

## See Also

### Creating the gesture

`init(First, Second)`

Creates a gesture from two gestures where only one of them succeeds.

`var second: Second`

The second of two gestures.

Instance Property

# second

The second of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var second: Second

## See Also

### Creating the gesture

`init(First, Second)`

Creates a gesture from two gestures where only one of them succeeds.

`var first: First`

The first of two gestures.

Enumeration

# ExclusiveGesture.Value

The value of an exclusive gesture that indicates which of two gestures
succeeded.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Value

## Topics

### Getting gesture values

`case first(First.Value)`

The first of two gestures succeeded.

`case second(Second.Value)`

The second of two gestures succeeded.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

