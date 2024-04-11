Instance Property

# body

The content and behavior of the scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @SceneBuilder @MainActor
    var body: Self.Body { get }

**Required**

## Discussion

For any scene that you create, provide a computed `body` property that defines
the scene as a composition of other scenes. You can assemble a scene from
built-in scenes that SwiftUI provides, as well as other scenes that you’ve
defined.

Swift infers the scene’s `Body` associated type based on the contents of the
`body` property.

## See Also

### Creating a scene

`associatedtype Body : Scene`

The type of scene that represents the body of this scene.

**Required**

Associated Type

# Body

The type of scene that represents the body of this scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : Scene

**Required**

## Discussion

When you create a custom scene, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Creating a scene

`var body: Self.Body`

The content and behavior of the scene.

**Required**

Instance Method

# onChange(of:initial:_:)

Adds an action to perform when the given value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping () -> Void
    ) -> some Scene where V : Equatable
    

##  Parameters

`value`

    

The value to check when determining whether to run the closure. The value must
conform to the `Equatable` protocol.

`initial`

    

Whether the action should be run when this scene initially appears.

`action`

    

A closure to run when the value changes.

## Return Value

A scene that triggers an action in response to a change.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the
value associated with an `Environment` key or a `Binding`. For example, you
can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task:

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value.

## See Also

### Watching for changes

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some Scene`

Adds an action to perform when the given value changes.

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

Instance Method

# onChange(of:initial:_:)

Adds an action to perform when the given value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping (V, V) -> Void
    ) -> some Scene where V : Equatable
    

##  Parameters

`value`

    

The value to check when determining whether to run the closure. The value must
conform to the `Equatable` protocol.

`initial`

    

Whether the action should be run when this scene initially appears.

`action`

    

A closure to run when the value changes.

`oldValue`

    

The old value that failed the comparison check (or the initial value when
requested).

`newValue`

    

The new value that failed the comparison check.

## Return Value

A scene that triggers an action in response to a change.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the
value associated with an `Environment` key or a `Binding`. For example, you
can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task:

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. The system passes the old and new observed values into the
closure.

## See Also

### Watching for changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some Scene`

Adds an action to perform when the given value changes.

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

Instance Method

# handlesExternalEvents(matching:)

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func handlesExternalEvents(matching conditions: Set<String>) -> some Scene
    

##  Parameters

`conditions`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if SwiftUI can open a new scene instance to handle the external
event.

## Return Value

A scene type that limits the kinds of external events for which SwiftUI opens
a new instance.

## Discussion

When your app receives an external event like a user activity or a URL,
SwiftUI routes the event to a scene for processing. SwiftUI selects the scene
that receives the event according to the following rules, which it evaluates
in order until it finds a destination scene:

  * On platforms that support only a single scene per app, send the event to the one open scene.

  * Find an open scene that indicates it prefers to or can handle the event, if any, and send the event to that scene. You use the `handlesExternalEvents(preferring:allowing:)` view modifier on a view inside the scene to register this preference.

  * Find a scene declaration with a `handlesExternalEvents(matching:)` scene modifier containing `conditions` that match the external event. Create a new instance of the first scene that matches and route the event there.

  * Find the first scene declaration that doesn’t have the scene modifier. Create a new instance of this scene and route the event there.

Make sure that at least one of these rules succeeds in your app for all events
that your app claims to handle. Also, make sure that the scene that receives
an event actually handles it. For example, be sure that a scene that receives
user activities handles them with an appropriate
`onContinueUserActivity(_:perform:)` view modifier.

Don’t confuse the `handlesExternalEvents(matching:)` scene modifier with the
`handlesExternalEvents(preferring:allowing:)` _view_ modifier. You use the
scene modifier to help SwiftUI choose a new scene to open when no open scene
handles an external event, whereas you use the view modifier to indicate that
an open scene can or prefers to handle certain events.

### Matching an event

To find a scene type that handles a particular external event, SwiftUI
compares a property of the event against the strings that you specify in the
`conditions` set. SwiftUI examines the following event properties to perform
the comparison:

  * For an `NSUserActivity`, like when your app handles Handoff, SwiftUI uses the activity’s `targetContentIdentifier` property, or if that’s `nil`, its `webpageURL` property rendered as an `absoluteString`.

  * For a `URL`, like when another process opens a URL that your app handles, SwiftUI uses the URL’s `absoluteString`.

