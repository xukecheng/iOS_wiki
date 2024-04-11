Type Property

# monochrome

A standard grayscale tint effect.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let monochrome: ListItemTint

## Discussion

The system doesn’t override monochrome tints.

## See Also

### Getting list item tint options

`static func fixed(Color) -> ListItemTint`

An explicit tint color.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

Type Method

# fixed(_:)

An explicit tint color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func fixed(_ tint: Color) -> ListItemTint

##  Parameters

`tint`

    

The color to use to tint the content.

## Discussion

The system doesn’t override this tint effect.

## See Also

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

Type Method

# preferred(_:)

An explicit tint color that the system can override.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func preferred(_ tint: Color) -> ListItemTint

##  Parameters

`tint`

    

The color to use to tint the content.

## Discussion

The system can override this tint effect, like when the system has a custom
user accent color on macOS.

## See Also

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func fixed(Color) -> ListItemTint`

An explicit tint color.

