Type Property

# automatic

Scroll indicator visibility depends on the policies of the component accepting
the visibility configuration.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: ScrollIndicatorVisibility { get }

## See Also

### Getting visibilties

`static var hidden: ScrollIndicatorVisibility`

Hide the scroll indicators.

`static var never: ScrollIndicatorVisibility`

Scroll indicators should never be visible.

`static var visible: ScrollIndicatorVisibility`

Show the scroll indicators.

Type Property

# hidden

Hide the scroll indicators.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var hidden: ScrollIndicatorVisibility { get }

## Discussion

By default, scroll views in macOS show indicators when a mouse is connected.
Use `never` to indicate a stronger preference that can override this behavior.

## See Also

### Getting visibilties

`static var automatic: ScrollIndicatorVisibility`

Scroll indicator visibility depends on the policies of the component accepting
the visibility configuration.

`static var never: ScrollIndicatorVisibility`

Scroll indicators should never be visible.

`static var visible: ScrollIndicatorVisibility`

Show the scroll indicators.

Type Property

# never

Scroll indicators should never be visible.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var never: ScrollIndicatorVisibility { get }

## Discussion

This value behaves like `hidden`, but overrides scrollable views that choose
to keep their indidicators visible. When using this value, provide an
alternative method of scrolling. The typical horizontal swipe gesture might
not be available, depending on the current input device.

## See Also

### Getting visibilties

`static var automatic: ScrollIndicatorVisibility`

Scroll indicator visibility depends on the policies of the component accepting
the visibility configuration.

`static var hidden: ScrollIndicatorVisibility`

Hide the scroll indicators.

`static var visible: ScrollIndicatorVisibility`

Show the scroll indicators.

Type Property

# visible

Show the scroll indicators.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var visible: ScrollIndicatorVisibility { get }

## Discussion

The actual visibility of the indicators depends on platform conventions like
auto-hiding behaviors in iOS or user preference behaviors in macOS.

## See Also

### Getting visibilties

`static var automatic: ScrollIndicatorVisibility`

Scroll indicator visibility depends on the policies of the component accepting
the visibility configuration.

`static var hidden: ScrollIndicatorVisibility`

Hide the scroll indicators.

`static var never: ScrollIndicatorVisibility`

Scroll indicators should never be visible.

