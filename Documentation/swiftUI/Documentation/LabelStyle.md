Type Property

# automatic

A label style that resolves its appearance automatically based on the current
context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var automatic: DefaultLabelStyle { get }

Available when `Self` is `DefaultLabelStyle`.

## See Also

### Getting built-in label styles

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# iconOnly

A label style that only displays the icon of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var iconOnly: IconOnlyLabelStyle { get }

Available when `Self` is `IconOnlyLabelStyle`.

## Discussion

The title of the label is still used for non-visual descriptions, such as
VoiceOver.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# titleAndIcon

A label style that shows both the title and icon of the label using a system-
standard layout.

iOS 14.5+  iPadOS 14.5+  macOS 11.3+  Mac Catalyst 14.5+  tvOS 14.5+  watchOS
7.4+  visionOS 1.0+

    
    
    static var titleAndIcon: TitleAndIconLabelStyle { get }

Available when `Self` is `TitleAndIconLabelStyle`.

## Discussion

In most cases, labels show both their title and icon by default. However, some
containers might apply a different default label style to their content, such
as only showing icons within toolbars on macOS and iOS. To opt in to showing
both the title and the icon, you can apply the title and icon label style:

To apply the title and icon style to a group of labels, apply the style to the
view hierarchy that contains the labels:

The relative layout of the title and icon is dependent on the context it is
displayed in. In most cases, however, the label is arranged horizontally with
the icon leading.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# titleOnly

A label style that only displays the title of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var titleOnly: TitleOnlyLabelStyle { get }

Available when `Self` is `TitleOnlyLabelStyle`.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the label.

## Discussion

The system calls this method for each `Label` instance in a view hierarchy
where this style is the current label style.

## See Also

### Creating custom label styles

`typealias Configuration`

The properties of a label.

`associatedtype Body : View`

A view that represents the body of a label.

**Required**

Type Alias

# LabelStyle.Configuration

The properties of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    typealias Configuration = LabelStyleConfiguration

## See Also

### Creating custom label styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a label.

**Required**

` associatedtype Body : View`

A view that represents the body of a label.

**Required**

Associated Type

# Body

A view that represents the body of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom label styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a label.

**Required**

` typealias Configuration`

The properties of a label.

Structure

# DefaultLabelStyle

The default label style in the current context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DefaultLabelStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the label style

`init()`

Creates an automatic label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# IconOnlyLabelStyle

A label style that only displays the icon of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct IconOnlyLabelStyle

## Overview

You can also use `iconOnly` to construct this style.

## Topics

### Creating the label style

`init()`

Creates an icon-only label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# TitleAndIconLabelStyle

A label style that shows both the title and icon of the label using a system-
standard layout.

iOS 14.5+  iPadOS 14.5+  macOS 11.3+  Mac Catalyst 14.5+  tvOS 14.5+  watchOS
7.4+  visionOS 1.0+

    
    
    struct TitleAndIconLabelStyle

## Overview

You can also use `titleAndIcon` to construct this style.

## Topics

### Creating the label style

`init()`

Creates a label style that shows both the title and icon of the label using a
system-standard layout.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# TitleOnlyLabelStyle

A label style that only displays the title of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct TitleOnlyLabelStyle

## Overview

You can also use `titleOnly` to construct this style.

## Topics

### Creating the label style

`init()`

Creates a title-only label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

