Structure

# Environment

A property wrapper that reads a value from a view’s environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct Environment<Value>

## Overview

Use the `Environment` property wrapper to read a value stored in a view’s
environment. Indicate the value to read using an `EnvironmentValues` key path
in the property declaration. For example, you can create a property that reads
the color scheme of the current view using the key path of the `colorScheme`
property:

You can condition a view’s content on the associated value, which you read
from the declared property’s `wrappedValue`. As with any property wrapper, you
access the wrapped value by directly referring to the property:

If the value changes, SwiftUI updates any parts of your view that depend on
the value. For example, that might happen in the above example if the user
changes the Appearance settings.

You can use this property wrapper to read — but not set — an environment
value. SwiftUI updates some environment values automatically based on system
settings and provides reasonable defaults for others. You can override some of
these, as well as set custom environment values that you define, using the
`environment(_:_:)` view modifier.

For the complete list of environment values provided by SwiftUI, see the
properties of the `EnvironmentValues` structure. For information about
creating custom environment values, see the `EnvironmentKey` protocol.

### Get an observable object

You can also use `Environment` to get an observable object from a view’s
environment. The observable object must conform to the `Observable` protocol,
and your app must set the object in the environment using the the object
itself or a key path.

To set the object in the environment using the object itself, use the
`environment(_:)` modifier:

To get the observable object using its type, create a property and provide the
`Environment` property wrapper the object’s type:

By default, reading an object from the environment returns a non-optional
object when using the object type as the key. This default behavior assumes
that a view in the current hierarchy previously stored a non-optional instance
of the type using the `environment(_:)` modifier. If a view attempts to
retrieve an object using its type and that object isn’t in the environment,
SwiftUI throws an exception.

In cases where there is no guarantee that an object is in the environment,
retrieve an optional version of the object as shown in the following code. If
the object isn’t available the environment, SwiftUI returns `nil` instead of
throwing an exception.

### Get an observable object using a key path

To set the object with a key path, use the `environment(_:_:)` modifier:

To get the object, create a property and specify the key path:

## Topics

### Creating an environment instance

`init(KeyPath<EnvironmentValues, Value>)`

Creates an environment property to read the specified key path.

`init(Value.Type)`

Creates an environment property to read an observable object from the
environment.

`init<T>(T.Type)`

Creates an environment property to read an observable object from the
environment, returning `nil` if no corresponding object has been set in the
current view’s environment.

### Getting the value

`var wrappedValue: Value`

The current value of the environment property.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Accessing environment values

`struct EnvironmentValues`

A collection of environment values propagated through a view hierarchy.

Structure

# EnvironmentValues

A collection of environment values propagated through a view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct EnvironmentValues

## Overview

SwiftUI exposes a collection of values to your app’s views in an
`EnvironmentValues` structure. To read a value from the structure, declare a
property using the `Environment` property wrapper and specify the value’s key
path. For example, you can read the current locale:

Use the property you declare to dynamically control a view’s layout. SwiftUI
automatically sets or updates many environment values, like `pixelLength`,
`scenePhase`, or `locale`, based on device characteristics, system state, or
user settings. For others, like `lineLimit`, SwiftUI provides a reasonable
default value.

You can set or override some values using the `environment(_:_:)` view
modifier:

The value that you set affects the environment for the view that you modify —
including its descendants in the view hierarchy — but only up to the point
where you apply a different environment modifier.

SwiftUI provides dedicated view modifiers for setting some values, which
typically makes your code easier to read. For example, rather than setting the
`lineLimit` value directly, as in the previous example, you should instead use
the `lineLimit(_:)` modifier:

In some cases, using a dedicated view modifier provides additional
functionality. For example, you must use the `preferredColorScheme(_:)`
modifier rather than setting `colorScheme` directly to ensure that the new
value propagates up to the presenting container when presenting a view like a
popover:

Create custom environment values by defining a type that conforms to the
`EnvironmentKey` protocol, and then extending the environment values structure
with a new property. Use your key to get and set the value, and provide a
dedicated modifier for clients to use when setting the value:

Clients of your value then access the value in the usual way, reading it with
the `Environment` property wrapper, and setting it with the `myCustomValue`
view modifier.

## Topics

### Creating and accessing values

`init()`

