Type Property

# automatic

Use the default leading column visibility for the current device.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: NavigationSplitViewVisibility { get }

## Discussion

This computed property returns one of the three concrete cases: `detailOnly`,
`doubleColumn`, or `all`.

## See Also

### Getting visibilities

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# all

Show all the columns of a three-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var all: NavigationSplitViewVisibility { get }

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# doubleColumn

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var doubleColumn: NavigationSplitViewVisibility { get }

## Discussion

For a two-column navigation split view, `doubleColumn` is equivalent to `all`.

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

Type Property

# detailOnly

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var detailOnly: NavigationSplitViewVisibility { get }

## See Also

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

