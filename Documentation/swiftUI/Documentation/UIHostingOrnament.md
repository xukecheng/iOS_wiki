Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this ornament.

visionOS 1.0+

    
    
    var rootView: Content { get set }

Instance Property

# contentAlignment

The alignment in the ornament used to position it.

visionOS 1.0+

    
    
    var contentAlignment: Alignment { get set }

Initializer

# init(sceneAnchor:contentAlignment:content:)

Creates an ornament with the specified alignment and content.

visionOS 1.0+

    
    
    init(
        sceneAnchor: UnitPoint,
        contentAlignment: Alignment = .center,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`sceneAnchor`

    

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

`contentAlignment`

    

The alignment in the ornament used to position it.

`content`

    

The content of the ornament.

Instance Property

# sceneAnchor

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

visionOS 1.0+

    
    
    var sceneAnchor: UnitPoint { get set }

