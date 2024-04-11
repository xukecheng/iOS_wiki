Type Property

# automatic

A disclosure group style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticDisclosureGroupStyle { get }

Available when `Self` is `AutomaticDisclosureGroupStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the instance being created.

## Discussion

SwiftUI calls this method for each instance of `DisclosureGroup` that you
create within a view hierarchy where this style is the current
`DisclosureGroupStyle`.

## See Also

### Creating custom disclosure group styles

`struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`typealias Configuration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Structure

# DisclosureGroupStyleConfiguration

The properties of a disclosure group instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct DisclosureGroupStyleConfiguration

## Topics

### Configuring the label

`let label: DisclosureGroupStyleConfiguration.Label`

The label for the disclosure group.

`struct Label`

A type-erased label of a disclosure group.

### Configuring the content

`let content: DisclosureGroupStyleConfiguration.Content`

The content of the disclosure group.

`struct Content`

A type-erased content of a disclosure group.

### Managing disclosure

`var isExpanded: Bool`

A binding to a Boolean that indicates whether the disclosure group is
expanded.

`var $isExpanded: Binding<Bool>`

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` typealias Configuration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Type Alias

# DisclosureGroupStyle.Configuration

The properties of a disclosure group instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    typealias Configuration = DisclosureGroupStyleConfiguration

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Associated Type

# Body

A view that represents the body of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`typealias Configuration`

The properties of a disclosure group instance.

Structure

# AutomaticDisclosureGroupStyle

A disclosure group style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct AutomaticDisclosureGroupStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the disclosure group style

`init()`

Creates an automatic disclosure group style.

## Relationships

### Conforms To

  * `DisclosureGroupStyle`

