Type Property

# automatic

The default style for group box views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var automatic: DefaultGroupBoxStyle { get }

Available when `Self` is `DefaultGroupBoxStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the group box instance being created.

## Discussion

SwiftUI calls this method for each instance of `GroupBox` created within a
view hierarchy where this style is the current group box style.

## See Also

### Creating custom group box styles

`typealias Configuration`

The properties of a group box instance.

`associatedtype Body : View`

A view that represents the body of a group box.

**Required**

Type Alias

# GroupBoxStyle.Configuration

The properties of a group box instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias Configuration = GroupBoxStyleConfiguration

## See Also

### Creating custom group box styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a group box.

**Required**

` associatedtype Body : View`

A view that represents the body of a group box.

**Required**

Associated Type

# Body

A view that represents the body of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom group box styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a group box.

**Required**

` typealias Configuration`

The properties of a group box instance.

Structure

# DefaultGroupBoxStyle

The default style for group box views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DefaultGroupBoxStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the group box style

`init()`

## Relationships

### Conforms To

  * `GroupBoxStyle`

