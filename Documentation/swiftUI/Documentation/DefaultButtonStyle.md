Initializer

# init()

Creates a default button style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func makeBody(configuration: DefaultButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

