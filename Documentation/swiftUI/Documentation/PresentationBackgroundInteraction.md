Type Property

# automatic

The default background interaction for the presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var automatic: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Property

# disabled

People can’t interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var disabled: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Property

# enabled

People can interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var enabled: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Method

# enabled(upThrough:)

People can interact with the view behind a presentation up through a specified
detent.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static func enabled(upThrough detent: PresentationDetent) -> PresentationBackgroundInteraction

##  Parameters

`detent`

    

The largest detent at which people can interact with the view behind the
presentation.

## Discussion

At detents larger than the one you specify, SwiftUI disables interaction.

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

