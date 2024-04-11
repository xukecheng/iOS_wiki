Type Property

# automatic

The default navigation view style in the current context of the view being
styled.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    static var automatic: DefaultNavigationViewStyle { get }

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Type Property

# columns

A navigation view style represented by a series of views in columns.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  visionOS 1.0+

    
    
    static var columns: ColumnNavigationViewStyle { get }

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

`static var stack: StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Type Property

# stack

A navigation view style represented by a view stack that only shows a single
top view at a time.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 7.0–10.4
Deprecated  visionOS 1.0+

    
    
    static var stack: StackNavigationViewStyle { get }

Available when `Self` is `StackNavigationViewStyle`.

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## See Also

### Getting built-in navigation view styles

`static var automatic: DefaultNavigationViewStyle`

The default navigation view style in the current context of the view being
styled.

Available when `Self` is `DefaultNavigationViewStyle`.

Deprecated

`static var columns: ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Available when `Self` is `ColumnNavigationViewStyle`.

Deprecated

Structure

# DefaultNavigationViewStyle

The default navigation view style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct DefaultNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `automatic` to construct this style.

## Topics

### Creating a default navigation view style

`init()`

Creates the default navigation view style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# ColumnNavigationViewStyle

A navigation view style represented by a series of views in columns.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct ColumnNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `columns` to construct this style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# StackNavigationViewStyle

A navigation view style represented by a view stack that only shows a single
top view at a time.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 7.0–10.4
Deprecated  visionOS 1.0+

    
    
    struct StackNavigationViewStyle

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Overview

Use `stack` to construct this style.

## Topics

### Creating a stack navigation view style

`init()`

Creates a navigation view style represented by a view stack that only shows a
single top view at a time.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct DoubleColumnNavigationViewStyle`

A navigation view style represented by a primary view stack that navigates to
a detail view.

Deprecated

Structure

# DoubleColumnNavigationViewStyle

A navigation view style represented by a primary view stack that navigates to
a detail view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
visionOS 1.0+

    
    
    struct DoubleColumnNavigationViewStyle

Deprecated

Use `ColumnNavigationViewStyle` instead.

## Topics

### Create a double column view style

`init()`

Creates a double column navigation view style.

## Relationships

### Conforms To

  * `NavigationViewStyle`

## See Also

### Supporting types

`struct DefaultNavigationViewStyle`

The default navigation view style.

Deprecated

`struct ColumnNavigationViewStyle`

A navigation view style represented by a series of views in columns.

Deprecated

`struct StackNavigationViewStyle`

A navigation view style represented by a view stack that only shows a single
top view at a time.

Deprecated

