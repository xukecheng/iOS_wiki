Case

# GlassBackgroundDisplayMode.always

Always display the glass material.

visionOS 1.0+

    
    
    case always

## See Also

### Getting the mode

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.

`case never`

Never display the glass material.

Case

# GlassBackgroundDisplayMode.implicit

Display the glass material only when the view isn’t already contained in
glass.

visionOS 1.0+

    
    
    case implicit

## Discussion

Use this value to avoid duplicate backgrounds when a view that has a glass
background contains another view that also has a glass background.

This display mode doesn’t suppress duplicate glass backgrounds for views that
are offset by any amount in the z-axis. For example, the two subviews of the
following `HStack` behave differently:

The first instance of `MyView` doesn’t display a background because its
container displays one. However the second instance does display a background
because that view is offset from its container by 100 points along the z-axis.

## See Also

### Getting the mode

`case always`

Always display the glass material.

`case never`

Never display the glass material.

Case

# GlassBackgroundDisplayMode.never

Never display the glass material.

visionOS 1.0+

    
    
    case never

## See Also

### Getting the mode

`case always`

Always display the glass material.

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.

