Article

# Picking container views for your content

Build flexible user interfaces by using stacks, grids, lists, and forms.

## Overview

SwiftUI provides a range of container views that group and repeat views. Use
some containers purely for structure and layout, like stack views, lazy stack
views, and grid views. Use others, like lists and forms, to also adopt system-
standard visuals and interactivity.

Choosing the most appropriate container views for each part of your app’s user
interface is an important skill to learn; it helps you with everything from
positioning two views next to each other, to creating complex layouts with
hundreds of elements.

### Group collections of views

Stack views are the most primitive layout container available in SwiftUI. Use
stacks to group collections of views into horizontal or vertical lines, or to
stack them on top of one another.

Use `HStack` to lay out views in a horizontal line, `VStack` to position views
in a vertical line, and `ZStack` to layer views on top of one another. Then,
combine stack views to compose more complex layouts. These three kinds of
stacks, along with their alignment and spacing properties, view modifiers, and
`Spacer` views combine to allow extensive layout flexibility.

You often use stack views as building blocks inside other container views. For
example, a `List` typically contains stack views, with which you lay out views
inside each row.

For more information on using stack views to lay out views, see Building
layouts with stack views.

### Repeat views or groups of views

You can also use `HStack`, `VStack`, `LazyHStack`, and `LazyVStack` to repeat
views or groups of views. Place a stack view inside a `ScrollView` so your
content can expand beyond the bounds of its container. Users can
simultaneously scroll horizontally, vertically, or in both directions.

Stack views and lazy stacks have similar functionality, and they may feel
interchangeable, but they each have strengths in different situations. Stack
views load their child views all at once, making layout fast and reliable,
because the system knows the size and shape of every subview as it loads them.
Lazy stacks trade some degree of layout correctness for performance, because
the system only calculates the geometry for subviews as they become visible.

When choosing the type of stack view to use, always start with a standard
stack view and only switch to a lazy stack if profiling your code shows a
worthwhile performance improvement. For more information on lazy stack views
and how to measure your app’s view loading performance, see Creating
performant scrollable stacks.

### Position views in a two-dimensional layout

To lay out views horizontally and vertically at the same time, use a
`LazyVGrid` or `LazyHGrid`. Grids are a good container choice to lay out
content that naturally displays in square containers, like an image gallery.
Grids are also a good choice to scale user interface layouts up for display on
larger devices. For example, a directory of contact information might suit a
list or vertical stack on an iPhone, but might fit more naturally in a grid
layout when scaled up to a larger device like the iPad or Mac.

Like stack views, SwiftUI grid views don’t inherently include a scrolling
viewport; place them inside a `ScrollView` if the content might be larger than
the available space.

### Display and interact with collections of data

`List` views in SwiftUI are conceptually similar to the combination of a
`LazyVStack` and `ScrollView`, but by default will include platform-
appropriate visual styling around and between their contained items. For
example, when running on iOS, the default configuration of a `List` adds
separator lines between rows, and draws disclosure indicators for items which
have navigation, and where the list is contained in a `NavigationView`.

`List` views also support platform-appropriate interactivity for common tasks
such as inserting, reordering, and removing items. For example, adding the
`onDelete(perform:)` modifier to a `ForEach` inside a `List` will enable
system-standard swipe-to-delete interactivity.

Like `LazyHStack` and `LazyVStack`, rows inside a SwiftUI `List` also load
lazily, and there is no non-lazy equivalent. Lists inherently scroll when
necessary, and you don’t need to wrap them in a `ScrollView`.

### Group views and controls for data entry

Use `Form` to build data-entry interfaces, settings, or preference screens
that use system-standard controls.

Like all SwiftUI views, forms display their content in a platform-appropriate
way. Be aware that the layout of controls inside a `Form` may differ
significantly based on the platform. For example, a `Picker` control in a
`Form` on iOS adds navigation, showing the picker’s choices on a separate
screen, while the same `Picker` on macOS displays a pop-up button or set of
radio buttons.

Article

# Building layouts with stack views

Compose complex layouts from primitive container views.

## Overview

Individually, `HStack`, `VStack`, and `ZStack` are simple views. `HStack`
positions views in a horizontal line, `VStack` positions them in a vertical
line, and `ZStack` overlays views on top of one another.

When you initialize them with default parameters, stack views center align
their content and insert a small amount of spacing between each contained
view. But, when you combine and customize stacks with view modifiers,
`Spacer`, and `Divider` views, you can create highly flexible and complex
layouts.

### Plan your layout hierarchy

Think about a layout in terms of how you might create it using the various
types of stack views as you start to translate your design into code. Break
down complex designs into smaller, simpler pieces you can build with stack
views.

For example, you might build this profile view using three stack views:

A `ZStack` contains an `Image` view that displays a profile picture with a
semi-transparent `HStack` overlaid on top. The `HStack` contains a `VStack`
with a pair of `Text` views inside it, and a `Spacer` view pushes the `VStack`
to the leading side.

To create this stack view:

### Position views with alignment and spacer views

Align any contained views inside a stack view by using a combination of the
`alignment` property, `Spacer`, and `Divider` views.

In the previous example layout, the `VStack` that contains the two `Text`
views uses the `leading` alignment:

The `alignment` property doesn’t position the `VStack` inside its container;
instead, it positions the views inside the `VStack`.

The `alignment` property of a `VStack` only applies to the horizontal
alignment of the contained controls using `HorizontalAlignment`. Similarly,
the `alignment` property for an `HStack` only controls the vertical alignment
using `VerticalAlignment`. Finally, you can align views inside a `ZStack`
along both axes with `Alignment`.

Use `Spacer` views to align views along the primary axis of an `HStack` or
`VStack`. Spacers expand to fill any available space and push content apart
from other views or the edges of the stack.

