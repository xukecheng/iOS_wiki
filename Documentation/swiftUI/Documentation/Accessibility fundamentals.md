Structure

# AccessibilityChildBehavior

Defines the behavior for the child elements of the new parent element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityChildBehavior

## Topics

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Creating accessible elements

`func accessibilityElement(children: AccessibilityChildBehavior) -> some View`

Creates a new accessibility element, or modifies the
`AccessibilityChildBehavior` of the existing accessibility element.

`func accessibilityChildren<V>(children: () -> V) -> some View`

Replaces the existing accessibility element’s children with one or more new
synthetic accessibility elements.

`func accessibilityRepresentation<V>(representation: () -> V) -> some View`

Replaces one or more accessibility elements for this view with new
accessibility elements.

Structure

# AccessibilityTechnologies

Accessibility technologies available to the system.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityTechnologies

## Topics

### Getting technology types

`static var switchControl: AccessibilityTechnologies`

The value that represents a Switch Control, allowing the use of the entire
system using controller buttons, a breath-controlled switch or similar
hardware.

`static var voiceOver: AccessibilityTechnologies`

The value that represents the VoiceOver screen reader, allowing use of the
system without seeing the screen visually.

### Creating a technology type

`init()`

Creates a new accessibility technologies structure with an empy accessibility
technology set.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Supporting types

`struct AccessibilityAttachmentModifier`

A view modifier that adds accessibility properties to the view

Structure

# AccessibilityAttachmentModifier

A view modifier that adds accessibility properties to the view

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityAttachmentModifier

## Relationships

### Conforms To

  * `ViewModifier`

## See Also

### Supporting types

`struct AccessibilityTechnologies`

Accessibility technologies available to the system.

