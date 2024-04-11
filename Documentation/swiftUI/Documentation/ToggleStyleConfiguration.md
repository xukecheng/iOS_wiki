Instance Property

# label

A view that describes the effect of switching the toggle between states.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let label: ToggleStyleConfiguration.Label

## Discussion

Use this value in your implementation of the `makeBody(configuration:)` method
when defining a custom `ToggleStyle`. Access it through the that method’s
`configuration` parameter.

Because the label is a `View`, you can incorporate it into the view hierarchy
that you return from your style definition. For example, you can combine the
label with a circle image in an `HStack`:

## See Also

### Getting the label view

`struct Label`

A type-erased label of a toggle.

Structure

# ToggleStyleConfiguration.Label

A type-erased label of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Label

## Overview

SwiftUI provides a value of this type — which is a `View` type — as the
`label` to your custom toggle style implementation. Use the label to help
define the appearance of the toggle.

## Relationships

### Conforms To

  * `View`

## See Also

### Getting the label view

`let label: ToggleStyleConfiguration.Label`

A view that describes the effect of switching the toggle between states.

Instance Property

# isMixed

Whether the `Toggle` is currently in a mixed state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isMixed: Bool

## Discussion

Use this property to determine whether the toggle style should render a mixed
state presentation. A mixed state corresponds to an underlying collection with
a mix of true and false Bindings. To toggle the state, use the `Bool.toggle()`
method on the `isOn` binding.

In the following example, a custom style uses the `isMixed` property to render
the correct toggle state using symbols:

## See Also

### Managing the toggle state

`var isOn: Bool`

A binding to a state property that indicates whether the toggle is on.

`var $isOn: Binding<Bool>`

Instance Property

# isOn

A binding to a state property that indicates whether the toggle is on.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @Binding
    var isOn: Bool { get nonmutating set }

## Discussion

Because this value is a `Binding`, you can both read and write it in your
implementation of the `makeBody(configuration:)` method when defining a custom
`ToggleStyle`. Access it through that method’s `configuration` parameter.

Read this value to set the appearance of the toggle. For example, you can
choose between empty and filled circles based on the `isOn` value:

Write this value when the user takes an action that’s meant to change the
state of the toggle. For example, you can toggle it inside the `action`
closure of a `Button` instance:

## See Also

### Managing the toggle state

`var isMixed: Bool`

Whether the `Toggle` is currently in a mixed state.

`var $isOn: Binding<Bool>`

Instance Property

# $isOn

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var $isOn: Binding<Bool> { get }

## See Also

### Managing the toggle state

`var isMixed: Bool`

Whether the `Toggle` is currently in a mixed state.

`var isOn: Bool`

A binding to a state property that indicates whether the toggle is on.

Instance Property

# label

A view that describes the effect of switching the toggle between states.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let label: ToggleStyleConfiguration.Label

## Discussion

Use this value in your implementation of the `makeBody(configuration:)` method
when defining a custom `ToggleStyle`. Access it through the that method’s
`configuration` parameter.

Because the label is a `View`, you can incorporate it into the view hierarchy
that you return from your style definition. For example, you can combine the
label with a circle image in an `HStack`:

## See Also

### Getting the label view

`struct Label`

A type-erased label of a toggle.

Structure

# ToggleStyleConfiguration.Label

A type-erased label of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Label

## Overview

SwiftUI provides a value of this type — which is a `View` type — as the
`label` to your custom toggle style implementation. Use the label to help
define the appearance of the toggle.

## Relationships

### Conforms To

  * `View`

## See Also

### Getting the label view

`let label: ToggleStyleConfiguration.Label`

A view that describes the effect of switching the toggle between states.

Instance Property

# isMixed

Whether the `Toggle` is currently in a mixed state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isMixed: Bool

## Discussion

Use this property to determine whether the toggle style should render a mixed
state presentation. A mixed state corresponds to an underlying collection with
a mix of true and false Bindings. To toggle the state, use the `Bool.toggle()`
method on the `isOn` binding.

In the following example, a custom style uses the `isMixed` property to render
the correct toggle state using symbols:

## See Also

### Managing the toggle state

`var isOn: Bool`

A binding to a state property that indicates whether the toggle is on.

`var $isOn: Binding<Bool>`

Instance Property

# isOn

A binding to a state property that indicates whether the toggle is on.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @Binding
    var isOn: Bool { get nonmutating set }

## Discussion

Because this value is a `Binding`, you can both read and write it in your
implementation of the `makeBody(configuration:)` method when defining a custom
`ToggleStyle`. Access it through that method’s `configuration` parameter.

Read this value to set the appearance of the toggle. For example, you can
choose between empty and filled circles based on the `isOn` value:

    
    
    Image(systemName: configuration.isOn
        ? "checkmark.circle.fill"
        : "circle")
    

Write this value when the user takes an action that’s meant to change the
state of the toggle. For example, you can toggle it inside the `action`
closure of a `Button` instance:

    
    
    Button {
        configuration.isOn.toggle()
    } label: {
        // Draw the toggle.
    }
    

## See Also

### Managing the toggle state

`var isMixed: Bool`

Whether the `Toggle` is currently in a mixed state.

`var $isOn: Binding<Bool>`

Instance Property

# $isOn

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var $isOn: Binding<Bool> { get }

## See Also

### Managing the toggle state

`var isMixed: Bool`

Whether the `Toggle` is currently in a mixed state.

`var isOn: Bool`

A binding to a state property that indicates whether the toggle is on.

