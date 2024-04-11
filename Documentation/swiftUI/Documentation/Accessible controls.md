Structure

# AccessibilityActionKind

The structure that defines the kinds of available accessibility actions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityActionKind

## Topics

### Getting the kind of action

`static let `default`: AccessibilityActionKind`

The value that represents the default accessibility action.

`static let delete: AccessibilityActionKind`

`static let escape: AccessibilityActionKind`

The value that represents an accessibility action that dismisses a modal view
or cancels an operation.

`static let magicTap: AccessibilityActionKind`

`static let showMenu: AccessibilityActionKind`

### Creating an action type

`init(named: Text)`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Adding actions to views

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`enum AccessibilityAdjustmentDirection`

A directional indicator you use when making an accessibility adjustment.

Enumeration

# AccessibilityAdjustmentDirection

A directional indicator you use when making an accessibility adjustment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum AccessibilityAdjustmentDirection

## Topics

### Getting an adjustment direction

`case decrement`

`case increment`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding actions to views

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityActionKind`

The structure that defines the kinds of available accessibility actions.

Protocol

# AccessibilityQuickActionStyle

A type that describes the presentation style of an accessibility quick action.

watchOS 9.0+

    
    
    protocol AccessibilityQuickActionStyle

## Topics

### Getting built-in menu styles

`static var outline: AccessibilityQuickActionOutlineStyle`

A presentation style that animates an outline around the view when the
accessibility quick action is active.

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

`static var prompt: AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

### Supporting types

`struct AccessibilityQuickActionOutlineStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

`struct AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

## Relationships

### Conforming Types

  * `AccessibilityQuickActionOutlineStyle`
  * `AccessibilityQuickActionPromptStyle`

## See Also

### Offering Quick Actions to people

`func accessibilityQuickAction<Style, Content>(style: Style, content: () ->
Content) -> some View`

Adds a quick action to be shown by the system when active.

`func accessibilityQuickAction<Style, Content>(style: Style, isActive:
Binding<Bool>, content: () -> Content) -> some View`

Adds a quick action to be shown by the system when active.

Structure

# AccessibilityDirectTouchOptions

An option set that defines the functionality of a view’s direct touch area.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AccessibilityDirectTouchOptions

## Topics

### Getting the options

`static let requiresActivation: AccessibilityDirectTouchOptions`

Prevents touch passthrough with the direct touch area until an assistive
technology, such as VoiceOver, has activated the direct touch area through a
user action, for example a double tap.

`static let silentOnTouch: AccessibilityDirectTouchOptions`

Allows a direct touch area to immediately receive touch events without an
assitive technology, such as VoiceOver, speaking. Appropriate for apps that
provide direct audio feedback on touch that would conflict with speech
feedback.

### Creating a set of options

`init(rawValue: AccessibilityDirectTouchOptions.RawValue)`

Create a set of direct touch options

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Making gestures accessible

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityZoomGestureAction`

Position and direction information of a zoom gesture that someone performs
with an assistive technology like VoiceOver.

Structure

# AccessibilityZoomGestureAction

Position and direction information of a zoom gesture that someone performs
with an assistive technology like VoiceOver.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AccessibilityZoomGestureAction

## Topics

### Getting the action’s direction

`let direction: AccessibilityZoomGestureAction.Direction`

The zoom gesture’s direction.

`enum Direction`

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

### Getting location information

`let location: UnitPoint`

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.

`let point: CGPoint`

The zoom gesture’s activation point within the window’s coordinate space.

## See Also

### Making gestures accessible

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

`struct AccessibilityDirectTouchOptions`

An option set that defines the functionality of a view’s direct touch area.

Structure

# AccessibilityFocusState

A property wrapper type that can read and write a value that SwiftUI updates
as the focus of any active accessibility technology, such as VoiceOver,
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct AccessibilityFocusState<Value> where Value : Hashable

## Overview

Use this capability to request that VoiceOver or other accessibility
technologies programmatically focus on a specific element, or to determine
whether VoiceOver or other accessibility technologies are focused on
particular elements. Use `accessibilityFocused(_:equals:)` or
`accessibilityFocused(_:)` in conjunction with this property wrapper to
identify accessibility elements for which you want to get or set accessibility
focus. When accessibility focus enters the modified accessibility element, the
framework updates the wrapped value of this property to match a given
prototype value. When accessibility focus leaves, SwiftUI resets the wrapped
value of an optional property to `nil` or the wrapped value of a Boolean
property to `false`. Setting the property’s value programmatically has the
reverse effect, causing accessibility focus to move to whichever accessibility
element is associated with the updated value.

In the example below, when `notification` changes, and its `isPriority`
property is `true`, the accessibility focus moves to the notification `Text`
element above the rest of the view’s content:

To allow for cases where accessibility focus is completely absent from the
tree of accessibility elements, or accessibility technologies are not active,
the wrapped value must be either optional or Boolean.

Some initializers of `AccessibilityFocusState` also allow specifying
accessibility technologies, determining to which types of accessibility focus
this binding applies. If you specify no accessibility technologies, SwiftUI
uses an aggregate of any and all active accessibility technologies.

## Topics

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

`struct Binding`

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Controlling focus

`func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some
View`

Modifies this view by binding its accessibility element’s focus state to the
given boolean state value.

`func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding,
equals: Value) -> some View`

Modifies this view by binding its accessibility element’s focus state to the
given state value.