An empty set of strings never matches. Similarly, empty strings never match.
Conversely, as a special case, the string that contains only an asterisk (`*`)
matches anything. The modifier performs string comparisons that are case and
diacritic insensitive.

Important

`DocumentGroup` scenes ignore this modifier. Instead, document scenes decide
whether to open a new scene to handle an external event by comparing the
incoming URL or user activity’s `webpageURL` against the document group’s
supported types.

### Choosing a window to open

The following example shows an app with a photo browser scene that displays a
collection of photos, and a photo detail scene that enables closer examination
of a particular photo:

The app uses the `handlesExternalEvents(matching:)` modifier on the second
scene to ensure that an external event with an identifier that contains the
string `photoIdentifier=` creates a new scene of the second type. Other
events, if not handled by an open scene, cause the creation of a new browser
window instead.

## See Also

### Handling external events

`func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) ->
some View`

Specifies the external events that the view’s scene handles if the scene is
already open.

Instance Method

# backgroundTask(_:action:)

Runs the specified action when the system provides a background task.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundTask<D, R>(
        _ task: BackgroundTask<D, R>,
        action: @escaping (D) async -> R
    ) -> some Scene where D : Sendable, R : Sendable
    

##  Parameters

`task`

    

The type of task with which to associate the provided action.

`action`

    

An async closure that the system runs for the specified task type.

## Discussion

When the system wakes your app or extension for one or more background tasks,
it will call any actions associated with matching tasks. When your async
actions return, the system put your app back into a suspended state. The
system considers the task completed when the action closure that you provide
returns. If the action closure has not returned when the task runs out of time
to complete, the system cancels the task. Use
`withTaskCancellationHandler(operation:onCancel:)` to observe whether the task
is low on runtime.

## See Also

### Handling background tasks

`struct BackgroundTask`

The kinds of background tasks that your app or extension can handle.

`struct SnapshotData`

The associated data of a snapshot background task.

`struct SnapshotResponse`

Your appplication’s response to a snapshot background task.

Instance Method

# defaultAppStorage(_:)

The default store used by `AppStorage` contained within the scene and its view
content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func defaultAppStorage(_ store: UserDefaults) -> some Scene
    

##  Parameters

`store`

    

The user defaults to use as the default store for `AppStorage`.

## Discussion

If unspecified, the default store for a view hierarchy is
`UserDefaults.standard`, but can be set a to a custom one. For example,
sharing defaults between an app and an extension can override the default
store to one created with `UserDefaults.init(suiteName:_)`.

Instance Method

# commands(content:)

Adds commands to the scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func commands<Content>(@CommandsBuilder content: () -> Content) -> some Scene where Content : Commands
    

## Discussion

Commands are realized in different ways on different platforms. On macOS, the
main menu uses the available command menus and groups to organize its main
menu items. Each menu is represented as a top-level menu bar menu, and each
command group has a corresponding set of menu items in one of the top-level
menus, delimited by separator menu items.

On iPadOS, commands with keyboard shortcuts are exposed in the shortcut
discoverability HUD that users see when they hold down the Command (⌘) key.

## See Also

### Defining commands

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Instance Method

# commandsRemoved()

Removes all commands defined by the modified scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func commandsRemoved() -> some Scene
    

## Return Value

A scene that excludes any commands defined by its children.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of
commands that they include by default. Apply this modifier to a scene to
exclude those commands.

For example, the following code adds a scene for presenting the details of an
individual data model in a separate window. To ensure that the window can only
appear programmatically, we remove the scene’s commands, including File > New
Note Window.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Instance Method

# commandsReplaced(content:)

Replaces all commands defined by the modified scene with the commands from the
builder.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func commandsReplaced<Content>(@CommandsBuilder content: () -> Content) -> some Scene where Content : Commands
    

##  Parameters

`content`

    

A `Commands` builder whose output will be used to replace the commands
normally provided by the modified scene.

## Return Value

A scene that replaces any commands defined by its children with alternative
content.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of
commands that they include by default. Apply this modifier to a scene to
replace those commands with the output from the given builder.

