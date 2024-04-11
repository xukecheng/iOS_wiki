Initializer

# init(content:)

Creates a destination-based navigation view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Deprecated

Use `NavigationStack` and `NavigationSplitView` instead. For more information,
see Migrating to new navigation types.

##  Parameters

`content`

    

A `ViewBuilder` that produces the content that the navigation view wraps. Any
views after the first act as placeholders for corresponding columns in a
multicolumn display.

## Discussion

Perform navigation by initializing a link with a destination view. For
example, consider a `ColorDetail` view that displays a color sample:

The following `NavigationView` presents three links to color detail views:

When the horizontal size class is `UserInterfaceSizeClass.regular`, like on an
iPad in landscape mode, or on a Mac, the navigation view presents itself as a
multicolumn view, using its second and later content views — a single `Text`
view in the example above — as a placeholder for the corresponding column:

When the user selects one of the navigation links from the list, the linked
destination view replaces the placeholder text in the detail column:

When the size class is `UserInterfaceSizeClass.compact`, like on an iPhone in
portrait orientation, the navigation view presents itself as a single column
that the user navigates as a stack. Tapping one of the links replaces the list
with the detail view, which provides a back button to return to the list:

Instance Method

# navigationViewStyle(_:)

Sets the style for navigation views within this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle
    

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Discussion

Use this modifier to change the appearance and behavior of navigation views.
For example, by default, navigation views appear with multiple columns in
wider environments, like iPad in landscape orientation:

You can apply the `stack` style to force single-column stack navigation in
these environments:

## See Also

### Styling navigation views

`protocol NavigationViewStyle`

A specification for the appearance and interaction of a navigation view.

Deprecated

Protocol

# NavigationViewStyle

A specification for the appearance and interaction of a navigation view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    protocol NavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Topics

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

## Relationships

### Conforming Types

  * `ColumnNavigationViewStyle`
  * `DefaultNavigationViewStyle`
  * `DoubleColumnNavigationViewStyle`
  * `StackNavigationViewStyle`

## See Also

### Styling navigation views

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

Deprecated

