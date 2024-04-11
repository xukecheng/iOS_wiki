Instance Property

# height

The view’s height.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var height: CGFloat { get }

## See Also

### Getting dimensions

`var width: CGFloat`

The view’s width.

Instance Property

# width

The view’s width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var width: CGFloat { get }

## See Also

### Getting dimensions

`var height: CGFloat`

The view’s height.

Instance Subscript

# subscript(_:)

Gets the value of the given vertical guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(guide: VerticalAlignment) -> CGFloat { get }

## Overview

Find the offset of a particular guide in the corresponding view by using that
guide as an index to read from the context:

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(_:)

Gets the value of the given horizontal guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(guide: HorizontalAlignment) -> CGFloat { get }

## Overview

Find the offset of a particular guide in the corresponding view by using that
guide as an index to read from the context:

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(explicit:)

Gets the explicit value of the given vertical alignment guide

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(explicit guide: VerticalAlignment) -> CGFloat? { get }

## Overview

Find the vertical offset of a particular guide in the corresponding view by
using that guide as an index to read from the context:

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(explicit:)

Gets the explicit value of the given horizontal alignment guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(explicit guide: HorizontalAlignment) -> CGFloat? { get }

## Overview

Find the horizontal offset of a particular guide in the corresponding view by
using that guide as an index to read from the context:

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

