Protocol

# Layout

A type that defines the geometry of a collection of views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol Layout : Animatable

## Overview

You traditionally arrange views in your app’s user interface using built-in
layout containers like `HStack` and `Grid`. If you need more complex layout
behavior, you can define a custom layout container by creating a type that
conforms to the `Layout` protocol and implementing its required methods:

  * `sizeThatFits(proposal:subviews:cache:)` reports the size of the composite layout view.

  * `placeSubviews(in:proposal:subviews:cache:)` assigns positions to the container’s subviews.

You can define a basic layout type with only these two methods:

Use your layout the same way you use a built-in layout container, by providing
a `ViewBuilder` with the list of subviews to arrange:

### Support additional behaviors

You can optionally implement other protocol methods and properties to provide
more layout container features:

  * Define explicit horizontal and vertical layout guides for the container by implementing `explicitAlignment(of:in:proposal:subviews:cache:)` and `explicitAlignment(of:in:proposal:subviews:cache:)`, respectively.

  * Establish the preferred spacing around the container by implementing `spacing(subviews:cache:)`.

  * Indicate the axis of orientation for a container that has characteristics of a stack by implementing the `layoutProperties` static property.

  * Create and manage a cache to store computed values across different layout protocol calls by implementing `makeCache(subviews:)`.

The protocol provides default implementations for these symbols if you don’t
implement them. See each method or property for details.

### Add input parameters

You can define parameters as inputs to the layout, like you might for a
`View`:

Set the parameters at the point where you instantiate the layout:

If the layout provides default values for its parameters, you can omit the
parameters at the call site, but you might need to keep the parentheses after
the name of the layout, depending on how you specify the defaults. For
example, suppose you set a default alignment for the basic stack in the
parameter declaration:

To instantiate this layout using the default center alignment, you don’t have
to specify the alignment value, but you do need to add empty parentheses:

The Swift compiler requires the parentheses in this case because of how the
layout protocol implements this call site syntax. Specifically, the layout’s
`callAsFunction(_:)` method looks for an initializer with exactly zero input
arguments when you omit the parentheses from the call site. You can enable the
simpler call site for a layout that doesn’t have an implicit initializer of
this type by explicitly defining one:

For information about Swift initializers, see Initialization in _The Swift
Programming Language_.

### Interact with subviews through their proxies

To perform layout, you need information about all of its subviews, which are
the views that your container arranges. While your layout can’t interact
directly with its subviews, it can access a set of subview proxies through the
`Layout.Subviews` collection that each protocol method receives as an input
parameter. That type is an alias for the `LayoutSubviews` collection type,
which in turn contains `LayoutSubview` instances that are the subview proxies.

You can get information about each subview from its proxy, like its dimensions
and spacing preferences. This enables you to measure subviews before you
commit to placing them. You also assign a position to each subview by calling
its proxy’s `place(at:anchor:proposal:)` method. Call the method on each
subview from within your implementation of the layout’s
`placeSubviews(in:proposal:subviews:cache:)` method.

### Access layout values

Views have layout values that you set with view modifiers. Layout containers
can choose to condition their behavior accordingly. For example, a built-in
`HStack` allocates space to its subviews based in part on the priorities that
you set with the `layoutPriority(_:)` view modifier. Your layout container
accesses this value for a subview by reading the proxy’s `priority` property.

You can also create custom layout values by creating a layout key. Set a value
on a view with the `layoutValue(key:value:)` view modifier. Read the
corresponding value from the subview’s proxy using the key as an index on the
subview. For more information about creating, setting, and accessing custom
layout values, see `LayoutValueKey`.

## Topics

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

### Supporting types

`func callAsFunction<V>(() -> V) -> some View`

Combines the specified views into a single composite view using the layout
algorithms of the custom layout container.

## Relationships

### Inherits From

  * `Animatable`

### Conforming Types

  * `AnyLayout`
  * `GridLayout`
  * `HStackLayout`
  * `VStackLayout`
  * `ZStackLayout`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`struct LayoutSubview`

