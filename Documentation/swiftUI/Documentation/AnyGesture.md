Initializer

# init(_:)

Creates an instance from another gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<T>(_ gesture: T) where Value == T.Value, T : Gesture

##  Parameters

`gesture`

    

A gesture that you use to create a new gesture.