`Divider` views also add space in between a stack’s subviews, but only insert
enough space to draw a line across the stack’s minor axis. They don’t expand
to fill available space.

### Create adaptive layouts instead of explicit layouts

Wherever possible, define structure and hierarchy rather than explicitly
positioning view frames. Instead of using explicit heights and widths for
views, let them expand to fill available space. Adaptive layouts that you
build adapt more easily to different device sizes and platforms.

It is possible to create this article’s example layout with two stack views
rather than three, by manipulating the `Text` view frames explicitly. While
the output might look the same, the code to implement it is more brittle, and
might not scale as well across devices of different size classes.

You may need to make adjustments to a layout that uses explicit adjustments by
using view modifiers such as `frame(width:height:alignment:)` or
`position(x:y:)`, but only consider this when you can’t achieve your desired
layout in an adaptive, flexible way. For more information on making fine
adjustments to view layout, see Making fine adjustments to a view’s position.

### Add depth in alternative ways

In some situations it may make sense to add depth to your layout by using the
`overlay(_:alignment:)` and `background(_:alignment:)` view modifiers instead
of a `ZStack`. The background view modifier places another view behind the
view you’re modifying, and overlay places a view on top of it.

Choose between a stack-based approach and the view modifier approach based on
how you want to determine the size of the final layout. If your layout has one
dominant view that defines the size of the layout, use the
`overlay(_:alignment:)` or `background(_:alignment:)` view modifier on that
view. If you want the final view size to come from an aggregation of all the
contained views, use a `ZStack`.

For example, this code overlays a `ProfileDetail` view on top of the `Image`
view:

## See Also

### Statically arranging views in one dimension

`struct HStack`

A view that arranges its subviews in a horizontal line.

`struct VStack`

A view that arranges its subviews in a vertical line.

Structure

# HStack

A view that arranges its subviews in a horizontal line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct HStack<Content> where Content : View

## Overview

Unlike `LazyHStack`, which only renders the views when your app needs to
display them onscreen, an `HStack` renders the views all at once, regardless
of whether they are on- or offscreen. Use the regular `HStack` when you have a
small number of subviews or don’t want the delayed rendering behavior of the
“lazy” version.

The following example shows a simple horizontal stack of five text views:

Note

If you need a horizontal stack that conforms to the `Layout` protocol, like
when you want to create a conditional layout using `AnyLayout`, use
`HStackLayout` instead.

## Topics

### Creating a stack

`init(alignment: VerticalAlignment, spacing: CGFloat?, content: () ->
Content)`

Creates a horizontal stack with the given spacing and vertical alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Statically arranging views in one dimension

Building layouts with stack views

Compose complex layouts from primitive container views.

`struct VStack`

A view that arranges its subviews in a vertical line.

Structure

# VStack

A view that arranges its subviews in a vertical line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct VStack<Content> where Content : View

## Overview

Unlike `LazyVStack`, which only renders the views when your app needs to
display them, a `VStack` renders the views all at once, regardless of whether
they are on- or offscreen. Use the regular `VStack` when you have a small
number of subviews or don’t want the delayed rendering behavior of the “lazy”
version.

The following example shows a simple vertical stack of 10 text views:

Note

If you need a vertical stack that conforms to the `Layout` protocol, like when
you want to create a conditional layout using `AnyLayout`, use `VStackLayout`
instead.

## Topics

