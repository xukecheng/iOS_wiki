Initializer

# init()

Creates a default toggle style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `automatic` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that acts as a toggle.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `automatic` toggle style. Don’t call
this method directly. Rather, the system calls this method for each `Toggle`
instance in a view hierarchy that needs the default style.

