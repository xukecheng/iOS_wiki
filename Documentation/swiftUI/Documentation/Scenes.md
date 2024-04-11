Protocol

# Scene

A part of an app’s user interface with a life cycle managed by the system.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol Scene

## Overview

You create an `App` by combining one or more instances that conform to the
`Scene` protocol in the app’s `body`. You can use the built-in scenes that
SwiftUI provides, like `WindowGroup`, along with custom scenes that you
compose from other scenes. To create a custom scene, declare a type that
conforms to the `Scene` protocol. Implement the required `body` computed
property and provide the content for your custom scene:

A scene acts as a container for a view hierarchy that you want to display to
the user. The system decides when and how to present the view hierarchy in the
user interface in a way that’s platform-appropriate and dependent on the
current state of the app. For example, for the window group shown above, the
system lets the user create or remove windows that contain `MyRootView` on
platforms like macOS and iPadOS. On other platforms, the same view hierarchy
might consume the entire display when active.

Read the `scenePhase` environment value from within a scene or one of its
views to check whether a scene is active or in some other state. You can
create a property that contains the scene phase, which is one of the values in
the `ScenePhase` enumeration, using the `Environment` attribute:

The `Scene` protocol provides scene modifiers, defined as protocol methods
with default implementations, that you use to configure a scene. For example,
you can use the `onChange(of:perform:)` modifier to trigger an action when a
value changes. The following code empties a cache when all of the scenes in
the window group have moved to the background:

## Topics

### Creating a scene

`var body: Self.Body`

The content and behavior of the scene.

**Required**

` associatedtype Body : Scene`

The type of scene that represents the body of this scene.

**Required**

### Watching for changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some Scene`

Adds an action to perform when the given value changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some Scene`

Adds an action to perform when the given value changes.

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

### Creating background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some Scene`

Runs the specified action when the system provides a background task.

### Managing app storage

`func defaultAppStorage(UserDefaults) -> some Scene`

The default store used by `AppStorage` contained within the scene and its view
content.

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

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some Scene`

Defines a keyboard shortcut for opening new scene windows.

### Sizing and positioning the scene

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

### Styling the scene

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

`func upperLimbVisibility(Visibility) -> some Scene`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

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

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some Scene`

Sets the model container in this scene for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this scene’s environment.

### Managing the environment

`func environment<T>(T?) -> some Scene`

Places an observable object in the scene’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene`

Sets the environment value of the specified key path to the given value.

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some Scene`

Transforms the environment value of the specified key path with the given
function.

### Deprecated symbols

`func onChange<V>(of: V, perform: (V) -> Void) -> some Scene`

Adds an action to perform when the given value changes.

Deprecated

## Relationships

### Conforming Types

  * `DocumentGroup`
  * `Group`

Conforms when `Content` conforms to `Scene`.

  * `ImmersiveSpace`
  * `MenuBarExtra`
  * `ModifiedContent`

Conforms when `Content` conforms to `Scene` and `Modifier` conforms to
`_SceneModifier`.

  * `Settings`
  * `WKNotificationScene`
  * `Window`
  * `WindowGroup`

## See Also

### Creating scenes

`struct SceneBuilder`

A result builder for composing a collection of scenes into a single composite
scene.

Instance Property

# scenePhase

The current phase of the scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var scenePhase: ScenePhase { get set }

## Discussion

The system sets this value to provide an indication of the operational state
of a scene or collection of scenes. The exact meaning depends on where you
access the value. For more information, see `ScenePhase`.

## See Also

### Monitoring scene life cycle

`enum ScenePhase`

An indication of a scene’s operational state.

Enumeration

# ScenePhase

An indication of a scene’s operational state.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    enum ScenePhase

## Overview

The system moves your app’s `Scene` instances through phases that reflect a
scene’s operational state. You can trigger actions when the phase changes.
Read the current phase by observing the `scenePhase` value in the
`Environment`:

How you interpret the value depends on where it’s read from. If you read the
phase from inside a `View` instance, you obtain a value that reflects the
phase of the scene that contains the view. The following example uses the
`onChange(of:perform:)` method to enable a timer whenever the enclosing scene
enters the `ScenePhase.active` phase and disable the timer when entering any
other phase:

If you read the phase from within an `App` instance, you obtain an aggregate
value that reflects the phases of all the scenes in your app. The app reports
a value of `ScenePhase.active` if any scene is active, or a value of
`ScenePhase.inactive` when no scenes are active. This includes multiple scene
instances created from a single scene declaration; for example, from a
`WindowGroup`. When an app enters the `ScenePhase.background` phase, expect
the app to terminate soon after. You can use that opportunity to free any
resources:

If you read the phase from within a custom `Scene` instance, the value
similarly reflects an aggregation of all the scenes that make up the custom
scene:

## Topics

### Getting scene phases

`case active`

The scene is in the foreground and interactive.

`case inactive`

The scene is in the foreground but should pause its work.

`case background`

The scene isn’t currently visible in the UI.

## Relationships

