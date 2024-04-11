Type Property

# automatic

An effect that attempts to determine the effect automatically. This is the
default effect.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    static let automatic: HoverEffect

## See Also

### Getting hover effects

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

Type Property

# highlight

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 17.0+  visionOS 1.0+

    
    
    static let highlight: HoverEffect

## Discussion

On tvOS, it applies a projection effect accompanied with a specular highlight
on the view when contained within a focused view. It also incorporates motion
effects to produce a parallax effect by adjusting the projection matrix and
specular offset.

## See Also

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

Type Property

# lift

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    static let lift: HoverEffect

## See Also

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