### Creating a stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?, content: () ->
Content)`

Creates an instance with the given spacing and horizontal alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Statically arranging views in one dimension

Building layouts with stack views

Compose complex layouts from primitive container views.

`struct HStack`

A view that arranges its subviews in a horizontal line.

Article

# Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

## Overview

`LazyHStack` and `LazyVStack` views are both able to display groups of views
organized into logical sections, arranging their children in lines that grow
horizontally and vertically, respectively. These stacks are “lazy” in that the
stack views don’t create items until they need to be rendered onscreen. Like
stack views, lazy stacks don’t include any inherent support for scrolling, and
you should wrap lazy stack views in `ScrollView` containers.

To group content or data inside a lazy stack view, use `Section` instances as
containers for collections of grouped views. `Section` views don’t have any
visual representation themselves but can contain header and footer views that
can either scroll with the stack’s content or that you can pin to the top or
bottom of the `ScrollView`.

Note

Use `Section` views to get platform-appropriate grouping inside stack views or
lazy stacks, lazy grids, `List`, `CommandMenu`, `Form`, and several other
container types.

The code samples in this article build a user interface for visualizing shades
of primary colors. Each section in the stack represents a primary color,
containing five subviews, each showing a different variation of the color.

### Prepare your data

As with views contained within a stack, each `Section` must be uniquely
identifiable when iterated by `ForEach`. In this example, `ColorData`
instances represent the sections, and `ShadeData` instances represent the
shades of each color inside a section. Both `ColorData` and `ShadeData`
conform to the `Identifiable` protocol.

### Display sections with headers and footers

The `ColorSelectionView` below sets up an array containing `ColorData`
instances for each primary color. The `LazyVStack` iterates over the array of
color data to create sections, then iterates over the `variations` to create
views from the shades.

Group data with `Section` views and pass in a header or footer view with the
`header` and `footer` properties. This example implements a
`SectionHeaderView` as a header view, containing a semi-transparent stack view
and the name of the section’s color in a `Text` label.

For more information on using `ForEach` to repeat views inside a stack, see
Creating performant scrollable stacks.

### Keep important information visible

By default, section header and footer views will scroll in sync with section
content. If you want header and footer views to always remain visible,
regardless of whether the top or bottom of the section is visible, then
specify a set of `PinnedScrollableViews` for the `pinnedViews` property of the
lazy stack view.

In `LazyVStack` containers, headers attach to the top and footers to the
bottom. In `LazyHStack` containers, headers attach to the leading edge and
footers to the trailing edge.

With this change, section headers are pinned to the top of the view as the
user begins to scroll.

## See Also

### Dynamically arranging views in one dimension

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Article

# Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

## Overview

Your apps often need to display more data within a container view than there
is space for on a device’s screen. Horizontal and vertical stacks are a good
solution for repeating views or groups of views, but they don’t have a built-
in mechanism for scrolling. You can add scrolling by wrapping stacks inside a
`ScrollView`, and switch to lazy stacks as performance issues arise.

### Display groups of views in a scrollable container

Implementing repeating views or groups of views can be as simple as wrapping
them in an `HStack` or `VStack` inside a `ScrollView`.

If the `ProfileView` in the example code above has an intrinsic content size
of 200 x 200 points, the maximum width of 500 points that the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
view modifier applies to the `ScrollView` causes the stack to scroll inside
it.

For an introduction to using stacks to group views together, see Building
layouts with stack views.

### Repeat views for your data

Use `ForEach` to repeat views for the data in your app. From a list of profile
data in a `profiles` array, use `ForEach` to create one `ProfileView` per
element in the array inside an `HStack`.

Note

When you use `ForEach`, each element you iterate over must be uniquely
identifiable. Either conform elements to the `Identifiable` protocol, or pass
a key path to a unique identifier as the `id` parameter of
`init(_:id:content:)`.

### Consider lazy stacks for large numbers of views

The three standard stack views, `HStack`, `VStack`, and `ZStack`, all load
their contained view hierarchy when they display, and loading large numbers of
views all at once can result in slow runtime performance.

In the above example, `ProfileView` is a compound view that consists of nested
stack views, text labels, and an image view. Loading a large number of
profiles all at once causes a noticeable slowdown.

As the number of views inside a stack grows, consider using a `LazyHStack` and
`LazyVStack` instead of `HStack` and `VStack`. Lazy stacks load and render
their subviews on-demand, providing significant performance gains when loading
large numbers of subviews.

Stack views and lazy stacks have similar functionality, and they may feel
interchangeable, but they each have strengths in different situations. Stack
views load their child views all at once, making layout fast and reliable,
because the system knows the size and shape of every subview as it loads them.
Lazy stacks trade some degree of layout correctness for performance, because
the system only calculates the geometry for subviews as they become visible.

When choosing the type of stack view to use, always start with a standard
stack view and only switch to a lazy stack if profiling your code shows a
worthwhile performance improvement.

### Profile to find performance problems

When considering which type of stack to use, use the Instruments tool to
profile your application to identify the areas of your user interface code
where large numbers of views are loading inside a stack.

To profile SwiftUI view loading, open the Instruments tool by selecting
Profile from the Xcode Product menu and choosing the SwiftUI profiling
template. This template loads four instruments: View Body, View Properties,
Core Animation Commits, and Time Profiler. The combination of these
instruments provides a good starting point to find opportunities to speed up
your app.

Note

Never profile your code using the iOS simulator. Always use real devices for
performance testing.

When profiling the above code, the View Body instrument shows that 1,000
`ProfileView` instances load into memory at the same time as the `HStack`. You
can also see the same number of `Image` views load as the system loads each
profile.

In this case, the solution is to replace the `HStack` with a `LazyHStack` as
the following code shows:

Running another trace shows a drastic reduction in the number of initially
loaded views as only four `ProfileView` instances start as visible. You can
also see a corresponding decrease in the Total Duration column.

For more information about using the Instruments tool, see
doc://com.apple.documentation/documentation/metrickit/improving_your_app_s_performance.

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# LazyHStack

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyHStack<Content> where Content : View

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it
needs to render them onscreen.

In the following example, a `ScrollView` contains a `LazyHStack` that consists
of a horizontal row of text views. The stack aligns to the top of the scroll
view and uses 10-point spacing between each text view.

## Topics

### Creating a lazy-loading horizontal stack

`init(alignment: VerticalAlignment, spacing: CGFloat?, pinnedViews:
PinnedScrollableViews, content: () -> Content)`

Creates a lazy horizontal stack view with the given spacing, vertical
alignment, pinning behavior, and content.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# LazyVStack

A view that arranges its children in a line that grows vertically, creating
items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyVStack<Content> where Content : View

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it
needs to render them onscreen.

In the following example, a `ScrollView` contains a `LazyVStack` that consists
of a vertical row of text views. The stack aligns to the leading edge of the
scroll view, and uses default spacing between the text views.

## Topics

### Creating a lazy-loading vertical stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?, pinnedViews:
PinnedScrollableViews, content: () -> Content)`

Creates a lazy vertical stack view with the given spacing, vertical alignment,
pinning behavior, and content.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# PinnedScrollableViews

A set of view types that may be pinned to the bounds of a scroll view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct PinnedScrollableViews

## Topics

### Getting scrollable view types

`static let sectionHeaders: PinnedScrollableViews`

The header view of each `Section` will be pinned.

`static let sectionFooters: PinnedScrollableViews`

The footer view of each `Section` will be pinned.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

Structure

# Grid

A container view that arranges other views in a two dimensional layout.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct Grid<Content> where Content : View

## Overview

Create a two dimensional layout by initializing a `Grid` with a collection of
`GridRow` structures. The first view in each grid row appears in the grid’s
first column, the second view in the second column, and so on. The following
example creates a grid with two rows and two columns:

A grid and its rows behave something like a collection of `HStack` instances
wrapped in a `VStack`. However, the grid handles row and column creation as a
single operation, which applies alignment and spacing to cells, rather than
first to rows and then to a column of unrelated rows. The grid produced by the
example above demonstrates this:

