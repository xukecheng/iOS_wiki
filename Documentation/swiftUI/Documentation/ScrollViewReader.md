Initializer

# init(content:)

Creates an instance that can perform programmatic scrolling of its child
scroll views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: @escaping (ScrollViewProxy) -> Content)

##  Parameters

`content`

    

The reader’s content, containing one or more scroll views. This view builder
receives a `ScrollViewProxy` instance that you use to perform scrolling.

Instance Property

# content

The view builder that creates the reader’s content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var content: (ScrollViewProxy) -> Content

