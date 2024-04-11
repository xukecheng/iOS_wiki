Type Property

# automatic

The default progress view style in the current context of the view being
styled.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var automatic: DefaultProgressViewStyle { get }

Available when `Self` is `DefaultProgressViewStyle`.

## Discussion

The default style represents the recommended style based on the original
initialization parameters of the progress view, and the progress view’s
context within the view hierarchy.

## See Also

### Getting built-in progress view styles

`static var circular: CircularProgressViewStyle`

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

Available when `Self` is `CircularProgressViewStyle`.

`static var linear: LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Available when `Self` is `LinearProgressViewStyle`.

Type Property

# circular

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var circular: CircularProgressViewStyle { get }

Available when `Self` is `CircularProgressViewStyle`.

## Discussion

On watchOS, and in widgets and complications, a circular progress view appears
as a gauge with the `accessoryCircularCapacity` style. If the progress view is
indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available,
circular progress views use an indeterminate style.

## See Also

### Getting built-in progress view styles

`static var automatic: DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

Available when `Self` is `DefaultProgressViewStyle`.

`static var linear: LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Available when `Self` is `LinearProgressViewStyle`.

Type Property

# linear

A progress view that visually indicates its progress using a horizontal bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var linear: LinearProgressViewStyle { get }

Available when `Self` is `LinearProgressViewStyle`.

## See Also

### Getting built-in progress view styles

`static var automatic: DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

Available when `Self` is `DefaultProgressViewStyle`.

`static var circular: CircularProgressViewStyle`

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

Available when `Self` is `CircularProgressViewStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the progress view being created.

`configuration`

    

The properties of the progress view, such as its preferred progress type.

## Discussion

The view hierarchy calls this method for each progress view where this style
is the current progress view style.

## See Also

### Creating custom progress view styles

`typealias Configuration`

A type alias for the properties of a progress view instance.

`associatedtype Body : View`

A view representing the body of a progress view.

**Required**

Type Alias

# ProgressViewStyle.Configuration

A type alias for the properties of a progress view instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    typealias Configuration = ProgressViewStyleConfiguration

## See Also

### Creating custom progress view styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a progress view.

**Required**

` associatedtype Body : View`

A view representing the body of a progress view.

**Required**

Associated Type

# Body

A view representing the body of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom progress view styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a progress view.

**Required**

` typealias Configuration`

A type alias for the properties of a progress view instance.

Structure

# DefaultProgressViewStyle

The default progress view style in the current context of the view being
styled.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DefaultProgressViewStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the progress view style

`init()`

Creates a default progress view style.

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct CircularProgressViewStyle`

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

`struct LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Structure

# CircularProgressViewStyle

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct CircularProgressViewStyle

## Overview

On watchOS, and in widgets and complications, a circular progress view appears
as a gauge with the `accessoryCircularCapacity` style. If the progress view is
indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available,
circular progress views use an indeterminate style.

Use `circular` to construct the circular progress view style.

## Topics

### Creating the progress view style

`init()`

Creates a circular progress view style.

### Deprecated initializers

`init(tint: Color)`

Creates a circular progress view style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

`struct LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Structure

# LinearProgressViewStyle

A progress view that visually indicates its progress using a horizontal bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LinearProgressViewStyle

## Overview

Use `linear` to construct this style.

## Topics

### Creating the progress view style

`init()`

Creates a linear progress view style.

### Deprecated initializers

`init(tint: Color)`

Creates a linear progress view style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

`struct CircularProgressViewStyle`

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