Note

If you need a grid that conforms to the `Layout` protocol, like when you want
to create a conditional layout using `AnyLayout`, use `GridLayout` instead.

### Multicolumn cells

If you provide a view rather than a `GridRow` as an element in the grid’s
content, the grid uses the view to create a row that spans all of the grid’s
columns. For example, you can add a `Divider` between the rows of the previous
example:

Because a divider takes as much horizontal space as its parent offers, the
entire grid widens to fill the width offered by its parent view.

To prevent a flexible view from taking more space on a given axis than the
other cells in a row or column require, add the `gridCellUnsizedAxes(_:)` view
modifier to the view:

This restores the grid to the width that the text and images require:

To make a cell span a specific number of columns rather than the whole grid,
use the `gridCellColumns(_:)` modifier on a view that’s contained inside a
`GridRow`.

### Column count

The grid’s column count grows to handle the row with the largest number of
columns. If you create rows with different numbers of columns, the grid adds
empty cells to the trailing edge of rows that have fewer columns. The example
below creates three rows with different column counts:

The resulting grid has as many columns as the widest row, adding empty cells
to rows that don’t specify enough views:

The grid sets the width of all the cells in a column to match the needs of
column’s widest cell. In the example above, the width of the first column
depends on the width of the widest `Text` view that the column contains. The
other columns, which contain flexible `Color` views, share the remaining
horizontal space offered by the grid’s parent view equally.

Similarly, the tallest cell in a row sets the height of the entire row. The
cells in the first column of the grid above need only the height required for
each string, but the `Color` cells expand to equally share the total height
available to the grid. As a result, the color cells determine the row heights.

### Cell spacing and alignment

You can control the spacing between cells in both the horizontal and vertical
dimensions and set a default alignment for the content in all the grid cells
when you initialize the grid using the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
Consider a modified version of the previous example:

This configuration causes all of the cells to use `bottom` alignment — which
only affects the text cells because the colors fill their cells completely —
and it reduces the spacing between cells:

You can override the alignment of specific cells or groups of cells. For
example, you can change the horizontal alignment of the cells in a column by
adding the `gridColumnAlignment(_:)` modifier, or the vertical alignment of
the cells in a row by configuring the row’s `init(alignment:content:)`
initializer. You can also align a single cell with the `gridCellAnchor(_:)`
modifier.

### Performance considerations

A grid can size its rows and columns correctly because it renders all of its
child views immediately. If your app exhibits poor performance when it first
displays a large grid that appears inside a `ScrollView`, consider switching
to a `LazyVGrid` or `LazyHGrid` instead.

Lazy grids render their cells when SwiftUI needs to display them, rather than
all at once. This reduces the initial cost of displaying a large scrollable
grid that’s never fully visible, but also reduces the grid’s ability to
optimally lay out cells. Switch to a lazy grid only if profiling your code
shows a worthwhile performance improvement.

## Topics

### Creating a grid

`init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing:
CGFloat?, content: () -> Content)`

Creates a grid with the specified spacing, alignment, and child views.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Statically arranging views in two dimensions

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Structure

# GridRow

A horizontal row in a two dimensional grid container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct GridRow<Content> where Content : View

## Overview

Use one or more `GridRow` instances to define the rows of a `Grid` container.
The child views inside the row define successive grid cells. You can add rows
to the grid explicitly, or use the `ForEach` structure to generate multiple
rows. Similarly, you can add cells to the row explicitly or you can use
`ForEach` to generate multiple cells inside the row. The following example
mixes these strategies:

The grid in the example above has an explicit first row and three generated
rows. Similarly, each row has an explicit first cell and three generated
cells:

To create an empty cell, use something invisible, like the `clear` color that
appears in the first column of the first row in the example above. However, if
you use a flexible view like a `Color` or a `Spacer`, you might also need to
add the `gridCellUnsizedAxes(_:)` modifier to prevent the view from taking up
more space than the other cells in the row or column need.

Important

You can’t use `EmptyView` to create a blank cell because that resolves to the
absence of a view and doesn’t generate a cell.

By default, the cells in the row use the `Alignment` that you define when you
initialize the `Grid`. However, you can override the vertical alignment for
the cells in a row by providing a `VerticalAlignment` value to the row’s
`init(alignment:content:)` initializer.

If you apply a view modifier to a row, the row applies the modifier to all of
the cells, similar to how a `Group` behaves. For example, if you apply the
`border(_:width:)` modifier to a row, SwiftUI draws a border on each cell in
the row rather than around the row.

## Topics

### Creating a grid row

`init(alignment: VerticalAlignment?, content: () -> Content)`

Creates a horizontal row of child views in a grid.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellColumns(_:)

Tells a view that acts as a cell in a grid to span the specified number of
columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellColumns(_ count: Int) -> some View
    

##  Parameters

`count`

    

The number of columns that the view should consume when placed in a grid row.

## Return Value

A view that occupies the specified number of columns in a grid row.

## Discussion

By default, each view that you put into the content closure of a `GridRow`
corresponds to exactly one column of the grid. Apply the `gridCellColumns(_:)`
modifier to a view that you want to span more than one column, as in the
following example of a typical macOS configuration view:

The `Toggle` in the example above spans the column that contains the font
names and the column that contains the buttons:

Important

When you tell a cell to span multiple columns, the grid changes the merged
cell to use anchor alignment, rather than the usual alignment guides. For
information about the behavior of anchor alignment, see `gridCellAnchor(_:)`.

As a convenience you can cause a view to span all of the `Grid` columns by
placing the view directly in the content closure of the `Grid`, outside of a
`GridRow`, and omitting the modifier. To do the opposite and include more than
one view in a cell, group the views using an appropriate layout container,
like an `HStack`, so that they act as a single view.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellAnchor(_:)

