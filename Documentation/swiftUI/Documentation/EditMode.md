Case

# EditMode.active

The user can edit the view content.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    case active

## Discussion

The `isEditing` property is `true` in this state.

## See Also

### Getting edit modes

`case inactive`

The user can’t edit the view content.

`case transient`

The view is in a temporary edit mode.

Case

# EditMode.inactive

The user can’t edit the view content.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    case inactive

## Discussion

The `isEditing` property is `false` in this state.

## See Also

### Getting edit modes

`case active`

The user can edit the view content.

`case transient`

The view is in a temporary edit mode.

Case

# EditMode.transient

The view is in a temporary edit mode.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    case transient

## Discussion

The use of this state varies by platform and for different controls. As an
example, SwiftUI might engage temporary edit mode over the duration of a swipe
gesture.

The `isEditing` property is `true` in this state.

## See Also

### Getting edit modes

`case active`

The user can edit the view content.

`case inactive`

The user can’t edit the view content.

Instance Property

# isEditing

Indicates whether a view is being edited.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    var isEditing: Bool { get }

## Discussion

This property returns `true` if the mode is something other than inactive.

