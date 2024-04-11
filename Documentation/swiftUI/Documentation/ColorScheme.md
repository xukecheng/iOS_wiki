Case

# ColorScheme.light

The color scheme that corresponds to a light appearance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case light

## See Also

### Getting color schemes

`case dark`

The color scheme that corresponds to a dark appearance.

Case

# ColorScheme.dark

The color scheme that corresponds to a dark appearance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case dark

## See Also

### Getting color schemes

`case light`

The color scheme that corresponds to a light appearance.

Initializer

# init(_:)

Creates a color scheme from its user interface style equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiUserInterfaceStyle: UIUserInterfaceStyle)

Structure

# PreferredColorSchemeKey

A key for specifying the preferred color scheme.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreferredColorSchemeKey

## Overview

Don’t use this key directly. Instead, set a preferred color scheme for a view
using the `preferredColorScheme(_:)` view modifier. Get the current color
scheme for a view by accessing the `colorScheme` value.

## Relationships

### Conforms To

  * `PreferenceKey`