A proxy that represents one subview of a layout.

`struct LayoutSubviews`

A collection of proxy values that represent the subviews of a layout view.

Structure

# LayoutSubview

A proxy that represents one subview of a layout.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutSubview

## Overview

This type acts as a proxy for a view that your custom layout container places
in the user interface. `Layout` protocol methods receive a `LayoutSubviews`
collection that contains exactly one proxy for each of the subviews arranged
by your container.

Use a proxy to get information about the associated subview, like its
dimensions, layout priority, or custom layout values. You also use the proxy
to tell its corresponding subview where to appear by calling the proxy’s
`place(at:anchor:proposal:)` method. Do this once for each subview from your
implementation of the layout’s `placeSubviews(in:proposal:subviews:cache:)`
method.

You can read custom layout values associated with a subview by using the
property’s key as an index on the subview. For more information about
defining, setting, and reading custom values, see `LayoutValueKey`.

## Topics

### Placing the subview

`func place(at: CGPoint, anchor: UnitPoint, proposal: ProposedViewSize)`

Assigns a position and proposed size to the subview.

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

### Getting custom values

`subscript<K>(K.Type) -> K.Value`

Gets the value for the subview that’s associated with the specified key.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`protocol Layout`

A type that defines the geometry of a collection of views.

`struct LayoutSubviews`

A collection of proxy values that represent the subviews of a layout view.

Structure

# LayoutSubviews

A collection of proxy values that represent the subviews of a layout view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutSubviews

## Overview

You receive a `LayoutSubviews` input to your implementations of `Layout`
protocol methods, like `placeSubviews(in:proposal:subviews:cache:)` and
`sizeThatFits(proposal:subviews:cache:)`. The `subviews` parameter (which the
protocol aliases to the `Layout.Subviews` type) is a collection that contains
proxies for the layout’s subviews (of type `LayoutSubview`). The proxies
appear in the collection in the same order that they appear in the
`ViewBuilder` input to the layout container. Use the proxies to perform layout
operations.

Access the proxies in the collection as you would the contents of any Swift
random-access collection. For example, you can enumerate all of the subviews
and their indices to inspect or operate on them:

## Topics

### Getting the layout direction

`var layoutDirection: LayoutDirection`

The layout direction inherited by the container view.

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `Equatable`
  * `RandomAccessCollection`
  * `Sendable`
  * `Sequence`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`protocol Layout`

A type that defines the geometry of a collection of views.

`struct LayoutSubview`

A proxy that represents one subview of a layout.

Structure

# LayoutProperties

Layout-specific properties of a layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutProperties

## Overview

This structure contains configuration information that’s applicable to a
layout container. For example, the `stackOrientation` value indicates the
layout’s primary axis, if any.

You can use an instance of this type to characterize a custom layout
container, which is a type that conforms to the `Layout` protocol. Implement
the protocol’s `layoutProperties` property to return an instance. For example,
you can indicate that your layout has a vertical stack orientation:

If you don’t implement the property in your custom layout, the protocol
provides a default implementation that returns a `LayoutProperties` instance
with default values.

## Topics

### Creating a layout properties instance

`init()`

Creates a default set of properties.

### Getting layout properties

`var stackOrientation: Axis?`

The orientation of the containing stack-like container.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring a custom layout

`struct ProposedViewSize`

A proposal for the size of a view.

`struct ViewSpacing`

A collection of the geometric spacing preferences of a view.

Structure

# ProposedViewSize

A proposal for the size of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ProposedViewSize

## Overview

During layout in SwiftUI, views choose their own size, but they do that in
response to a size proposal from their parent view. When you create a custom
layout using the `Layout` protocol, your layout container participates in this
process using `ProposedViewSize` instances. The layout protocol’s methods take
a proposed size input that you can take into account when arranging views and
calculating the size of the composite container. Similarly, your layout
proposes a size to each of its own subviews when it measures and places them.

