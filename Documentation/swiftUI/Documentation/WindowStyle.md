Type Property

# automatic

The default window style.

macOS 11.0+  visionOS 1.0+

    
    
    static var automatic: DefaultWindowStyle { get }

Available when `Self` is `DefaultWindowStyle`.

## See Also

### Getting built-in window styles

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# hiddenTitleBar

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

macOS 11.0+

    
    
    static var hiddenTitleBar: HiddenTitleBarWindowStyle { get }

Available when `Self` is `HiddenTitleBarWindowStyle`.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# plain

The plain window style.

visionOS 1.0+

    
    
    static var plain: PlainWindowStyle { get }

Available when `Self` is `PlainWindowStyle`.

## Discussion

Unlike `automatic`, a plain window does not receive a glass background in
visionOS. Use this style if you want more control over how glass is used in
your window.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# titleBar

A window style which displays the title bar section of the window.

macOS 11.0+

    
    
    static var titleBar: TitleBarWindowStyle { get }

Available when `Self` is `TitleBarWindowStyle`.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# volumetric

A window style that creates a 3D volumetric window.

visionOS 1.0+

    
    
    static var volumetric: VolumetricWindowStyle { get }

Available when `Self` is `VolumetricWindowStyle`.

## Discussion

Use a volumetric window — or a _volume_ — to display 3D content within a
bounded region. For example, Hello World uses a volume to present a `Globe`
model that people can pick up and move around the Shared Space using the
window bar:

A volume enables someone to view content from all angles, unlike other windows
which fade out as people move around the window. Also unlike other windows, a
volume uses fixed scale, which means that objects in the volume appear smaller
when the volume is farther away, like real objects would. For a comparison of
fixed and dynamic scale, see Spatial layout in the Human Interface Guidelines.

You can specify a size for the volume using one of the default size scene
modifiers, like `defaultSize(width:height:depth:in:)`. Because volumes use
fixed scale, it’s typically convenient to specify a size in physical units —
like meters, as the above code demonstrates. People can’t change the size of
the volume after it appears.

For design guidance, see Windows in the Human Interface Guidelines. If you
want to place 3D objects arbitrarily throughout the Shared Space or in a Full
Space, use an `ImmersiveSpace` instead.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

Structure

# DefaultWindowStyle

The default window style.

macOS 11.0+  visionOS 1.0+

    
    
    struct DefaultWindowStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# HiddenTitleBarWindowStyle

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

macOS 11.0+

    
    
    struct HiddenTitleBarWindowStyle

## Overview

You can also use `hiddenTitleBar` to construct this style.

## Topics

### Creating the window style

`init()`

Creates a hidden title bar window style.

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# PlainWindowStyle

The plain window style.

visionOS 1.0+

    
    
    struct PlainWindowStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# TitleBarWindowStyle

A window style which displays the title bar section of the window.

macOS 11.0+

    
    
    struct TitleBarWindowStyle

## Overview

You can also use `titleBar` to construct this style.

## Topics

### Creating the window style

`init()`

Creates a title bar window style.

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# VolumetricWindowStyle

A window style that creates a 3D volumetric window.

visionOS 1.0+

    
    
    struct VolumetricWindowStyle

## Overview

Use `volumetric` to construct this style:

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

