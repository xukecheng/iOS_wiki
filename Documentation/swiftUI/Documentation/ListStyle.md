Type Property

# automatic

The list style that describes a platform’s default behavior and appearance for
a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultListStyle { get }

Available when `Self` is `DefaultListStyle`.

## See Also

### Getting built-in list styles

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# bordered

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0+

    
    
    static var bordered: BorderedListStyle { get }

Available when `Self` is `BorderedListStyle`.

## Discussion

Bordered lists are expected to be inset from their outer containers, but do
not have inset style rows or selection.

To customize whether the rows of the list should alternate their backgrounds,
use `bordered(alternatesRowBackgrounds:)`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# carousel

The carousel list style.

watchOS 6.0+

    
    
    static var carousel: CarouselListStyle { get }

Available when `Self` is `CarouselListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# elliptical

The list style that describes the behavior and appearance of an elliptical
list.

watchOS 7.0+

    
    
    static var elliptical: EllipticalListStyle { get }

Available when `Self` is `EllipticalListStyle`.

## Discussion

On watchOS, the elliptical list style uses a transform for items rolling off
the top or bottom of the list, as if on a rounded surface that faces the user.

Apple Watch Series 3 does not support this style and will instead fall back to
using the `plain` style.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# grouped

The list style that describes the behavior and appearance of a grouped list.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    static var grouped: GroupedListStyle { get }

Available when `Self` is `GroupedListStyle`.

## Discussion

On iOS, the grouped list style displays a larger header and footer than the
`plain` style, which visually distances the members of different sections.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# inset

The list style that describes the behavior and appearance of an inset list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var inset: InsetListStyle { get }

Available when `Self` is `InsetListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# insetGrouped

The list style that describes the behavior and appearance of an inset grouped
list.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var insetGrouped: InsetGroupedListStyle { get }

Available when `Self` is `InsetGroupedListStyle`.

## Discussion

On iOS, the inset grouped list style displays a continuous background color
that extends from the section header, around both sides of list items in the
section, and down to the section footer. This visually groups the items to a
greater degree than either the `inset` or `grouped` styles do.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# plain

The list style that describes the behavior and appearance of a plain list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var plain: PlainListStyle { get }

Available when `Self` is `PlainListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# sidebar

The list style that describes the behavior and appearance of a sidebar list.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var sidebar: SidebarListStyle { get }

Available when `Self` is `SidebarListStyle`.

## Discussion

On macOS and iOS, the sidebar list style displays disclosure indicators in the
section headers that allow the user to collapse and expand sections.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

Type Method

# bordered(alternatesRowBackgrounds:)

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0–14.4  Deprecated

    
    
    static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle

Available when `Self` is `BorderedListStyle`.

Deprecated

Use the `bordered` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## Discussion

Bordered lists are expected to be inset from their outer containers, but do
not have inset style rows or selection.

## See Also

### Deprecated styles

`static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle`

The list style that describes the behavior and appearance of an inset list
with optional alternating row backgrounds.

Available when `Self` is `InsetListStyle`.

Deprecated

Type Method

# inset(alternatesRowBackgrounds:)

The list style that describes the behavior and appearance of an inset list
with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle

Available when `Self` is `InsetListStyle`.

Deprecated

Use the `inset` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## See Also

### Deprecated styles

`static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

Deprecated

Structure

# DefaultListStyle

The list style that describes a platform’s default behavior and appearance for
a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultListStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a default list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# BorderedListStyle

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0+

    
    
    struct BorderedListStyle

## Overview

You can also use `bordered` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a bordered list style.

`init(alternatesRowBackgrounds: Bool)`

Creates a bordered list style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# CarouselListStyle

The carousel list style.

watchOS 6.0+

    
    
    struct CarouselListStyle

## Overview

You can also use `carousel` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a carousel list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# EllipticalListStyle

The list style that describes the behavior and appearance of an elliptical
list.

watchOS 7.0+

    
    
    struct EllipticalListStyle

## Overview

You can also use `elliptical` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an elliptical list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# GroupedListStyle

The list style that describes the behavior and appearance of a grouped list.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    struct GroupedListStyle

## Overview

You can also use `grouped` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a grouped list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# InsetListStyle

The list style that describes the behavior and appearance of an inset list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct InsetListStyle

## Overview

You can also use `inset` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an inset list style.

`init(alternatesRowBackgrounds: Bool)`

Creates an inset list style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# InsetGroupedListStyle

The list style that describes the behavior and appearance of an inset grouped
list.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct InsetGroupedListStyle

## Overview

You can also use `insetGrouped` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an inset grouped list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# PlainListStyle

The list style that describes the behavior and appearance of a plain list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PlainListStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a plain list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# SidebarListStyle

The list style that describes the behavior and appearance of a sidebar list.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct SidebarListStyle

## Overview

You can also use `sidebar` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a sidebar list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

