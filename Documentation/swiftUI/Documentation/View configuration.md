Instance Method

# opacity(_:)

Sets the transparency of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some View
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

A view that sets the transparency of this view.

## Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize
a view.

When applying the `opacity(_:)` modifier to a view that has already had its
opacity transformed, the modifier multiplies the effect of the underlying
opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The
top yellow rectangle has its opacity set to 50%, allowing the occluded portion
of the bottom rectangle to be visible:

## See Also

### Hiding views

`func hidden() -> some View`

Hides this view unconditionally.

Instance Method

# hidden()

Hides this view unconditionally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hidden() -> some View
    

## Return Value

A hidden view.

## Discussion

Hidden views are invisible and can’t receive or respond to interactions.
However, they do remain in the view hierarchy and affect layout. Use this
modifier if you want to include a view for layout purposes, but don’t want it
to display.

The third circle takes up space, because it’s still present, but SwiftUI
doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if`
statement instead:

Depending on the current value of the `isHidden` state variable in the example
above, controlled by the `Toggle` instance, SwiftUI draws the circle or
completely omits it from the layout.

## See Also

### Hiding views

`func opacity(Double) -> some View`

Sets the transparency of this view.

Instance Method

# labelsHidden()

Hides the labels of any controls contained within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func labelsHidden() -> some View
    

## Discussion

Use this modifier when you want to omit a label from one or more controls in
your user interface. For example, the first `Toggle` in the following example
hides its label:

The `VStack` in the example above centers the first toggle’s control element
in the available space, while it centers the second toggle’s combined label
and control element:

Always provide a label for controls, even when you hide the label, because
SwiftUI uses labels for other purposes, including accessibility.

Note

This modifier doesn’t work for all labels. It applies to labels that are
separate from the rest of the control’s interface, like they are for `Toggle`,
but not to controls like a bordered button where the label is inside the
button’s border.

## See Also

### Hiding system elements

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# menuIndicator(_:)

Sets the menu indicator visibility for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for
controls in this view. For example, the code below creates a menu without an
indicator:

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

Instance Method

# statusBarHidden(_:)

Sets the visibility of the status bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func statusBarHidden(_ hidden: Bool = true) -> some View
    

##  Parameters

`hidden`

    

A Boolean value that indicates whether to hide the status bar.

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# persistentSystemOverlays(_:)

Sets the preferred visibility of the non-transient system views overlaying the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func persistentSystemOverlays(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value that indicates the visibility of the non-transient system views
overlaying the app.

## Discussion

Use this modifier if you would like to customise the immersive experience of
your app by hiding or showing system overlays that may affect user experience.
The following example hides every persistent system overlay.

Note that this modifier only sets a preference and, ultimately the system will
decide if it will honour it or not.

These non-transient system views include:

  * The Home indicator

  * The SharePlay indicator

  * The Multi-task indicator and Picture-in-picture on iPad

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Enumeration

# Visibility

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum Visibility

## Overview

For example, the preferred visibility of list row separators can be configured
using the `listRowSeparator(_:edges:)`.

## Topics

### Getting visibility options

`case automatic`

The element may be visible or hidden depending on the policies of the
component accepting the visibility configuration.

`case visible`

The element may be visible.

`case hidden`

The element may be hidden.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

Instance Method

# disabled(_:)

Adds a condition that controls whether users can interact with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func disabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether users can interact with this view.

## Return Value

A view that controls whether users can interact with this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button isn’t interactive because the outer
`disabled(_:)` modifier overrides the inner one:

## See Also

### Managing view interaction

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Property

# isEnabled

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# interactionActivityTrackingTag(_:)

Sets a tag that you use for tracking interactivity.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func interactionActivityTrackingTag(_ tag: String) -> some View
    

##  Parameters

`tag`

    

The tag used to track user interactions hosted by this view as activities.

## Return Value

A view that uses a tracking tag.

## Discussion

The following example tracks the scrolling activity of a `List`:

The resolved activity tracking tag is additive, so using the modifier across
the view hierarchy builds the tag from top to bottom. The example below shows
a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# invalidatableContent(_:)

Mark the receiver as their content might be invalidated.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func invalidatableContent(_ invalidatable: Bool = true) -> some View
    

##  Parameters

`invalidatable`

    

Whether the receiver content might be invalidated.

## Discussion

Use this modifier to annotate views that display values that are derived from
the current state of your data and might be invalidated in response of, for
example, user interaction.

The view will change its appearance when `RedactionReasons.invalidated` is
present in the environment.

In an interactive widget a view is invalidated from the moment the user
interacts with a control on the widget to the moment when a new timeline
update has been presented.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

Instance Method

# help(_:)

Adds help text to a view using a localized string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ textKey: LocalizedStringKey) -> some View
    

##  Parameters

`textKey`

    

The key for the localized text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help<S>(_ text: S) -> some View where S : StringProtocol
    

##  Parameters

`text`

    

The text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a text view that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ text: Text) -> some View
    

##  Parameters

`text`

    

The `Text` view to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

Instance Method

# glassBackgroundEffect(displayMode:)

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

visionOS 1.0+

    
    
    func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode = .always) -> some View
    

##  Parameters

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

## See Also

### Adding a glass background

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# glassBackgroundEffect(in:displayMode:)

Fills the view’s background with a glass material using a shape that you
specify.

visionOS 1.0+

    
    
    func glassBackgroundEffect<S>(
        in shape: S,
        displayMode: GlassBackgroundDisplayMode = .always
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An `InsettableShape` instance that SwiftUI draws behind the view. Unsupported
shapes resolve to a rectangle.

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

Prefer a shape for the background that has rounded corners. An unsupported
shape style resolves to a rectangle.

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Enumeration

# GlassBackgroundDisplayMode

The display mode of a glass background.

visionOS 1.0+

    
    
    enum GlassBackgroundDisplayMode

## Overview

Use a value of this type to indicate when to display a glass background that
you add to a view using a view modifier like
`glassBackgroundEffect(displayMode:)`.

## Topics

### Getting the mode

`case always`

Always display the glass material.

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.

`case never`

Never display the glass material.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

Instance Method

# preferredColorScheme(_:)

Sets the preferred color scheme for this presentation.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme for this view.

## Return Value

A view that sets the color scheme.

## Discussion

Use one of the values in `ColorScheme` with this modifier to set a preferred
color scheme for the nearest enclosing presentation, like a popover, a sheet,
or a window. The value that you set overrides the user’s Dark Mode selection
for that presentation. In the example below, the `Toggle` controls an
`isDarkMode` state variable, which in turn controls the color scheme of the
sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this
case are a `List` and a `Toggle` — the value that you set propagates up
through the view hierarchy to the enclosing presentation, or until another
color scheme modifier higher in the hierarchy overrides it. The value you set
also flows down to all child views of the enclosing presentation.

A common use for this modifier is to create side-by-side previews of the same
view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read
the `colorScheme` environment value:

## See Also

### Detecting and requesting the light or dark appearance

`var colorScheme: ColorScheme`

The color scheme of this environment.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Instance Property

# colorScheme

The color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorScheme: ColorScheme { get set }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using the `ColorScheme.light` or
`ColorScheme.dark` appearance. The value that you receive depends on whether
the user has enabled Dark Mode, possibly superseded by the configuration of
the current presentation’s view hierarchy.

You can set the `colorScheme` environment value directly, but that usually
isn’t what you want. Doing so changes the color scheme of the given view and
its child views but _not_ the views above it in the view hierarchy. Instead,
set a color scheme using the `preferredColorScheme(_:)` modifier, which also
propagates the value up through the view hierarchy to the enclosing
presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider
also checking the `colorSchemeContrast` property, which reflects a system-wide
contrast setting that the user controls. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Detecting and requesting the light or dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Enumeration

# ColorScheme

The possible color schemes, corresponding to the light and dark appearances.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorScheme

## Overview

You receive a color scheme value when you read the `colorScheme` environment
value. The value tells you if a light or dark appearance currently applies to
the view. SwiftUI updates the value whenever the appearance changes, and
redraws views that depend on the value. For example, the following `Text` view
automatically updates when the user enables Dark Mode:

Set a preferred appearance for a particular view hierarchy to override the
user’s Dark Mode setting using the `preferredColorScheme(_:)` view modifier.

## Topics

### Getting color schemes

`case light`

The color scheme that corresponds to a light appearance.

`case dark`

The color scheme that corresponds to a dark appearance.

### Creating a color scheme

`init?(UIUserInterfaceStyle)`

Creates a color scheme from its user interface style equivalent.

### Supporting types

`struct PreferredColorSchemeKey`

A key for specifying the preferred color scheme.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Detecting and requesting the light or dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`var colorScheme: ColorScheme`

The color scheme of this environment.

Instance Property

# colorSchemeContrast

The contrast associated with the color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorSchemeContrast: ColorSchemeContrast { get }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using `ColorSchemeContrast.standard` or
`ColorSchemeContrast.increased` contrast. The value that you read depends
entirely on user settings, and you can’t change it.

When adjusting your app’s user interface to match the contrast, consider also
checking the `colorScheme` property to find out if SwiftUI is displaying the
view with a light or dark appearance. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Getting the color scheme contrast

`enum ColorSchemeContrast`

The contrast between the app’s foreground and background colors.

Enumeration

# ColorSchemeContrast

The contrast between the app’s foreground and background colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorSchemeContrast

## Overview

You receive a contrast value when you read the `colorSchemeContrast`
environment value. The value tells you if a standard or increased contrast
currently applies to the view. SwiftUI updates the value whenever the contrast
changes, and redraws views that depend on the value. For example, the
following `Text` view automatically updates when the user enables increased
contrast:

The user sets the contrast by selecting the Increase Contrast option in
Accessibility > Display in System Preferences on macOS, or Accessibility >
Display & Text Size in the Settings app on iOS. Your app can’t override the
user’s choice. For information about using color and contrast in your app, see
Accessibility in the Human Interface Guidelines.

## Topics

### Getting contrast options

`case standard`

SwiftUI displays views with standard contrast between the app’s foreground and
background colors.

`case increased`

SwiftUI displays views with increased contrast between the app’s foreground
and background colors.

### Creating a color scheme contrast

`init?(UIAccessibilityContrast)`

Creates a contrast from its accessibility contrast equivalent.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the color scheme contrast

`var colorSchemeContrast: ColorSchemeContrast`

The contrast associated with the color scheme of this environment.

Instance Method

# preferredSurroundingsEffect(_:)

Applies an effect to passthrough video.

visionOS 1.0+

    
    
    func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some View
    

##  Parameters

`effect`

    

The effect that you want to apply.

## Return Value

A view that exhibits the specified preference.

## Discussion

Use this modifier to indicate a preference for the appearance of passthrough
video when displaying the modified view. For example, you can enhance the
immersiveness of a scene that uses the default `mixed` immersion style by
applying the `systemDark` preference to a view inside the scene:

When the system presents the `Orbit` view in the above code, it also dims
passthrough video. This helps to draw attention to the scene’s virtual content
while still enabling people to remain aware of their surroundings.

Note

This modifier expresses a preference, but the system might not be able to
honor it.

Use a value of `nil` to indicate that you have no preference. You typically do
this to counteract a preference expressed by a view lower in the view
hierarchy.

## See Also

### Configuring passthrough

`struct SurroundingsEffect`

Effects that the system can apply to passthrough video.

Structure

# SurroundingsEffect

Effects that the system can apply to passthrough video.

visionOS 1.0+

    
    
    struct SurroundingsEffect

## Overview

Use one of these values with the `preferredSurroundingsEffect(_:)` view
modifier to indicate what effect to apply to passthrough video when the
modified view is displayed.

## Topics

### Getting the effect

`static var systemDark: SurroundingsEffect`

An effect that dims passthrough video.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Configuring passthrough

`func preferredSurroundingsEffect(SurroundingsEffect?) -> some View`

Applies an effect to passthrough video.

Article

# Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

## Overview

The launch of watchOS 6 introduced the Always On state. Supported devices
continued to display the time, even when the user isn’t actively interacting
with the watch; however, when running an app, the system blurs the app’s user
interface and displays the time over it.

In watchOS 8, Always On expands to include your apps. Apple Watch continues to
display your app’s user interface as long as it’s either the frontmost app or
running a background session. To preserve battery life, the system updates the
user interface at a much lower frequency than when running in the foreground.
It also dims the watch.

Even though your app is inactive or running in the background, the system
continues to update and monitor many of the user interface elements. For
example, when displaying dates and times, using `Text.DateStyle` values like
`relative`, `offset`, and `timer`, the system automatically updates the `Text`
view while in Always On.

Additionally, any controls in the user interface remain interactive. Users can
tap buttons, toggle switches, or select items from a list. When the user
interacts with a control, the system runs the associated action and
transitions your app back to the active state.

Note

Always On isn’t available on Apple Watch SE or Apple Watch Series 4 and
earlier. For these devices, the screen turns off when the app transitions to
the background or inactive states.

Apps compiled for watchOS 8 and later have Always On enabled by default. You
can disable this feature by setting the `WKSupportsAlwaysOnDisplay` key to
`false` in the WatchKit Extension’s `Info.plist` file. Users can also disable
Always On for the entire device or on a per-app basis by choosing Settings >
Display & Brightness > Always On.

### Understand frontmost app behavior

By default, when the user lowers their wrist or stops interacting with their
watch, your app transitions to the inactive state. The system continues to
display your app’s user interface as long as your app remains the frontmost
app (usually two minutes) before transitioning to the background and becoming
suspended. If the user dismisses the app (for example, by pressing the Digital
Crown or by covering the screen), the app transitions immediately to the
background and doesn’t become the frontmost app.

Users can set the amount of time that apps remain the frontmost app by
changing the settings at Settings > General > Wake Screen > Return to Clock.
They can also specify a custom time for individual apps from the Wake Screen.
In watchOS 8 and later, apps can remain in the frontmost app state for a
maximum of 1 hour.

When the app is inactive, the user interface doesn’t update by default.
However, you can use a `TimelineView` to schedule periodic updates. For more
information, see Updating watchOS apps with timelines.

### Update the display during background sessions

Apps running a background session, such as a workout session or background
audio session, remain onscreen as long as the session is active. Unlike
frontmost apps, apps running a background session can continue to update their
user interface; however, to save battery life, the system reduces the update
frequency.

For the best user experience when the app transitions to the background, pause
any animation and show the final state (or a good static image), and remove
any subsecond updates. For example, when the workout app is running in the
foreground, the duration shows hundredths of a second, and the BPM row shows
an animated heart beat. When it transitions to the background, the app
displays a static heart image and the duration only shows time to the nearest
second.

For animation or updates driven by a `TimelineView`, check the view’s cadence
and update the appearance to match. For more information on timelines, see
Updating watchOS apps with timelines.

For other views, monitor the app’s `scenePhase` environment variable, and hide
or stop subsecond updates when it becomes `ScenePhase.inactive` or
`ScenePhase.background`.

### Hide sensitive information

Because displayed information may be visible to casual observers, be sure to
hide any sensitive data while your app is in Always On. Add the
`privacySensitive(_:)` view modifier to blur out specific user interface
elements during Always On.

Or access the `redactionReasons` environment variable.

Check if this variable contains the `privacy` value. If it does, eliminate or
obscure any sensitive data.

The resulting user interface displays the private data while the app is
running in the foreground.

But the interface obscures sensitive data, such as the account number and
balance, when the app is in the Always On state.

To protect the user’s privacy, always hide any highly sensitive information,
such as financial information or health data. For information that may or may
not be sensitive, such as incoming messages or appointments, default to
showing the information. If the user has any concerns, they can disable Always
On on a per-app basis.

### Customize the reduced luminance appearance

To preserve battery life, the system dims the screen during Always On. The
system determines the screen’s overall luminance by comparing the ratio of lit
pixels to dark pixels. It then reduces the overall brightness to an
appropriate level.

Many system controls also automatically update their appearance during Always
On. For example, the `List` view automatically dims the background for the
`CarouselListStyle`.

Many apps can use the system’s default Always On appearance. For example, if
your view is mostly black and uses system controls, you may not need to change
anything. However, you can customize the appearance during Always On to
highlight glanceable, important information in your user interface.

For example, you may consider replacing large blocks of bright content with
stroked outlines and dimmed interiors, as shown on the Numerals Duo watch
face.

You can also dim or remove nonessential information. To customize your
interface, use the `isLuminanceReduced` environment variable.

You can then use this value to modify your user interface, as needed.

The resulting interface displays the title text at full brightness when
active.

Then it dims the title in Always On. Because the ratio of lit to dark pixels
is low, the system doesn’t need to make any other changes to the view.

### Preview both interfaces in Xcode

You can preview both the regular and Always On interfaces in Xcode. To see the
Always On interface, set the `isLuminanceReduced` and `redactionReasons`
environment variables in the preview.

The resulting preview shows both the regular and the Always On interfaces.

Note

The system doesn’t automatically dim the user interface when previewing in
Xcode. To see how the system automatically dims the user interface, you must
test it on a device or in the simulator.

### Test Always On in the Simulator

Xcode supports Always On in the simulator. Simply click the Toggle Always On
button in the status bar to test.

You can view any changes to your user interface related to privacy, reduced
luminance, or transitioning to an inactive state.

## See Also

### Related Documentation

`property list key WKSupportsAlwaysOnDisplay`

A Boolean value that determines whether the system displays the app in the
Always On state.

### User interface

Supporting multiple watch sizes

Customize the layout of your user interface to support all Apple Watch screen
sizes.

Setting the app’s accent color

Set your app’s accent color.

Instance Method

# privacySensitive(_:)

Marks the view as containing sensitive, private user data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func privacySensitive(_ sensitive: Bool = true) -> some View
    

## Discussion

SwiftUI redacts views marked with this modifier when you apply the `privacy`
redaction reason.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# redacted(reason:)

Adds a reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func redacted(reason: RedactionReasons) -> some View
    

## Discussion

Adding a redaction is an additive process: any redaction provided will be
added to the reasons provided by the parent.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# unredacted()

Removes any reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func unredacted() -> some View
    

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# redactionReasons

The current redaction reasons applied to the view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var redactionReasons: RedactionReasons { get set }

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# isSceneCaptured

The current capture state.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var isSceneCaptured: Bool { get set }

## Discussion

Use this value to determine whether the scene is actively being cloned to
another destination (like during AirPlay) or is being mirrored or recorded.

Your app can respond to changes in this value to take appropriate action, like
obscuring content.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Structure

# RedactionReasons

The reasons to apply a redaction to data displayed on screen.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct RedactionReasons

## Topics

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

### Creating redaction reasons

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

