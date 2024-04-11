Instance Method

# onKeyPress(_:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        action: @escaping () -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`action`

    

The action to perform. Return `.handled` to consume the event and prevent
further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for key-down and key-repeat events.

## See Also

### Responding to keyboard input

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(phases:action:)

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(_:phases:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        phases: KeyPress.Phases,
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.up`, and `.repeat`).

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for the specified event phases.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(characters:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        characters: CharacterSet,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`characters`

    

The set of characters to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(keys:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        keys: Set<KeyEquivalent>,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`keys`

    

A set of keys to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Structure

# KeyPress

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct KeyPress

## Topics

### Getting the keypress

`let key: KeyEquivalent`

The key equivalent value for the pressed key.

`let characters: String`

The characters generated by the pressed key as if no modifier key applies.

`let modifiers: EventModifiers`

The set of modifier keys the user held in addition to the pressed key.

### Getting the phase of the keypress

`let phase: KeyPress.Phases`

The phase of the key-press event (`.down`, `.repeat`, or `.up`).

`struct Phases`

Options for matching different phases of a key-press event.

### Getting the result

`enum Result`

A result value returned from a key-press action that indicates whether the
action consumed the event.

## Relationships

### Conforms To

  * `CustomDebugStringConvertible`
  * `Sendable`

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

Instance Method

# keyboardShortcut(_:)

Assigns a keyboard shortcut to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:)

Assigns an optional keyboard shortcut to the modified control.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used. If the provided shortcut is `nil`, the modifier will have no
effect.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

The default localization configuration is set to `automatic`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:localization:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

### Localization

Provide a `localization` value to specify how this shortcut should be
localized. Given that `key` is always defined in relation to the US-English
keyboard layout, it might be hard to reach on different international layouts.
For example the shortcut `⌘[` works well for the US layout but is hard to
reach for German users, where `[` is available by pressing `⌥5`, making users
type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut
to an appropriate replacement, `⌘Ö` in this case.

Certain shortcuts carry information about directionality. For instance, `⌘[`
can reveal a previous view. Following the layout direction of the UI, this
shortcut will be automatically mirrored to `⌘]`. However, this does not apply
to items such as “Align Left `⌘{`”, which will be “left” independently of the
layout direction. When the shortcut shouldn’t follow the directionality of the
UI, but rather be the same in both right-to-left and left-to-right directions,
using `withoutMirroring` will prevent the system from flipping it.

Lastly, providing the option `custom` disables the automatic localization for
this shortcut to tell the system that internationalization is taken care of in
a different way.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Property

# keyboardShortcut

The keyboard shortcut that buttons in this environment will be triggered with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var keyboardShortcut: KeyboardShortcut? { get }

## Discussion

This is particularly useful in button styles when a button’s appearance
depends on the shortcut associated with it. On macOS, for example, when a
button is bound to the Return key, it is typically drawn with a special
emphasis. This happens automatically when using the built-in button styles,
and can be implemented manually in custom styles using this environment key:

If no keyboard shortcut has been applied to the view or its ancestor, then the
environment value will be `nil`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# KeyboardShortcut

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct KeyboardShortcut

## Topics

### Getting standard shortcuts

`static let cancelAction: KeyboardShortcut`

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

`static let defaultAction: KeyboardShortcut`

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# KeyEquivalent

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct KeyEquivalent

## Overview

Key equivalents are used to establish keyboard shortcuts to app functionality.
Any key can be used as a key equivalent as long as pressing it produces a
single character value. Key equivalents are typically initialized using a
single-character string literal, with constants for unprintable or hard-to-
type values.

The modifier keys necessary to type a key equivalent are factored in to the
resulting keyboard shortcut. That is, a key equivalent whose raw value is the
capitalized string “A” corresponds with the keyboard shortcut Command-Shift-A.
The exact mapping may depend on the keyboard layout—for example, a key
equivalent with the character value “}” produces a shortcut equivalent to
Command-Shift-] on ANSI keyboards, but would produce a different shortcut for
keyboard layouts where punctuation characters are in different locations.

## Topics

### Getting arrow keys

`static let upArrow: KeyEquivalent`

Up Arrow (U+F700)

`static let downArrow: KeyEquivalent`

Down Arrow (U+F701)

`static let leftArrow: KeyEquivalent`

Left Arrow (U+F702)

`static let rightArrow: KeyEquivalent`

Right Arrow (U+F703)

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

### Creating a key equivalent

`init(Character)`

Creates a new key equivalent from the given character value.

`var character: Character`

The character value that the key equivalent represents.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `Hashable`
  * `Sendable`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# EventModifiers

A set of key modifiers that you can add to a gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EventModifiers

## Topics

### Getting modifier keys

`static let all: EventModifiers`

All possible modifier keys.

`static let capsLock: EventModifiers`

The Caps Lock key.

`static let command: EventModifiers`

The Command key.

`static let control: EventModifiers`

The Control key.

`static let numericPad: EventModifiers`

Any key on the numeric keypad.

`static let option: EventModifiers`

The Option key.

`static let shift: EventModifiers`

The Shift key.

### Creating a set of options

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

### Deprecated modifiers

`static let function: EventModifiers`

The Function key.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

Instance Method

# onHover(perform:)

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onHover(perform action: @escaping (Bool) -> Void) -> some View
    

##  Parameters

`action`

    

The action to perform whenever the pointer enters or exits this view’s frame.
If the pointer is in the view’s frame, the `action` closure passes `true` as a
parameter; otherwise, `false`.

## Return Value

A view that triggers `action` when the pointer enters or exits this view’s
frame.

## Discussion

Calling this method defines a region for detecting pointer movement with the
size and position of this view.

## See Also

### Responding to hover events

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# onContinuousHover(coordinateSpace:perform:)

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onContinuousHover(
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (HoverPhase) -> Void
    ) -> some View
    

##  Parameters

`coordinateSpace`

    

The coordinate space for the location values. The default value is
`CoordinateSpace.local`.

`action`

    

The action to perform whenever the pointer enters, moves within, or exits the
view’s bounds. The closure takes a `phase` input that has the value
`HoverPhase.active(_:)` and contains the pointer’s coordinates if the pointer
is within the view’s bounds. The closure receives the `HoverPhase.ended` phase
when the pointer leaves the view’s bounds.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the
view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a
view. The following example updates a small rectangle’s position and style by
modifying `hoverLocation` and `isHovering` as the pointer moves within the
larger, red rectangle:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffect(_:isEnabled:)

Applies a hover effect to this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffect(
        _ effect: HoverEffect = .automatic,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffectDisabled(_:)

Adds a condition that controls whether this view can display hover effects.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display hover effects.

## Return Value

A view that controls whether hover effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a hover effect
because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# defaultHoverEffect(_:)

Sets the default hover effect to use for views within this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func defaultHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The default hover effect to use for views within this view.

## Return Value

A view that uses this effect as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the
`hoverEffect(_:)` modifier applied within a view. The default effect is
typically used when no `HoverEffect` was provided or if `automatic` is
specified.

For example, this view uses `highlight` for both the red and green Color
views:

This also works for customizing the default hover effect in views like
`Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`,
which can provide a hover effect by default. For example, this view replaces
the hover effect for a `Button` with `highlight`:

Use a `nil` effect to indicate that the default hover effect should not be
modified.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Property

# isHoverEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    var isHoverEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`enum HoverPhase`

The current hovering state and value of the pointer.

Enumeration

# HoverPhase

The current hovering state and value of the pointer.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @frozen
    enum HoverPhase

## Overview

When you use the `onContinuousHover(coordinateSpace:perform:)` modifier, you
can handle the hovering state using the `action` closure. SwiftUI calls the
closure with a phase value to indicate the current hovering state. The
following example updates `hoverLocation` and `isHovering` based on the phase
provided to the closure:

## Topics

### Getting hover phases

`case active(CGPoint)`

The pointer’s location moved to the specified point within the view.

`case ended`

The pointer exited the view.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

Instance Method

# hoverEffect(_:)

Applies a hover effect to this view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    func hoverEffect(_ effect: HoverEffect = .automatic) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Changing view appearance for hover events

`struct HoverEffect`

An effect applied when the pointer hovers over a view.

Structure

# HoverEffect

An effect applied when the pointer hovers over a view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    struct HoverEffect

## Topics

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

## See Also

### Changing view appearance for hover events

`func hoverEffect(HoverEffect) -> some View`

Applies a hover effect to this view.

Instance Method

# onSubmit(of:_:)

Adds an action to perform when the user submits a value to this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func onSubmit(
        of triggers: SubmitTriggers = .text,
        _ action: @escaping (() -> Void)
    ) -> some View
    

##  Parameters

`triggers`

    

The triggers that should invoke the provided action.

`action`

    

The action to perform on submission of a value.

## Discussion

Different views may have different triggers for the provided action. A
`TextField`, or `SecureField` will trigger this action when the user hits the
hardware or software return key. This modifier may also bind this action to a
default action keyboard shortcut. You may set this action on an individual
view or an entire view hierarchy.

You can use the `submitScope(_:)` modifier to stop a submit trigger from a
control from propagating higher up in the view hierarchy to higher
`View.onSubmit(of:_:)` modifiers.

You can use different submit triggers to filter the types of triggers that
should invoke the provided submission action. For example, you may provide a
value of `search` to only hear submission triggers that originate from search
fields vended by searchable modifiers.

## See Also

### Responding to submission events

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitScope(_:)

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitScope(_ isBlocking: Bool = true) -> some View
    

##  Parameters

`isBlocking`

    

A Boolean that indicates whether this scope is actively blocking submission
triggers from reaching higher submission actions.

## Discussion

Use this modifier when you want to avoid specific views from initiating a
submission action configured by the `onSubmit(of:_:)` modifier. In the example
below, the tag field doesn’t trigger the submission of the form:

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Structure

# SubmitTriggers

A type that defines various triggers that result in the firing of a submission
action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SubmitTriggers

## Overview

These triggers may be provided to the `onSubmit(of:_:)` modifier to alter
which types of user behaviors trigger a provided submission action.

## Topics

### Getting submit triggers

`static let search: SubmitTriggers`

Defines triggers originating from search fields constructed from searchable
modifiers.

`static let text: SubmitTriggers`

Defines triggers originating from text input controls like `TextField` and
`SecureField`.

### Creating a set of options

`init(rawValue: SubmitTriggers.RawValue)`

Creates a set of submit triggers.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

Instance Method

# submitLabel(_:)

Sets the submit label for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitLabel(_ submitLabel: SubmitLabel) -> some View
    

##  Parameters

`submitLabel`

    

One of the cases specified in `SubmitLabel`.

## Discussion

## See Also

### Labeling a submission event

`struct SubmitLabel`

A semantic label describing the label of submission within a view hierarchy.

Structure

# SubmitLabel

A semantic label describing the label of submission within a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SubmitLabel

## Overview

A submit label is a description of a submission action provided to a view
hierarchy using the `onSubmit(of:_:)` modifier.

## Topics

### Getting submission labels

`static var `continue`: SubmitLabel`

Defines a submit label with text of “Continue”.

`static var done: SubmitLabel`

Defines a submit label with text of “Done”.

`static var go: SubmitLabel`

Defines a submit label with text of “Go”.

`static var join: SubmitLabel`

Defines a submit label with text of “Join”.

`static var next: SubmitLabel`

Defines a submit label with text of “Next”.

`static var `return`: SubmitLabel`

Defines a submit label with text of “Return”.

`static var route: SubmitLabel`

Defines a submit label with text of “Route”.

`static var search: SubmitLabel`

Defines a submit label with text of “Search”.

`static var send: SubmitLabel`

Defines a submit label with text of “Send”.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Labeling a submission event

`func submitLabel(SubmitLabel) -> some View`

Sets the submit label for this view.

Instance Method

# onMoveCommand(perform:)

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

macOS 10.15+  tvOS 13.0+

    
    
    func onMoveCommand(perform action: ((MoveCommandDirection) -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onDeleteCommand(perform:)

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

macOS 10.15+

    
    
    func onDeleteCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# pageCommand(value:in:step:)

Steps a value through a range in response to page up or page down commands.

tvOS 14.3+

    
    
    func pageCommand<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V = 1
    ) -> some View where V : BinaryInteger
    

##  Parameters

`value`

    

A `Binding` to the value to modify when the user pages up or down.

`bounds`

    

A closed range that specifies the upper and lower bounds of `value`.

`step`

    

The amount by which to increment or decrement `value`. Defaults to 1.

## Discussion

Use this command to step through sections of a data model associated with a
view by providing a binding to a value, a range, and step. If taking another
step would cause the value to exceed the bounds, then the value remains
unchanged.

On tvOS, the user triggers ‘pageUp’ and ‘pageDown’ commands by pressing a
dedicated button on a connected remote. For example, you can let a user page
through a TV programming guide using the channel buttons:

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onExitCommand(perform:)

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

macOS 10.15+  tvOS 13.0+

    
    
    func onExitCommand(perform action: (() -> Void)?) -> some View
    

## Discussion

The user generates an exit command by pressing the Menu button on tvOS, or the
escape key on macOS.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onPlayPauseCommand(perform:)

Adds an action to perform in response to the system’s Play/Pause command.

tvOS 13.0+

    
    
    func onPlayPauseCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onCommand(_:perform:)

Adds an action to perform in response to the given selector.

macOS 10.15+

    
    
    func onCommand(
        _ selector: Selector,
        perform action: (() -> Void)?
    ) -> some View
    

##  Parameters

`selector`

    

The selector to register for `action`.

`action`

    

The action to perform. If `action` is `nil`, `command` keeps its association
with this view but doesn’t trigger.

## Return Value

A view that triggers `action` when the `command` occurs.

## Discussion

This view or one of the views it contains must be in focus in order for the
action to trigger. Other actions for the same command on views _closer_ to the
view in focus take priority, potentially overriding this action.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Enumeration

# MoveCommandDirection

Specifies the direction of an arrow key movement.

macOS 10.15+  tvOS 13.0+

    
    
    enum MoveCommandDirection

## Topics

### Getting move command directions

`case up`

`case down`

`case left`

`case right`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

Instance Method

# allowsTightening(_:)

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsTightening(_ flag: Bool) -> some View
    

##  Parameters

`flag`

    

A Boolean value that indicates whether the space between characters compresses
when necessary.

## Return Value

A view that can compress the space between characters when necessary to fit
text in a line.

## Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character
spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects
of `allowsTightening(_:)` on the compression of the spacing between
characters:

## See Also

### Controlling hit testing

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:eoFill:)

Defines the content shape for hit testing.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The hit testing shape for the view.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for hit testing.

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:_:eoFill:)

Sets the content shape for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ kind: ContentShapeKinds,
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`kind`

    

The kinds to apply to this content shape.

`shape`

    

The shape to use.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for the specified kind.

## Discussion

The content shape has a variety of uses. You can control the kind of the
content shape by specifying one in `kind`. For example, the following example
only sets the focus ring shape of the view, without affecting its shape for
hit-testing:

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Structure

# ContentShapeKinds

A kind for the content shape of a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ContentShapeKinds

## Overview

The kind is used by the system to influence various effects, hit-testing, and
more.

## Topics

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

### Creating a set of options

`init(rawValue: Int)`

Creates a content shape kind.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

Instance Method

# digitalCrownAccessory(_:)

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the digital crown accessory.

## Discussion

Use this method to customize the visibility of a Digital Crown accessory
`View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You
may want to keep an accessory visible even when the Digital Crown Indicator is
not visible to indicate what scrolling the crown will do.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownAccessory(content:)

Places an accessory View next to the Digital Crown on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory<Content>(@ViewBuilder content: @escaping () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The view to be used as a Digital Crown Accessory.

## Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple
Watch. Use `digitalCrownAccessory(_:)` to specify the visibility of your
custom view.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive continuous values on a binding you provides as the
user turns the Digital Crown on Apple Watch. The example below receives
changes to the binding value, starting at the `minValue` of `0.0` up to the
`maxValue` of `10.0` settling in to multiples of `0.1` increasing or
decreasing depending on the direction that the user turns the Digital Crown,
rolling over if the user exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`detent`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
detents.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values. The binding will always be updated to a
value that is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryInteger, V.Stride : BinaryInteger
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0` up to the `maxValue` of `100`
in steps of `1` incrementing or decrementing depending on the direction that
the user turns the Digital Crown, rolling over if the user exceeds the
specified boundary values. The binding will always be updated to a value that
is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(_ binding: Binding<V>) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride? = nil,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Structure

# DigitalCrownEvent

An event emitted when the user rotates the Digital Crown.

watchOS 9.0+

    
    
    struct DigitalCrownEvent

## Overview

Use the `digitalCrownRotation(_:)` modifier to receive these events.

## Topics

### Getting events

`var offset: Double`

The offset of the digital crown when this event was sent.

`var velocity: Double`

The velocity at which the offset was changing when this event was sent.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Enumeration

# DigitalCrownRotationalSensitivity

The amount of Digital Crown rotation needed to move between two integer
numbers.

watchOS 6.0+

    
    
    enum DigitalCrownRotationalSensitivity

## Overview

You may need to experiment to find the level of sensitivity that works for
your use case.

## Topics

### Getting sensitivity options

`case low`

Low sensitivity.

`case medium`

Medium sensitivity.

`case high`

High sensitivity.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

Instance Method

# touchBar(content:)

Sets the content that the Touch Bar displays.

macOS 10.15+

    
    
    func touchBar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A collection of views to be displayed by the Touch Bar.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the
Touch Bar. The content is displayed by the Touch Bar when appropriate,
depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and
then added to the Touch Bar:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBar(_:)

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

macOS 10.15+

    
    
    func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View
    

##  Parameters

`touchBar`

    

A collection of views that the Touch Bar displays.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` to provide a static set of views that are displayed by the
Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content
the Touch Bar displays:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPrincipal(_:)

Sets principal views that have special significance to this Touch Bar.

macOS 10.15+

    
    
    func touchBarItemPrincipal(_ principal: Bool = true) -> some View
    

##  Parameters

`principal`

    

A Boolean value that indicates whether to display this view prominently in the
Touch Bar compared to other views.

## Return Value

A Touch Bar view with one element centered in the Touch Bar row.

## Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in
the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch
Bar view.

Note

Multiple visible bars may each specify a principal view, but the system only
honors one of them.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarCustomizationLabel(_:)

Sets a user-visible string that identifies the view’s functionality.

macOS 10.15+

    
    
    func touchBarCustomizationLabel(_ label: Text) -> some View
    

##  Parameters

`label`

    

A `Text` view containing the customization label.

## Return Value

A Touch Bar element with a set customization label.

## Discussion

This string is visible during user customization.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPresence(_:)

Sets the behavior of the user-customized view.

macOS 10.15+

    
    
    func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View
    

##  Parameters

`presence`

    

One of the allowed `TouchBarItemPresence` descriptions.

## Return Value

A trait that describes the behavior for this Touch Bar view.

## Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a
particular Touch Bar view during customization by the user.

Touch Bar views may be:

  * `.required`: not allowed to be removed by the user.

  * `.default`: shown by default prior to user customization, but removable.

  * `.optional`: not visible by default, but can be added through the customization palette.

Each `TouchBarItemPresence` must be initialized with a string that is a
globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar
by default, except for the “Clubs” item. It’s set to `.optional` but is
configurable by the user:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Structure

# TouchBar

A container for a view that you can show in the Touch Bar.

macOS 10.15+

    
    
    struct TouchBar<Content> where Content : View

## Topics

### Creating a Touch Bar view

`init(content: () -> Content)`

Creates a non-customizable Touch Bar view container.

`init(id: String, content: () -> Content)`

Creates a customizable Touch Bar view container with a globally unique
identifier.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Enumeration

# TouchBarItemPresence

Options that affect user customization of the Touch Bar.

macOS 10.15+

    
    
    enum TouchBarItemPresence

## Topics

### Getting presence options

`case `default`(String)`

The Touch Bar view is visible by default, but can be removed during
customization.

`case optional(String)`

The Touch Bar view isn’t visible by default, but appears in the customization
palette.

`case required(String)`

The Touch Bar view is visible by default and cannot be removed during
customization.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

