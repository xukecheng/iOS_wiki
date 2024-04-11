Initializer

# init()

Creates a checkbox toggle style.

macOS 10.15+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `checkbox` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle checkbox.

macOS 10.15+

    
    
    func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that represents a checkbox.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `checkbox` toggle style. Don’t call
this method directly. Rather, the system calls this method for each `Toggle`
instance in a view hierarchy that’s styled as a checkbox.