Specifies a custom alignment anchor for a view that acts as a grid cell.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellAnchor(_ anchor: UnitPoint) -> some View
    

##  Parameters

`anchor`

    

The unit point that defines how to align the view within the bounds of its
grid cell.

## Return Value

A view that uses the specified anchor point to align its content.

## Discussion

Grids, like stacks and other layout containers, perform most alignment
operations using alignment guides. The grid moves the contents of each cell in
a row in the y direction until the specified `VerticalAlignment` guide of each
view in the row aligns with the same guide of all the other views in the row.
Similarly, the grid aligns the `HorizontalAlignment` guides of views in a
column by adjusting views in the x direction. See the guide types for more
information about typical SwiftUI alignment operations.

When you use the `gridCellAnchor(_:)` modifier on a view in a grid, the grid
changes to an anchor-based alignment strategy for the associated cell. With
anchor alignment, the grid projects a `UnitPoint` that you specify onto both
the view and the cell, and aligns the two projections. For example, consider
the following grid:

The grid creates red reference squares in the first row and column to
establish row and column sizes. Without the anchor modifier, the blue marker
in the remaining cell would appear at the center of its cell, because of the
grid’s default `center` alignment. With the anchor modifier shown in the code
above, the grid aligns the one quarter point of the marker with the one
quarter point of its cell in the x direction, as measured from the origin at
the top left of the cell. The grid also aligns the three quarters point of the
marker with the three quarters point of the cell in the y direction:

`UnitPoint` defines many convenience points that correspond to the typical
alignment guides, which you can use as well. For example, you can use
`topTrailing` to align the top and trailing edges of a view in a cell with the
top and trailing edges of the cell:

Applying the anchor-based alignment strategy to a single cell doesn’t affect
the alignment strategy that the grid uses on other cells.

### Anchor alignment for merged cells

If you use the `gridCellColumns(_:)` modifier to cause a cell to span more
than one column, or if you place a view in a grid outside of a row so that the
view spans the entire grid, the grid automatically converts its vertical and
horizontal alignment guides to the unit point equivalent for the merged cell,
and uses an anchor-based approach for that cell. For example, the following
grid places the marker at the center of the merged cell by converting the
grid’s default `center` alignment guide to a `center` anchor for the blue
marker in the merged cell:

The grid makes this conversion in part to avoid ambiguity. Each column has its
own horizontal guide, and it isn’t clear which of these a cell that spans
multiple columns should align with. Further, in the example above, neither of
the center alignment guides for the second or third column would provide the
expected behavior, which is to center the marker in the merged cell. Anchor
alignment provides this behavior:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellUnsizedAxes(_:)

Asks grid layouts not to offer the view extra size in the specified axes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellUnsizedAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The dimensions in which the grid shouldn’t offer the view a share of any
available space. This prevents a flexible view like a `Spacer`, `Divider`, or
`Color` from defining the size of a row or column.

## Return Value

A view that doesn’t ask an enclosing grid for extra size in one or more axes.

## Discussion

Use this modifier to prevent a flexible view from taking more space on the
specified axes than the other cells in a row or column require. For example,
consider the following `Grid` that places a `Divider` between two rows of
content:

The text and images all have ideal widths for their content. However, because
a divider takes as much space as its parent offers, the grid fills the width
of the display, expanding all the other cells to match:

You can prevent the grid from giving the divider more width than the other
cells require by adding the modifier with the `Axis.horizontal` parameter:

This restores the grid to the width that it would have without the divider:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridColumnAlignment(_:)

Overrides the default horizontal alignment of the grid column that the view
appears in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
    

##  Parameters

`guide`

    

The `HorizontalAlignment` guide to use for the grid column that the view
appears in.

## Return Value

A view that uses the specified horizontal alignment, and that causes all cells
in the same column of a grid to use the same alignment.

## Discussion

You set a default alignment for the cells in a grid in both vertical and
horizontal dimensions when you create the grid with the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
However, you can use the `gridColumnAlignment(_:)` modifier to override the
horizontal alignment of a column within the grid. The following example sets a
grid’s alignment to `leadingFirstTextBaseline`, and then sets the first column
to use `trailing` alignment:

This creates the layout of a typical macOS configuration view, with the
trailing edge of the first column flush with the leading edge of the second
column:

Add the modifier to only one cell in a column. The grid automatically aligns
all cells in that column the same way. You get undefined behavior if you apply
different alignments to different cells in the same column.

To override row alignment, see `init(alignment:content:)`. To override
alignment for a single cell, see `gridCellAnchor(_:)`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

Structure

# LazyHGrid

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyHGrid<Content> where Content : View

## Overview

Use a lazy horizontal grid when you want to display a large, horizontally
scrollable collection of views arranged in a two dimensional layout. The first
view that you provide to the grid’s `content` closure appears in the top row
of the column that’s on the grid’s leading edge. Additional views occupy
successive cells in the grid, filling the first column from top to bottom,
then the second column, and so on. The number of columns can grow unbounded,
but you specify the number of rows by providing a corresponding number of
`GridItem` instances to the grid’s initializer.

The grid in the following example defines two rows and uses a `ForEach`
structure to repeatedly generate a pair of `Text` views for the rows in each
column:

For each column in the grid, the top row shows a Unicode code point from the
“Smileys” group, and the bottom shows its corresponding emoji:

You can achieve a similar layout using a `Grid` container. Unlike a lazy grid,
which creates child views only when SwiftUI needs to display them, a regular
grid creates all of its child views right away. This enables the grid to
provide better support for cell spacing and alignment. Only use a lazy grid if
profiling your app shows that a `Grid` view performs poorly because it tries
to load too many views at once.