Layout containers typically measure their subviews by proposing several sizes
and looking at the responses. The container can use this information to decide
how to allocate space among its subviews. A layout might try the following
special proposals:

  * The `zero` proposal; the view responds with its minimum size.

  * The `infinity` proposal; the view responds with its maximum size.

  * The `unspecified` proposal; the view responds with its ideal size.

A layout might also try special cases for one dimension at a time. For
example, an `HStack` might measure the flexibility of its subviews’ widths,
while using a fixed value for the height.

## Topics

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

### Creating a custom size proposal

`init(CGSize)`

Creates a new proposed size from a specified size.

`init(width: CGFloat?, height: CGFloat?)`

Creates a new proposed size using the specified width and height.

### Getting the proposal’s dimensions

`var height: CGFloat?`

The proposed vertical size measured in points.

`var width: CGFloat?`

The proposed horizontal size measured in points.

### Modifying a proposal

`func replacingUnspecifiedDimensions(by: CGSize) -> CGSize`

Creates a new proposal that replaces unspecified dimensions in this proposal
with the corresponding dimension of the specified size.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Configuring a custom layout

`struct LayoutProperties`

Layout-specific properties of a layout container.

`struct ViewSpacing`

A collection of the geometric spacing preferences of a view.

Structure

# ViewSpacing

A collection of the geometric spacing preferences of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ViewSpacing

## Overview

This type represents how much space a view prefers to have between it and the
next view in a layout. The type stores independent values for each of the top,
bottom, leading, and trailing edges, and can also record different values for
different kinds of adjacent views. For example, it might contain one value for
the spacing to the next text view along the top and bottom edges, other values
for the spacing to text views on other edges, and yet other values for other
kinds of views. Spacing preferences can also vary by platform.

Your `Layout` type doesn’t have to take preferred spacing into account, but if
it does, you can use the `spacing` preferences of the subviews in your layout
container to:

  * Add space between subviews when you implement the `placeSubviews(in:proposal:subviews:cache:)` method.

  * Create a spacing preferences instance for the container view by implementing the `spacing(subviews:cache:)` method.

## Topics

### Creating spacing instances

`init()`

Initializes an instance with default spacing values.

`static let zero: ViewSpacing`

A view spacing instance that contains zero on all edges.

### Measuring spacing distance

`func distance(to: ViewSpacing, along: Axis) -> CGFloat`

Gets the preferred spacing distance along the specified axis to the view that
returns a specified spacing preference.

### Merging spacing instances

`func formUnion(ViewSpacing, edges: Edge.Set)`

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.

`func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing`

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring a custom layout

`struct LayoutProperties`

Layout-specific properties of a layout container.

`struct ProposedViewSize`

A proposal for the size of a view.

Instance Method

# layoutValue(key:value:)

Associates a value with a custom layout property.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func layoutValue<K>(
        key: K.Type,
        value: K.Value
    ) -> some View where K : LayoutValueKey
    

##  Parameters

`key`

    

The type of the key that you want to set a value for. Create the key as a type
that conforms to the `LayoutValueKey` protocol.

`value`

    

The value to assign to the key for this view. The value must be of the type
that you establish for the key’s associated value when you implement the key’s
`defaultValue` property.

## Return Value

A view that has the specified value for the specified key.

## Discussion

Use this method to set a value for a custom property that you define with
`LayoutValueKey`. For example, if you define a `Flexibility` key, you can set
the key on a `Text` view using the key’s type and a value:

For convenience, you might define a method that does this in an extension to
`View`:

This method makes the call site easier to read:

If you perform layout operations in a type that conforms to the `Layout`
protocol, you can read the key’s associated value for each subview of your
custom layout type. Do this by indexing the subview’s proxy with the key. For
more information, see `LayoutValueKey`.

## See Also

### Associating values with views in a custom layout

`protocol LayoutValueKey`

A key for accessing a layout value of a layout container’s subviews.

