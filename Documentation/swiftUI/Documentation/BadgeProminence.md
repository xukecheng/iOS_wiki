Type Property

# standard

The standard level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let standard: BadgeProminence

## Discussion

This level of prominence should be used for badges that display a value that
suggests user action, such as a count of unread messages or new invitations.

In lists on macOS, this results in a badge label on a grayscale platter; and
in lists on iOS, this prominence of badge has no platter.

## See Also

### Getting background prominence

`static let increased: BadgeProminence`

The highest level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

Type Property

# increased

The highest level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let increased: BadgeProminence

## Discussion

This level of prominence should be used for badges that display a value that
requires user action, such as number of updates or account errors.

In lists on iOS and macOS, this results in badge labels being displayed on a
red platter.

## See Also

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

Type Property

# decreased

The lowest level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let decreased: BadgeProminence

## Discussion

This level or prominence should be used for badges that display a value of
passive information that requires no user action, such as total number of
messages or content.

In lists on iOS and macOS, this results in badge labels being displayed
without any extra decoration. On iOS, this looks the same as `.standard`.

## See Also

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let increased: BadgeProminence`

The highest level of prominence for a badge.

