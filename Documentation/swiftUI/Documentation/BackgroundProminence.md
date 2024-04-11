Type Property

# standard

The standard prominence of a background

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let standard: BackgroundProminence

## Discussion

This is the default level of prominence and doesn’t require any adjustment to
achieve satisfactory contrast with the background.

## See Also

### Getting background prominence

`static let increased: BackgroundProminence`

A more prominent background that likely requires some changes to the views
above it.

Type Property

# increased

A more prominent background that likely requires some changes to the views
above it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let increased: BackgroundProminence

## Discussion

This is the level of prominence for more highly saturated and full color
backgrounds, such as focused/emphasized selected list rows. Typically
foreground content should take on monochrome styling to have greater contrast
against the background.

## See Also

### Getting background prominence

`static let standard: BackgroundProminence`

The standard prominence of a background

