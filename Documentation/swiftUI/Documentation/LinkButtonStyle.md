Initializer

# init()

Creates a link button style.

macOS 10.15+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

macOS 10.15+

    
    
    func makeBody(configuration: LinkButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

