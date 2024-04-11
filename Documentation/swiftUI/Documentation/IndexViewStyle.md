Type Property

# page

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var page: PageIndexViewStyle { get }

Available when `Self` is `PageIndexViewStyle`.

## See Also

### Getting built-in index view styles

`static func page(backgroundDisplayMode:
PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

Type Method

# page(backgroundDisplayMode:)

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static func page(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle

Available when `Self` is `PageIndexViewStyle`.

##  Parameters

`backgroundDisplayMode`

    

The display mode of the background of any page index views receiving this
style

## See Also

### Getting built-in index view styles

`static var page: PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

Structure

# PageIndexViewStyle

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    struct PageIndexViewStyle

## Overview

You can also use `page` to construct this style.

## Topics

### Creating the control group style

`init(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode)`

Creates a page index view style.

`struct BackgroundDisplayMode`

The background style for the page index view.

## Relationships

### Conforms To

  * `IndexViewStyle`

