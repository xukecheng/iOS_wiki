Instance Property

# body

The content and behavior of this widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## See Also

### Implementing a widget

`associatedtype Body : WidgetConfiguration`

The type of widget configuration representing the body of this configuration.

**Required**

Associated Type

# Body

The type of widget configuration representing the body of this configuration.

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

The content and behavior of this widget.

**Required**

Instance Method

# configurationDisplayName(_:)

Sets the name shown for a widget when a user adds or edits it using the
specified string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName<S>(_ displayName: S) -> some WidgetConfiguration where S : StringProtocol
    

##  Parameters

`displayName`

    

A string describing the widget.

## Return Value

A widget configuration that includes a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

Instance Method

# configurationDisplayName(_:)

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName(_ displayName: Text) -> some WidgetConfiguration
    

##  Parameters

`displayName`

    

A text view containing a localized string to display.

## Return Value

A widget configuration with a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

Instance Method

# configurationDisplayName(_:)

Sets the localized name shown for a widget when a user adds or edits the
widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName(_ displayNameKey: LocalizedStringKey) -> some WidgetConfiguration
    

##  Parameters

`displayName`

    

The key for the localized name to display.

## Return Value

A widget configuration that includes a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

Instance Method

# description(_:)

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description(_ description: Text) -> some WidgetConfiguration
    

##  Parameters

`description`

    

A text view containing a localized string to display.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

Instance Method

# description(_:)

Sets the description shown for a widget when a user adds or edits it using the
specified string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol
    

##  Parameters

`displayName`

    

A string describing the widget.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

Instance Method

# description(_:)

Sets the localized description shown for a widget when a user adds or edits
the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description(_ descriptionKey: LocalizedStringKey) -> some WidgetConfiguration
    

##  Parameters

`descriptionKey`

    

The key for the localized description to display.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

Instance Method

# supportedFamilies(_:)

Sets the sizes that a widget supports.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func supportedFamilies(_ families: [WidgetFamily]) -> some WidgetConfiguration
    

##  Parameters

`families`

    

The set of sizes the widget supports.

## Return Value

A widget configuration that supports the sizes you specify.

## See Also

### Setting the appearance

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# contentMarginsDisabled()

Disable default content margins.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func contentMarginsDisabled() -> some WidgetConfiguration
    

## Return Value

A modified widget configuration that doesn’t use default content margins.

## Discussion

When you disable content margins for a widget, the system doesn’t
automatically add margins around the widget’s content, and you are responsible
for specifying margins and padding around your widget content for each
context. To specify custom margins, use `widgetContentMargins` in combination
with `View/padding(_)` to selectively or partially apply the default content
margins.

This modifier has no effect on operation system versions prior to iOS 17,
watchOS 10, or macOS 14.

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# disfavoredLocations(_:for:)

Sets the disfavored locations for a widget.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func disfavoredLocations(
        _ locations: [WidgetLocation],
        for families: [WidgetFamily]
    ) -> some WidgetConfiguration
    

##  Parameters

`locations`

    

An array of disfavored locations for a widget.

`families`

    

The families you want to mark as disfavored in the given locations.

## Discussion

A widget can appear in different contexts on different platforms. For example,
a small system widget appears by default on the Home Screen and in Today View
on iPhone, on the iPad Lock Screen, and so on. This gives more people
opportunity to view data and functionality that your widget provides. However,
some widgets may not work well in a location. For example, a widget that
heavily relies on high-resolution photos and background colors for its
functionality may not work well on the Lock Screen, where the system applies a
vibrant treatment to the widget. To tell the system that the widget gallery
should show a widget in the “Other” section of the widget gallery for a
specific context, use the `.disfavoredLocations` modifier.

The following code snippet tells the system to show the small system family
widget in the “Other” section of the widget gallery for the disfavored
`WidgetLocation/lockScreen` and `WidgetLocation/homeScreen` locations.

You can use subsequent calls to `disfavoredLocations(_:families:)` to join
them and set disfavored locations for different families:

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# containerBackgroundRemovable(_:)

A modifier that marks the background of a widget as removable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func containerBackgroundRemovable(_ isRemovable: Bool = true) -> some WidgetConfiguration
    

##  Parameters

