Instance Property

# body

Declares the group of widgets that an app supports.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @WidgetBundleBuilder
    var body: Self.Body { get }

**Required**

## Discussion

The order that the widgets appear in this property determines the order they
are shown to the user when adding a widget. The following example shows how to
use a widget bundle builder to define a body showing a game status widget
first and a character detail widget second:

## See Also

### Implementing a widget bundle

`associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

Associated Type

# Body

The type of widget that represents the content of the bundle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    associatedtype Body : Widget

**Required**

## Discussion

When you support more than one widget, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

Structure

# WidgetBundleBuilder

A custom attribute that constructs a widget bundle’s body.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @resultBuilder
    struct WidgetBundleBuilder

## Overview

Use the `@WidgetBundleBuilder` attribute to group multiple widgets listed in
the `body` property of a widget bundle. For example, the following code
defines a widget bundle that consists of two widgets.

## Topics

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

## See Also

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

Initializer

# init()

Creates a widget bundle using the bundle’s body as its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()

**Required**

## See Also

### Running a widget bundle

`static func main()`

Initializes and runs the widget bundle.

Type Method

# main()

Initializes and runs the widget bundle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func main()

## Overview

Because you precede your `WidgetBundle` conformer’s declaration with the @main
attribute, the system calls your widget bundle’s `main()` method to launch the
widget bundle. SwiftUI provides a default implementation of the method that
manages the launch process in a platform-appropriate way.

## See Also

### Running a widget bundle

`init()`

Creates a widget bundle using the bundle’s body as its content.

**Required**

