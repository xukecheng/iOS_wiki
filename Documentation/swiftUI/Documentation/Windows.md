Structure

# WindowGroup

A scene that presents a group of identically structured windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct WindowGroup<Content> where Content : View

## Overview

Use a `WindowGroup` as a container for a view hierarchy that your app
presents. The hierarchy that you declare as the group’s content serves as a
template for each window that the app creates from that group:

SwiftUI takes care of certain platform-specific behaviors. For example, on
platforms that support it, like macOS and iPadOS, people can open more than
one window from the group simultaneously. In macOS, people can gather open
windows together in a tabbed interface. Also in macOS, window groups
automatically provide commands for standard window management.

Important

To enable an iPadOS app to simultaneously display multiple windows, be sure to
include the `UIApplicationSupportsMultipleScenes` key with a value of `true`
in the UIApplicationSceneManifest dictionary of your app’s Information
Property List.

Every window in the group maintains independent state. For example, the system
allocates new storage for any `State` or `StateObject` variables instantiated
by the scene’s view hierarchy for each window that it creates.

For document-based apps, use `DocumentGroup` to define windows instead.

### Open windows programmatically

If you initialize a window group with an identifier, a presentation type, or
both, you can programmatically open a window from the group. For example, you
can give the mail viewer scene from the previous example an identifier:

Elsewhere in your code, you can use the `openWindow` action from the
environment to create a new window from the group:

Be sure to use unique strings for identifiers that you apply to window groups
in your app.

### Present data in a window

If you initialize a window group with a presentation type, you can pass data
of that type to the window when you open it. For example, you can define a
second window group for the Mail app that displays a specified message:

When you call the `openWindow` action with a value, SwiftUI finds the window
group with the matching type and passes a binding to the value into the window
group’s content closure. For example, you can define a button that opens a
message by passing the message’s identifier:

Be sure that the type you present conforms to both the `Hashable` and
`Codable` protocols. Also, prefer lightweight data for the presentation value.
For model values that conform to the `Identifiable` protocol, the value’s
identifier works well as a presentation type, as the above example
demonstrates.

If a window with a binding to the same value that you pass to the `openWindow`
action already appears in the user interface, the system brings the existing
window to the front rather than opening a new window. If SwiftUI doesn’t have
a value to provide — for example, when someone opens a window by choosing File
> New Window from the macOS menu bar — SwiftUI passes a binding to a `nil`
value instead. To avoid receiving a `nil` value, you can optionally specify a
default value in your window group initializer. For example, for the message
viewer, you can present a new empty message:

SwiftUI persists the value of the binding for the purposes of state
restoration, and reapplies the same value when restoring the window. If the
restoration process results in an error, SwiftUI sets the binding to the
default value if you provide one, or `nil` otherwise.

### Title your app’s windows

To help people distinguish among windows from different groups, include a
title as the first parameter in the group’s initializer:

SwiftUI uses this title when referring to the window in:

  * The list of new windows that someone can open using the File > New menu.

  * The window’s title bar.

  * The list of open windows that the Window menu displays.

If you don’t provide a title for a window, the system refers to the window
using the app’s name instead.

Note

You can override the title that SwiftUI uses for a window in the window’s
title bar and the menu’s list of open windows by adding one of the
`navigationTitle(_:)` modifiers to the window’s content. This enables you to
customize and dynamically update the title for each individual window
instance.

### Distinguish windows that present like data

To programmatically distinguish between windows that present the same type of
data, like when you use a `UUID` as the identifier for more than one model
type, add the `id` parameter to the group’s initializer to provide a unique
string identifier:

Then use both the identifer and a value to open the window:

### Dismiss a window programmatically

The system provides people with platform-appropriate controls to dismiss a
window. You can also dismiss windows programmatically by calling the `dismiss`
action from within the window’s view hierarchy. For example, you can include a
button in the account detail view from the previous example that dismisses the
view:

The dismiss action doesn’t close the window if you call it from a modal — like
a sheet or a popover — that you present from the window. In that case, the
action dismisses the modal presentation instead.