For example, the following code adds a scene for showing the contents of the
pasteboard in a dedicated window. We replace the scene’s default Window >
Clipboard menu command with a custom Edit > Show Clipboard command that we
place next to the other pasteboard commands.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Instance Method

# keyboardShortcut(_:)

Defines a keyboard shortcut for opening new scene windows.

macOS 13.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some Scene
    

##  Parameters

`shortcut`

    

The keyboard shortcut for presenting the scene, or `nil`.

## Return Value

A scene that can be presented with a keyboard shortcut.

## Discussion

A scene’s keyboard shortcut is bound to the command it adds for creating new
windows (in the case of `WindowGroup` and `DocumentGroup`) or bringing a
singleton window forward (in the case of `Window` and, on macOS, `Settings`).
Pressing the keyboard shortcut is equivalent to selecting the menu command.

In cases where a command already has a keyboard shortcut, the scene’s keyboard
shortcut is used instead. For example, `WindowGroup` normally creates a File >
New Window menu command whose keyboard shortcut is `⌘N`. The following code
changes it to something based on dynamic state:

If `shortcut` is `nil`, the scene’s presentation command will not be
associated with a keyboard shortcut, even if SwiftUI normally assigns one
automatically.

## See Also

### Setting commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some Scene`

Defines a keyboard shortcut for opening new scene windows.

Instance Method

# keyboardShortcut(_:modifiers:localization:)

Defines a keyboard shortcut for opening new scene windows.

macOS 13.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization = .automatic
    ) -> some Scene
    

##  Parameters

`key`

    

The key equivalent the user presses to present the scene.

`modifiers`

    

The modifier keys required to perform the shortcut.

`localization`

    

The localization style to apply to the shortcut.

## Return Value

A scene that can be presented with a keyboard shortcut.

## Discussion

A scene’s keyboard shortcut is bound to the command it adds for creating new
windows (in the case of `WindowGroup` and `DocumentGroup`) or bringing a
singleton window forward (in the case of `Window` and, on macOS, `Settings`).
Pressing the keyboard shortcut is equivalent to selecting the menu command.

In cases where a command already has a keyboard shortcut, the scene’s keyboard
shortcut is used instead. For example, `WindowGroup` normally creates a File >
New Window menu command whose keyboard shortcut is `⌘N`. The following code
changes it to `⌥⌘N`:

### Localization

Provide a `localization` value to specify how this shortcut should be
localized.

