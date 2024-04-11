Initializer

# init(sidebar:detail:)

Creates a two-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

##  Parameters

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Creating a navigation split view

`init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view.

Initializer

# init(sidebar:content:detail:)

Creates a three-column navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

##  Parameters

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Creating a navigation split view

`init(sidebar: () -> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view.

Initializer

# init(columnVisibility:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading column.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

Initializer

# init(columnVisibility:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading columns.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

Initializer

# init(preferredCompactColumn:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(preferredCompactColumn:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(columnVisibility:preferredCompactColumn:sidebar:detail:)

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder detail: () -> Detail
    ) where Content == EmptyView

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading column.

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

Initializer

# init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        columnVisibility: Binding<NavigationSplitViewVisibility>,
        preferredCompactColumn: Binding<NavigationSplitViewColumn>,
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail: () -> Detail
    )

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

##  Parameters

`columnVisibility`

    

A `Binding` to state that controls the visibility of the leading columns.

`preferredCompactColumn`

    

A `Binding` to state that controls which column appears on top when the view
collapses.

`sidebar`

    

The view to show in the leading column.

`content`

    

The view to show in the middle column.

`detail`

    

The view to show in the detail area.

## See Also

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

