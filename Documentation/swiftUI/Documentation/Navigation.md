Article

# Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

## Overview

If your app has a minimum deployment target of iOS 16, iPadOS 16, macOS 13,
tvOS 16, watchOS 9, or visionOS 1, or later, transition away from using
`NavigationView`. In its place, use `NavigationStack` and
`NavigationSplitView` instances. How you use these depends on whether you
perform navigation in one column or across multiple columns. With these newer
containers, you get better control over view presentation, container
configuration, and programmatic navigation.

### Update single column navigation

If your app uses a `NavigationView` that you style using the `stack`
navigation view style, where people navigate by pushing a new view onto a
stack, switch to `NavigationStack`.

In particular, stop doing this:

Instead, create a navigation stack:

### Update multicolumn navigation

If your app uses a two- or three-column `NavigationView`, or for apps that
have multiple columns in some cases and a single column in others — which is
typical for apps that run on iPhone and iPad — switch to
`NavigationSplitView`.

Instead of using a two-column navigation view:

Create a navigation split view that has explicit sidebar and detail content
using the `init(sidebar:detail:)` initializer:

Similarly, instead of using a three-column navigation view:

Create a navigation split view that has explicit sidebar, content, and detail
components using the `init(sidebar:content:detail:)` initializer:

If you need navigation within a column, embed a navigation stack in that
column. This arrangement provides finer control over what each column
displays. `NavigationSplitView` also enables you to customize column
visibility and width.

### Update programmatic navigation

If you perform programmatic navigation using one of the `NavigationLink`
initializers that has an `isActive` input parameter, move the automation to
the enclosing stack. Do this by changing your navigation links to use the
`init(value:label:)` initializer, then use one of the navigation stack
initializers that takes a path input, like `init(path:root:)`.

For example, if you have a navigation view with links that activate in
response to individual state variables:

When some other part of your code sets one of the state variables to true, the
navigation link that has the matching tag activates in response.

Rewrite this as a navigation stack that takes a path input:

This version uses the `navigationDestination(for:destination:)` view modifier
to detach the presented data from the corresponding view. That makes it
possible for the `path` array to represent every view on the stack. Changes
that you make to the array affect what the container displays right now, as
well as what people encounter as they navigate through the stack. You can
support even more sophisticated programmatic navigation if you use a
`NavigationPath` to store the path information, rather than a plain collection
of data. For more information, see `NavigationStack`.

### Update selection-based navigation

If you perform programmatic navigation on `List` elements that use one of the
`NavigationLink` initializers with a `selection` input parameter, you can move
the selection to the list. For example, suppose you have a navigation view
with links that activate in response to a `selection` state variable:

Using the same properties, you can rewrite the body as:

The list coordinates with the navigation logic so that changing the selection
state variable in another part of your code activates the navigation link with
the corresponding color. Similarly, if someone chooses the navigation link
associated with a particular color, the list updates the selection value that
other parts of your code can read.

### Provide backward compatibility with an availability check

If your app needs to run on platform versions earlier than iOS 16, iPadOS 16,
macOS 13, tvOS 16, watchOS 9, or visionOS 1, you can start migration while
continuing to support older clients by using an availability condition. For
example, you can create a custom wrapper view that conditionally uses either
`NavigationSplitView` or `NavigationView`:

Customize the wrapper to meet your app’s needs. For example, you can add a
navigation split view style modifier like `navigationSplitViewStyle(_:)` to
the `NavigationSplitView` in the appropriate branch of the availability check.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationSplitView

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitView<Sidebar, Content, Detail> where Sidebar : View, Content : View, Detail : View

## Overview

You create a navigation split view with two or three columns, and typically
use it as the root view in a `Scene`. People choose one or more items in a
leading column to display details about those items in subsequent columns.

To create a two-column navigation split view, use the `init(sidebar:detail:)`
initializer:

In the above example, the navigation split view coordinates with the `List` in
its first column, so that when people make a selection, the detail view
updates accordingly. Programmatic changes that you make to the selection
property also affect both the list appearance and the presented detail view.

To create a three-column view, use the `init(sidebar:content:detail:)`
initializer. The selection in the first column affects the second, and the
selection in the second column affects the third. For example, you can show a
list of departments, the list of employees in the selected department, and the
details about all of the selected employees:

You can also embed a `NavigationStack` in a column. Tapping or clicking a
`NavigationLink` that appears in an earlier column sets the view that the
stack displays over its root view. Activating a link in the same column adds a
view to the stack. Either way, the link must present a data type for which the
stack has a corresponding `navigationDestination(for:destination:)` modifier.

On watchOS and tvOS, and with narrow sizes like on iPhone or on iPad in Slide
Over, the navigation split view collapses all of its columns into a stack, and
shows the last column that displays useful information. For example, the
three-column example above shows the list of departments to start, the
employees in the department after someone selects a department, and the
employee details when someone selects an employee. For rows in a list that
have `NavigationLink` instances, the list draws disclosure chevrons while in
the collapsed state.

### Control column visibility

You can programmatically control the visibility of navigation split view
columns by creating a `State` value of type `NavigationSplitViewVisibility`.
Then pass a `Binding` to that state to the appropriate initializer — such as
`init(columnVisibility:sidebar:detail:)` for two columns, or the
`init(columnVisibility:sidebar:content:detail:)` for three columns.

The following code updates the first example above to always hide the first
column when the view appears:

The split view ignores the visibility control when it collapses its columns
into a stack.

### Collapsed split views

At narrow size classes, such as on iPhone or Apple Watch, a navigation split
view collapses into a single stack. Typically SwiftUI automatically chooses
the view to show on top of this single stack, based on the content of the
split view’s columns.

For custom navigation experiences, you can provide more information to help
SwiftUI choose the right column. Create a `State` value of type
`NavigationSplitViewColumn`. Then pass a `Binding` to that state to the
appropriate initializer, such as
`init(preferredCompactColumn:sidebar:detail:)` or
`init(preferredCompactColumn:sidebar:content:detail:)`.

The following code shows the blue detail view when run on iPhone. When the
person using the app taps the back button, they’ll see the yellow view. The
value of `preferredPreferredCompactColumn` will change from `.detail` to
`.sidebar`:

### Customize a split view

To specify a preferred column width in a navigation split view, use the
`navigationSplitViewColumnWidth(_:)` modifier. To set minimum, maximum, and
ideal sizes for a column, use
`navigationSplitViewColumnWidth(min:ideal:max:)`. You can specify a different
modifier in each column. The navigation split view does its best to
accommodate the preferences that you specify, but might make adjustments based
on other constraints.

To specify how columns in a navigation split view interact, use the
`navigationSplitViewStyle(_:)` modifier with a `NavigationSplitViewStyle`
value. For example, you can specify whether to emphasize the detail column or
to give all of the columns equal prominence.

On some platforms, `NavigationSplitView` adds a `sidebarToggle` toolbar item.
Use the `toolbar(removing:)` modifier to remove the default item.

## Topics

### Creating a navigation split view

`init(sidebar: () -> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view.

`init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view.

### Hiding columns in a navigation split view

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility.

`init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility.

### Specifying a preferred compact column

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

`init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: ()
-> Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
over which column appears on top when the view collapses into a single column
in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

