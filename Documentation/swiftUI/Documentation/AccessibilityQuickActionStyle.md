Type Property

# outline

A presentation style that animates an outline around the view when the
accessibility quick action is active.

watchOS 9.0+

    
    
    static var outline: AccessibilityQuickActionOutlineStyle { get }

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

## Discussion

Use the `contentShape(_:_:eoFill:)` modifier to provide a shape for
`focusEffect` if necessary.

The following example shows how to add an
`accessibilityQuickAction(style:content:)` to play and pause music.

## See Also

### Getting built-in menu styles

`static var prompt: AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

Type Property

# prompt

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    static var prompt: AccessibilityQuickActionPromptStyle { get }

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

## Discussion

The following example shows how to add an
`accessibilityQuickAction(style:content:)` to pause and resume a workout.

## See Also

### Getting built-in menu styles

`static var outline: AccessibilityQuickActionOutlineStyle`

A presentation style that animates an outline around the view when the
accessibility quick action is active.

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

Structure

# AccessibilityQuickActionOutlineStyle

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    struct AccessibilityQuickActionOutlineStyle

## Overview

Don’t use this type directly. Instead, use `outline`.

## Relationships

### Conforms To

  * `AccessibilityQuickActionStyle`

## See Also

### Supporting types

`struct AccessibilityQuickActionPromptStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

Structure

# AccessibilityQuickActionPromptStyle

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

watchOS 9.0+

    
    
    struct AccessibilityQuickActionPromptStyle

## Overview

Don’t use this type directly. Instead, use `prompt`.

## Relationships

### Conforms To

  * `AccessibilityQuickActionStyle`

## See Also

### Supporting types

`struct AccessibilityQuickActionOutlineStyle`

A presentation style that displays a prompt to the user when the accessibility
quick action is active.

