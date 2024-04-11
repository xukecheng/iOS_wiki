Instance Method

# userActivity(_:element:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity<P>(
        _ activityType: String,
        element: P?,
        _ update: @escaping (P, NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`element`

    

If the element is `nil`, the handler will not be associated with the activity
(and if there are no handlers, no activity is advertised). The method passes
the non-`nil` element to the handler as a convenience so the handlers don’t
all need to implement an early exit with `guard element = element else {
return }`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# userActivity(_:isActive:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity(
        _ activityType: String,
        isActive: Bool = true,
        _ update: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`isActive`

    

When `false`, avoids advertising the activity. Defaults to `true`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

You can use `userActivity(_:isActive:_:)` to start, stop, or modify the
advertisement of a specific type of user activity.

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# onContinueUserActivity(_:perform:)

Registers a handler to invoke in response to a user activity that your app
receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onContinueUserActivity(
        _ activityType: String,
        perform action: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity that the `action` closure handles. Be sure that this
string matches one of the values that you list in the `NSUserActivityTypes`
array in your app’s Information Property List.

`action`

    

A closure that SwiftUI calls when your app receives a user activity of the
specified type. The closure takes the activity as an input parameter.

## Return Value

A view that handles incoming user activities.

## Discussion

Use this view modifier to receive `NSUserActivity` instances in a particular
scene within your app. The scene that SwiftUI routes the incoming user
activity to depends on the structure of your app, what scenes are active, and
other configuration. For more information, see
`handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using a user
activity. However, SwiftUI passes a Universal Link to your app directly as a
URL. To receive a Universal Link, use the `onOpenURL(perform:)` modifier
instead.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

Instance Property

# openURL

An action that opens a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var openURL: OpenURLAction { get set }

## Discussion

Read this environment value to get an `OpenURLAction` instance for a given
`Environment`. Call the instance to open a URL. You call the instance directly
because it defines a `callAsFunction(_:)` method that Swift calls when you
call the instance.

For example, you can open a web site when the user taps a button:

If you want to know whether the action succeeds, add a completion handler that
takes a Boolean value. In this case, Swift implicitly calls the
`callAsFunction(_:completion:)` method instead. That method calls your
completion handler after it determines whether it can open the URL, but
possibly before it finishes opening the URL. You can add a handler to the
example above so that it prints the outcome to the console:

The system provides a default open URL action with behavior that depends on
the contents of the URL. For example, the default action opens a Universal
Link in the associated app if possible, or in the user’s default web browser
if not.

You can also set a custom action using the `environment(_:_:)` view modifier.
Any views that read the action from the environment, including the built-in
`Link` view and `Text` views with markdown links, or links in attributed
strings, use your action. Initialize an action by calling the `init(handler:)`
initializer with a handler that takes a URL and returns an
`OpenURLAction.Result`:

SwiftUI translates the value that your custom action’s handler returns into an
appropriate Boolean result for the action call. For example, a view that uses
the action declared above receives `true` when calling the action, because the
handler always returns `handled`.

## See Also

### Sending and receiving URLs

`struct OpenURLAction`

An action that opens a URL.

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

Structure

# OpenURLAction

An action that opens a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct OpenURLAction

## Overview

Read the `openURL` environment value to get an instance of this structure for
a given `Environment`. Call the instance to open a URL. You call the instance
directly because it defines a `callAsFunction(_:)` method that Swift calls
when you call the instance.

For example, you can open a web site when the user taps a button:

If you want to know whether the action succeeds, add a completion handler that
takes a Boolean value. In this case, Swift implicitly calls the
`callAsFunction(_:completion:)` method instead. That method calls your
completion handler after it determines whether it can open the URL, but
possibly before it finishes opening the URL. You can add a handler to the
example above so that it prints the outcome to the console:

The system provides a default open URL action with behavior that depends on
the contents of the URL. For example, the default action opens a Universal
Link in the associated app if possible, or in the user’s default web browser
if not.

You can also set a custom action using the `environment(_:_:)` view modifier.
Any views that read the action from the environment, including the built-in
`Link` view and `Text` views with markdown links, or links in attributed
strings, use your action. Initialize an action by calling the `init(handler:)`
initializer with a handler that takes a URL and returns an
`OpenURLAction.Result`:

SwiftUI translates the value that your custom action’s handler returns into an
appropriate Boolean result for the action call. For example, a view that uses
the action declared above receives `true` when calling the action, because the
handler always returns `handled`.

## Topics

### Creating the action

`init(handler: (URL) -> OpenURLAction.Result)`

Creates an action that opens a URL.

`struct Result`

The result of a custom open URL action.

### Calling the action

`func callAsFunction(URL)`

Opens a URL, following system conventions.

`func callAsFunction(URL, completion: (Bool) -> Void)`

Asynchronously opens a URL, following system conventions.

## See Also

### Sending and receiving URLs

`var openURL: OpenURLAction`

An action that opens a URL.

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

Instance Method

# onOpenURL(perform:)

Registers a handler to invoke in response to a URL that your app receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onOpenURL(perform action: @escaping (URL) -> ()) -> some View
    

##  Parameters

`action`

    

A closure that SwiftUI calls when your app receives a Universal Link or a
custom `URL`. The closure takes the URL as an input parameter.

## Return Value

A view that handles incoming URLs.

## Discussion

Use this view modifier to receive URLs in a particular scene within your app.
The scene that SwiftUI routes the incoming URL to depends on the structure of
your app, what scenes are active, and other configuration. For more
information, see `handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using an
`NSUserActivity`. However, SwiftUI passes a Universal Link to your app
directly as a URL, which you receive using this modifier. To receive other
user activities, like when your app participates in Handoff, use the
`onContinueUserActivity(_:perform:)` modifier instead.

For more information about linking into your app, see Allowing apps and
websites to link to your content.

## See Also

### Sending and receiving URLs

`var openURL: OpenURLAction`

An action that opens a URL.

`struct OpenURLAction`

An action that opens a URL.

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

# handlesExternalEvents(preferring:allowing:)

Specifies the external events that the view’s scene handles if the scene is
already open.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func handlesExternalEvents(
        preferring: Set<String>,
        allowing: Set<String>
    ) -> some View
    

##  Parameters

`preferring`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene prefers to handle the external event.

`allowing`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene can handle the exernal event.

## Return Value

A view whose enclosing scene — if already open — handles incoming external
events.

## Discussion

Apply this modifier to a view to indicate whether an open scene that contains
the view handles specified user activities or URLs that your app receives.
Specify two sets of string identifiers to distinguish between the kinds of
events that the scene _prefers_ to handle and those that it _can_ handle. You
can dynamically update the identifiers in each set to reflect changing app
state.

When your app receives an event on a platform that supports multiple
simultaneous scenes, SwiftUI sends the event to the first open scene it finds
that prefers to handle the event. Otherwise, it sends the event to the first
open scene it finds that can handle the event. If it finds neither — including
when you don’t add this view modifier — SwiftUI creates a new scene for the
event.

Important

Don’t confuse this view modifier with the `handlesExternalEvents(matching:)`
_scene_ modifier. You use the view modifier to indicate that an open scene
handles certain events, whereas you use the scene modifier to help SwiftUI
choose a new scene to open when no open scene handles the event.

On platforms that support only a single scene, SwiftUI ignores this modifier
and sends all external events to the one open scene.

### Matching an event

To find an open scene that handles a particular external event, SwiftUI
compares a property of the event against the strings that you specify in the
`preferring` and `allowing` sets. SwiftUI examines the following event
properties to perform the comparison:

  * For an `NSUserActivity`, like when your app handles Handoff, SwiftUI uses the activity’s `targetContentIdentifier` property, or if that’s `nil`, its `webpageURL` property rendered as an `absoluteString`.

  * For a `URL`, like when another process opens a URL that your app handles, SwiftUI uses the URL’s `absoluteString`.

For both parameter sets, an empty set of strings never matches. Similarly,
empty strings never match. Conversely, as a special case, the string that
contains only an asterisk (`*`) matches anything. The modifier performs string
comparisons that are case and diacritic insensitive.

If you specify multiple instances of this view modifier inside a single scene,
the scene uses the union of the respective `preferring` and `allowing` sets
from all the modifiers.

### Handling a user activity in an open scene

As an example, the following view — which participates in Handoff through the
`userActivity(_:isActive:_:)` and `onContinueUserActivity(_:perform:)` methods
— updates its `preferring` set according to the current selection. The
enclosing scene prefers to handle an event for a contact that’s already
selected, but doesn’t volunteer itself as a preferred scene when no contact is
selected:

The above code also updates the `allowing` set to indicate that the scene can
handle any incoming event when there’s no current selection, but that it can’t
handle any event if the view already displays a contact. The `preferring` set
takes precedence in the special case where the incoming event exactly matches
the currently selected contact.

## See Also

### Handling external events

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

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

Structure

# BackgroundTask

The kinds of background tasks that your app or extension can handle.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct BackgroundTask<Request, Response>

## Overview

Use a value of this type with the `backgroundTask(_:action:)` scene modifier
to create a handler for background tasks that the system sends to your app or
extension. For example, you can use `urlSession` to define an asynchronous
closure that the system calls when it launches your app or extension to handle
a response from a background `URLSession`.

## Topics

### Refreshing the app

`static var appRefresh: BackgroundTask<String?, Void>`

A task that updates your app’s state in the background.

`static func appRefresh(String) -> BackgroundTask<Void, Void>`

A task that updates your app’s state in the background for a matching
identifier.

### Preparing for a snapshot

`static var snapshot: BackgroundTask<SnapshotData, SnapshotResponse>`

A background task used to update your app’s user interface in preparation for
a snapshot.

### Receiving connectivity updates

`static var bluetoothAlert: BackgroundTask<Void, Void>`

A background task used to receive critical alerts from paired bluetooth
accessories.

`static var watchConnectivity: BackgroundTask<Void, Void>`

A background task used to receive background updates from the Watch
Connectivity framework.

### Responding to URL sessions

`static var urlSession: BackgroundTask<String, Void>`

A task that responds to background URL sessions.

`static func urlSession(String) -> BackgroundTask<Void, Void>`

A task that responds to background URL sessions matching the given identifier.

`static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String,
Void>`

A task that responds to background URL sessions matching the given predicate.

### Updating intents and shortcuts

`static var intentDidRun: BackgroundTask<Void, Void>`

A background task used to update your app after a SiriKit intent runs.

`static var relevantShortcut: BackgroundTask<Void, Void>`

A background task used to periodically donate relevant Siri shortcuts.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Handling background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some Scene`

Runs the specified action when the system provides a background task.

`struct SnapshotData`

The associated data of a snapshot background task.

`struct SnapshotResponse`

Your appplication’s response to a snapshot background task.

Structure

# SnapshotData

The associated data of a snapshot background task.

watchOS 9.0+

    
    
    struct SnapshotData

## Topics

### Getting the data

`let identifier: String?`

The identifier associated with this snapshot request.

`let reason: SnapshotData.SnapshotReason`

The reason for a background snapshot task.

`enum SnapshotReason`

The reason for a background snapshot task.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Handling background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some Scene`

Runs the specified action when the system provides a background task.

`struct BackgroundTask`

The kinds of background tasks that your app or extension can handle.

`struct SnapshotResponse`

Your appplication’s response to a snapshot background task.

Structure

# SnapshotResponse

Your appplication’s response to a snapshot background task.

watchOS 9.0+

    
    
    struct SnapshotResponse

## Topics

### Creating a response

`init(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date?,
identifier: String?)`

Creates a snapshot response.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Handling background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some Scene`

Runs the specified action when the system provides a background task.

`struct BackgroundTask`

The kinds of background tasks that your app or extension can handle.

`struct SnapshotData`

The associated data of a snapshot background task.

Instance Method

# importableFromServices(for:action:)

Enables importing items from services, such as Continuity Camera on macOS.

macOS 13.0+

    
    
    func importableFromServices<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the imported models.

`action`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## Discussion

## See Also

### Importing and exporting transferable items

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# exportableToServices(_:)

Exports items for consumption by shortcuts, quick actions, and services.

macOS 13.0+

    
    
    func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# exportableToServices(_:onEdit:)

Exports read-write items for consumption by shortcuts, quick actions, and
services.

macOS 13.0+

    
    
    func exportableToServices<T>(
        _ payload: @autoclosure @escaping () -> [T],
        onEdit: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

Instance Method

# importsItemProviders(_:onImport:)

Enables importing item providers from services, such as Continuity Camera on
macOS.

macOS 12.0+

    
    
    func importsItemProviders(
        _ contentTypes: [UTType],
        onImport: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports importing. An empty array means
the view does not currently support importing.

`onImport`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## See Also

### Importing and exporting using item providers

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportsItemProviders(_:onExport:)

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider]
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting. An empty array means
the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportsItemProviders(_:onExport:onEdit:)

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider],
        onEdit: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting and importing. An empty
array means the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