### Specifying a preferred compact column and column visibility

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, detail: () -> Detail)`

Creates a two-column navigation split view that enables programmatic control
of the sidebar’s visibility in regular sizes and which column appears on top
when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

`init(columnVisibility: Binding<NavigationSplitViewVisibility>,
preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () ->
Sidebar, content: () -> Content, detail: () -> Detail)`

Creates a three-column navigation split view that enables programmatic control
of leading columns’ visibility in regular sizes and which column appears on
top when the view collapses into a single column in narrow sizes.

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and
`Detail` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewStyle(_:)

Sets the style for navigation split views within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewStyle<S>(_ style: S) -> some View where S : NavigationSplitViewStyle
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified navigation split view style.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewColumnWidth(_:)

Sets a fixed, preferred width for the column containing this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewColumnWidth(_ width: CGFloat) -> some View
    

## Discussion

Apply this modifier to the content of a column in a `NavigationSplitView` to
specify a fixed preferred width for the column. Use
`navigationSplitViewColumnWidth(min:ideal:max:)` if you need to specify a
flexible width.

The following example shows a three-column navigation split view where the
first column has a preferred width of 150 points, and the second column has a
flexible, preferred width between 150 and 400 points:

Only some platforms enable resizing columns. If you specify a width that the
current presentation environment doesn’t support, SwiftUI may use a different
width for your column.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Instance Method

# navigationSplitViewColumnWidth(min:ideal:max:)

Sets a flexible, preferred width for the column containing this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewColumnWidth(
        min: CGFloat? = nil,
        ideal: CGFloat,
        max: CGFloat? = nil
    ) -> some View
    

## Discussion

Apply this modifier to the content of a column in a `NavigationSplitView` to
specify a preferred flexible width for the column. Use
`navigationSplitViewColumnWidth(_:)` if you need to specify a fixed width.

The following example shows a three-column navigation split view where the
first column has a preferred width of 150 points, and the second column has a
flexible, preferred width between 150 and 400 points:

Only some platforms enable resizing columns. If you specify a width that the
current presentation environment doesn’t support, SwiftUI may use a different
width for your column.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationSplitViewVisibility

The visibility of the leading columns in a navigation split view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewVisibility

## Overview

Use a value of this type to control the visibility of the columns of a
`NavigationSplitView`. Create a `State` property with a value of this type,
and pass a `Binding` to that state to the
`init(columnVisibility:sidebar:detail:)` or
`init(columnVisibility:sidebar:content:detail:)` initializer when you create
the navigation split view. You can then modify the value elsewhere in your
code to:

  * Hide all but the trailing column with `detailOnly`.

  * Hide the leading column of a three-column navigation split view with `doubleColumn`.

  * Show all the columns with `all`.

  * Rely on the automatic behavior for the current context with `automatic`.

Note

Some platforms don’t respect every option. For example, macOS always displays
the content column.

## Topics

### Getting visibilities

`static var automatic: NavigationSplitViewVisibility`

Use the default leading column visibility for the current device.

`static var all: NavigationSplitViewVisibility`

Show all the columns of a three-column navigation split view.

`static var doubleColumn: NavigationSplitViewVisibility`

Show the content column and detail area of a three-column navigation split
view, or the sidebar column and detail area of a two-column navigation split
view.

`static var detailOnly: NavigationSplitViewVisibility`

Hide the leading two columns of a three-column navigation split view, so that
just the detail area shows.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Sendable`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationLink`

A view that controls a navigation presentation.

Structure

# NavigationLink

A view that controls a navigation presentation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct NavigationLink<Label, Destination> where Label : View, Destination : View

## Overview

People click or tap a navigation link to present a view inside a
`NavigationStack` or `NavigationSplitView`. You control the visual appearance
of the link by providing view content in the link’s `label` closure. For
example, you can use a `Label` to display a link:

For a link composed only of text, you can use one of the convenience
initializers that takes a string and creates a `Text` view for you:

### Link to a destination view

You can perform navigation by initializing a link with a destination view that
you provide in the `destination` closure. For example, consider a
`ColorDetail` view that fills itself with a color:

The following `NavigationStack` presents three links to color detail views:

### Create a presentation link

Alternatively, you can use a navigation link to perform navigation based on a
presented data value. To support this, use the
`navigationDestination(for:destination:)` view modifier inside a navigation
stack to associate a view with a kind of data, and then present a value of
that data type from a navigation link. The following example reimplements the
previous example as a series of presentation links:

Separating the view from the data facilitates programmatic navigation because
you can manage navigation state by recording the presented data.

### Control a presentation link programmatically

To navigate programmatically, introduce a state variable that tracks the items
on a stack. For example, you can create an array of colors to store the stack
state from the previous example, and initialize it as an empty array to start
with an empty stack:

Then pass a `Binding` to the state to the navigation stack:

You can use the array to observe the current state of the stack. You can also
modify the array to change the contents of the stack. For example, you can
programmatically add `blue` to the array, and navigation to a new color detail
view using the following method:

### Coordinate with a list

You can also use a navigation link to control `List` selection in a
`NavigationSplitView`:

The list coordinates with the navigation logic so that changing the selection
state variable in another part of your code activates the navigation link with
the corresponding color. Similarly, if someone chooses the navigation link
associated with a particular color, the list updates the selection value that
other parts of your code can read.

## Topics

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

### Configuring the link

`func isDetailLink(Bool) -> some View`

Sets the navigation link to present its destination as the detail component of
the containing navigation view.

Available when `Label` conforms to `View` and `Destination` conforms to
`View`.

### Deprecated symbols

API Reference

Deprecated symbols

Review deprecated navigation link initializers.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

Structure

# NavigationStack

A view that displays a root view and enables you to present additional views
over the root view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    struct NavigationStack<Data, Root> where Root : View

## Overview

Use a navigation stack to present a stack of views over a root view. People
can add views to the top of the stack by clicking or tapping a
`NavigationLink`, and remove views using built-in, platform-appropriate
controls, like a Back button or a swipe gesture. The stack always displays the
most recently added view that hasn’t been removed, and doesn’t allow the root
view to be removed.

To create navigation links, associate a view with a data type by adding a
`navigationDestination(for:destination:)` modifier inside the stack’s view
hierarchy. Then initialize a `NavigationLink` that presents an instance of the
same kind of data. The following stack displays a `ParkDetails` view for
navigation links that present data of type `Park`:

In this example, the `List` acts as the root view and is always present.
Selecting a navigation link from the list adds a `ParkDetails` view to the
stack, so that it covers the list. Navigating back removes the detail view and
reveals the list again. The system disables backward navigation controls when
the stack is empty and the root view, namely the list, is visible.

### Manage navigation state

By default, a navigation stack manages state to keep track of the views on the
stack. However, your code can share control of the state by initializing the
stack with a binding to a collection of data values that you create. The stack
adds items to the collection as it adds views to the stack and removes items
when it removes views. For example, you can create a `State` property to
manage the navigation for the park detail view:

Initializing the state as an empty array indicates a stack with no views.
Provide a `Binding` to this state property using the dollar sign (`$`) prefix
when you create a stack using the `init(path:root:)` initializer:

Like before, when someone taps or clicks the navigation link for a park, the
stack displays the `ParkDetails` view using the associated park data. However,
now the stack also puts the park data in the `presentedParks` array. Your code
can observe this array to read the current stack state. It can also modify the
array to change the views on the stack. For example, you can create a method
that configures the stack with a specific set of parks:

The `showParks` method replaces the stack’s display with a view that shows
details for Sequoia, the last item in the new `presentedParks` array.
Navigating back from that view removes Sequoia from the array, which reveals a
view that shows details for Yosemite. Use a path to support deep links, state
restoration, or other kinds of programmatic navigation.

### Navigate to different view types

To create a stack that can present more than one kind of view, you can add
multiple `navigationDestination(for:destination:)` modifiers inside the
stack’s view hierarchy, with each modifier presenting a different data type.
The stack matches navigation links with navigation destinations based on their
respective data types.

To create a path for programmatic navigation that contains more than one kind
of data, you can use a `NavigationPath` instance as the path.

## Topics

### Creating a navigation stack

`init(root: () -> Root)`

Creates a navigation stack that manages its own navigation state.

### Creating a navigation stack with a path

`init(path: Binding<Data>, root: () -> Root)`

Creates a navigation stack with homogeneous navigation state that you can
control.

`init(path: Binding<NavigationPath>, root: () -> Root)`

Creates a navigation stack with heterogeneous navigation state that you can
control.

## Relationships

### Conforms To

  * `View`

## See Also

### Stacking views in one column

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Structure

# NavigationPath

A type-erased list of data representing the content of a navigation stack.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct NavigationPath

## Overview

You can manage the state of a `NavigationStack` by initializing the stack with
a binding to a collection of data. The stack stores data items in the
collection for each view on the stack. You also can read and write the
collection to observe and alter the stack’s state.

When a stack displays views that rely on only one kind of data, you can use a
standard collection, like an array, to hold the data. If you need to present
different kinds of data in a single stack, use a navigation path instead. The
path uses type erasure so you can manage a collection of heterogeneous
elements. The path also provides the usual collection controls for adding,
counting, and removing data elements.

### Serialize the path

When the values you present on the navigation stack conform to the `Codable`
protocol, you can use the path’s `codable` property to get a serializable
representation of the path. Use that representation to save and restore the
contents of the stack. For example, you can define an `ObservableObject` that
handles serializing and deserializing the path:

Then, using that object in your view, you can save the state of the navigation
path when the `Scene` enters the `ScenePhase.background` state:

## Topics

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

### Encoding a path

`var codable: NavigationPath.CodableRepresentation?`

A value that describes the contents of this path in a serializable format.

`struct CodableRepresentation`

A serializable representation of a navigation path.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(for:destination:)

Associates a destination view with a presented data type for use within a
navigation stack.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDestination<D, C>(
        for data: D.Type,
        @ViewBuilder destination: @escaping (D) -> C
    ) -> some View where D : Hashable, C : View
    

##  Parameters

`data`

    

The type of data that this destination matches.

`destination`

    

A view builder that defines a view to display when the stack’s navigation
state contains a value of type `data`. The closure takes one argument, which
is the value of the data to present.

## Discussion

Add this view modifer to a view inside a `NavigationStack` to describe the
view that the stack displays when presenting a particular kind of data. Use a
`NavigationLink` to present the data. For example, you can present a
`ColorDetail` view for each presentation of a `Color` instance:

You can add more than one navigation destination modifier to the stack if it
needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation stack can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(isPresented:destination:)

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDestination<V>(
        isPresented: Binding<Bool>,
        @ViewBuilder destination: () -> V
    ) -> some View where V : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view to present.

## Discussion

In general, favor binding a path to a navigation stack for programmatic
navigation. Add this view modifer to a view inside a `NavigationStack` to
programmatically push a single view onto the stack. This is useful for
building components that can push an associated view. For example, you can
present a `ColorDetail` view for a particular color:

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation stack can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

Instance Method

# navigationDestination(item:destination:)

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func navigationDestination<D, C>(
        item: Binding<Optional<D>>,
        @ViewBuilder destination: @escaping (D) -> C
    ) -> some View where D : Hashable, C : View
    

##  Parameters

`item`

    

A binding to the data presented, or `nil` if nothing is currently presented.

`destination`

    

A view builder that defines a view to display when `item` is not `nil`.

## Discussion

Add this view modifer to a view inside a `NavigationStack` or
`NavigationSplitView` to describe the view that the stack displays when
presenting a particular kind of data. Programmatically update the binding to
display or remove the view. For example, you can replace the view showing in
the detail column of a navigation split view:

When the person using the app taps on the Mint button, the mint color shows in
the detail and `colorShown` gets the value `Color.mint`. You can reset the
navigation split view to show the message “Select a color” by setting
`colorShown` back to `nil`.

You can add more than one navigation destination modifier to the stack if it
needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like
`List` or `LazyVStack`. These containers create child views only when needed
to render on screen. Add the navigation destination modifier outside these
containers so that the navigation split view can always see the destination.

## See Also

### Stacking views in one column

`struct NavigationStack`

A view that displays a root view and enables you to present additional views
over the root view.

`struct NavigationPath`

A type-erased list of data representing the content of a navigation stack.

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

Structure

# NavigationSplitViewColumn

A view that represents a column in a navigation split view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct NavigationSplitViewColumn

## Overview

A `NavigationSplitView` collapses into a single stack in some contexts, like
on iPhone or Apple Watch. Use this type with the `preferredCompactColumn`
parameter to control which column of the navigation split view appears on top
of the collapsed stack.

## Topics

### Getting a column

`static var sidebar: NavigationSplitViewColumn`

`static var content: NavigationSplitViewColumn`

`static var detail: NavigationSplitViewColumn`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a localized
string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle(_ titleKey: LocalizedStringKey) -> some View
    

##  Parameters

`titleKey`

    

The key to a localized string to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle(_ title: Text) -> some View
    

##  Parameters

`title`

    

The title to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func navigationTitle<S>(_ title: S) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The string to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a custom view.

watchOS 7.0+

    
    
    func navigationTitle<V>(@ViewBuilder _ title: () -> V) -> some View where V : View
    

##  Parameters

`title`

    

The view to display.

## Discussion

A view’s navigation title is used to visually display the current navigation
state of an interface. On iOS and watchOS, when a view is navigated to inside
of a navigation view, that view’s title is displayed in the navigation bar. On
iPadOS, the primary destination’s navigation title is reflected as the
window’s title in the App Switcher. Similarly on macOS, the primary
destination’s title is used as the window title in the titlebar, Windows menu
and Mission Control.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationTitle(_:)

Configures the view’s title for purposes of navigation, using a string
binding.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationTitle(_ title: Binding<String>) -> some View
    

##  Parameters

`title`

    

The text of the title.

## Discussion

In iOS, iPadOS, and macOS, this allows editing the navigation title when the
title is displayed in the toolbar.

Refer to the Configure your apps navigation titles article for more
information on navigation title modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation, using a string.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle<S>(_ subtitle: S) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The subtitle to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle(_ subtitle: Text) -> some View
    

##  Parameters

`subtitle`

    

The subtitle to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationSubtitle(_:)

Configures the view’s subtitle for purposes of navigation, using a localized
string.

macOS 11.0+  Mac Catalyst 14.0+

    
    
    func navigationSubtitle(_ subtitleKey: LocalizedStringKey) -> some View
    

##  Parameters

`subtitleKey`

    

The key to a localized string to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual
information alongside the navigation title. On macOS, the primary
destination’s subtitle is displayed with the navigation title in the titlebar.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDocument<D>(_ document: D) -> some View where D : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationDocument(_ url: URL) -> some View
    

##  Parameters

`document`

    

The URL content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I>(
        _ document: D,
        preview: SharePreview<I, Never>
    ) -> some View where D : Transferable, I : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I>(
        _ document: D,
        preview: SharePreview<Never, I>
    ) -> some View where D : Transferable, I : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D>(
        _ document: D,
        preview: SharePreview<Never, Never>
    ) -> some View where D : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationDocument(_:preview:)

Configures the view’s document for purposes of navigation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func navigationDocument<D, I1, I2>(
        _ document: D,
        preview: SharePreview<I1, I2>
    ) -> some View where D : Transferable, I1 : Transferable, I2 : Transferable
    

##  Parameters

`document`

    

The transferable content associated to the navigation title.

`preview`

    

The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the
document. In macOS, this populates a proxy icon.

Refer to the Configure your apps navigation titles article for more
information on navigation document modifiers.

## See Also

### Setting titles for navigation content

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

Instance Method

# navigationBarBackButtonHidden(_:)

Hides the navigation bar back button for the view.

iOS 13.0+  iPadOS 13.0+  macOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func navigationBarBackButtonHidden(_ hidesBackButton: Bool = true) -> some View
    

##  Parameters

`hidesBackButton`

    

A Boolean value that indicates whether to hide the back button. The default
value is `true`.

## Discussion

Use `navigationBarBackButtonHidden(_:)` to hide the back button for this view.

This modifier only takes effect when this view is inside of and visible within
a `NavigationView`.

## See Also

### Configuring the navigation bar

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

`struct NavigationBarItem`

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

Instance Method

# navigationBarTitleDisplayMode(_:)

Configures the title display mode for this view.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  watchOS 8.0+  visionOS 1.0+

    
    
    func navigationBarTitleDisplayMode(_ displayMode: NavigationBarItem.TitleDisplayMode) -> some View
    

##  Parameters

`displayMode`

    

The style to use for displaying the title.

## See Also

### Configuring the navigation bar

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`struct NavigationBarItem`

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

Structure

# NavigationBarItem

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct NavigationBarItem

## Overview

Use one of the `NavigationBarItem.TitleDisplayMode` values to configure a
navigation bar title’s display mode with the
`navigationBarTitleDisplayMode(_:)` view modifier.

## Topics

### Setting a title display mode

`enum TitleDisplayMode`

A style for displaying the title of a navigation bar.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring the navigation bar

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

Instance Property

# sidebarRowSize

The current size of sidebar rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var sidebarRowSize: SidebarRowSize { get set }

## Discussion

On macOS, reflects the value of the “Sidebar icon size” in System Settings’
Appearance settings.

This can be used to update the content shown in the sidebar in response to
this size. And it can be overridden to force a sidebar to a particularly size,
regardless of the user preference.

On other platforms, the value is always `.medium` and setting a different
value has no effect.

SwiftUI views like `Label` automatically adapt to the sidebar row size.

## See Also

### Configuring the sidebar

`enum SidebarRowSize`

The standard sizes of sidebar rows.

Enumeration

# SidebarRowSize

The standard sizes of sidebar rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    enum SidebarRowSize

## Overview

On macOS, sidebar rows have three different sizes: small, medium, and large.
The size is primarily controlled by the current users’ “Sidebar Icon Size” in
Appearance settings, and applies to all applications.

On all other platforms, the only supported sidebar size is `.medium`.

This size can be read or written in the environment using
`EnvironmentValues.sidebarRowSize`.

## Topics

### Getting row sizes

`case small`

The standard “small” row size

`case medium`

The standard “medium” row size

`case large`

The standard “large” row size

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring the sidebar

`var sidebarRowSize: SidebarRowSize`

The current size of sidebar rows.

Structure

# TabView

A view that switches between multiple child views using interactive user
interface elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct TabView<SelectionValue, Content> where SelectionValue : Hashable, Content : View

## Overview

To create a user interface with tabs, place views in a `TabView` and apply the
`tabItem(_:)` modifier to the contents of each tab. On iOS, you can also use
one of the badge modifiers, like `badge(_:)`, to assign a badge to each of the
tabs.

The following example creates a tab view with three tabs, each presenting a
custom child view. The first tab has a numeric badge and the third has a
string badge.

Use a `Label` for each tab item, or optionally a `Text`, an `Image`, or an
image followed by text. Passing any other type of view results in a visible
but empty tab item.

## Topics

### Creating a tab view

`init(content: () -> Content)`

Available when `SelectionValue` is `Int` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>?, content: () -> Content)`