Creates an environment values instance.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`subscript<T>(T.Type) -> T?`

Reads an observable object of the specified type from the environment.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`var description: String`

A string that represents the contents of the environment values instance.

### Accessibility

`var accessibilityDimFlashingLights: Bool`

Whether the setting to reduce flashing or strobing lights in video content is
on. This setting can also be used to determine if UI in playback controls
should be shown to indicate upcoming content that includes flashing or
strobing lights.

`var accessibilityDifferentiateWithoutColor: Bool`

Whether the system preference for Differentiate without Color is enabled.

`var accessibilityEnabled: Bool`

A Boolean value that indicates whether the user has enabled an assistive
technology.

`var accessibilityInvertColors: Bool`

Whether the system preference for Invert Colors is enabled.

`var accessibilityLargeContentViewerEnabled: Bool`

Whether the Large Content Viewer is enabled.

`var accessibilityPlayAnimatedImages: Bool`

Whether the setting for playing animations in an animated image is on. When
this value is false, any presented image that contains animation should not
play automatically.

`var accessibilityPrefersHeadAnchorAlternative: Bool`

Whether the system setting to prefer alternatives to head-anchored content is
on.

`var accessibilityQuickActionsEnabled: Bool`

A Boolean that indicates whether the quick actions feature is enabled.

`var accessibilityReduceMotion: Bool`

Whether the system preference for Reduce Motion is enabled.

`var accessibilityReduceTransparency: Bool`

Whether the system preference for Reduce Transparency is enabled.

`var accessibilityShowButtonShapes: Bool`

Whether the system preference for Show Button Shapes is enabled.

`var accessibilitySwitchControlEnabled: Bool`

A Boolean value that indicates whether the Switch Control motor accessibility
feature is in use.

`var accessibilityVoiceOverEnabled: Bool`

A Boolean value that indicates whether the VoiceOver screen reader is in use.

`var legibilityWeight: LegibilityWeight?`

The font weight to apply to text.

### Actions

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`var openImmersiveSpace: OpenImmersiveSpaceAction`

An action that presents an immersive space.

`var dismissImmersiveSpace: DismissImmersiveSpaceAction`

An immersive space dismissal action stored in a view’s environment.

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`var openURL: OpenURLAction`

An action that opens a URL.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

`var purchase: PurchaseAction`

An action that starts an in-app purchase.

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`var resetFocus: ResetFocusAction`

An action that requests the focus system to reevaluate default focus.

### Authentication

`var authorizationController: AuthorizationController`

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

`var webAuthenticationSession: WebAuthenticationSession`

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

### Controls and input

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`var controlSize: ControlSize`

The size to apply to controls within a view.

`var controlActiveState: ControlActiveState`

The active state of controls in the view.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

`var searchSuggestionsPlacement: SearchSuggestionsPlacement`

The current placement of search suggestions.

### Display characteristics

`var colorScheme: ColorScheme`

The color scheme of this environment.

`var colorSchemeContrast: ColorSchemeContrast`

The contrast associated with the color scheme of this environment.

`var displayScale: CGFloat`

The display scale of this environment.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var imageScale: Image.Scale`

The image scale for this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var sidebarRowSize: SidebarRowSize`

The current size of sidebar rows.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

### Global objects

`var calendar: Calendar`

The current calendar that views should use when handling dates.

`var documentConfiguration: DocumentConfiguration?`

The configuration of a document in a `DocumentGroup`.

`var locale: Locale`

The current locale that views should use.

`var managedObjectContext: NSManagedObjectContext`

`var modelContext: ModelContext`

The SwiftData model context that will be used for queries and other model
operations within this environment.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

### Scrolling

`var isScrollEnabled: Bool`

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode`

The way that scrollable content interacts with the software keyboard.

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

### State

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`var isActivityFullscreen: Bool`

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var isSceneCaptured: Bool`

The current capture state.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var scenePhase: ScenePhase`

The current phase of the scene.

`var supportsMultipleWindows: Bool`

A Boolean value that indicates whether the current platform supports opening
multiple windows.

### StoreKit configuration

`var displayStoreKitMessage: DisplayMessageAction`

`var requestReview: RequestReviewAction`

### Text styles

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`var font: Font?`

The default font of this environment.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

### View attributes

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

`var backgroundMaterial: Material?`

The material underneath the current view.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var physicalMetrics: PhysicalMetricsConverter`

