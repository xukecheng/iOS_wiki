Type Property

# automatic

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let automatic: KeyboardShortcut.Localization

## Discussion

This is the default configuration.

## See Also

### Getting localization strategies

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

Type Property

# custom

Don’t use automatic shortcut remapping.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let custom: KeyboardShortcut.Localization

## Discussion

When you use this mode, you have to take care of international use-cases
separately.

## See Also

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let withoutMirroring: KeyboardShortcut.Localization`

Don’t mirror shortcuts.

Type Property

# withoutMirroring

Don’t mirror shortcuts.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let withoutMirroring: KeyboardShortcut.Localization

## Discussion

Use this for shortcuts that always have a specific directionality, like
aligning something on the right.

Don’t use this option for navigational shortcuts like “Go Back” because
navigation is flipped in right-to-left contexts.

## See Also

### Getting localization strategies

`static let automatic: KeyboardShortcut.Localization`

Remap shortcuts to their international counterparts, mirrored for right-to-
left usage if appropriate.

`static let custom: KeyboardShortcut.Localization`

Don’t use automatic shortcut remapping.