Creates an instance that selects from content associated with `Selection`
values.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting views in tabs

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

Instance Method

# tabViewStyle(_:)

Sets the style for the tab view within the current environment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func tabViewStyle<S>(_ style: S) -> some View where S : TabViewStyle
    

##  Parameters

`style`

    

The style to apply to this tab view.

## See Also

### Presenting views in tabs

`struct TabView`

A view that switches between multiple child views using interactive user
interface elements.

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

Instance Method

# tabItem(_:)

Sets the tab bar item associated with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func tabItem<V>(@ViewBuilder _ label: () -> V) -> some View where V : View
    

##  Parameters

`label`

    

The tab bar item to associate with this view.

## Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a `TabView`. The
example below adds two views as tabs in a `TabView`:

## See Also

### Presenting views in tabs

`struct TabView`

A view that switches between multiple child views using interactive user
interface elements.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

Structure

# HSplitView

A layout container that arranges its children in a horizontal line and allows
the user to resize them using dividers placed between them.

macOS 10.15+

    
    
    struct HSplitView<Content> where Content : View

## Topics

### Creating a horizontal split view

`init(content: () -> Content)`

## Relationships

### Conforms To

  * `View`

## See Also

### Displaying views in multiple panes

`struct VSplitView`

A layout container that arranges its children in a vertical line and allows
the user to resize them using dividers placed between them.

