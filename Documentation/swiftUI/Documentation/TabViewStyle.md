Type Property

# automatic

The default `TabView` style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var automatic: DefaultTabViewStyle { get }

Available when `Self` is `DefaultTabViewStyle`.

## See Also

### Getting built-in tab view styles

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

Type Property

# carousel

A style that implements the carousel interaction and appearance.

watchOS 7.0–10.4  Deprecated

    
    
    static var carousel: CarouselTabViewStyle { get }

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

Use `verticalPage` or `verticalPage(transitionStyle:)` instead.

## See Also

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

Type Property

# page

A `TabViewStyle` that implements a paged scrolling `TabView`.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    static var page: PageTabViewStyle { get }

Available when `Self` is `PageTabViewStyle`.

## See Also

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

Type Method

# page(indexDisplayMode:)

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) -> PageTabViewStyle

Available when `Self` is `PageTabViewStyle`.

## See Also

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

Type Property

# verticalPage

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

watchOS 10.0+

    
    
    static var verticalPage: VerticalPageTabViewStyle { get }

Available when `Self` is `VerticalPageTabViewStyle`.

## See Also

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

Type Method

# verticalPage(transitionStyle:)

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

watchOS 10.0+

    
    
    static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle

Available when `Self` is `VerticalPageTabViewStyle`.

## See Also

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

Structure

# DefaultTabViewStyle

The default `TabView` style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DefaultTabViewStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the tab view style

`init()`

## Relationships

### Conforms To

  * `TabViewStyle`

## See Also

### Supporting types

`struct CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Deprecated

`struct PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

`struct VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical `TabView` interaction and
appearance.

Structure

# CarouselTabViewStyle

A style that implements the carousel interaction and appearance.

watchOS 7.0–10.4  Deprecated

    
    
    struct CarouselTabViewStyle

Deprecated

Use `VerticalPageTabViewStyle` instead.

## Topics

### Creating the tab view style

`init()`

Creates a carousel table view style.

## Relationships

### Conforms To

  * `TabViewStyle`

## See Also

### Supporting types

`struct DefaultTabViewStyle`

The default `TabView` style.

`struct PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

`struct VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical `TabView` interaction and
appearance.

Structure

# PageTabViewStyle

A `TabViewStyle` that implements a paged scrolling `TabView`.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct PageTabViewStyle

## Overview

You can also use `page` or `page(indexDisplayMode:)` to construct this style.

## Topics

### Creating a page tab view style

`init(indexDisplayMode: PageTabViewStyle.IndexDisplayMode)`

Creates a new `PageTabViewStyle` with an index display mode

`struct IndexDisplayMode`

A style for displaying the page index view

## Relationships

### Conforms To

  * `TabViewStyle`

## See Also

### Supporting types

`struct DefaultTabViewStyle`

The default `TabView` style.

`struct CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Deprecated

`struct VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical `TabView` interaction and
appearance.

Structure

# VerticalPageTabViewStyle

A `TabViewStyle` that implements the vertical `TabView` interaction and
appearance.

watchOS 10.0+

    
    
    struct VerticalPageTabViewStyle

## Overview

You can also use `verticalPage` to construct this style.

## Topics

### Creating the tab view style

`init()`

`init(transitionStyle: VerticalPageTabViewStyle.TransitionStyle)`

Creates a new `VerticalPageTabViewStyle` with a transition style.

`struct TransitionStyle`

A transition style used between tabs.

## Relationships

### Conforms To

  * `TabViewStyle`

## See Also

### Supporting types

`struct DefaultTabViewStyle`

The default `TabView` style.

`struct CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Deprecated

`struct PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

