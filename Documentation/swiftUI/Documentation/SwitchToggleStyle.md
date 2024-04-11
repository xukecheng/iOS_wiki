Initializer

# init()

Creates a switch toggle style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `switch` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle switch.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    func makeBody(configuration: SwitchToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that represents a switch.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `switch` toggle style. Don’t call
this method directly. Rather, the system calls this method for each `Toggle`
instance in a view hierarchy that’s styled as a switch.

Initializer

# init(tint:)

Creates a switch style with a tint color.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  watchOS 7.0–10.4  Deprecated
visionOS 1.0+

    
    
    init(tint: Color)

Deprecated

Use the `tint(_:)` view modifier instead.

