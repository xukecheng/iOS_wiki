# ZStack

Initializer

# init(alignment:content:)

Creates an instance with the given alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack on both the x- and y-axes.

`content`

    

A view builder that creates the content of this stack.



# ZStackLayout

Initializer

# init(alignment:)

Creates a stack with the specified alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(alignment: Alignment = .center)

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack on both the x- and y-axes.

Instance Property

# alignment

The alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: Alignment



