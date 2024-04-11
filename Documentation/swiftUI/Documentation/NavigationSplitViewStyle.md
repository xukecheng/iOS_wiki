Type Property

# automatic

A navigation split style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticNavigationSplitViewStyle { get }

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var balanced: BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

Available when `Self` is `BalancedNavigationSplitViewStyle`.

`static var prominentDetail: ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

Type Property

# balanced

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var balanced: BalancedNavigationSplitViewStyle { get }

Available when `Self` is `BalancedNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var automatic: AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

`static var prominentDetail: ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

Type Property

# prominentDetail

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var prominentDetail: ProminentDetailNavigationSplitViewStyle { get }

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

## See Also

### Creating built-in styles

`static var automatic: AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

`static var balanced: BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

Available when `Self` is `BalancedNavigationSplitViewStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the instance to create.

## Discussion

SwiftUI calls this method for each instance of `NavigationSplitView`, where
this style is the current `NavigationSplitViewStyle`.

## See Also

### Creating custom styles

`typealias Configuration`

The properties of a navigation split view instance.

`associatedtype Body : View`

A view that represents the body of a navigation split view.

**Required**

Type Alias

# NavigationSplitViewStyle.Configuration

The properties of a navigation split view instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = NavigationSplitViewStyleConfiguration

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a navigation split view.

**Required**

` associatedtype Body : View`

A view that represents the body of a navigation split view.

**Required**

Associated Type

# Body

A view that represents the body of a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a navigation split view.

**Required**

` typealias Configuration`

The properties of a navigation split view instance.

Structure

# AutomaticNavigationSplitViewStyle

A navigation split style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticNavigationSplitViewStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of the automatic navigation split view style.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# BalancedNavigationSplitViewStyle

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct BalancedNavigationSplitViewStyle

## Overview

Use `balanced` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of `BalancedNavigationSplitViewStyle`.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# ProminentDetailNavigationSplitViewStyle

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ProminentDetailNavigationSplitViewStyle

## Overview

Use `prominentDetail` to construct this style.

## Topics

### Creating the navigation split view style

`init()`

Creates an instance of `ProminentDetailNavigationSplitViewStyle`.

## Relationships

### Conforms To

  * `NavigationSplitViewStyle`

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

Structure

# NavigationSplitViewStyleConfiguration

The properties of a navigation split view instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewStyleConfiguration

## See Also

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

