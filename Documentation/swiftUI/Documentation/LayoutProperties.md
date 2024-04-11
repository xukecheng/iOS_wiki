Initializer

# init()

Creates a default set of properties.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use a layout properties instance to provide information about a type that
conforms to the `Layout` protocol. For example, you can create a layout
properties instance in your layout’s implementation of the `layoutProperties`
method, and use it to indicate that the layout has a `Axis.vertical`
orientation:

Instance Property

# stackOrientation

The orientation of the containing stack-like container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var stackOrientation: Axis?

## Discussion

Certain views alter their behavior based on the stack orientation of the
container that they appear in. For example, `Spacer` and `Divider` align their
major axis to match that of their container.

Set the orientation for your custom layout container by returning a configured
`LayoutProperties` instance from your `Layout` type’s implementation of the
`layoutProperties` method. For example, you can indicate that your layout has
a `Axis.vertical` major axis:

A value of `nil`, which is the default when you don’t specify a value,
indicates an unknown orientation, or that a layout isn’t one-dimensional.

