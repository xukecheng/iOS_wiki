Initializer

# init(content:)

Creates a non-customizable Touch Bar view container.

macOS 10.15+

    
    
    init(@ViewBuilder content: () -> Content)

## See Also

### Creating a Touch Bar view

`init(id: String, content: () -> Content)`

Creates a customizable Touch Bar view container with a globally unique
identifier.

Initializer

# init(id:content:)

Creates a customizable Touch Bar view container with a globally unique
identifier.

macOS 10.15+

    
    
    init(
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`id`

    

A globally unique identifier for this Touch Bar.

`content`

    

A collection of views to be displayed by the Touch Bar.

## Discussion

Be sure that each view in `content` has an explicit `touchBarItemPresence`
value with customization identifier.

## See Also

### Creating a Touch Bar view

`init(content: () -> Content)`

Creates a non-customizable Touch Bar view container.