## Topics

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

### Supporting types

`struct PresentedWindowContent`

A view that represents the content of a presented window.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct Window`

A scene that presents its content in a single, unique window.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

Structure

# Window

A scene that presents its content in a single, unique window.

macOS 13.0+

    
    
    struct Window<Content> where Content : View

## Overview

Use a `Window` scene to augment the main interface of your app with a window
that gives people access to supplemental functionality. For example, you can
create a secondary window in a mail reader app that enables people to view the
status of their account connections:

Provide a title as the first argument to the window’s intializer. The system
uses the title to identify the window to people using your app in the window’s
title bar or in the list of available singleton windows that the Windows menu
displays automatically.

Note

You can override the title in the window’s title bar by adding one of the
`navigationTitle(_:)` view modifiers to the window’s content. This enables you
to dynamically update the title bar.

### Open a window programmatically

People open the window by selecting it in the Windows menu, but you can also
open the window programmatically using the `openWindow` action that you read
from the environment. Use the `id` parameter that you initialize the window
with to indicate which window to open. For example, you can create a button to
open the window from the previous example:

If the window is already open when you call this action, the action brings the
open window to the front. Be sure to use unique identifiers across all of the
`Window` and `WindowGroup` instances that you define.

### Dismiss a window programmatically

The system provides people with controls to close windows, but you can also
close a window programmatically using the `dismiss` action from within the
window’s view hierarchy. For example, you can include a button in the
connection doctor view that dismisses the view:

The dismiss action doesn’t close the window if you call it from a modal — like
a sheet or a popover — that you present from within the window. In that case,
the action dismisses the modal presentation instead.

### Use a window as the main scene

You can use a window as the main scene of your app when multi-window
functionality isn’t appropriate. For example, it might not make sense to
display more than one window for a video call app that relies on a hardware
resource, like a camera:

If your app uses a single window as its primary scene, the app quits when the
window closes. This behavior differs from an app that uses a `WindowGroup` as
its primary scene, where the app continues to run even after closing all of
its windows.

Note

In most cases it’s best to use a `WindowGroup` to represent the main scene of
your app. A window group provides multi-window functionality on platforms that
support it, like iPadOS and macOS, and makes it easier to share code across
platforms.

## Topics

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

Protocol

# WindowStyle

A specification for the appearance and interaction of a window.

macOS 11.0+  visionOS 1.0+

    
    
    protocol WindowStyle

## Topics

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

## Relationships

### Conforming Types

  * `DefaultWindowStyle`
  * `HiddenTitleBarWindowStyle`
  * `PlainWindowStyle`
  * `TitleBarWindowStyle`
  * `VolumetricWindowStyle`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`struct Window`

A scene that presents its content in a single, unique window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

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

Protocol

# WindowToolbarStyle

A specification for the appearance and behavior of a window’s toolbar.

macOS 11.0+

    
    
    protocol WindowToolbarStyle

## Topics

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

## Relationships

### Conforming Types

  * `DefaultWindowToolbarStyle`
  * `ExpandedWindowToolbarStyle`
  * `UnifiedCompactWindowToolbarStyle`
  * `UnifiedWindowToolbarStyle`

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

Article

# Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

## Overview

An app’s scenes, which contain views that people interact with, can take
different forms. For example, a scene can fill a window, a tab in a window, or
an entire screen. Some scenes can even place views throughout a person’s
surroundings. How a scene appears depends on its type, the platform, and the
context.

When someone launches your app, SwiftUI looks for the first `WindowGroup`,
`Window`, or `DocumentGroup` in your app declaration and opens a scene of that
type, typically filling a new window or the entire screen, depending on the
platform. For example, the following app running in macOS presents a window
that contains a `MailViewer` view:

In visionOS, you can alternatively configure your app to open the first
`ImmersiveSpace` that the app declares. In any case, specific platforms and
configurations enable you to open more than one scene at a time. Under those
conditions, you can use actions that appear in the environment to
programmatically open and close the scenes in your app.

### Check for multiple-scene support

If you share code among different platforms and need to find out at runtime
whether the current system supports displaying multiple scenes, read the
`supportsMultipleWindows` environment value. The following code creates a
button that’s hidden unless the app supports multiple windows:

The value that you read depends on both the platform and how you configure
your app:

  * In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.

  * In iPadOS and visionOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key `UIApplicationSupportsMultipleScenes` set to `true`, and `false` otherwise.

  * For all other platforms and configurations, the value returns `false`.

If your app only ever runs in one of these situations, you can assume the
associated behavior and don’t need to check the value.

### Enable multiple simultaneous scenes

You can always present multiple scenes in macOS. To enable an iPadOS or
visionOS app to simultaneously display multiple scenes — including
`ImmersiveSpace` scenes in visionOS — add the
`UIApplicationSupportsMultipleScenes` key with a value of `true` in the
UIApplicationSceneManifest dictionary of your app’s Information Property List.
Use the Info tab in Xcode for your app’s target to add this key:

Apps on other platforms can display only one scene during their lifetime.

### Open windows programmatically

Some platforms provide built-in controls that enable people to open instances
of the window-style scenes that your app defines. For example, in macOS people
can choose File > New Window from the menu bar to open a new window. SwiftUI
also provides ways for you to open new windows programmatically.

To do this, get the `openWindow` action from the environment and call it with
an identifier, a value, or both to indicate what kind of window to open and
optionally what data to open it with. The following view opens a new instance
of the previously defined mail viewer window when someone clicks or taps the
button:

When the action runs on a system that supports multiple scenes, SwiftUI looks
for a window in the app declaration that has a matching identifier and creates
a new scene of that type.

Important

If `supportsMultipleWindows` is `false` and you try to open a new window,
SwiftUI ignores the action and logs a runtime error.

In addition to opening more instances of an app’s main window, as in the above
example, you can also open other window types that your app’s body declares.
For example, you can open an instance of the `Window` that displays
connectivity information:

### Open a space programmatically

In visionOS, you open an immersive space — a scene that you can use to present
unbounded content in a person’s surroundings — in much the same way that you
open a window, except that you use the `openImmersiveSpace` action. The action
runs asynchronously, so you use the `await` keyword when you call it, and
typically do so from inside a `Task`:

Because your app operates in a Full Space when you open an `ImmersiveSpace`
scene, you can only open one scene of this type at a time. If you try to open
a space when one is already open, the system logs a runtime error.

Your app can display any number of windows together with an immersive space.
However, when you open a space from your app, the system hides all windows
that belong to other apps. After you dismiss your space, the other apps’
windows reappear. Similarly, the system hides your app’s windows if another
app opens an immersive space.

### Designate a space as your app’s main interface

When visionOS launches an app, it opens the first window group, window, or
document scene that the app’s body declares, just like on other platforms.
This is true even if you first declare a space. However, if you want to open
your app into an immersive space directly, specify a space as the default
scene for your app by adding the
`UIApplicationPreferredDefaultSceneSessionRole` key to your app’s information
property list and setting its value to
`UISceneSessionRoleImmersiveSpaceApplication`. In that case, visionOS opens
the first space that it finds in your app declaration.

Important

Be careful not to overwhelm people when starting your app with an immersive
space. For design guidance, see Immersive experiences.

### Close windows programmatically

People can close windows using system controls, like the close button built
into the frame around a macOS window. You can also close windows
programmatically. Get the `dismissWindow` action from the environment, and
call it using the identifier of the window that you want to dismiss:

In iPadOS and visionOS, the system ignores the dismiss action if you use it to
close a window that’s your app’s only open scene.

### Close spaces programmatically

To close a space, call the `dismissImmersiveSpace` action. Like the
corresponding open space action, the close action operates asynchronously and
requires the `await` keyword:

You don’t need to specify an identifier for this action, because there can
only ever be one space open at a time. Like with windows, you can’t dismiss a
space that’s your app’s only open scene.

### Transition between a window and a space

Because you can’t programmatically close the last open window or immersive
space in a visionOS app, be sure to open a new scene before closing the old
one. Pay particular attention to the sequencing when moving between a window
and an immersive space, because the space’s open and dismiss actions run
asynchronously.

For example, consider a chess game that begins by displaying a start button in
a window. When someone taps the button, the app dismisses the window and opens
an immersive space that presents a chess board. The following button
demonstrates proper sequencing by opening the space and then closing the
window:

In the above code, it’s important to include the `dismissWindow` action inside
the task, so that it waits until the `openImmersiveSpace` action completes. If
you put the action outside the task — either before or after — it might
execute before the asynchronous open action completes, when the window is
still the only open scene. In that case, the system opens the space but
doesn’t close the window.

## See Also

### SwiftUI

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

Instance Property

# supportsMultipleWindows

A Boolean value that indicates whether the current platform supports opening
multiple windows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var supportsMultipleWindows: Bool { get }

## Discussion

Read this property from the environment to determine if your app can use the
`openWindow` action to open new windows:

The reported value depends on both the platform and how you configure your
app:

  * In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.

  * In iPadOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key `UIApplicationSupportsMultipleScenes` set to `true`.

  * For all other platforms and configurations, the value returns `false`.

If the value is false and you try to open a window, SwiftUI ignores the action
and logs a runtime error.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

`struct OpenWindowAction`

An action that presents a window.

Instance Property

# openWindow

A window presentation action stored in a view’s environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var openWindow: OpenWindowAction { get }

## Discussion

Use the `openWindow` environment value to get an `OpenWindowAction` instance
for a given `Environment`. Then call the instance to open a window. You call
the instance directly because it defines a `callAsFunction(id:)` method that
Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

You indicate which scene to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter, as in the above example.

  * A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.

  * Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type like a `UUID`.

Use the first option to target either a `WindowGroup` or a `Window` scene in
your app that has a matching identifier. For a `WindowGroup`, the system
creates a new window for the group. If the window group presents data, the
system provides the default value or `nil` to the window’s root view. If the
targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a `WindowGroup` and provide a value to
present. If the interface already has a window from the group that’s
presenting the specified value, the system brings the window to the front.
Otherwise, the system creates a new window and passes a binding to the
specified value.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var supportsMultipleWindows: Bool`

