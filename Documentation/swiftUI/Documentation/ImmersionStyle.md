Type Property

# automatic

The default immersion style.

visionOS 1.0+

    
    
    static var automatic: AutomaticImmersionStyle { get }

Available when `Self` is `AutomaticImmersionStyle`.

## Discussion

The system uses this style for an `ImmersiveSpace` if you don’t provide an
`immersionStyle(selection:in:)` scene modifier. You don’t typically specify
the `automatic` style explicitly.

By default, the system uses the `mixed` immersion style as the `automatic`
style.

## See Also

### Getting built-in styles

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# full

An immersion style that displays unbounded content that completely replaces
passthrough video.

visionOS 1.0+

    
    
    static var full: FullImmersionStyle { get }

Available when `Self` is `FullImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`.

When using this style, the space’s content fully obscures passthrough except
for the user’s upper limbs. You can manage limb visibility separately by
applying the `upperLimbVisibility(_:)` scene modifier to the space, or the
view modifier equivalent to a view inside the scene.

The immersion style affects how windows interact with virtual objects in the
environment. In `full` immersion, windows always render in front of virtual
content, no matter how someone positions the window or the content. This helps
people to avoid losing track of windows behind virtual content when
passthrough is off.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# mixed

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

visionOS 1.0+

    
    
    static var mixed: MixedImmersionStyle { get }

Available when `Self` is `MixedImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`. However, this is the default immersion style if you
don’t specify one.

The immersion style affects how windows interact with virtual objects in the
environment. In `mixed` immersion, a virtual object obscures part or all of a
window that’s behind the object. Similarly, a window obscures a virtual object
that’s behind the window.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# progressive

An immersion style that displays unbounded content that partially replaces
passthrough video.

visionOS 1.0+

    
    
    static var progressive: ProgressiveImmersionStyle { get }

Available when `Self` is `ProgressiveImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`.

The system initially uses a radial portal effect that replaces passthrough in
a portion of the field of view. People can interactively adjust the size of
the portal by rotating the Digital Crown, including down to the point where
the portal disappears and up to the point where the portal fully replaces
passthrough. The latter matches the behavior of the `full` immersion style,
including the configurable visibility of the viewer’s upper limbs.

The immersion style affects how windows interact with virtual objects in the
environment. In `progressive` immersion, windows always render in front of
virtual content, no matter how someone positions the window or the content.
This helps people to avoid losing track of windows behind virtual content when
passthrough is off.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

Structure

# AutomaticImmersionStyle

The default style of immersive spaces.

visionOS 1.0+

    
    
    struct AutomaticImmersionStyle

## Overview

You don’t typically use this style explicitly, but if you need to, use
`automatic` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# FullImmersionStyle

An immersion style that displays unbounded content that completely replaces
passthrough video.

visionOS 1.0+

    
    
    struct FullImmersionStyle

## Overview

Use `full` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# MixedImmersionStyle

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

visionOS 1.0+

    
    
    struct MixedImmersionStyle

## Overview

Use `mixed` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# ProgressiveImmersionStyle

An immersion style that displays unbounded content that partially replaces
passthrough video.

visionOS 1.0+

    
    
    struct ProgressiveImmersionStyle

## Overview

Use `progressive` with the `immersionStyle(selection:in:)`modifier to specify
this style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

