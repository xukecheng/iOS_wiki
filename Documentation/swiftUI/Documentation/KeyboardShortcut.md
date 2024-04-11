Type Property

# cancelAction

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let cancelAction: KeyboardShortcut

## See Also

### Getting standard shortcuts

`static let defaultAction: KeyboardShortcut`

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

Type Property

# defaultAction

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let defaultAction: KeyboardShortcut

## Discussion

On macOS, the default button is designated with special coloration. If more
than one control is assigned this shortcut, only the first one is emphasized.

## See Also

### Getting standard shortcuts

`static let cancelAction: KeyboardShortcut`

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

Initializer

# init(_:modifiers:)

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    )

## Discussion

The localization configuration defaults to `automatic`.

## See Also

### Creating a shortcut

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

Instance Property

# key

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var key: KeyEquivalent

## See Also

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

Instance Property

# modifiers

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    var modifiers: EventModifiers

## See Also

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

Initializer

# init(_:modifiers:localization:)

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    )

## Discussion

Use the `localization` parameter to specify a localization strategy for this
shortcut.

## See Also

### Creating a localized shortcut

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

Instance Property

# localization

The localization strategy to apply to this shortcut.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var localization: KeyboardShortcut.Localization

## See Also

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

Structure

# KeyboardShortcut.Localization

Options for how a keyboard shortcut participates in automatic localization.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct Localization

## Overview

A shortcut’s `key` that is defined on an US-English keyboard layout might not
be reachable on international layouts. For example the shortcut `⌘[` works
well for the US layout but is hard to reach for German users. On the German
keyboard layout, pressing `⌥5` will produce `[`, which causes the shortcut to
become `⌥⌘5`. If configured, which is the default behavior, automatic shortcut
remapping will convert it to `⌘Ö`.

In addition to that, some keyboard shortcuts carry information about
directionality. Right-aligning a block of text or seeking forward in context
of music playback are such examples. These kinds of shortcuts benefit from the
option `withoutMirroring` to tell the system that they won’t be flipped when
running in a right-to-left context.

## Topics

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.

