Type Property

# automatic

The automatic behavior.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var automatic: ScrollBounceBehavior { get }

## Discussion

The scrollable view automatically chooses whether content bounces when people
scroll to the end of the view’s content. By default, scrollable views use the
`always` behavior.

## See Also

### Bounce behaviors

`static var always: ScrollBounceBehavior`

The scrollable view always bounces.

`static var basedOnSize: ScrollBounceBehavior`

The scrollable view bounces when its content is large enough to require
scrolling.

Type Property

# always

The scrollable view always bounces.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var always: ScrollBounceBehavior { get }

## Discussion

The scrollable view always bounces along the specified axis, regardless of the
size of the content.

## See Also

### Bounce behaviors

`static var automatic: ScrollBounceBehavior`

The automatic behavior.

`static var basedOnSize: ScrollBounceBehavior`

The scrollable view bounces when its content is large enough to require
scrolling.

Type Property

# basedOnSize

The scrollable view bounces when its content is large enough to require
scrolling.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var basedOnSize: ScrollBounceBehavior { get }

## Discussion

The scrollable view bounces along the specified axis if the size of the
content exceeeds the size of the scrollable view in that axis.

## See Also

### Bounce behaviors

`static var automatic: ScrollBounceBehavior`

The automatic behavior.

`static var always: ScrollBounceBehavior`

The scrollable view always bounces.