A Boolean value that indicates whether the current platform supports opening
multiple windows.

`struct OpenWindowAction`

An action that presents a window.

Structure

# OpenWindowAction

An action that presents a window.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct OpenWindowAction

## Overview

Use the `openWindow` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to open a window. You call
the instance directly because it defines a `callAsFunction(id:)` method that
Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

You indicate which scene to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter, as in the above example.

  * A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.

  * Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type, like a `UUID`.

Use the first option to target either a `WindowGroup` or a `Window` scene in
your app that has a matching identifier. For a `WindowGroup`, the system
creates a new window for the group. If the window group presents data, the
system provides the default value or `nil` to the window’s root view. If the
targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a `WindowGroup` and provide a value to
present. If the interface already has a window from the group that’s
presenting the specified value, the system brings the window to the front.
Otherwise, the system creates a new window and passes a binding to the
specified value.

## Topics

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var supportsMultipleWindows: Bool`

A Boolean value that indicates whether the current platform supports opening
multiple windows.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

Instance Property

# dismissWindow

A window dismissal action stored in a view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var dismissWindow: DismissWindowAction { get }

## Discussion

Use the `dismissWindow` environment value to get an `DismissWindowAction`
instance for a given `Environment`. Then call the instance to dismiss a
window. You call the instance directly because it defines a
`callAsFunction(id:)` method that Swift calls when you call the instance.

For example, you can define a button that dismisses an auxiliary window:

## See Also

### Closing windows

`struct DismissWindowAction`

An action that dismisses a window associated to a particular scene.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`struct DismissBehavior`

Programmatic window dismissal behaviors.

Structure

# DismissWindowAction

An action that dismisses a window associated to a particular scene.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DismissWindowAction

## Overview

Use the `dismissWindow` environment value to get the instance of this
structure for a given `Environment`. Then call the instance to dismiss a
window. You call the instance directly because it defines a
`callAsFunction(id:)` method that Swift calls when you call the instance.

For example, you can define a button that closes an auxiliary window:

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

## See Also

### Closing windows

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`struct DismissBehavior`

Programmatic window dismissal behaviors.

Instance Property

# dismiss

An action that dismisses the current presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dismiss: DismissAction { get }

## Discussion

Use this environment value to get the `DismissAction` instance for the current
`Environment`. Then call the instance to perform the dismissal. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

You can use this action to:

  * Dismiss a modal presentation, like a sheet or a popover.

  * Pop the current view from a `NavigationStack`.

  * Close a window that you create with `WindowGroup` or `Window`.

The specific behavior of the action depends on where you call it from. For
example, you can create a button that calls the `DismissAction` inside a view
that acts as a sheet:

When you present the `SheetContents` view, someone can dismiss the sheet by
tapping or clicking the sheet’s button:

Be sure that you define the action in the appropriate environment. For
example, don’t reorganize the `DetailView` in the example above so that it
creates the `dismiss` property and calls it from the
`sheet(item:onDismiss:content:)` view modifier’s `content` closure:

If you do this, the sheet fails to dismiss because the action applies to the
environment where you declared it, which is that of the detail view, rather
than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root
view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If
you need to query whether SwiftUI is currently presenting a view, read the
`isPresented` environment value.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`struct DismissAction`

An action that dismisses a presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Structure

# DismissAction

An action that dismisses a presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct DismissAction

## Overview

Use the `dismiss` environment value to get the instance of this structure for
a given `Environment`. Then call the instance to perform the dismissal. You
call the instance directly because it defines a `callAsFunction()` method that
Swift calls when you call the instance.

You can use this action to:

  * Dismiss a modal presentation, like a sheet or a popover.

  * Pop the current view from a `NavigationStack`.

  * Close a window that you create with `WindowGroup` or `Window`.

The specific behavior of the action depends on where you call it from. For
example, you can create a button that calls the `DismissAction` inside a view
that acts as a sheet:

When you present the `SheetContents` view, someone can dismiss the sheet by
tapping or clicking the sheet’s button:

Be sure that you define the action in the appropriate environment. For
example, don’t reorganize the `DetailView` in the example above so that it
creates the `dismiss` property and calls it from the
`sheet(item:onDismiss:content:)` view modifier’s `content` closure:

If you do this, the sheet fails to dismiss because the action applies to the
environment where you declared it, which is that of the detail view, rather
than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root
view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If
you need to query whether SwiftUI is currently presenting a view, read the
`isPresented` environment value.

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the view if it is currently presented.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Structure

# DismissBehavior

Programmatic window dismissal behaviors.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DismissBehavior

## Overview

Use values of this type to control window dismissal during the current
transaction.

For example, to dismiss windows showing a modal presentation that would
otherwise prohibit dismissal, use the `destructive` behavior:

## Topics

### Getting behaviors

`static let destructive: DismissBehavior`

The destructive dismiss behavior.

`static let interactive: DismissBehavior`

The interactive dismiss behavior.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Closing windows

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`struct DismissWindowAction`

An action that dismisses a window associated to a particular scene.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

Article

# Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

## Overview

visionOS and macOS enable people to move and resize windows. In some cases,
your app can use scene modifiers to influence a window’s initial geometry on
these platforms, as well as to specify the strategy that the system employs to
place minimum and maximum size limitations on a window. This kind of
configuration affects both windows and volumes, which are windows with the
`volumetric` window style.

Your ability to configure window size and position is subject to the following
constraints:

  * The system might be unable to fulfill your request. For example, if you specify a default size that’s outside the range of the window’s resizability, the system clamps the affected dimension to keep it in range.

  * Although you can change the window’s content, you can’t directly manipulate window position or size after the window appears. This ensures that people have full control over their workspace.

  * During state restoration, the system restores windows to their previous position and size.

Note

Windows in iPadOS occupy the full screen, or share the screen with another
window in Slide Over or Split View. You can’t programmatically affect window
geometry on that platform.

### Specify initial window position

In macOS, the first time your app opens a window from a particular scene
declaration, the system places the window at the center of the screen by
default. For scene types that support multiple simultaneous windows, the
system offsets each additional window by a small amount to avoid fully
obscuring existing windows.

You can override the default placement of the first window in macOS by
applying the `defaultPosition(_:)` scene modifier to indicate where to place
the window relative to the screen bounds. For example, you can request that
the system place a new window in the bottom trailing corner of the screen:

The system aligns the point in the window that corresponds to the specified
`UnitPoint` with the point in the screen that corresponds to the same unit
point. You can use a built-in unit point, like `bottomTrailing` in the above
example, or define a custom one.

Important

You can’t use `defaultPosition(_:)` in visionOS. The system always places new
windows directly in front of people, where they happen to be looking at the
moment the window opens. This helps to make people aware of new windows.

### Specify initial window size

You can indicate a default initial size for a new window that the system
creates from a `Scene` declaration by applying one of the default size scene
modifiers, like `defaultSize(width:height:)`. For example, you can request
that new windows that a `WindowGroup` generates occupy 600 points in the
x-dimension and 400 points in the y-dimension:

The system might clamp the actual size of the window depending on both the
window’s content and resizability settings.

### Specify window resizability

Both macOS and visionOS provide interface controls that enable people to
resize windows, within certain limits. For example, people can use the control
that appears when they look at the corner of a visionOS window to resize a
window on that platform.

Play

You can specify how the system limits window resizability. The default
resizability for all scenes is `automatic`. With that strategy, `Settings`
windows use the `contentSize` strategy, where both the minimum and maximum
window size match the respective minimum and maximum sizes of the content that
the window contains. Other scene types use `contentMinSize` by default, which
retains the minimum size restriction, but doesn’t limit the maximium size.

You can specify one of these resizability strategies explicitly by adding the
`windowResizability(_:)` scene modifier to a scene. For example, people can
resize windows from the following window group to between 100 and 400 points
in both dimensions because the frame modifier imposes those bounds on the
content view:

You can take this even further and enforce a specific size for a window with
content that has a fixed size.

### Specify a volume size

When you create a volume, which is a window with the `volumetric` style, you
can specify the volume’s size using one of the three-dimensional default size
modifiers, like `defaultSize(width:height:depth:in:)`. The following code
creates a volume that’s one meter on a side:

The volume maintains this size for its entire lifetime. People can’t change
the size of a volume at runtime.

Although you can specify a volume’s size in points, it’s typically better to
use physical units, like the above code which specifies a size in meters. This
is because the system renders a volume with fixed scaling rather than dynamic
scaling, unlike a regular window, which means the volume appears more like a
physical object than a user interface. For information about the different
kinds of scaling, see Spatial layout.

## See Also

### SwiftUI

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

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

    
    
    WindowGroup {
        ContentView()
    }
    .windowStyle(.volumetric)
    .defaultSize(Size3D(width: 600, height: 400, depth: 600))
    

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

    
    
    WindowGroup {
        ContentView()
    }
    .windowStyle(.volumetric)
    .defaultSize(width: 600, height: 400, depth: 600)
    

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

    
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .frame(
                        minWidth: 100, maxWidth: 400,
                        minHeight: 100, maxHeight: 400)
            }
            .windowResizability(.contentSize)
        }
    }
    

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

Structure

# WindowResizability

The resizability of a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct WindowResizability

## Overview

Use the `windowResizability(_:)` scene modifier to apply a value of this type
to a `Scene` that you define in your `App` declaration. The value that you
specify indicates the strategy the system uses to place minimum and maximum
size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between
100 and 400 points in both dimensions by applying both a frame with those
constraints to the scene’s content, and the `contentSize` resizability to the
scene:

The default value for all scenes if you don’t apply the modifier is
`automatic`. With that strategy, `Settings` windows use the `contentSize`
strategy, while all others use `contentMinSize`.

## Topics

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

## Relationships

### Conforms To

  * `Sendable`

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

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