Structure

# VSplitView

A layout container that arranges its children in a vertical line and allows
the user to resize them using dividers placed between them.

macOS 10.15+

    
    
    struct VSplitView<Content> where Content : View

## Topics

### Creating a vertical split view

`init(content: () -> Content)`

## Relationships

### Conforms To

  * `View`

## See Also

### Displaying views in multiple panes

`struct HSplitView`

A layout container that arranges its children in a horizontal line and allows
the user to resize them using dividers placed between them.

Structure

# NavigationView

A view for presenting a stack of views that represents a visible path in a
navigation hierarchy.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct NavigationView<Content> where Content : View

Deprecated

Use `NavigationStack` and `NavigationSplitView` instead. For more information,
see Migrating to new navigation types.

## Overview

Use a `NavigationView` to create a navigation-based app in which the user can
traverse a collection of views. Users navigate to a destination view by
selecting a `NavigationLink` that you provide. On iPadOS and macOS, the
destination content appears in the next column. Other platforms push a new
view onto the stack, and enable removing items from the stack with platform-
specific controls, like a Back button or a swipe gesture.

Use the `init(content:)` initializer to create a navigation view that directly
associates navigation links and their destination views:

Style a navigation view by modifying it with the `navigationViewStyle(_:)`
view modifier. Use other modifiers, like `navigationTitle(_:)`, on views
presented by the navigation view to customize the navigation interface for the
presented view.

## Topics

### Creating a navigation view

`init(content: () -> Content)`

Creates a destination-based navigation view.

### Styling navigation views

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

`protocol NavigationViewStyle`

A specification for the appearance and interaction of a navigation view.

## Relationships

### Conforms To

  * `View`