## Topics

### Creating a horizontal grid

`init(rows: [GridItem], alignment: VerticalAlignment, spacing: CGFloat?,
pinnedViews: PinnedScrollableViews, content: () -> Content)`

Creates a grid that grows horizontally.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyVGrid`

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

`struct GridItem`

A description of a row or a column in a lazy grid.

Structure

# LazyVGrid

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyVGrid<Content> where Content : View

## Overview

Use a lazy vertical grid when you want to display a large, vertically
scrollable collection of views arranged in a two dimensional layout. The first
view that you provide to the grid’s `content` closure appears in the top row
of the column that’s on the grid’s leading edge. Additional views occupy
successive cells in the grid, filling the first row from leading to trailing
edges, then the second row, and so on. The number of rows can grow unbounded,
but you specify the number of columns by providing a corresponding number of
`GridItem` instances to the grid’s initializer.

The grid in the following example defines two columns and uses a `ForEach`
structure to repeatedly generate a pair of `Text` views for the columns in
each row:

For each row in the grid, the first column shows a Unicode code point from the
“Smileys” group, and the second shows its corresponding emoji:

You can achieve a similar layout using a `Grid` container. Unlike a lazy grid,
which creates child views only when SwiftUI needs to display them, a regular
grid creates all of its child views right away. This enables the grid to
provide better support for cell spacing and alignment. Only use a lazy grid if
profiling your app shows that a `Grid` view performs poorly because it tries
to load too many views at once.

## Topics

### Creating a vertical grid

`init(columns: [GridItem], alignment: HorizontalAlignment, spacing: CGFloat?,
pinnedViews: PinnedScrollableViews, content: () -> Content)`

Creates a grid that grows vertically.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyHGrid`

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

`struct GridItem`

A description of a row or a column in a lazy grid.

Structure

# GridItem

A description of a row or a column in a lazy grid.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct GridItem

## Overview

Use an array of `GridItem` instances to configure the layout of items in a
lazy grid. Each grid item in the array specifies layout properties like size
and spacing for the rows of a `LazyHGrid` or the columns of a `LazyVGrid`. The
following example defines four rows for a horizontal grid, each with different
characteristics:

A lazy horizontal grid sets the width of each column based on the widest cell
in the column. It can do this because it has access to all of the views in a
given column at once. In the example above, the `Color` views always have the
same fixed width, resulting in a uniform column width across the whole grid.

However, a lazy horizontal grid doesn’t generally have access to all the views
in a row, because it generates new cells as people scroll through information
in your app. Instead, it relies on a grid item for information about each row.
The example above indicates a different fixed height for each row, and sets a
different amount of spacing to appear after each row:

## Topics

### Creating a grid item

`init(GridItem.Size, spacing: CGFloat?, alignment: Alignment?)`

Creates a grid item with the specified size, spacing, and alignment.

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyHGrid`

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

`struct LazyVGrid`

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

Article

# Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

## Overview

You can add a view as a background with the `background(_:alignment:)` view
modifier. To add a background under multiple views, or to have a background
larger than an existing view, you can layer the views by placing them within a
`ZStack`, and place the view you want to be in the background at the bottom of
the view stack. You can specify that a background view should ignore the safe
area insets to extend the background to some or all edges.

### Add a background

If your design calls for a background, you can use the
`background(_:alignment:)` modifier to add it underneath an existing view. The
following example adds a gradient to the vertical stack using the
`background(_:alignment:)` view modifier:

The `background(_:alignment:)` view modifier constrains the size of the
background view to be the same size as the view to which it’s attached:

### Expand the background underneath your view

To create a background that’s larger than the vertical stack, use a different
technique. You could add `Spacer` views above and below the content in the
`VStack` to expand it, but that would also expand the size of the stack,
possibly changing it’s layout. To add in a larger background without changing
the size of the stack, nest the views within a `ZStack` to layer the `VStack`
over the background view:

View sizes within a depth stack are independent, unlike when using the
background view modifier. The view from `Gradient` expands to fill the space
available to the stack, but avoids the safe area insets by default:

For more information on usings stacks to combine views, see Building layouts
with stack views.

### Extend the background into the safe areas

By default, SwiftUI sizes and positions views to avoid system defined safe
areas to ensure that system content or the edges of the device won’t obstruct
your views. If your design calls for the background to extend to the screen
edges, use the `ignoresSafeArea(_:edges:)` modifier to override the default.

The background gradient fills the display area of the device and ignores the
safe area insets.

### Adjust views when displaying the keyboard

You can ignore the keyboard’s safe area by adding the
`ignoresSafeArea(_:edges:)` modifier. When you activate the keyboard, the
content of the vertical stack remains fixed, ignoring the space used by the
keyboard:

To get the contents of the vertical stack to respect the safe areas and adjust
to the keyboard, move the modifier to only apply to the background view.

To accommodate the keyboard, SwiftUI resizes and positions your view. Because
the background view has the `ignoresSafeArea(_:edges:)` modifier, it remains
unchanged.

## See Also

### Layering views

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Structure

# ZStack

A view that overlays its subviews, aligning them in both axes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ZStack<Content> where Content : View

## Overview

The `ZStack` assigns each successive subview a higher z-axis value than the
one before it, meaning later subviews appear “on top” of earlier ones.

The following example creates a `ZStack` of 100 x 100 point `Rectangle` views
filled with one of six colors, offsetting each successive subview by 10 points
so they don’t completely overlap:

The `ZStack` uses an `Alignment` to set the x- and y-axis coordinates of each
subview, defaulting to a `center` alignment. In the following example, the
`ZStack` uses a `bottomLeading` alignment to lay out two subviews, a red 100 x
50 point rectangle below, and a blue 50 x 100 point rectangle on top. Because
of the alignment value, both rectangles share a bottom-left corner with the
`ZStack` (in locales where left is the leading side).

Note

If you need a version of this stack that conforms to the `Layout` protocol,
like when you want to create a conditional layout using `AnyLayout`, use
`ZStackLayout` instead.

## Topics

### Creating a stack

`init(alignment: Alignment, content: () -> Content)`

Creates an instance with the given alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# zIndex(_:)

Controls the display order of overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func zIndex(_ value: Double) -> some View
    

##  Parameters

`value`

    

A relative front-to-back ordering for this view; the default is `0`.

## Discussion

Use `zIndex(_:)` when you want to control the front-to-back ordering of views.

In this example there are two overlapping rotated rectangles. The frontmost is
represented by the larger index value.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(alignment:content:)

Layers the views that you specify behind this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw behind this view,
stacked in a cascading order from bottom to top. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a background.

## Discussion

Use this modifier to place one or more views behind another view. For example,
you can place a collection of stars beind a `Text` view:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places behind the text:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can layer a vertical bar
behind a circle, with both of those behind a horizontal bar:

Both the background modifier and the implicit `ZStack` composed from the
background content — the circle and the vertical bar — use a default `center`
alignment. The vertical bar appears centered behind the circle, and both
appear as a composite view centered behind the horizontal bar:

If you specify an alignment for the background, it applies to the implicit
stack rather than to the individual views in the closure. You can see this if
you add the `leading` alignment:

The vertical bar and the circle move as a unit to align the stack with the
leading edge of the horizontal bar, while the vertical bar remains centered on
the circle:

To control the placement of individual items inside the `content` closure,
either use a different background modifier for each item, as the earlier
example of stars under text demonstrates, or add an explicit `ZStack` inside
the content closure with its own alignment:

The stack alignment ensures that the circle’s leading edge aligns with the
vertical bar’s, while the background modifier aligns the composite view with
the horizontal bar:

You can achieve layering without a background modifier by putting both the
modified view and the background content into a `ZStack`. This produces a
simpler view hierarchy, but it changes the layout priority that SwiftUI
applies to the views. Use the background modifier when you want the modified
view to dominate the layout.

If you want to specify a `ShapeStyle` like a `HierarchicalShapeStyle` or a
`Material` as the background, use `background(_:ignoresSafeAreaEdges:)`
instead. To specify a `Shape` or `InsettableShape`, use
`background(_:in:fillStyle:)` or `background(_:in:fillStyle:)`, respectively.
To configure the background of a presentation, like a sheet, use
`presentationBackground(alignment:content:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:ignoresSafeAreaEdges:)

