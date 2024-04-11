Initializer

# init()

Creates a settings link with the default system label.

macOS 14.0+

    
    
    init() where Label == DefaultSettingsLinkLabel

## Discussion

The display of the label may be customized using the `labelStyle(_:)`
modifier.

## See Also

### Creating a settings link

`init(label: () -> Label)`

Creates a settings link with a custom label.

Initializer

# init(label:)

Creates a settings link with a custom label.

macOS 14.0+

    
    
    init(@ViewBuilder label: () -> Label)

##  Parameters

`label`

    

A view to use as the label for this settings link.

## See Also

### Creating a settings link

`init()`

Creates a settings link with the default system label.

Structure

# DefaultSettingsLinkLabel

The default label to use for a settings link.

macOS 14.0+

    
    
    struct DefaultSettingsLinkLabel

## Overview

You don’t use this type directly. Instead, the system creates it automatically
when you construct a `SettingsLink` with the default label.

## Relationships

### Conforms To

  * `View`