### Conforms To

  * `Comparable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Monitoring scene life cycle

`var scenePhase: ScenePhase`

The current phase of the scene.

Structure

# Settings

A scene that presents an interface for viewing and modifying an app’s
settings.

macOS 11.0+

    
    
    struct Settings<Content> where Content : View

## Overview

Use a settings scene to have SwiftUI manage views with controls for your app’s
settings when you declare your app using the `App` protocol. When you use an
`App` declaration for multiple platforms, compile the settings scene only in
macOS:

Passing a view as the argument to a settings scene in the `App` declaration
causes SwiftUI to enable the app’s Settings menu item. SwiftUI manages
displaying and removing the settings view when the user selects the Settings
item from the application menu or the equivalent keyboard shortcut:

The contents of your settings view are controls that modify bindings to
`UserDefaults` values that SwiftUI manages using the `AppStorage` property
wrapper:

You can define your settings in a single view, or you can use a `TabView` to
group settings into different collections:

## Topics

### Creating a settings scene

`init(content: () -> Content)`

Creates a scene that presents an interface for viewing and modifying an app’s
preferences.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Managing a settings window

`struct SettingsLink`

A view that opens the Settings scene defined by an app.

Structure

# SettingsLink

A view that opens the Settings scene defined by an app.

macOS 14.0+

    
    
    struct SettingsLink<Label> where Label : View

## Overview

On macOS, clicking on the link opens the window for the scene or orders it to
the front if it is already open.

## Topics

### Creating a settings link

`init()`

Creates a settings link with the default system label.

`init(label: () -> Label)`

Creates a settings link with a custom label.

### Supporting types

`struct DefaultSettingsLinkLabel`

The default label to use for a settings link.

## Relationships

### Conforms To

  * `View`

## See Also

### Managing a settings window

`struct Settings`

A scene that presents an interface for viewing and modifying an app’s
settings.

Structure

# MenuBarExtra

A scene that renders itself as a persistent control in the system menu bar.

macOS 13.0+

    
    
    struct MenuBarExtra<Label, Content> where Label : View, Content : View

## Overview

Use a `MenuBarExtra` when you want to provide access to commonly used
functionality, even when your app is not active.

Or alternatively, to create a utility app that only shows in the menu bar.

An app that only shows in the menu bar will be automatically terminated if the
user removes the extra from the menu bar.

For apps that only show in the menu bar, a common behavior is for the app to
not display its icon in either the Dock or the application switcher. To enable
this behavior, set the `LSUIElement` flag in your app’s Information Property
List file to `true`.

For more complex or data rich menu bar extras, you can use the `window` style,
which displays a popover-like window from the menu bar icon that contains
standard controls. You define the layout and contents of those controls with
the content that you provide:

## Topics

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating a menu bar extra

`func menuBarExtraStyle<S>(S) -> some Scene`

Sets the style for menu bar extra created by this scene.

`protocol MenuBarExtraStyle`

A specification for the appearance and behavior of a menu bar extra scene.

Instance Method

# menuBarExtraStyle(_:)

Sets the style for menu bar extra created by this scene.

macOS 13.0+

    
    
    func menuBarExtraStyle<S>(_ style: S) -> some Scene where S : MenuBarExtraStyle
    

## See Also

### Creating a menu bar extra

`struct MenuBarExtra`

A scene that renders itself as a persistent control in the system menu bar.

`protocol MenuBarExtraStyle`

A specification for the appearance and behavior of a menu bar extra scene.

Protocol

# MenuBarExtraStyle

A specification for the appearance and behavior of a menu bar extra scene.

macOS 13.0+

    
    
    protocol MenuBarExtraStyle

## Topics

### Getting menu bar extra styles

`static var automatic: AutomaticMenuBarExtraStyle`

The default menu bar extra style.

Available when `Self` is `AutomaticMenuBarExtraStyle`.

`static var menu: PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

Available when `Self` is `PullDownMenuBarExtraStyle`.

`static var window: WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

Available when `Self` is `WindowMenuBarExtraStyle`.

### Supporting types

`struct AutomaticMenuBarExtraStyle`

The default menu bar extra style. You can also use `automatic` to construct
this style.

`struct PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

`struct WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

## Relationships

### Conforming Types

  * `AutomaticMenuBarExtraStyle`
  * `PullDownMenuBarExtraStyle`
  * `WindowMenuBarExtraStyle`

## See Also

### Creating a menu bar extra

`struct MenuBarExtra`

A scene that renders itself as a persistent control in the system menu bar.

`func menuBarExtraStyle<S>(S) -> some Scene`

Sets the style for menu bar extra created by this scene.

Structure

# WKNotificationScene

A scene which appears in response to receiving the specified category of
remote or local notifications.

watchOS 7.0+

    
    
    struct WKNotificationScene<Content, Controller> where Content : View, Controller : WKUserNotificationHostingController<Content>

## Topics

### Creating a notification scene

`init(controller: Controller.Type, category: String)`

Creates a scene that appears in response to receiving a specific category of
remote or local notifications.

## Relationships

### Conforms To

  * `Scene`