Given that `key` is always defined in relation to the US-English keyboard
layout, it might be hard to reach on different international layouts. For
example the shortcut `⌘[` works well for the US layout but is hard to reach
for German users, where `[` is available by pressing `⌥5`, making users type
`⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut to an
appropriate replacement, `⌘Ö` in this case.

Providing the option `custom` disables the automatic localization for this
shortcut to tell the system that internationalization is taken care of in a
different way.

## See Also

### Setting commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`func keyboardShortcut(KeyboardShortcut?) -> some Scene`

Defines a keyboard shortcut for opening new scene windows.

Instance Method

# defaultPosition(_:)

Sets a default position for a window.

macOS 13.0+

    
    
    func defaultPosition(_ position: UnitPoint) -> some Scene
    

##  Parameters

`position`

    

A `UnitPoint` that specifies where to place a newly opened window relative to
the screen bounds.

## Return Value

A scene that uses a default position for new windows.

## Discussion

The first time your app opens a window from a particular scene declaration,
the system places the window at the center of the screen by default. For scene
types that support multiple simultaneous windows, the system offsets each
additional window by a small amount to avoid completely obscuring existing
windows.

You can override the default placement of the first window by applying a scene
modifier that indicates where to place the window relative to the screen
bounds. For example, you can request that the system place a new window in the
bottom trailing corner of the screen:

The system aligns the point in the window that corresponds to the specified
`UnitPoint` with the point in the screen that corresponds to the same unit
point.

You typically use one of the predefined unit points — like `bottomTrailing` in
the above example — but you can also use a custom unit point. For example, the
following modifier aligns the point that’s one quarter of the way from the
leading edge of the window with the point that’s one quarter of the way from
the leading edge of the screen, while centering the window in the y-dimension:

The modifier affects any scene type that creates windows in macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

The value that you provide acts only as an initial default. During state
restoration, the system restores the window to the position that it last
occupied.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:)

Sets a default size for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func defaultSize(_ size: CGSize) -> some Scene
    

##  Parameters

`size`

    

The default size for new windows created from a scene.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this scene modifier to indicate a default initial size for a new window
that the system creates from a `Scene` declaration. For example, you can
request that new windows that a `WindowGroup` generates occupy 600 points in
the x-dimension and 400 points in the y-dimension:

The size that you specify acts only as a default for when the window first
appears. People can later resize the window using interface controls that the
system provides. Also, during state restoration, the system restores windows
to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s
inherent resizability in one or both dimensions, the system clamps the
affected dimension to keep it in range. You can configure the resizability of
a scene using the `windowResizability(_:)` modifier.

The default size modifier affects any scene type that creates windows in
macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

If you want to specify the input directly in terms of width and height, use
`defaultSize(width:height:)` instead.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(_ size: Size3D) -> some Scene
    

##  Parameters

`size`

    

The default 3D size for the created window.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in points. The size of a volumetric scene is
immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:)

Sets a default width and height for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for windows created from a scene.

`height`

    

The default height for windows created from a scene.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this scene modifier to indicate a default initial size for a new window
that the system creates from a `Scene` declaration. For example, you can
request that new windows that a `WindowGroup` generates occupy 600 points in
the x-dimension and 400 points in the y-dimension:

The size that you specify acts only as a default for when the window first
appears. People can later resize the window using interface controls that the
system provides. Also, during state restoration, the system restores windows
to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s
inherent resizability in one or both dimensions, the system clamps the
affected dimension to keep it in range. You can configure the resizability of
a scene using the `windowResizability(_:)` modifier.

The default size modifier affects any scene type that creates windows in
macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

If you want to specify the size input in terms of size instance, use
`defaultSize(_:)` instead.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:depth:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat,
        depth: CGFloat
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in points. The size of a volumetric scene is
immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:in:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        _ size: Size3D,
        in unit: UnitLength
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

`unit`

    

The unit of length the dimensions of the window are specified in.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in the unit you provide. The size of a volumetric
scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:depth:in:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat,
        depth: CGFloat,
        in unit: UnitLength
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

`unit`

    

The unit of length the dimensions of the window are specified in.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in the unit you provide. The size of a volumetric
scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# windowResizability(_:)

Sets the kind of resizability to use for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func windowResizability(_ resizability: WindowResizability) -> some Scene
    

##  Parameters

`resizability`

    

The resizability to use for windows created by this scene.

## Return Value

A scene that uses the specified resizability strategy.

## Discussion

Use this scene modifier to apply a value of type `WindowResizability` to a
`Scene` that you define in your `App` declaration. The value that you specify
indicates the strategy the system uses to place minimum and maximum size
restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between
100 and 400 points in both dimensions by applying both a frame with those
constraints to the scene’s content, and the `contentSize` resizability to the
scene:

The default value for all scenes if you don’t apply the modifier is
`automatic`. With that strategy, `Settings` windows use the `contentSize`
strategy, while all others use `contentMinSize`.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# immersionStyle(selection:in:)

Sets the style for an immersive space.

visionOS 1.0+

    
    
    func immersionStyle(
        selection: Binding<any ImmersionStyle>,
        in styles: any ImmersionStyle...
    ) -> some Scene
    

##  Parameters

`selection`

    

A `Binding` to the style that the space uses. You can change this value to
change the scene’s style even after you present the immersive space. Even
though you provide a binding, the value changes only if you change it.

`styles`

    

The list of styles that the `selection` input can have. Include any styles
that you plan to use during the lifetime of the scene.

## Return Value

A scene that uses one of the specified `styles`.

## Discussion

Use this modifier to configure the appearance and behavior of an
`ImmersiveSpace`. Specify a style that conforms to the `ImmersionStyle`
protocol, like `mixed` or `full`. For example, the following app defines a
solar system scene that uses full immersion:

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`protocol ImmersionStyle`

The styles that an immersive space can have.

Instance Method

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some Scene
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some View`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# windowStyle(_:)

Sets the style for windows created by this scene.

macOS 11.0+  visionOS 1.0+

    
    
    func windowStyle<S>(_ style: S) -> some Scene where S : WindowStyle
    

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`struct Window`

