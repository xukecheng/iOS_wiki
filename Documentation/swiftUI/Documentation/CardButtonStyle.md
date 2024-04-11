Initializer

# init()

Creates a style that doesn’t pad a button’s content and applies a motion
effect to a focused button.

tvOS 14.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

tvOS 14.0+

    
    
    func makeBody(configuration: CardButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy in
which `CardButtonStyle` is the current button style.