Sets the view’s background to a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI draws behind
the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the specified style drawn behind it.

## Discussion

Use this modifier to place a type that conforms to the `ShapeStyle` protocol —
like a `Color`, `Material`, or `HierarchicalShapeStyle` — behind a view. For
example, you can add the `regularMaterial` behind a `Label`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
background fills the entirety of the label’s frame, which includes the
padding:

SwiftUI limits the background style’s extent to the modified view’s container-
relative shape. You can see this effect if you constrain the `FlagLabel` view
with a `containerShape(_:)` modifier:

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(ignoresSafeAreaEdges:)

Sets the view’s background to the default background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the `background` shape style drawn behind it.

## Discussion

This modifier behaves like `background(_:ignoresSafeAreaEdges:)`, except that
it always uses the `background` shape style. For example, you can add a
background to a `Label`:

Without the background modifier, the teal color behind the label shows through
the label. With the modifier, the label’s text and icon appear backed by a
region filled with a color that’s appropriate for light or dark appearance:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to an insettable shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : InsettableShape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `InsettableShape`
protocol — like a `Rectangle`, `Circle`, or `Capsule` — behind a view. Specify
the `ShapeStyle` that’s used to fill the shape. For example, you can place a
`RoundedRectangle` behind a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to an insettable shape filled with the default
background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified insettable
shape. For example, you can use a `RoundedRectangle` as a background on a
`Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to a shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol behind
a view. Specify the `ShapeStyle` that’s used to fill the shape. For example,
you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to a shape filled with the default background
style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified shape. For
example, you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(alignment:content:)

Layers the views that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the foreground views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw in front of this
view, stacked in the order that you list them. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a foreground.

## Discussion

Use this modifier to place one or more views in front of another view. For
example, you can place a group of stars on a `RoundedRectangle`:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can place a star and a
`Circle` on a field of `blue`:

Both the overlay modifier and the implicit `ZStack` composed from the overlay
content — the circle and the star — use a default `center` alignment. The star
appears centered on the circle, and both appear as a composite view centered
in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack
rather than to the individual views in the closure. You can see this if you
add the `bottom` alignment:

The circle and the star move down as a unit to align the stack’s bottom edge
with the bottom edge of the square, while the star remains centered on the
circle:

To control the placement of individual items inside the `content` closure,
either use a different overlay modifier for each item, as the earlier example
of stars in the corners of a rectangle demonstrates, or add an explicit
`ZStack` inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the
circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the
modified view and the overlay content into a `ZStack`. This can produce a
simpler view hierarchy, but changes the layout priority that SwiftUI applies
to the views. Use the overlay modifier when you want the modified view to
dominate the layout.

If you want to specify a `ShapeStyle` like a `Color` or a `Material` as the
overlay, use `overlay(_:ignoresSafeAreaEdges:)` instead. To specify a `Shape`,
use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:ignoresSafeAreaEdges:)

Layers the specified style in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI layers in
front of the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the overlay.
The default value is `all`. Specify an empty set to respect safe area insets
on all edges.

## Return Value

A view with the specified style drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `ShapeStyle` protocol,
like a `Color`, `Material`, or `HierarchicalShapeStyle`, in front of a view.
For example, you can overlay the `ultraThinMaterial` over a `Circle`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
overlay fills the entirety of the circle’s frame (which happens to be wider
than the circle is tall):

SwiftUI also limits the style’s extent to the view’s container-relative shape.
You can see this effect if you constrain the `CoveredCircle` view with a
`containerShape(_:)` modifier:

The overlay takes on the specified container shape:

By default, the overlay ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the overlay rather than
a style, use `overlay(alignment:content:)` instead. If you want to specify a
`Shape`, use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:in:fillStyle:)

Layers a shape that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws in front of
the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol — like
a `Rectangle`, `Circle`, or `Capsule` — in front of a view. Specify a
`ShapeStyle` that’s used to fill the shape. For example, you can overlay the
outline of one rectangle in front of another:

The example above uses the `inset(by:)` method to slightly reduce the size of
the overlaid rectangle, and the `stroke(lineWidth:)` method to fill only the
shape’s outline. This creates an inset border:

This modifier is a convenience method for layering a shape over a view. To
handle the more general case of overlaying a `View` — or a stack of views —
with control over the position, use `overlay(alignment:content:)` instead. To
cover a view with a `ShapeStyle`, use `overlay(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Property

# backgroundMaterial

The material underneath the current view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var backgroundMaterial: Material? { get set }

## Discussion

This value is `nil` if the current background isn’t one of the standard
materials. If you set a material, the standard content styles enable their
vibrant rendering modes.

You set this value by calling one of the background modifiers that takes a
`ShapeStyle`, like `background(_:ignoresSafeAreaEdges:)` or
`background(_:in:fillStyle:)`, and passing in a `Material`. You can also set
the value manually, using `nil` to disable vibrant rendering, or a `Material`
instance to enable the vibrancy style associated with the specified material.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(_:for:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<S>(
        _ style: S,
        for container: ContainerBackgroundPlacement
    ) -> some View where S : ShapeStyle
    

## Discussion

The following example uses a `LinearGradient` as a background:

The `.containerBackground(_:for:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

  * Parameters

    * style: The shape style to use as the container background.

    * container: The container that will use the background.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(for:alignment:content:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<V>(
        for container: ContainerBackgroundPlacement,
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`container`

    

The container that will use the background.

`content`

    

The view to use as the background of the container.

## Discussion

The following example uses a custom `View` as a background:

The `.containerBackground(for:alignment:content:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Structure

# ContainerBackgroundPlacement

The placement of a container background.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContainerBackgroundPlacement

## Overview

This method controls where to place a background that you specify with the
`containerBackground(_:for:)` or `containerBackground(for:alignment:content:)`
modifier.

## Topics

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

Structure

# ViewThatFits

A view that adapts to the available space by providing the first child view
that fits.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ViewThatFits<Content> where Content : View

## Overview

`ViewThatFits` evaluates its child views in the order you provide them to the
initializer. It selects the first child whose ideal size on the constrained
axes fits within the proposed size. This means that you provide views in order
of preference. Usually this order is largest to smallest, but since a view
might fit along one constrained axis but not the other, this isn’t always the
case. By default, `ViewThatFits` constrains in both the horizontal and
vertical axes.

The following example shows an `UploadProgressView` that uses `ViewThatFits`
to display the upload progress in one of three ways. In order, it attempts to
display:

  * An `HStack` that contains a `Text` view and a `ProgressView`.

  * Only the `ProgressView`.

  * Only the `Text` view.

The progress views are fixed to a 100-point width.

This use of `ViewThatFits` evaluates sizes only on the horizontal axis. The
following code fits the `UploadProgressView` to several fixed widths:

## Topics

### Creating a view that fits

`init(in: Axis.Set, content: () -> Content)`

Produces a view constrained in the given axes from one of several alternatives
provided by a view builder.

## Relationships

### Conforms To

  * `View`

Structure

# Spacer

A flexible space that expands along the major axis of its containing stack
layout, or on both axes if not contained in a stack.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Spacer

## Overview

A spacer creates an adaptive view with no content that expands as much as it
can. For example, when placed within an `HStack`, a spacer expands
horizontally as much as the stack allows, moving sibling views out of the way,
within the limits of the stack’s size. SwiftUI sizes a stack that doesn’t
contain a spacer up to the combined ideal widths of the content of the stack’s
child views.

The following example provides a simple checklist row to illustrate how you
can use a spacer:

Adding a spacer before the image creates an adaptive view with no content that
expands to push the image and text to the right side of the stack. The stack
also now expands to take as much space as the parent view allows, shown by the
blue border that indicates the boundary of the stack:

Moving the spacer between the image and the name pushes those elements to the
left and right sides of the `HStack`, respectively. Because the stack contains
the spacer, it expands to take as much horizontal space as the parent view
allows; the blue border indicates its size:

Adding two spacer views on the outside of the stack leaves the image and text
together, while the stack expands to take as much horizontal space as the
parent view allows:

## Topics

### Creating a spacer

`init(minLength: CGFloat?)`

`var minLength: CGFloat?`

The minimum length this spacer can be shrunk to, along the axis or axes of
expansion.

## Relationships

### Conforms To

  * `Sendable`
  * `View`

## See Also

### Separators

`struct Divider`

A visual element that can be used to separate other content.

Structure

# Divider

A visual element that can be used to separate other content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Divider

## Overview

When contained in a stack, the divider extends across the minor axis of the
stack, or horizontally when not in a stack.

## Topics

### Creating a divider

`init()`

## Relationships

### Conforms To

  * `View`

## See Also

### Separators

`struct Spacer`

A flexible space that expands along the major axis of its containing stack
layout, or on both axes if not contained in a stack.