A scene that presents its content in a single, unique window.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

Instance Method

# windowToolbarStyle(_:)

Sets the style for the toolbar defined within this scene.

macOS 11.0+

    
    
    func windowToolbarStyle<S>(_ style: S) -> some Scene where S : WindowToolbarStyle
    

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# modelContext(_:)

Sets the model context in this scene’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContext(_ modelContext: ModelContext) -> some Scene
    

##  Parameters

`modelContext`

    

The model context to set in this scene’s environment.

## Discussion

In this example, `RecipesApp` sets a shared model context to use for all of
its windows:

The environment’s `modelContext` property will be assigned a `myContext`. All
implicit model context operations in this scene, such as `Query` properties,
will use the environment’s context.

## See Also

### Configuring a data model

`func modelContainer(ModelContainer) -> some Scene`

Sets the model container and associated model context in this scene’s
environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

Instance Method

# modelContainer(_:)

Sets the model container and associated model context in this scene’s
environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(_ container: ModelContainer) -> some Scene
    

##  Parameters

`container`

    

The model container to use for this scene.

## Discussion

In this example, `RecipesApp` sets a shared model container to use for all of
its windows:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
scene, such as `Query` properties, will use the environment’s context.

## See Also

### Configuring a data model

`func modelContext(ModelContext) -> some Scene`

Sets the model context in this scene’s environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

Instance Method

# modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)

Sets the model container in this scene for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(
        for modelTypes: [any PersistentModel.Type],
        inMemory: Bool = false,
        isAutosaveEnabled: Bool = true,
        isUndoEnabled: Bool = false,
        onSetup: @escaping (Result<ModelContainer, any Error>) -> Void = { _ in }
    ) -> some Scene
    

##  Parameters

`modelTypes`

    

The model types defining the schema used to create the model container.

`inMemory`

    

Whether the container should store data only in memory.

`isAutosaveEnabled`

    

`true` if autosave is enabled.

`isUndoEnabled`

    

use `undoManager` in the scene’s environment to manage undo operations for the
model container.

`onSetup`

    

A callback that will be invoked when the creation of the container has has
succeeded or failed.

## Discussion

In this example, `RecipesApp` sets a shared model container to use for all of
its windows, configured to store instances of `Recipe` and `Ingredient`:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
scene, such as `Query` properties, will use the environment’s context.

By default, the container stores its model data persistently on disk. To only
store data in memory for the lifetime of the app’s process, pass `true` to the
`inMemory:` parameter.

The container will only be created once. New values that are passed to the
`modelTypes` and `inMemory` parameters after the view is first created will be
ignored.

## See Also

### Configuring a data model

`func modelContext(ModelContext) -> some Scene`

Sets the model context in this scene’s environment.

`func modelContainer(ModelContainer) -> some Scene`

Sets the model container and associated model context in this scene’s
environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

Instance Method

# modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)

Sets the model container in this scene for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(
        for modelType: any PersistentModel.Type,
        inMemory: Bool = false,
        isAutosaveEnabled: Bool = true,
        isUndoEnabled: Bool = false,
        onSetup: @escaping (Result<ModelContainer, any Error>) -> Void = { _ in }
    ) -> some Scene
    

##  Parameters

`modelType`

    

The model type defining the schema used to create the model container.

`inMemory`

    

Whether the container should store data only in memory.

`isAutosaveEnabled`

    

`true` if autosave is enabled.

`isUndoEnabled`

    

use `undoManager` in the scene’s environment to manage undo operations for the
model container.

`onSetup`

    

A callback that will be invoked when the creation of the container has has
succeeded or failed.

## Discussion

In this example, `RecipesApp` sets a shared model container to use for all of
its windows, configured to store instances of `Recipe`:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
scene, such as `Query` properties, will use the environment’s context.

By default, the container stores its model data persistently on disk. To only
store data in memory for the lifetime of the app’s process, pass `true` to the
`inMemory:` parameter.

The container will only be created once. New values that are passed to the
`modelType` and `inMemory` parameters after the view is first created will be
ignored.

## See Also

### Configuring a data model

`func modelContext(ModelContext) -> some Scene`

Sets the model context in this scene’s environment.

