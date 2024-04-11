Initializer

# init()

Creates a bordered button style.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func makeBody(configuration: BorderedButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

Initializer

# init(tint:)

Creates a bordered button style with a tint color.

watchOS 7.0–10.4  Deprecated

    
    
    init(tint: Color)

Deprecated

Use `tint(_:)` instead.