The physical metrics associated with a scene.

`var realityKitScene: Scene?`

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

### Widgets

`var showsWidgetContainerBackground: Bool`

An environment variable that indicates whether the background of a widget
appears.

`var showsWidgetLabel: Bool`

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

`var widgetFamily: WidgetFamily`

The template of the widget — small, medium, or large.

`var widgetRenderingMode: WidgetRenderingMode`

The widget’s rendering mode, based on where the system is displaying it.

`var widgetContentMargins: EdgeInsets`

A property that identifies the content margins of a widget.

### Deprecated environment values

`var disableAutocorrection: Bool?`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`var sizeCategory: ContentSizeCategory`

The size of content.

Deprecated

`var presentationMode: Binding<PresentationMode>`

A binding to the current presentation mode of the view associated with this
environment.

Deprecated

`struct PresentationMode`

An indication whether a view is currently presented by another view.

Deprecated

### Instance Properties

`var complicationRenderingMode: ComplicationRenderingMode`

The complication rendering mode for the current environment.

Deprecated

`var immersiveSpaceDisplacement: Pose3D`

Provides the pose applied by the system to displace the origin of the
immersive space.

## Relationships

### Conforms To

  * `CustomStringConvertible`

## See Also

### Accessing environment values

`struct Environment`

A property wrapper that reads a value from a view’s environment.

Protocol

# EnvironmentKey

A key for accessing values in the environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol EnvironmentKey

## Overview

You can create custom environment values by extending the `EnvironmentValues`
structure with new properties. First declare a new environment key type and
specify a value for the required `defaultValue` property:

The Swift compiler automatically infers the associated `Value` type as the
type you specify for the default value. Then use the key to define a new
environment value property:

Clients of your environment value never use the key directly. Instead, they
use the key path of your custom environment value property. To set the
environment value for a view and all its subviews, add the `environment(_:_:)`
view modifier to that view:

As a convenience, you can also define a dedicated view modifier to apply this
environment value:

This improves clarity at the call site:

To read the value from inside `MyView` or one of its descendants, use the
`Environment` property wrapper:

## Topics

### Getting the default value

`static var defaultValue: Self.Value`

The default value for the environment key.

**Required**

` associatedtype Value`

The associated type representing the type of the environment key’s value.

**Required**

## Relationships

### Inherited By

  * `UITraitBridgedEnvironmentKey`

Instance Method

# environment(_:)

Places an observable object in the view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environment<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

##  Parameters

`object`

    

The object to set for this object’s type in the environment, or `nil` to clear
an object of this type from the environment.

## Return Value

A view that has the specified object in its environment.

## Discussion

Use this modifier to place an object that you declare with the `Observable()`
macro into a view’s environment. For example, you can add an instance of a
custom observable `Profile` class to the environment of a `ContentView`:

You then read the object inside `ContentView` or one of its descendants using
the `Environment` property wrapper:

This modifier affects the given view, as well as that view’s descendant views.
It has no effect outside the view hierarchy on which you call it. The
environment of a given view hierarchy holds only one observable object of a
given type.

Note

This modifier takes an object that conforms to the `Observable` protocol. To
add environment objects that conform to the `ObservableObject` protocol, use
`environmentObject(_:)` instead.

## See Also

### Modifying the environment of a view

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# environment(_:_:)

Sets the environment value of the specified key path to the given value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func environment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        _ value: V
    ) -> some View
    

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
example, you can set the value associated with the `truncationMode` key:

You then read the value inside `MyView` or one of its descendants using the
`Environment` property wrapper:

SwiftUI provides dedicated view modifiers for setting most environment values,
like the `truncationMode(_:)` modifier which sets the `truncationMode` value:

Prefer the dedicated modifier when available, and offer your own when defining
custom environment values, as described in `EnvironmentKey`.

This modifier affects the given view, as well as that view’s descendant views.
It has no effect outside the view hierarchy on which you call it.

## See Also

### Modifying the environment of a view

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# transformEnvironment(_:transform:)

Transforms the environment value of the specified key path with the given
function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformEnvironment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        transform: @escaping (inout V) -> Void
    ) -> some View
    

## See Also

### Modifying the environment of a view

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

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