`func modelContainer(ModelContainer) -> some Scene`

Sets the model container and associated model context in this scene’s
environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

Instance Method

# environment(_:)

Places an observable object in the scene’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environment<T>(_ object: T?) -> some Scene where T : AnyObject, T : Observable
    

##  Parameters

`object`

    

The object to set for this object’s type in the environment, or `nil` to clear
an object of this type from the environment.

## Return Value

A scene that has the specified object in its environment.

## Discussion

Use this modifier to place an object that you declare with the `Observable()`
macro into a scene’s environment. For example, you can add an instance of a
custom observable `Profile` class to the environment of a `WindowGroup` scene:

You then read the object inside `ContentView` or one of its descendants using
the `Environment` property wrapper:

This modifier affects the given scene, as well as the scene’s descendant
views. It has no effect outside the view hierarchy on which you call it. The
environment of a given view hierarchy holds only one observable object of a
given type.

Note

This modifier takes an object that conforms to the `Observable` protocol. To
add environment objects that conform to the `ObservableObject` protocol, use
`environmentObject(_:)` instead.

## See Also

### Modifying the environment of a scene

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene`

Sets the environment value of the specified key path to the given value.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some Scene`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# environment(_:_:)

Sets the environment value of the specified key path to the given value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func environment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        _ value: V
    ) -> some Scene
    

##  Parameters

`keyPath`

    

A key path that indicates the property of the `EnvironmentValues` structure to
update.

`value`

    

The new value to set for the item specified by `keyPath`.

## Return Value

A view that has the given value set in its environment.

## Discussion

Use this modifier to set one of the writable properties of the
`EnvironmentValues` structure, including custom values that you create. For
example, you can create a custom environment key `styleOverrides` to set a
value that represents style settings that for the entire app:

You then read the value inside `ContentView` or one of its descendants using
the `Environment` property wrapper:

This modifier affects the given scene, as well as that scene’s descendant
views. It has no effect outside the view hierarchy on which you call it.

## See Also

### Modifying the environment of a scene

`func environment<T>(T?) -> some Scene`

Places an observable object in the scene’s environment.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some Scene`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# environmentObject(_:)

Supplies an `ObservableObject` to a view subhierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some Scene where T : ObservableObject
    

##  Parameters

`object`

    

the object to store and make available to the scene’s subhierarchy.

## Discussion

The object can be read by any child by using `EnvironmentObject`:

You then read the object inside `ContentView` or one of its descendants using
the `EnvironmentObject` property wrapper:

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Instance Method

# transformEnvironment(_:transform:)

Transforms the environment value of the specified key path with the given
function.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transformEnvironment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        transform: @escaping (inout V) -> Void
    ) -> some Scene
    

## See Also

### Modifying the environment of a scene

`func environment<T>(T?) -> some Scene`

Places an observable object in the scene’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene`

Sets the environment value of the specified key path to the given value.

Instance Method

# onChange(of:perform:)

Adds an action to perform when the given value changes.

iOS 14.0–17.0  Deprecated  iPadOS 14.0–17.0  Deprecated  macOS 11.0–14.0
Deprecated  Mac Catalyst 14.0–17.0  Deprecated  tvOS 14.0–17.0  Deprecated
watchOS 7.0–10.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func onChange<V>(
        of value: V,
        perform action: @escaping (V) -> Void
    ) -> some Scene where V : Equatable
    

Deprecated

Use `onChange(of:initial:_:)` or `onChange(of:initial:_:)` instead. The
trailing closure in each case takes either zero or two input parameters,
compared to this method which takes one.

Be aware that the replacements have slightly different behvavior. This
modifier’s closure captures values that represent the state before the change.
The new modifiers capture values that correspond to the new state. The new
behavior makes it easier to perform updates that rely on values other than the
one that caused the modifier’s closure to run.

##  Parameters

`value`

    

The value to check when determining whether to run the closure. The value must
conform to the `Equatable` protocol.

`action`

    

A closure to run when the value changes. The closure provides a single
`newValue` parameter that indicates the changed value.

## Return Value

A scene that triggers an action in response to a change.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the
value associated with an `Environment` value or a `Binding`. For example, you
can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task:

The system passes the new value into the closure. If you need the old value,
capture it in the closure.

