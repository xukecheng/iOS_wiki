Initializer

# init()

Creates an accessory toolbar action button style

macOS 14.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

macOS 14.0+  visionOS 1.0+

    
    
    func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