`isRemovable`

    

If `true`, the widget supports removal of the container background in contexts
that prefer no backgrounds. If `false`, the system doesn’t remove the
background.

## Return Value

A modified widget configuration.

## Discussion

In most cases, mark the background container of a widget as removable to allow
people to place the widget in as many contexts as possible. If you mark the
background as nonremovable, the widget becomes ineligible in various contexts
that require a removable background. For example, a small widget without a
removable background doesn’t appear in the widget gallery on the iPad Lock
Screen.

If you mark a background as nonremovable, the system always displays the
background container of the widget. Note that the background may render
differently; for example, it can appear faded or desaturated.

This modifier has no effect on operation system versions prior to iOS 17,
watchOS 10, or macOS 14.

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

Instance Method

# backgroundTask(_:action:)

Runs the given action when the system provides a background task.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func backgroundTask<D, R>(
        _ task: BackgroundTask<D, R>,
        action: @escaping (D) async -> R
    ) -> some WidgetConfiguration where D : Sendable, R : Sendable
    

##  Parameters

`task`

    

The type of task the action responds to.

`action`

    

The closure that is called when the system provides a task matching the
provided task.

## Discussion

When the system wakes your app or extension for one or more background tasks,
it will call any actions associated with matching tasks. When your async
actions return, the system will put your app back into a suspended state. In
Widget Extensions, this modifier can be used to handle URL Session background
tasks with `urlSession`.

## See Also

### Managing background tasks

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

Instance Method

# onBackgroundURLSessionEvents(matching:_:)

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func onBackgroundURLSessionEvents(
        matching matchingBlock: ((String) -> Bool)? = nil,
        _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void
    ) -> some WidgetConfiguration
    

##  Parameters

`matching`

    

A closure that takes a string identifier and returns a Boolean value
indicating whether to perform the action.

`urlSessionEvent`

    

A closure that takes a string parameter called `identifier` and a closure
called `completion`.

## Return Value

A widget that triggers `urlSessionEvent` when events are generated for a
`URLSession` with the specified identifier.

## Discussion

When a widget initiates a background network request, the system delivers
events related to the request directly to the widget extension instead of the
containing app. To process the events, do the following:

  1. Use the `identifier` parameter to determine if a corresponding `URLSession` object exists. If the system hasn’t terminated your widget extension, maintain a reference to the same `URLSession` object you used for the original background network request. If the system terminated your widget extension, use the identifier to create a new `URLSession` object so it can receive the events. You might consider lazily initializing, and caching, the `URLSession` objects in a central location so that your code works regardless of whether your extension remains active, is suspended, or is terminated.

  2. Store a reference to the `completion` closure to invoke it after the system delivers all events.

  3. After the system calls the `URLSession` delegate’s `urlSessionDidFinishEvents(forBackgroundURLSession:)` method, invoke the `completion` closure.

## See Also

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

Instance Method

# onBackgroundURLSessionEvents(matching:_:)

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func onBackgroundURLSessionEvents(
        matching matchingString: String,
        _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void
    ) -> some WidgetConfiguration
    

##  Parameters

`matching`

    

The identifier of a URL session to monitor for events.

`urlSessionEvent`

    

A closure that takes a string identifier and a closure called `completion` as
parameters.

## Return Value

A widget that triggers `urlSessionEvent` when events are generated for a
`URLSession` with the specified identifier.

## Discussion

When a widget initiates a background network request, the system delivers
events related to the request directly to the widget extension instead of the
containing app. To process the events, do the following:

  1. Use the `matching` parameter to determine if a corresponding `URLSession` object exists. If the system hasn’t terminated your widget extension, maintain a reference to the same `URLSession` object you used for the original background network request. If the system terminated your widget extension, use the identifier to create a new `URLSession` object so it can receive the events. You might consider lazily initializing, and caching, the `URLSession` objects in a central location so that your code works regardless of whether your extension remains active, is suspended, or is terminated.

  2. Store a reference to the `completion` closure of `urlSessionEvent` to invoke it after the system delivers all events.

  3. After the system calls the `URLSession` delegate’s `urlSessionDidFinishEvents(forBackgroundURLSession:)` method, invoke the `completion` closure.

## See Also

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

