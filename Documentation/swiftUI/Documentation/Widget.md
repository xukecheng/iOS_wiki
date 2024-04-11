Instance Property

# body

The content and behavior of the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## Discussion

For any widgets that you create, provide a computed `body` property that
defines the widget as a composition of SwiftUI views.

Swift infers the widget’s `Body` associated type based on the contents of the
`body` property.

## See Also

### Implementing a widget

`associatedtype Body : WidgetConfiguration`

The type of configuration representing the content of the widget.

**Required**

Associated Type

# Body

The type of configuration representing the content of the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    associatedtype Body : WidgetConfiguration

**Required**

## Discussion

When you create a custom widget, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing a widget

`var body: Self.Body`

The content and behavior of the widget.

**Required**

Initializer

# init()

Creates a widget using `body` as its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()

**Required**

## See Also

### Running a widget

`static func main()`

Initializes and runs the widget.

Type Method

# main()

Initializes and runs the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func main()

## Overview

Because you precede your `Widget` conformer’s declaration with the @main
attribute, the system calls your widget’s `main()` method to launch the
widget. SwiftUI provides a default implementation of the method that manages
the launch process in a platform-appropriate way.

## See Also

### Running a widget

`init()`

Creates a widget using `body` as its content.

**Required**

