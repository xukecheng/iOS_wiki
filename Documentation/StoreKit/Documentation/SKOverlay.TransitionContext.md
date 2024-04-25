Instance Method

# addAnimation(_:)

Adds a closure you can use to animate view properties.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+

    
    
    func addAnimation(_ block: @escaping () -> Void)

##  Parameters

`block`

    

A closure that sets animatable view properties and runs on the main thread.

## See Also

### Adding an Animation

`var startFrame: CGRect`

The size and location of the overlay before the transition.

`var endFrame: CGRect`

The size and location of the overlay at the end of the transition.

Instance Property

# startFrame

The size and location of the overlay before the transition.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+

    
    
    var startFrame: CGRect { get }

## See Also

### Adding an Animation

`func addAnimation(() -> Void)`

Adds a closure you can use to animate view properties.

`var endFrame: CGRect`

The size and location of the overlay at the end of the transition.

Instance Property

# endFrame

The size and location of the overlay at the end of the transition.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+

    
    
    var endFrame: CGRect { get }

## See Also

### Adding an Animation

`func addAnimation(() -> Void)`

Adds a closure you can use to animate view properties.

`var startFrame: CGRect`

The size and location of the overlay before the transition.

