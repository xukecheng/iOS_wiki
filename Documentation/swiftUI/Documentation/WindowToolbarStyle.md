Type Property

# automatic

The automatic window toolbar style.

macOS 11.0+

    
    
    static var automatic: DefaultWindowToolbarStyle { get }

Available when `Self` is `DefaultWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# expanded

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    static var expanded: ExpandedWindowToolbarStyle { get }

Available when `Self` is `ExpandedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unified

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static var unified: UnifiedWindowToolbarStyle { get }

Available when `Self` is `UnifiedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unified(showsTitle:)

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle

Available when `Self` is `UnifiedWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unifiedCompact

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static var unifiedCompact: UnifiedCompactWindowToolbarStyle { get }

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unifiedCompact(showsTitle:)

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Structure

# DefaultWindowToolbarStyle

The default window toolbar style.

macOS 11.0+

    
    
    struct DefaultWindowToolbarStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a default window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# ExpandedWindowToolbarStyle

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    struct ExpandedWindowToolbarStyle

## Overview

You can also use `expanded` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates an expanded window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedWindowToolbarStyle

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    struct UnifiedWindowToolbarStyle

## Overview

You can also use `unified` or `unified(showsTitle:)` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedCompactWindowToolbarStyle

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    struct UnifiedCompactWindowToolbarStyle

## Overview

You can also use `unifiedCompact` or `unifiedCompact(showsTitle:)` to
construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Type Property

# automatic

The automatic window toolbar style.

macOS 11.0+

    
    
    static var automatic: DefaultWindowToolbarStyle { get }

Available when `Self` is `DefaultWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# expanded

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    static var expanded: ExpandedWindowToolbarStyle { get }

Available when `Self` is `ExpandedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unified

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static var unified: UnifiedWindowToolbarStyle { get }

Available when `Self` is `UnifiedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unified(showsTitle:)

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle

Available when `Self` is `UnifiedWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unifiedCompact

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static var unifiedCompact: UnifiedCompactWindowToolbarStyle { get }

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unifiedCompact(showsTitle:)

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Structure

# DefaultWindowToolbarStyle

The default window toolbar style.

macOS 11.0+

    
    
    struct DefaultWindowToolbarStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a default window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# ExpandedWindowToolbarStyle

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    struct ExpandedWindowToolbarStyle

## Overview

You can also use `expanded` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates an expanded window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedWindowToolbarStyle

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    struct UnifiedWindowToolbarStyle

## Overview

You can also use `unified` or `unified(showsTitle:)` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedCompactWindowToolbarStyle

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    struct UnifiedCompactWindowToolbarStyle

## Overview

You can also use `unifiedCompact` or `unifiedCompact(showsTitle:)` to
construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