Protocol

# LayoutValueKey

A key for accessing a layout value of a layout container’s subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol LayoutValueKey

## Overview

If you create a custom layout by defining a type that conforms to the `Layout`
protocol, you can also create custom layout values that you set on individual
views, and that your container view can access to guide its layout behavior.
Your custom values resemble the built-in layout values that you set with view
modifiers like `layoutPriority(_:)` and `zIndex(_:)`, but have a purpose that
you define.

To create a custom layout value, define a type that conforms to the
`LayoutValueKey` protocol and implement the one required property that returns
the default value of the property. For example, you can create a property that
defines an amount of flexibility for a view, defined as an optional floating
point number with a default value of `nil`:

The Swift compiler infers this particular key’s associated type as an optional
`CGFloat` from this definition.

### Set a value on a view

Set the value on a view by adding the `layoutValue(key:value:)` view modifier
to the view. To make your custom value easier to work with, you can do this in
a convenience modifier in an extension of the `View` protocol:

Use your modifier to set the value on any views that need a nondefault value:

Any view that you don’t explicitly set a value for uses the default value, as
with the first `Text` view, above.

### Retrieve a value during layout

Access a custom layout value using the key as an index on subview’s proxy (an
instance of `LayoutSubview`) and use the value to make decisions about sizing,
placement, or other layout operations. For example, you might read the
flexibility value in your layout view’s `sizeThatFits(_:)` method, and adjust
your size calculations accordingly:

## Topics

### Providing a default value

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the key’s value.

**Required**

## See Also

### Associating values with views in a custom layout

`func layoutValue<K>(key: K.Type, value: K.Value) -> some View`

Associates a value with a custom layout property.

Structure

# AnyLayout

A type-erased instance of the layout protocol.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyLayout

## Overview

Use an `AnyLayout` instance to enable dynamically changing the type of a
layout container without destroying the state of the subviews. For example,
you can create a layout that changes between horizontal and vertical layouts
based on the current Dynamic Type setting:

The types that you use with `AnyLayout` must conform to the `Layout` protocol.
The above example chooses between the `HStackLayout` and `VStackLayout` types,
which are versions of the built-in `HStack` and `VStack` containers that
conform to the protocol. You can also use custom layout types that you define.

## Topics

### Creating the layout

`init<L>(L)`

Creates a type-erased value that wraps the specified layout.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`

## See Also

### Transitioning between layout types

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# HStackLayout

A horizontal container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct HStackLayout

## Overview

This layout container behaves like an `HStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `HStack` instead.

## Topics

### Creating a horizontal stack

`init(alignment: VerticalAlignment, spacing: CGFloat?)`

Creates a horizontal stack with the specified spacing and vertical alignment.

### Getting the stack’s properties

`var alignment: VerticalAlignment`

The vertical alignment of subviews.

`var spacing: CGFloat?`

The distance between adjacent subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# VStackLayout

A vertical container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct VStackLayout

## Overview

This layout container behaves like a `VStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `VStack` instead.

## Topics

### Creating a vertical stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?)`

Creates a vertical stack with the specified spacing and horizontal alignment.

### Getting the stack’s properties

`var alignment: HorizontalAlignment`

The horizontal alignment of subviews.

`var spacing: CGFloat?`

The distance between adjacent subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# ZStackLayout

An overlaying container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ZStackLayout

## Overview

This layout container behaves like a `ZStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `ZStack` instead.

## Topics

### Creating a stack

`init(alignment: Alignment)`

Creates a stack with the specified alignment.

### Getting the stack’s properties

`var alignment: Alignment`

The alignment of subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# GridLayout

A grid that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct GridLayout

## Overview

This layout container behaves like a `Grid`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `Grid` instead.

## Topics

### Creating a grid

`init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing:
CGFloat?)`

Creates a grid with the specified spacing and alignment.

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

### Default Implementations

API Reference

Layout Implementations

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

