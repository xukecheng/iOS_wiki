Type Property

# systemDark

An effect that dims passthrough video.

visionOS 1.0+

    
    
    static var systemDark: SurroundingsEffect { get }

## Discussion

Use this value with the `preferredSurroundingsEffect(_:)` view modifier when
you want to dim passthrough video while displaying a particular view. Doing so
helps to draw attention to your app’s content while still enabling people to
remain aware of their surroundings.

