Initializer

# init(content:)

Creates a form with the provided content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

A `ViewBuilder` that provides the content for the form.

Initializer

# init(_:)

Creates a form based on a form style configuration.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ configuration: FormStyleConfiguration)

Available when `Content` is `FormStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the form.

