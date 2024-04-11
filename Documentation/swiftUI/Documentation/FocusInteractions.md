Type Property

# automatic

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: FocusInteractions { get }

## See Also

### Creating the interaction types

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

Type Property

# activate

The view has a primary action that can be activated via focus gestures.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let activate: FocusInteractions

## Discussion

On macOS and iOS, focus-driven activation interactions are only possible when
all-controls keyboard navigation is enabled. On tvOS and watchOS, focus-driven
activation interactions are always possible.

## See Also

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

Type Property

# edit

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let edit: FocusInteractions

## Discussion

Views that support focus-driven editing interactions become focused when the
user taps or clicks on them, or when the user issues a focus movement command.

## See Also

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.

