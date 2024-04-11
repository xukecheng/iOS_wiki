Type Property

# automatic

A labeled content style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticLabeledContentStyle { get }

Available when `Self` is `AutomaticLabeledContentStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of labeled content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

## See Also

### Creating custom labeled content styles

`typealias Configuration`

The properties of a labeled content instance.

`associatedtype Body : View`

A view that represents the appearance and behavior of labeled content.

**Required**

Type Alias

# LabeledContentStyle.Configuration

The properties of a labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = LabeledContentStyleConfiguration

## See Also

### Creating custom labeled content styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of labeled content.

**Required**

` associatedtype Body : View`

A view that represents the appearance and behavior of labeled content.

**Required**

Associated Type

# Body

A view that represents the appearance and behavior of labeled content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom labeled content styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of labeled content.

**Required**

` typealias Configuration`

The properties of a labeled content instance.

Structure

# AutomaticLabeledContentStyle

The default labeled content style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticLabeledContentStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the labeled content style

`init()`

Creates an automatic labeled content style.

## Relationships

### Conforms To

  * `LabeledContentStyle`

