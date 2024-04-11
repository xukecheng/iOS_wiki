# DefaultTabViewStyle

Initializer

# init()

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# DynamicProperty Implementations

Instance Method

# update()

Updates the fetched results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    mutating func update()

Available when `Result` conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

Instance Method

# update()

Updates the fetched results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    func update()

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>`

The fetched results of the fetch request.



# DefaultToggleStyle

Initializer

# init()

Creates a default toggle style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `automatic` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that acts as a toggle.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `automatic` toggle style. Don’t call
this method directly. Rather, the system calls this method for each `Toggle`
instance in a view hierarchy that needs the default style.



# Deprecated modifiers

Instance Method

# colorScheme(_:)

Sets this view’s color scheme.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func colorScheme(_ colorScheme: ColorScheme) -> some View
    

Deprecated

Use `preferredColorScheme(_:)` instead.

##  Parameters

`colorScheme`

    

The color scheme for this view.

## Return Value

A view that sets this view’s color scheme.

## Discussion

Use `colorScheme(_:)` to set the color scheme for the view to which you apply
it and any subviews.

## See Also

### Appearance modifiers

`func listRowPlatterColor(Color?) -> some View`

Sets the color that the system applies to the row background when this view is
placed in a list.

Deprecated

`func background<Background>(Background, alignment: Alignment) -> some View`

Layers the given view behind this view.

Deprecated

`func overlay<Overlay>(Overlay, alignment: Alignment) -> some View`

Layers a secondary view in front of this view.

Deprecated

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

Instance Method

# listRowPlatterColor(_:)

Sets the color that the system applies to the row background when this view is
placed in a list.

watchOS 6.0–10.4  Deprecated

    
    
    func listRowPlatterColor(_ color: Color?) -> some View
    

Deprecated

Use `listItemTint(_:)` instead.

##  Parameters

`color`

    

The `Color` to apply to the system cell.

## Return Value

A view with the specified `color` applied to the system cell.

## Discussion

Use `listRowPlatterColor(_:)` to set the underlying row background color in a
list.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `List` builder iterates over the `Flavor` enumeration and
extracts the raw value of each of its elements using the resulting text to
create each list row item. After the list builder finishes, the
`listRowPlatterColor(_:)` modifier sets the underlying row background color to
the `Color` you specify.

## See Also

### Appearance modifiers

`func colorScheme(ColorScheme) -> some View`

Sets this view’s color scheme.

Deprecated

`func background<Background>(Background, alignment: Alignment) -> some View`

Layers the given view behind this view.

Deprecated

`func overlay<Overlay>(Overlay, alignment: Alignment) -> some View`

Layers a secondary view in front of this view.

Deprecated

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

Instance Method

# background(_:alignment:)

Layers the given view behind this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func background<Background>(
        _ background: Background,
        alignment: Alignment = .center
    ) -> some View where Background : View
    

Deprecated

Use `background(alignment:content:)` instead.

##  Parameters

`background`

    

The view to draw behind this view.

`alignment`

    

The alignment with a default value of `center` that you use to position the
background view.

## Discussion

Use `background(_:alignment:)` when you need to place one view behind another,
with the background view optionally aligned with a specified edge of the
frontmost view.

The example below creates two views: the `Frontmost` view, and the
`DiamondBackground` view. The `Frontmost` view uses the `DiamondBackground`
view for the background of the image element inside the `Frontmost` view’s
`VStack`.

## See Also

### Appearance modifiers

`func colorScheme(ColorScheme) -> some View`

Sets this view’s color scheme.

Deprecated

`func listRowPlatterColor(Color?) -> some View`

Sets the color that the system applies to the row background when this view is
placed in a list.

Deprecated

`func overlay<Overlay>(Overlay, alignment: Alignment) -> some View`

Layers a secondary view in front of this view.

Deprecated

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

Instance Method

# overlay(_:alignment:)

Layers a secondary view in front of this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func overlay<Overlay>(
        _ overlay: Overlay,
        alignment: Alignment = .center
    ) -> some View where Overlay : View
    

Deprecated

Use `overlay(alignment:content:)` instead.

##  Parameters

`overlay`

    

The view to layer in front of this view.

`alignment`

    

The alignment for `overlay` in relation to this view.

## Return Value

A view that layers `overlay` in front of the view.

## Discussion

When you apply an overlay to a view, the original view continues to provide
the layout characteristics for the resulting view. In the following example,
the heart image is shown overlaid in front of, and aligned to the bottom of
the folder image.

## See Also

### Appearance modifiers

`func colorScheme(ColorScheme) -> some View`

Sets this view’s color scheme.

Deprecated

`func listRowPlatterColor(Color?) -> some View`

Sets the color that the system applies to the row background when this view is
placed in a list.

Deprecated

`func background<Background>(Background, alignment: Alignment) -> some View`

Layers the given view behind this view.

Deprecated

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

Instance Method

# foregroundColor(_:)

Sets the color of the foreground elements displayed by this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func foregroundColor(_ color: Color?) -> some View
    

Deprecated

Use `foregroundStyle(_:)` instead.

##  Parameters

`color`

    

The foreground color to use when displaying this view. Pass `nil` to remove
any custom foreground color and to allow the system or the container to
provide its own foreground color. If a container-specific override doesn’t
exist, the system uses the primary color.

## Return Value

A view that uses the foreground color you supply.

## See Also

### Appearance modifiers

`func colorScheme(ColorScheme) -> some View`

Sets this view’s color scheme.

Deprecated

`func listRowPlatterColor(Color?) -> some View`

Sets the color that the system applies to the row background when this view is
placed in a list.

Deprecated

`func background<Background>(Background, alignment: Alignment) -> some View`

Layers the given view behind this view.

Deprecated

`func overlay<Overlay>(Overlay, alignment: Alignment) -> some View`

Layers a secondary view in front of this view.

Deprecated

Instance Method

# autocapitalization(_:)

Sets whether to apply auto-capitalization to this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func autocapitalization(_ style: UITextAutocapitalizationType) -> some View
    

Deprecated

Use `textInputAutocapitalization(_:)` instead.

##  Parameters

`style`

    

One of the autocapitalization modes defined in the
`UITextAutocapitalizationType` enumeration.

## Discussion

Use this method when you need to automatically capitalize words, sentences, or
other text like proper nouns.

In example below, as the user enters text each word is automatically
capitalized:

The `UITextAutocapitalizationType` enumeration defines the available
capitalization modes. The default is `UITextAutocapitalizationType.sentences`.

## See Also

### Text modifiers

`func disableAutocorrection(Bool?) -> some View`

Sets whether to disable autocorrection for this view.

Deprecated

Instance Method

# disableAutocorrection(_:)

Sets whether to disable autocorrection for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 8.0–10.4  Deprecated  visionOS 1.0+

    
    
    func disableAutocorrection(_ disable: Bool?) -> some View
    

Deprecated

Use `autocorrectionDisabled(_:)` instead.

##  Parameters

`enabled`

    

A Boolean value that indicates whether autocorrection is disabled for this
view.

## Discussion

Use this method when the effect of autocorrection would make it more difficult
for the user to input information. The entry of proper names and street
addresses are examples where autocorrection can negatively affect the user’s
ability complete a data entry task.

In the example below configures a `TextField` with the default keyboard.
Disabling autocorrection allows the user to enter arbitrary text without the
autocorrection system offering suggestions or attempting to override their
input.

## See Also

### Text modifiers

`func autocapitalization(UITextAutocapitalizationType) -> some View`

Sets whether to apply auto-capitalization to this view.

Deprecated

Instance Method

# navigationBarTitle(_:)

Sets the title in the navigation bar for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle(_ title: Text) -> some View
    

Deprecated

Use `navigationTitle(_:)` instead.

##  Parameters

`title`

    

A description of this view to display in the navigation bar.

## Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar. This
modifier only takes effect when this view is inside of and visible within a
`NavigationView`.

The example below shows setting the title of the navigation bar using a `Text`
view:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarTitle(_:displayMode:)

Sets the title and display mode in the navigation bar for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle(
        _ title: Text,
        displayMode: NavigationBarItem.TitleDisplayMode
    ) -> some View
    

Deprecated

Use `navigationTitle(_:)` with `navigationBarTitleDisplayMode(_:)`.

##  Parameters

`title`

    

A title for this view to display in the navigation bar.

`displayMode`

    

The style to use for displaying the navigation bar title.

## Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation
bar for this view and specify a display mode for the title from one of the
`NavigationBarItem.TitleDisplayMode` styles. This modifier only takes effect
when this view is inside of and visible within a `NavigationView`.

In the example below, text for the navigation bar title is provided using a
`Text` view. The navigation bar title’s `NavigationBarItem.TitleDisplayMode`
is set to `.inline` which places the navigation bar title in the bounds of the
navigation bar.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarTitle(_:)

Sets the title of this view’s navigation bar with a localized string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle(_ titleKey: LocalizedStringKey) -> some View
    

Deprecated

Use `navigationTitle(_:)` instead.

##  Parameters

`titleKey`

    

A key to a localized description of this view to display in the navigation
bar.

## Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar using a
`LocalizedStringKey` that will be used to search for a matching localized
string in the application’s localizable strings assets.

This modifier only takes effect when this view is inside of and visible within
a `NavigationView`.

In the example below, a string constant is used to access a
`LocalizedStringKey` that will be resolved at run time to provide a title for
the navigation bar. If the localization key cannot be resolved, the text of
the key name will be used as the title text.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarTitle(_:)

Sets the title of this view’s navigation bar with a string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle<S>(_ title: S) -> some View where S : StringProtocol
    

Deprecated

Use `navigationTitle(_:)` instead.

##  Parameters

`title`

    

A title for this view to display in the navigation bar.

## Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar using a
`String`. This modifier only takes effect when this view is inside of and
visible within a `NavigationView`.

In the example below, text for the navigation bar title is provided using a
string:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarTitle(_:displayMode:)

Sets the title and display mode in the navigation bar for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle(
        _ titleKey: LocalizedStringKey,
        displayMode: NavigationBarItem.TitleDisplayMode
    ) -> some View
    

Deprecated

Use `navigationTitle(_:)` with `navigationBarTitleDisplayMode(_:)`.

##  Parameters

`titleKey`

    

A key to a localized description of this view to display in the navigation
bar.

`displayMode`

    

The style to use for displaying the navigation bar title.

## Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation
bar for this view and specify a display mode for the title from one of the
`NavigationBarItem.TitleDisplayMode` styles. This modifier only takes effect
when this view is inside of and visible within a `NavigationView`.

In the example below, text for the navigation bar title is provided using a
string. The navigation bar title’s `NavigationBarItem.TitleDisplayMode` is set
to `.inline` which places the navigation bar title in the bounds of the
navigation bar.

If the `titleKey` can’t be found, the title uses the text of the key name
instead.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarTitle(_:displayMode:)

Sets the title and display mode in the navigation bar for this view.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  Mac Catalyst
14.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarTitle<S>(
        _ title: S,
        displayMode: NavigationBarItem.TitleDisplayMode
    ) -> some View where S : StringProtocol
    

Deprecated

Use `navigationTitle(_:)` with `navigationBarTitleDisplayMode(_:)`.

##  Parameters

`title`

    

A title for this view to display in the navigation bar.

`displayMode`

    

The way to display the title.

## Discussion

Use `navigationBarTitle(_:, displayMode)` to set the title of the navigation
bar for this view and specify a display mode for the title from one of the
`NavigationBarItem.Title.DisplayMode` styles. This modifier only takes effect
when this view is inside of and visible within a `NavigationView`.

In the example below, `navigationBarTitle(_:, displayMode)` uses a string to
provide a title for the navigation bar. Setting the title’s `displaymode` to
`.inline` places the navigation bar title within the bounds of the navigation
bar.

In the example below, text for the navigation bar title is provided using a
string. The navigation bar title’s `displayMode` is set to `.inline` which
places the navigation bar title in the bounds of the navigation bar.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarItems(leading:)

Sets the navigation bar items for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarItems<L>(leading: L) -> some View where L : View
    

Deprecated

Use `toolbar(content:)` with `navigationBarLeading` placement.

##  Parameters

`leading`

    

A view that appears on the leading edge of the title.

## Discussion

Use `navigationBarItems(leading:)` to add navigation bar items to the leading
edge of the navigation bar for this view.

This modifier only takes effect when this view is inside of and visible within
a `NavigationView`.

On iOS 14 and later, the leading item supplements a visible back button,
instead of replacing it, by default. To hide the back button, use
`navigationBarBackButtonHidden(_:)`.

The example below adds buttons to the leading edge of the button area of the
navigation view:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarItems(leading:trailing:)

Sets the navigation bar items for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarItems<L, T>(
        leading: L,
        trailing: T
    ) -> some View where L : View, T : View
    

Deprecated

Use `toolbar(content:)` with `navigationBarLeading` or `navigationBarTrailing`
placement.

##  Parameters

`leading`

    

A view that appears on the leading edge of the title.

`trailing`

    

A view that appears on the trailing edge of the title.

## Discussion

Use `navigationBarItems(leading:trailing:)` to add navigation bar items to the
leading and trailing edges of the navigation bar for this view.

This modifier only takes effect when this view is inside of and visible within
a `NavigationView`.

On iOS 14 and later, the leading item supplements a visible back button,
instead of replacing it, by default. To hide the back button, use
`navigationBarBackButtonHidden(_:)`.

The example below adds buttons to the leading and trailing edges of the button
area of the navigation view:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarItems(trailing:)

Configures the navigation bar items for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func navigationBarItems<T>(trailing: T) -> some View where T : View
    

Deprecated

Use `toolbar(content:)` with `navigationBarTrailing` placement.

##  Parameters

`trailing`

    

A view shown on the trailing edge of the title.

## Discussion

Use `navigationBarItems(trailing:)` to add navigation bar items to the
trailing edge of the navigation bar for this view. This modifier only takes
effect when this view is inside of and visible within a `NavigationView`.

The example below adds buttons to the trailing edge of the button area of the
navigation view:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# navigationBarHidden(_:)

Hides the navigation bar for this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func navigationBarHidden(_ hidden: Bool) -> some View
    

Deprecated

Use `toolbar(_:for:)` with the `Visibility.hidden` visibility and the
`navigationBar` placement instead.

##  Parameters

`hidden`

    

A Boolean value that indicates whether to hide the navigation bar.

## Discussion

Use this method to hide the navigation bar. This modifier only takes effect
when the modified view is inside of and visible within a `NavigationView`.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# statusBar(hidden:)

Sets the visibility of the status bar.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  visionOS 1.0+

    
    
    func statusBar(hidden: Bool) -> some View
    

Deprecated

Use `statusBarHidden(_:)` instead.

## Discussion

Use this method to show or hide the status bar.

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

Instance Method

# contextMenu(_:)

Adds a context menu to the view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–7.0  Deprecated
visionOS 1.0+

    
    
    func contextMenu<MenuItems>(_ contextMenu: ContextMenu<MenuItems>?) -> some View where MenuItems : View
    

Deprecated

Use `contextMenu(menuItems:)` instead.

##  Parameters

`contextMenu`

    

A context menu container for views that you present as menu items in a context
menu.

## Return Value

A view that can show a context menu.

## Discussion

Use this method to attach a specified context menu to a view. You can make the
context menu unavailable by conditionally passing `nil` as the value for the
`contextMenu`.

The example below creates a `ContextMenu` that contains two items and passes
them into the modifier. The Boolean value `shouldShowMenu`, which defaults to
`true`, controls the context menu availability:

## See Also

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

Instance Method

# menuButtonStyle(_:)

Sets the style for menu buttons within this view.

macOS 10.15–14.4  Deprecated

    
    
    func menuButtonStyle<S>(_ style: S) -> some View where S : MenuButtonStyle
    

Deprecated

Use `menuStyle(_:)` instead.

## See Also

### Styling a menu button

`protocol MenuButtonStyle`

A custom specification for the appearance and interaction of a menu button.

Deprecated

Instance Method

# navigationViewStyle(_:)

Sets the style for navigation views within this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle
    

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Discussion

Use this modifier to change the appearance and behavior of navigation views.
For example, by default, navigation views appear with multiple columns in
wider environments, like iPad in landscape orientation:

You can apply the `stack` style to force single-column stack navigation in
these environments:

## See Also

### Styling navigation views

`protocol NavigationViewStyle`

A specification for the appearance and interaction of a navigation view.

Deprecated

Instance Method

# frame()

Positions this view within an invisible frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame() -> some View
    

Deprecated

Use `frame(width:height:alignment:)` or
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
instead.

## See Also

### Layout modifiers

`func edgesIgnoringSafeArea(Edge.Set) -> some View`

Changes the view’s proposed area to extend outside the screen’s safe areas.

Deprecated

`func coordinateSpace<T>(name: T) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

Deprecated

Instance Method

# edgesIgnoringSafeArea(_:)

Changes the view’s proposed area to extend outside the screen’s safe areas.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func edgesIgnoringSafeArea(_ edges: Edge.Set) -> some View
    

Deprecated

Use `ignoresSafeArea(_:edges:)` instead.

##  Parameters

`edges`

    

The set of the edges in which to expand the size requested for this view.

## Return Value

A view that may extend outside of the screen’s safe area on the edges
specified by `edges`.

## Discussion

Use `edgesIgnoringSafeArea(_:)` to change the area proposed for this view so
that — were the proposal accepted — this view could extend outside the safe
area to the bounds of the screen for the specified edges.

For example, you can propose that a text view ignore the safe area’s top
inset:

Depending on the surrounding view hierarchy, SwiftUI may not honor an
`edgesIgnoringSafeArea(_:)` request. This can happen, for example, if the view
is inside a container that respects the screen’s safe area. In that case you
may need to apply `edgesIgnoringSafeArea(_:)` to the container instead.

## See Also

### Layout modifiers

`func frame() -> some View`

Positions this view within an invisible frame.

Deprecated

`func coordinateSpace<T>(name: T) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

Deprecated

Instance Method

# coordinateSpace(name:)

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func coordinateSpace<T>(name: T) -> some View where T : Hashable
    

Deprecated

Use `coordinateSpace(_:)` instead.

##  Parameters

`name`

    

A name used to identify this coordinate space.

## Discussion

Use `coordinateSpace(name:)` to allow another function to find and operate on
a view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its
enclosing view’s coordinate space:

Here, the `VStack` in the `ContentView` named “stack” is composed of a red
frame with a custom `Circle` view `overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing
VStack’s coordinate space. As the gesture recognizer’s closure registers
events inside `circle` it stores them in the shared `location` state variable
and the `VStack` displays the coordinates in a `Text` view.

## See Also

### Layout modifiers

`func frame() -> some View`

Positions this view within an invisible frame.

Deprecated

`func edgesIgnoringSafeArea(Edge.Set) -> some View`

Changes the view’s proposed area to extend outside the screen’s safe areas.

Deprecated

Instance Method

# accentColor(_:)

Sets the accent color for this view and the views it contains.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func accentColor(_ accentColor: Color?) -> some View
    

Deprecated

Use the asset catalog’s accent color or `tint(_:)` instead.

##  Parameters

`accentColor`

    

The color to use as an accent color. Set the value to `nil` to use the
inherited accent color.

## Discussion

Use `accentColor(_:)` when you want to apply a broad theme color to your app’s
user interface. Some styles of controls use the accent color as a default tint
color.

Note

In macOS, SwiftUI applies customization of the accent color only if the user
chooses Multicolor under General > Accent color in System Preferences.

In the example below, the outer `VStack` contains two child views. The first
is a button with the default accent color. The second is a `VStack` that
contains a button and a slider, both of which adopt the purple accent color of
their containing view. Note that the `Text` element used as a label alongside
the `Slider` retains its default color.

## See Also

### Graphics and rendering modifiers

`func mask<Mask>(Mask) -> some View`

Masks this view using the alpha channel of the given view.

Deprecated

`func animation(Animation?) -> some View`

Applies the given animation to all animatable values within this view.

Deprecated

`func cornerRadius(CGFloat, antialiased: Bool) -> some View`

Clips this view to its bounding frame, with the specified corner radius.

Deprecated

Instance Method

# mask(_:)

Masks this view using the alpha channel of the given view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func mask<Mask>(_ mask: Mask) -> some View where Mask : View
    

Deprecated

Use `mask(alignment:_:)` instead.

##  Parameters

`mask`

    

The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another
view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

## See Also

### Graphics and rendering modifiers

`func accentColor(Color?) -> some View`

Sets the accent color for this view and the views it contains.

Deprecated

`func animation(Animation?) -> some View`

Applies the given animation to all animatable values within this view.

Deprecated

`func cornerRadius(CGFloat, antialiased: Bool) -> some View`

Clips this view to its bounding frame, with the specified corner radius.

Deprecated

Instance Method

# animation(_:)

Applies the given animation to all animatable values within this view.

iOS 13.0–15.0  Deprecated  iPadOS 13.0–15.0  Deprecated  macOS 10.15–12.0
Deprecated  Mac Catalyst 13.0–15.0  Deprecated  tvOS 13.0–15.0  Deprecated
watchOS 6.0–8.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func animation(_ animation: Animation?) -> some View
    

Deprecated

Use `withAnimation(_:_:)` or `animation(_:value:)` instead.

##  Parameters

`animation`

    

The animation to apply to animatable values within this view.

## Return Value

A view that wraps this view and applies `animation` to all animatable values
used within the view.

## Discussion

Use this modifier on leaf views rather than container views. The animation
applies to all child views within this view; calling `animation(_:)` on a
container view can lead to unbounded scope.

## See Also

### Graphics and rendering modifiers

`func accentColor(Color?) -> some View`

Sets the accent color for this view and the views it contains.

Deprecated

`func mask<Mask>(Mask) -> some View`

Masks this view using the alpha channel of the given view.

Deprecated

`func cornerRadius(CGFloat, antialiased: Bool) -> some View`

Clips this view to its bounding frame, with the specified corner radius.

Deprecated

Instance Method

# cornerRadius(_:antialiased:)

Clips this view to its bounding frame, with the specified corner radius.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func cornerRadius(
        _ radius: CGFloat,
        antialiased: Bool = true
    ) -> some View
    

Deprecated

Use `clipShape(_:style:)` or `fill(style:)` instead.

##  Parameters

`antialiased`

    

A Boolean value that indicates whether the rendering system applies smoothing
to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame with the specified corner
radius.

## Discussion

By default, a view’s bounding frame only affects its layout, so any content
that extends beyond the edges of the frame remains visible. Use
`cornerRadius(_:antialiased:)` to hide any content that extends beyond these
edges while applying a corner radius.

The following code applies a corner radius of 25 to a text view:

## See Also

### Graphics and rendering modifiers

`func accentColor(Color?) -> some View`

Sets the accent color for this view and the views it contains.

Deprecated

`func mask<Mask>(Mask) -> some View`

Masks this view using the alpha channel of the given view.

Deprecated

`func animation(Animation?) -> some View`

Applies the given animation to all animatable values within this view.

Deprecated

Instance Method

# onChange(of:perform:)

Adds an action to perform when the given value changes.

iOS 14.0–17.0  Deprecated  iPadOS 14.0–17.0  Deprecated  macOS 11.0–14.0
Deprecated  Mac Catalyst 14.0–17.0  Deprecated  tvOS 14.0–17.0  Deprecated
watchOS 7.0–10.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    func onChange<V>(
        of value: V,
        perform action: @escaping (V) -> Void
    ) -> some View where V : Equatable
    

Deprecated

Use `onChange(of:initial:_:)` or `onChange(of:initial:_:)` instead. The
trailing closure in each case takes either zero or two input parameters,
compared to this method which takes one.

Be aware that the replacements have slightly different behvavior. This
modifier’s closure captures values that represent the state before the change.
The new modifiers capture values that correspond to the new state. The new
behavior makes it easier to perform updates that rely on values other than the
one that caused the modifier’s closure to run.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the
value associated with an `Environment` value or a `Binding`. For example, you
can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task:

The system passes the new value into the closure. If you need the old value,
capture it in the closure.

## See Also

### Input and events modifiers

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onTapGesture(count:coordinateSpace:perform:)

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

iOS 16.0–17.4  Deprecated  iPadOS 16.0–17.4  Deprecated  macOS 13.0–14.4
Deprecated  Mac Catalyst 16.0–17.4  Deprecated  watchOS 9.0–10.4  Deprecated
visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        coordinateSpace: CoordinateSpace = .local,
        perform action: @escaping (CGPoint) -> Void
    ) -> some View
    

Deprecated

Use `onTapGesture(count:coordinateSpace:perform:)` instead.

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`coordinateSpace`

    

The coordinate space in which to receive location values. Defaults to
`CoordinateSpace.local`.

`action`

    

The action to perform. This closure receives an input that indicates where the
interaction occurred.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the modified view `count` times. The action closure receives the location
of the interaction.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of
the circle based on the tap location.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)

Adds an action to perform when this view recognizes a long press gesture.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10,
        pressing: ((Bool) -> Void)? = nil,
        perform action: @escaping () -> Void
    ) -> some View
    

Deprecated

Use
`onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)`
instead.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onLongPressGesture(minimumDuration:pressing:perform:)

Adds an action to perform when this view recognizes a long press gesture.

tvOS 14.0–17.4  Deprecated

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        pressing: ((Bool) -> Void)? = nil,
        perform action: @escaping () -> Void
    ) -> some View
    

Deprecated

Use `onLongPressGesture(minimumDuration:perform:onPressingChanged:)` instead.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onPasteCommand(of:perform:)

Adds an action to perform in response to the system’s Paste command.

macOS 10.15–14.4  Deprecated

    
    
    func onPasteCommand(
        of supportedTypes: [String],
        perform payloadAction: @escaping ([NSItemProvider]) -> Void
    ) -> some View
    

Deprecated

Use `onPasteCommand(of:perform:)` instead.

##  Parameters

`supportedTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`payloadAction`

    

The action to perform when the Paste command triggers. The action closure’s
parameter contains items from the Clipboard with the types you specify in the
`supportedTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedTypes` parameter.
Place the higher priority types closer to the beginning of the array. The
Clipboard items that the `action` closure receives have the most preferred
type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `action` closure passes that rich
text along.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onPasteCommand(of:validator:perform:)

Adds an action to perform in response to the system’s Paste command with items
that you validate.

macOS 10.15–14.4  Deprecated

    
    
    func onPasteCommand<Payload>(
        of supportedTypes: [String],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        perform payloadAction: @escaping (Payload) -> Void
    ) -> some View
    

Deprecated

Use `onPasteCommand(of:validator:perform:)` instead.

##  Parameters

`supportedTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`validator`

    

A handler that validates the command. This handler receives items from the
Clipboard with the types you specify in the `supportedTypes` parameter. Use
this handler to decide whether the items are valid and preprocess them for the
`action` closure. If you return `nil` instead, the Paste command doesn’t
trigger.

`payloadAction`

    

The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked,
validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedTypes` parameter.
Place the higher priority types closer to the beginning of the array. The
Clipboard items that the `validator` closure receives have the most preferred
type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `validator` closure passes that
rich text along.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onDrop(of:delegate:)

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func onDrop(
        of supportedTypes: [String],
        delegate: any DropDelegate
    ) -> some View
    

Deprecated

Use `onDrop(of:delegate:)` instead.

##  Parameters

`supportedTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`delegate`

    

A type that conforms to the `DropDelegate` protocol. You have comprehensive
control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func onDrop(
        of supportedTypes: [String],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

Deprecated

Use `onDrop(of:isTargeted:perform:)` instead.

##  Parameters

`supportedTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The
parameter to `action` contains the dropped items, with types specified by
`supportedTypes`. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func onDrop(
        of supportedTypes: [String],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider], CGPoint) -> Bool
    ) -> some View
    

Deprecated

Use `onDrop(of:isTargeted:perform:)` instead.

##  Parameters

`supportedTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items, with types specified by
`supportedTypes`. The second parameter contains the drop location in this
view’s coordinate space. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# focusable(_:onFocusChange:)

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

macOS 10.15–12.0  Deprecated  tvOS 13.0–15.0  Deprecated  watchOS 6.0–8.0
Deprecated

    
    
    func focusable(
        _ isFocusable: Bool = true,
        onFocusChange: @escaping (Bool) -> Void = { _ in }
    ) -> some View
    

Deprecated

Use the `focusable(_:)` method instead.

##  Parameters

`isFocusable`

    

A Boolean value that indicates whether this view is focusable.

`onFocusChange`

    

A closure that’s called whenever this view either gains or loses focus. The
Boolean parameter to `onFocusChange` is `true` when the view is in focus;
otherwise, it’s `false`.

## Return Value

A view that sets whether a view is focusable, and triggers `onFocusChange`
when the view gains or loses focus.

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

Instance Method

# onContinuousHover(coordinateSpace:perform:)

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

iOS 16.0–17.4  Deprecated  iPadOS 16.0–17.4  Deprecated  macOS 13.0–14.4
Deprecated  Mac Catalyst 16.0–17.4  Deprecated  tvOS 16.0–17.4  Deprecated
visionOS 1.0+

    
    
    func onContinuousHover(
        coordinateSpace: CoordinateSpace = .local,
        perform action: @escaping (HoverPhase) -> Void
    ) -> some View
    

Deprecated

Use `onContinuousHover(coordinateSpace:perform:)` instead.

##  Parameters

`coordinateSpace`

    

The coordinate space for the location values. Defaults to
`CoordinateSpace.local`.

`action`

    

The action to perform whenever the pointer enters, moves within, or exits the
view’s bounds. The `action` closure passes the `HoverPhase.active(_:)` phase
with the pointer’s coordinates if the pointer is in the view’s bounds;
otherwise, it passes `HoverPhase.ended`.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the
view’s bounds.

## Discussion

Call this method to define a region for detecting pointer movement with the
size and position of this view. The following example updates `hoverLocation`
and `isHovering` to be based on the phase provided to the closure:

## See Also

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

Instance Method

# actionSheet(isPresented:content:)

Presents an action sheet when a given condition is true.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func actionSheet(
        isPresented: Binding<Bool>,
        content: () -> ActionSheet
    ) -> some View
    

Deprecated

Use `confirmationDialog(_:isPresented:titleVisibility:actions:message:)`
instead.

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the action
sheet that you create in the modifier’s `content` closure. When the user
presses or taps the sheet’s default action button the system sets this value
to `false` dismissing the sheet.

`content`

    

A closure returning the `ActionSheet` to present.

## Discussion

In the example below, a button conditionally presents an action sheet
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays an action sheet with both destructive
and default actions:

Note

In regular size classes in iOS, the system renders alert sheets as a popover
that the user dismisses by tapping anywhere outside the popover, rather than
displaying the default dismiss button.

## See Also

### View presentation modifiers

`func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some
View`

Presents an action sheet using the given item as a data source for the sheet’s
content.

Deprecated

`func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View`

Presents an alert to the user.

Deprecated

`func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some
View`

Presents an alert to the user.

Deprecated

Instance Method

# actionSheet(item:content:)

Presents an action sheet using the given item as a data source for the sheet’s
content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    func actionSheet<T>(
        item: Binding<T?>,
        content: (T) -> ActionSheet
    ) -> some View where T : Identifiable
    

Deprecated

Use
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

##  Parameters

`item`

    

A binding to an optional source of truth for the action sheet. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You use
this content to populate the fields of an action sheet that you create that
the system displays to the user. If `item` changes, the system dismisses the
currently displayed action sheet and replaces it with a new one using the same
process.

`content`

    

A closure returning the `ActionSheet` you create.

## Discussion

Use this method when you need to populate the fields of an action sheet with
content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the action sheet:

## See Also

### View presentation modifiers

`func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) ->
some View`

Presents an action sheet when a given condition is true.

Deprecated

`func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View`

Presents an alert to the user.

Deprecated

`func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some
View`

Presents an alert to the user.

Deprecated

Instance Method

# alert(isPresented:content:)

Presents an alert to the user.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func alert(
        isPresented: Binding<Bool>,
        content: () -> Alert
    ) -> some View
    

Deprecated

Use `alert(_:isPresented:actions:message:)` instead.

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert that
you create in the modifier’s `content` closure. When the user presses or taps
OK the system sets `isPresented` to `false` which dismisses the alert.

`content`

    

A closure returning the alert to present.

## Discussion

Use this method when you need to show an alert to the user. The example below
displays an alert that is shown when the user toggles a Boolean value that
controls the presentation of the alert:

## See Also

### View presentation modifiers

`func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) ->
some View`

Presents an action sheet when a given condition is true.

Deprecated

`func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some
View`

Presents an action sheet using the given item as a data source for the sheet’s
content.

Deprecated

`func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some
View`

Presents an alert to the user.

Deprecated

Instance Method

# alert(item:content:)

Presents an alert to the user.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func alert<Item>(
        item: Binding<Item?>,
        content: (Item) -> Alert
    ) -> some View where Item : Identifiable
    

Deprecated

Use `alert(_:isPresented:presenting:actions:message:)` instead.

##  Parameters

`item`

    

A binding to an optional source of truth for the alert. if `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You use
this content to populate the fields of an alert that you create that the
system displays to the user. If `item` changes, the system dismisses the
currently displayed alert and replaces it with a new one using the same
process.

`content`

    

A closure returning the alert to present.

## Discussion

Use this method when you need to show an alert that contains information from
a binding to an optional data source that you provide. The example below shows
a custom data source `FileInfo` whose properties configure the alert’s
`message` field:

## See Also

### View presentation modifiers

`func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) ->
some View`

Presents an action sheet when a given condition is true.

Deprecated

`func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some
View`

Presents an action sheet using the given item as a data source for the sheet’s
content.

Deprecated

`func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View`

Presents an alert to the user.

Deprecated

Instance Method

# searchable(text:placement:prompt:suggestions:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  tvOS 15.0–17.4  Deprecated
watchOS 8.0–10.4  Deprecated  visionOS 1.0+

    
    
    func searchable<S>(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder suggestions: () -> S
    ) -> some View where S : View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

Where the search field should attempt to be placed based on the containing
view hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`suggestions`

    

A view builder that produces content that populates a list of suggestions.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Search modifiers

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S, suggestions: () -> V) -> some View`

Marks this view as searchable, which configures the display of a search field.

Instance Method

# searchable(text:placement:prompt:suggestions:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  tvOS 15.0–17.4  Deprecated
watchOS 8.0–10.4  Deprecated  visionOS 1.0+

    
    
    func searchable<S>(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder suggestions: () -> S
    ) -> some View where S : View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

Where the search field should attempt to be placed based on the containing
view hierarchy.

`prompt`

    

A key for the localized prompt of the search field which provides users with
guidance on what to search for.

`suggestions`

    

A view builder that produces content that populates a list of suggestions.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Search modifiers

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S, suggestions: () -> V) -> some View`

Marks this view as searchable, which configures the display of a search field.

Instance Method

# searchable(text:placement:prompt:suggestions:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0–17.4  Deprecated  iPadOS 15.0–17.4  Deprecated  macOS 12.0–14.4
Deprecated  Mac Catalyst 15.0–17.4  Deprecated  tvOS 15.0–17.4  Deprecated
watchOS 8.0–10.4  Deprecated  visionOS 1.0+

    
    
    func searchable<V, S>(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S,
        @ViewBuilder suggestions: () -> V
    ) -> some View where V : View, S : StringProtocol
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

Where the search field should attempt to be placed based on the containing
view hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`suggestions`

    

A view builder that produces content that populates a list of suggestions.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Search modifiers

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.



# DisclosureGroupStyleConfiguration

Instance Property

# label

The label for the disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    let label: DisclosureGroupStyleConfiguration.Label

## See Also

### Configuring the label

`struct Label`

A type-erased label of a disclosure group.

Structure

# DisclosureGroupStyleConfiguration.Label

A type-erased label of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`let label: DisclosureGroupStyleConfiguration.Label`

The label for the disclosure group.

Instance Property

# content

The content of the disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    let content: DisclosureGroupStyleConfiguration.Content

## See Also

### Configuring the content

`struct Content`

A type-erased content of a disclosure group.

Structure

# DisclosureGroupStyleConfiguration.Content

A type-erased content of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the content

`let content: DisclosureGroupStyleConfiguration.Content`

The content of the disclosure group.

Instance Property

# isExpanded

A binding to a Boolean that indicates whether the disclosure group is
expanded.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @Binding
    var isExpanded: Bool { get nonmutating set }

## See Also

### Managing disclosure

`var $isExpanded: Binding<Bool>`

Instance Property

# $isExpanded

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var $isExpanded: Binding<Bool> { get }

## See Also

### Managing disclosure

`var isExpanded: Bool`

A binding to a Boolean that indicates whether the disclosure group is
expanded.



# DatePicker

Initializer

# init(selection:displayedComponents:label:)

Creates an instance that selects a `Date` with an unbounded range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker for any date

`init(LocalizedStringKey, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` within the given range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:displayedComponents:)

Creates an instance that selects a `Date` with an unbounded range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for any date

`init(selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` within the given range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:displayedComponents:)

Creates an instance that selects a `Date` within the given range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for any date

`init(selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker for a range

`init(LocalizedStringKey, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for a range

`init(selection: Binding<Date>, in: ClosedRange<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for a range

`init(selection: Binding<Date>, in: ClosedRange<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker with a start date

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeFrom<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with a start date

`init(selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with a start date

`init(selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeFrom<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker with an end date

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeThrough<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with an end date

`init(selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with an end date

`init(selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeThrough<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Type Alias

# DatePicker.Components

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    typealias Components = DatePickerComponents

## See Also

### Setting date picker components

`struct DatePickerComponents`

Structure

# DatePickerComponents

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DatePickerComponents

## Topics

### Getting date picker components

`static let date: DatePickerComponents`

Displays day, month, and year based on the locale

`static let hourAndMinute: DatePickerComponents`

Displays hour and minute components based on the locale

`static let hourMinuteAndSecond: DatePickerComponents`

Displays hour, minute and second components based on the locale

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Setting date picker components

`typealias Components`



# DynamicTypeSize

Case

# DynamicTypeSize.xSmall

An extra small size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case xSmall

## See Also

### Getting type sizes

`case small`

A small size.

`case medium`

A medium size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.small

A small size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case small

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case medium`

A medium size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.medium

A medium size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case medium

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.large

A large size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case large

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case medium`

A medium size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.xLarge

An extra large size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case xLarge

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case medium`

A medium size.

`case large`

A large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.xxLarge

An extra extra large size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case xxLarge

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case medium`

A medium size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxxLarge`

An extra extra extra large size.

Case

# DynamicTypeSize.xxxLarge

An extra extra extra large size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case xxxLarge

## See Also

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case medium`

A medium size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

Instance Property

# isAccessibilitySize

A Boolean value indicating whether the size is one that is associated with
accessibility.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isAccessibilitySize: Bool { get }

## See Also

### Getting accessibility type sizes

`case accessibility1`

The first accessibility size.

`case accessibility2`

The second accessibility size.

`case accessibility3`

The third accessibility size.

`case accessibility4`

The fourth accessibility size.

`case accessibility5`

The fifth accessibility size.

Initializer

# init(_:)

Create a Dynamic Type size from its `UIContentSizeCategory` equivalent.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  visionOS 1.0+

    
    
    init?(_ uiSizeCategory: UIContentSizeCategory)



# DefaultGaugeStyle

Initializer

# init()

Creates a default gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init()



# DragGesture.Value

Instance Property

# startLocation

The location of the drag gesture’s first event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var startLocation: CGPoint

## See Also

### Getting 2D position

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# location

The location of the drag gesture’s current event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var location: CGPoint

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# predictedEndLocation

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var predictedEndLocation: CGPoint { get }

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# translation

The total translation from the start of the drag gesture to the current event
of the drag gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var translation: CGSize { get }

## Discussion

This is equivalent to `location.{x,y} - startLocation.{x,y}`.

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# predictedEndTranslation

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var predictedEndTranslation: CGSize { get }

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

Instance Property

# startLocation3D

The 3D start location of the drag gesture.

visionOS 1.0+

    
    
    var startLocation3D: Point3D { get }

## See Also

### Getting 3D position

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# location3D

The 3D location of the drag gesture.

visionOS 1.0+

    
    
    var location3D: Point3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# predictedEndLocation3D

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

visionOS 1.0+

    
    
    var predictedEndLocation3D: Point3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# translation3D

The translation of the drag gesture from `startLocation3D` to `location3D`.

visionOS 1.0+

    
    
    var translation3D: Vector3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# predictedEndTranslation3D

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

visionOS 1.0+

    
    
    var predictedEndTranslation3D: Vector3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# startInputDevicePose3D

The starting 3D pose of the device driving the drag, if one exists.

visionOS 1.0+

    
    
    var startInputDevicePose3D: Pose3D? { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# inputDevicePose3D

The 3D pose of the device driving the drag, if one exists.

visionOS 1.0+

    
    
    var inputDevicePose3D: Pose3D? { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

Instance Property

# time

The time associated with the drag gesture’s current event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var time: Date

## See Also

### Handling changes over time

`var velocity: CGSize`

The current drag velocity.

Instance Property

# velocity

The current drag velocity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var velocity: CGSize { get }

## See Also

### Handling changes over time

`var time: Date`

The time associated with the drag gesture’s current event.



# DynamicMapContent Implementations

Instance Property

# data

The collection of underlying data.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    var data: Content.Data { get }

Available when `Content` conforms to `DynamicMapContent` and `Modifier`
conforms to `_MapContentModifier`.

Type Alias

# ModifiedContent.Data

The type of the underlying collection of data.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    typealias Data = Content.Data

Available when `Content` conforms to `DynamicMapContent` and `Modifier`
conforms to `_MapContentModifier`.



# DocumentConfiguration

Instance Property

# fileURL

A URL of an open document.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var fileURL: URL? { get }

## Discussion

If the document has never been saved, returns `nil`.

## See Also

### Getting configuration values

`var isEditable: Bool`

A Boolean value that indicates whether you can edit the document.

Instance Property

# isEditable

A Boolean value that indicates whether you can edit the document.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var isEditable: Bool { get }

## Discussion

On macOS, the document could be non-editable if the user lacks write
permissions, the parent directory or volume is read-only, or the document
couldn’t be autosaved.

On iOS, the document is not editable if there was an error reading or saving
it, there’s an unresolved conflict, the document is being uploaded or
downloaded, or otherwise, it is currently busy and unsafe for user edits.

## See Also

### Getting configuration values

`var fileURL: URL?`

A URL of an open document.



# DismissImmersiveSpaceAction

Instance Method

# callAsFunction()

Dismisses the currently opened immersive space.

visionOS 1.0+

    
    
    @MainActor
    func callAsFunction() async

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissImmersiveSpace` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.



# DragGesture

Initializer

# init(minimumDistance:coordinateSpace:)

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        minimumDistance: CGFloat = 10,
        coordinateSpace: some CoordinateSpaceProtocol = .local
    )

##  Parameters

`minimumDistance`

    

The minimum dragging distance for the gesture to succeed.

`coordinateSpace`

    

The coordinate space of the dragging gesture’s location.

## See Also

### Creating a drag gesture

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

Instance Property

# minimumDistance

The minimum dragging distance before the gesture succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var minimumDistance: CGFloat

## See Also

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

Instance Property

# coordinateSpace

The coordinate space in which to receive location values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var coordinateSpace: CoordinateSpace

## See Also

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

Initializer

# init(minimumDistance:coordinateSpace:)

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init(
        minimumDistance: CGFloat = 10,
        coordinateSpace: CoordinateSpace = .local
    )

Deprecated

Use `init(minimumDistance:coordinateSpace:)` instead.

##  Parameters

`minimumDistance`

    

The minimum dragging distance for the gesture to succeed.

`coordinateSpace`

    

The coordinate space of the dragging gesture’s location.

Structure

# DragGesture.Value

The attributes of a drag gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct Value

## Topics

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

### Handling changes over time

`var time: Date`

The time associated with the drag gesture’s current event.

`var velocity: CGSize`

The current drag velocity.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`



# DisclosureGroupStyle

Type Property

# automatic

A disclosure group style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticDisclosureGroupStyle { get }

Available when `Self` is `AutomaticDisclosureGroupStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the instance being created.

## Discussion

SwiftUI calls this method for each instance of `DisclosureGroup` that you
create within a view hierarchy where this style is the current
`DisclosureGroupStyle`.

## See Also

### Creating custom disclosure group styles

`struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`typealias Configuration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Structure

# DisclosureGroupStyleConfiguration

The properties of a disclosure group instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct DisclosureGroupStyleConfiguration

## Topics

### Configuring the label

`let label: DisclosureGroupStyleConfiguration.Label`

The label for the disclosure group.

`struct Label`

A type-erased label of a disclosure group.

### Configuring the content

`let content: DisclosureGroupStyleConfiguration.Content`

The content of the disclosure group.

`struct Content`

A type-erased content of a disclosure group.

### Managing disclosure

`var isExpanded: Bool`

A binding to a Boolean that indicates whether the disclosure group is
expanded.

`var $isExpanded: Binding<Bool>`

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` typealias Configuration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Type Alias

# DisclosureGroupStyle.Configuration

The properties of a disclosure group instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    typealias Configuration = DisclosureGroupStyleConfiguration

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

Associated Type

# Body

A view that represents the body of a disclosure group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`typealias Configuration`

The properties of a disclosure group instance.

Structure

# AutomaticDisclosureGroupStyle

A disclosure group style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct AutomaticDisclosureGroupStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the disclosure group style

`init()`

Creates an automatic disclosure group style.

## Relationships

### Conforms To

  * `DisclosureGroupStyle`



# DatePickerComponents

Type Property

# date

Displays day, month, and year based on the locale

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static let date: DatePickerComponents

## See Also

### Getting date picker components

`static let hourAndMinute: DatePickerComponents`

Displays hour and minute components based on the locale

`static let hourMinuteAndSecond: DatePickerComponents`

Displays hour, minute and second components based on the locale

Type Property

# hourAndMinute

Displays hour and minute components based on the locale

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static let hourAndMinute: DatePickerComponents

## See Also

### Getting date picker components

`static let date: DatePickerComponents`

Displays day, month, and year based on the locale

`static let hourMinuteAndSecond: DatePickerComponents`

Displays hour, minute and second components based on the locale

Type Property

# hourMinuteAndSecond

Displays hour, minute and second components based on the locale

watchOS 10.0+

    
    
    static let hourMinuteAndSecond: DatePickerComponents

## See Also

### Getting date picker components

`static let date: DatePickerComponents`

Displays day, month, and year based on the locale

`static let hourAndMinute: DatePickerComponents`

Displays hour and minute components based on the locale



# DisclosureGroup

Initializer

# init(_:content:)

Creates a disclosure group, using a provided string to create a text view for
the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ label: S,
        @ViewBuilder content: @escaping () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`label`

    

A description of the content of the disclosure group.

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: @escaping () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the localized label of `self` that describes the content of the
disclosure group.

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:isExpanded:content:)

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the localized label of `self` that describes the content of the
disclosure group.

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:isExpanded:content:)

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ label: S,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`label`

    

A description of the content of the disclosure group.

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a disclosure group with the given label and content views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: @escaping () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

The content shown when the disclosure group expands.

`label`

    

A view that describes the content of the disclosure group.

## See Also

### Creating a group with a label view

`init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

Initializer

# init(isExpanded:content:label:)

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

`label`

    

A view that describes the content of the disclosure group.

## See Also

### Creating a group with a label view

`init(content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views.



# DefaultGroupBoxStyle

Initializer

# init()

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init()



# DefaultDatePickerStyle

Initializer

# init()

Creates an instance of the default date picker style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init()



# DigitalCrownRotationalSensitivity

Case

# DigitalCrownRotationalSensitivity.low

Low sensitivity.

watchOS 6.0+

    
    
    case low

## See Also

### Getting sensitivity options

`case medium`

Medium sensitivity.

`case high`

High sensitivity.

Case

# DigitalCrownRotationalSensitivity.medium

Medium sensitivity.

watchOS 6.0+

    
    
    case medium

## See Also

### Getting sensitivity options

`case low`

Low sensitivity.

`case high`

High sensitivity.

Case

# DigitalCrownRotationalSensitivity.high

High sensitivity.

watchOS 6.0+

    
    
    case high

## See Also

### Getting sensitivity options

`case low`

Low sensitivity.

`case medium`

Medium sensitivity.



# DisclosureTableRow

Initializer

# init(_:isExpanded:content:)

Creates a disclosure group with the given value and table rows, and a binding
to the expansion state (expanded or collapsed).

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<Value>(
        _ value: Value,
        isExpanded: Binding<Bool>? = nil,
        @TableRowBuilder<Value> content: @escaping () -> Content
    ) where Label == TableRow<Value>, Value == Content.TableRowValue

##  Parameters

`value`

    

The value of the disclosable table row.

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The table row shown when the disclosure group expands.



# DigitalCrownEvent

Instance Property

# offset

The offset of the digital crown when this event was sent.

watchOS 9.0+

    
    
    var offset: Double

## See Also

### Getting events

`var velocity: Double`

The velocity at which the offset was changing when this event was sent.

Instance Property

# velocity

The velocity at which the offset was changing when this event was sent.

watchOS 9.0+

    
    
    var velocity: Double

## See Also

### Getting events

`var offset: Double`

The offset of the digital crown when this event was sent.



# DefaultButtonStyle

Initializer

# init()

Creates a default button style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func makeBody(configuration: DefaultButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



# Drawing and graphics

Structure

# Canvas

A view type that supports immediate mode drawing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Canvas<Symbols> where Symbols : View

## Overview

Use a canvas to draw rich and dynamic 2D graphics inside a SwiftUI view. The
canvas passes a `GraphicsContext` to the closure that you use to perform
immediate mode drawing operations. The canvas also passes a `CGSize` value
that you can use to customize what you draw. For example, you can use the
context’s `stroke(_:with:lineWidth:)` command to draw a `Path` instance:

The example above draws the outline of an ellipse that exactly inscribes a
canvas with a blue border:

In addition to outlined and filled paths, you can draw images, text, and
complete SwiftUI views. To draw views, use the
`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)` method to
supply views that you can reference from inside the renderer. You can also add
masks, apply filters, perform transforms, control blending, and more. For
information about how to draw, see `GraphicsContext`.

A canvas doesn’t offer interactivity or accessibility for individual elements,
including for views that you pass in as symbols. However, it might provide
better performance for a complex drawing that involves dynamic data. Use a
canvas to improve performance for a drawing that doesn’t primarily involve
text or require interactive elements.

## Topics

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void)`

Creates and configures a canvas.

Available when `Symbols` is `EmptyView`.

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () ->
Symbols)`

Creates and configures a canvas that you supply with renderable child views.

### Managing opacity and color

`var isOpaque: Bool`

A Boolean that indicates whether the canvas is fully opaque.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the canvas.

### Referencing symbols

`var symbols: Symbols`

A view that provides child views that you can use in the drawing callback.

### Rendering

`var rendersAsynchronously: Bool`

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.

`var renderer: (inout GraphicsContext, CGSize) -> Void`

The drawing callback that you use to draw into the canvas.

## Relationships

### Conforms To

  * `View`

Conforms when `Symbols` conforms to `View`.

## See Also

### Immediate mode drawing

Add Rich Graphics to Your SwiftUI App

Make your apps stand out by adding background materials, vibrancy, custom
graphics, and animations.

`struct GraphicsContext`

An immediate mode drawing destination, and its current state.

Structure

# GraphicsContext

An immediate mode drawing destination, and its current state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct GraphicsContext

## Overview

Use a context to execute 2D drawing primitives. For example, you can draw
filled shapes using the `fill(_:with:style:)` method inside a `Canvas` view:

The example above draws an ellipse that just fits inside a canvas that’s
constrained to 300 points wide and 200 points tall:

In addition to outlining or filling paths, you can draw images, text, and
SwiftUI views. You can also use the context to perform many common graphical
operations, like adding masks, applying filters and transforms, and setting a
blend mode. For example you can add a mask using the `clip(to:style:options:)`
method:

The rectangular mask hides all but one quadrant of the ellipse:

The order of operations matters. Changes that you make to the state of the
context, like adding a mask or a filter, apply to later drawing operations. If
you reverse the fill and clip operations in the example above, so that the
fill comes first, the mask doesn’t affect the ellipse.

Each context references a particular layer in a tree of transparency layers,
and also contains a full copy of the drawing state. You can modify the state
of one context without affecting the state of any other, even if they refer to
the same layer. For example you can draw the masked ellipse from the previous
example into a copy of the main context, and then add a rectangle into the
main context:

The mask doesn’t clip the rectangle because the mask isn’t part of the main
context. However, both contexts draw into the same view because you created
one context as a copy of the other:

The context has access to an `EnvironmentValues` instance called `environment`
that’s initially copied from the environment of its enclosing view. SwiftUI
uses environment values — like the display resolution and color scheme — to
resolve types like `Image` and `Color` that appear in the context. You can
also access values stored in the environment for your own purposes.

## Topics

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

`struct GradientOptions`

Options that affect the rendering of color gradients.

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedImage`

An image resolved to a particular environment.

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedText`

A text view resolved to a particular environment.

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, at: CGPoint, anchor: UnitPoint)`

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

`func draw(GraphicsContext.ResolvedSymbol, in: CGRect)`

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

`func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?`

Gets the identified child view as a resolved symbol, if the view exists.

`struct ResolvedSymbol`

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

### Drawing into a new layer

`func drawLayer(content: (inout GraphicsContext) throws -> Void) rethrows`

Draws a new layer, created by drawing code that you provide, into the context.

### Masking

`func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)`

Adds a path to the context’s array of clip shapes.

`func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions,
content: (inout GraphicsContext) throws -> Void) rethrows`

Adds a clip shape that you define in a new layer to the context’s array of
clip shapes.

`var clipBoundingRect: CGRect`

The bounding rectangle of the intersection of all current clip shapes in the
current user space.

`struct ClipOptions`

Options that affect the use of clip shapes.

### Setting opacity and the blend mode

`var opacity: Double`

The opacity of drawing operations in the context.

`var blendMode: GraphicsContext.BlendMode`

The blend mode used by drawing operations in the context.

`struct BlendMode`

The ways that a graphics context combines new content with background content.

### Filtering

`func addFilter(GraphicsContext.Filter, options:
GraphicsContext.FilterOptions)`

Adds a filter that applies to subsequent drawing operations.

`struct Filter`

A type that applies image processing operations to rendered content.

`struct FilterOptions`

Options that configure a filter that you add to a graphics context.

`struct BlurOptions`

Options that configure the graphics context filter that creates blur.

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

### Drawing with a core graphics context

`func withCGContext(content: (CGContext) throws -> Void) rethrows`

Provides a Core Graphics context that you can use as a proxy to draw into this
context.

### Accessing the environment

`var environment: EnvironmentValues`

The environment associated with the graphics context.

## See Also

### Immediate mode drawing

Add Rich Graphics to Your SwiftUI App

Make your apps stand out by adding background materials, vibrancy, custom
graphics, and animations.

`struct Canvas`

A view type that supports immediate mode drawing.

Instance Method

# tint(_:)

Sets the tint within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tint<S>(_ tint: S?) -> some View where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

Use this method to override the default accent color for this view with a
given styling. Unlike an app’s accent color, which can be overridden by user
preference, tint is always respected and should be used as a way to provide
additional meaning to the control.

Controls which are unable to style themselves using the given type of
`ShapeStyle` will try to approximate the styling as best as they can (i.e.
controls which can not style themselves using a gradient will attempt to use
the color of the gradient’s first stop).

This example shows a linear dashboard styled gauge tinted with a gradient from
`green` to `red`.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint(Color?) -> some View`

Sets the tint color within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# tint(_:)

Sets the tint color within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func tint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The tint `Color` to apply.

## Discussion

Use this method to override the default accent color for this view. Unlike an
app’s accent color, which can be overridden by user preference, the tint color
is always respected and should be used as a way to provide additional meaning
to the control.

This example shows Answer and Decline buttons with `green` and `red` tint
colors, respectively.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`struct Color`

A representation of a color that adapts to a given context.

Structure

# Color

A representation of a color that adapts to a given context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Color

## Overview

You can create a color in one of several ways:

  * Load a color from an Asset Catalog:

  * Specify component values, like red, green, and blue; hue, saturation, and brightness; or white level:

  * Create a color instance from another color, like a `UIColor` or an `NSColor`:

  * Use one of a palette of predefined colors, like `black`, `green`, and `purple`.

Some view modifiers can take a color as an argument. For example,
`foregroundStyle(_:)` uses the color you provide to set the foreground color
for view elements, like text or SF Symbols:

Because SwiftUI treats colors as `View` instances, you can also directly add
them to a view hierarchy. For example, you can layer a rectangle beneath a sun
image using colors defined above:

A color used as a view expands to fill all the space it’s given, as defined by
the frame of the enclosing `ZStack` in the above example:

SwiftUI only resolves a color to a concrete value just before using it in a
given environment. This enables a context-dependent appearance for system
defined colors, or those that you load from an Asset Catalog. For example, a
color can have distinct light and dark variants that the system chooses from
at render time.

## Topics

### Creating a color from an asset

`init(String, bundle: Bundle?)`

Creates a color from a color set that you indicate by name.

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

### Creating a color from a color resource

`init(ColorResource)`

Initialize a `Color` with a color resource.

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let primary: Color`

The color to use for primary content.

`static let secondary: Color`

The color to use for secondary content.

### Modifying a color

`func opacity(Double) -> Color`

Multiplies the opacity of the color by the given amount.

`var gradient: AnyGradient`

Returns the standard gradient for the color `self`.

### Describing a color

`var description: String`

A textual representation of the color.

### Comparing colors

`static func == (Color, Color) -> Bool`

Indicates whether two colors are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the color by feeding them into the given
hash function.

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

### Default Implementations

API Reference

ShapeStyle Implementations

API Reference

Transferable Implementations

## Relationships

### Conforms To

  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `Sendable`
  * `ShapeStyle`
  * `Transferable`
  * `View`

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`func tint(Color?) -> some View`

Sets the tint color within this view.

Instance Method

# border(_:width:)

Adds a border to this view with the specified style and width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func border<S>(
        _ content: S,
        width: CGFloat = 1
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

A value that conforms to the `ShapeStyle` protocol, like a `Color` or
`HierarchicalShapeStyle`, that SwiftUI uses to fill the border.

`width`

    

The thickness of the border. The default is 1 pixel.

## Return Value

A view that adds a border with the specified style and width to this view.

## Discussion

Use this modifier to draw a border of a specified width around the view’s
frame. By default, the border appears inside the bounds of this view. For
example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same
width before adding the border:

## See Also

### Styling content

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:)

Sets a view’s foreground elements to use a given style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The color or pattern to use when filling in the foreground elements. To
indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or one
of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`. To
set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

## Return Value

A view that uses the given foreground style.

## Discussion

Use this method to style foreground content like text, shapes, and template
images (including symbols):

The example above creates a row of `teal` foreground elements:

You can use any style that conforms to the `ShapeStyle` protocol, like the
`teal` color in the example above, or the
`linearGradient(colors:startPoint:endPoint:)` gradient shown below:

Tip

If you want to fill a single `Shape` instance with a style, use the
`fill(style:)` shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a
`Color` that you load from an asset catalog can have different light and dark
appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a
style of their own, but instead modify other styles. In particular, they
modify the primary level of the current foreground style to the degree given
by the hierarchical style’s name. To find the current foreground style to
modify, SwiftUI looks for the innermost containing style that you apply with
the `foregroundStyle(_:)` or the `foregroundColor(_:)` modifier. If you
haven’t specified a style, SwiftUI uses the default foreground style, as in
the following example:

If you add a foreground style on the enclosing `VStack`, the hierarchical
styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect
for foreground elements in that view, or in any of its child views, that it
would otherwise gain from adding a background material — for example, using
the `background(_:ignoresSafeAreaEdges:)` modifier. However, hierarchical
styles applied to the default foreground don’t disable vibrancy.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:)

Sets the primary and secondary levels of the foreground style in the child
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2>(
        _ primary: S1,
        _ secondary: S2
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:_:)

Sets the primary, secondary, and tertiary levels of the foreground style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2, S3>(
        _ primary: S1,
        _ secondary: S2,
        _ tertiary: S3
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

`tertiary`

    

The tertiary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# backgroundStyle(_:)

Sets the specified style to render backgrounds within the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

## Discussion

The following example uses this modifier to set the `backgroundStyle`
environment value to a `blue` color that includes a subtle `gradient`. SwiftUI
fills the `Circle` shape that acts as a background element with this style:

To restore the default background style, set the `backgroundStyle` environment
value to `nil` using the `environment(_:_:)` modifer:

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Property

# backgroundStyle

An optional style that overrides the default system background style when set.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var backgroundStyle: AnyShapeStyle? { get set }

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Protocol

# ShapeStyle

A color or pattern to use when rendering a shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ShapeStyle : Sendable

## Overview

You create custom shape styles by declaring a type that conforms to the
`ShapeStyle` protocol and implementing the required `resolve` function to
return a shape style that represents the desired appearance based on the
current environment.

For example this shape style reads the current color scheme from the
environment to choose the blend mode its color will be composited with:

In addition to creating a custom shape style, you can also use one of the
concrete styles that SwiftUI defines. To indicate a specific color or pattern,
you can use `Color` or the style returned by `image(_:sourceRect:scale:)`, or
one of the gradient types, like the one returned by
`radialGradient(_:center:startRadius:endRadius:)`. To set a color that’s
appropriate for a given context on a given platform, use one of the semantic
styles, like `background` or `primary`.

You can use a shape style by:

  * Filling a shape with a style with the `fill(_:style:)` modifier:

  * Tracing the outline of a shape with a style with either the `stroke(_:lineWidth:)` or the `stroke(_:style:)` modifier:

  * Styling the foreground elements in a view with the `foregroundStyle(_:)` modifier:

## Topics

### System colors

`static var black: Color`

A black color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var blue: Color`

A context-dependent blue color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var brown: Color`

A context-dependent brown color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var clear: Color`

A clear color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var gray: Color`

A context-dependent gray color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var green: Color`

A context-dependent green color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var mint: Color`

A context-dependent mint color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var orange: Color`

A context-dependent orange color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var pink: Color`

A context-dependent pink color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var purple: Color`

A context-dependent purple color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var red: Color`

A context-dependent red color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var teal: Color`

A context-dependent teal color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var white: Color`

A white color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Available when `Self` is `Color`.

### Angular gradients

`static func angularGradient(Gradient, center: UnitPoint, startAngle: Angle,
endAngle: Angle) -> AngularGradient`

An angular gradient, which applies the color function as the angle changes
between the start and end angles, and anchored to a relative center point
within the filled shape.

Available when `Self` is `AngularGradient`.

`static func angularGradient(AnyGradient, center: UnitPoint, startAngle:
Angle, endAngle: Angle) -> some ShapeStyle`

An angular gradient, which applies the color function as the angle changes
between the start and end angles, and anchored to a relative center point
within the filled shape.

Available when `Self` is `AngularGradient`.

`static func angularGradient(colors: [Color], center: UnitPoint, startAngle:
Angle, endAngle: Angle) -> AngularGradient`

An angular gradient defined by a collection of colors.

Available when `Self` is `AngularGradient`.

`static func angularGradient(stops: [Gradient.Stop], center: UnitPoint,
startAngle: Angle, endAngle: Angle) -> AngularGradient`

An angular gradient defined by a collection of color stops.

Available when `Self` is `AngularGradient`.

### Conic gradients

`static func conicGradient(Gradient, center: UnitPoint, angle: Angle) ->
AngularGradient`

A conic gradient that completes a full turn, optionally starting from a given
angle and anchored to a relative center point within the filled shape.

Available when `Self` is `AngularGradient`.

`static func conicGradient(AnyGradient, center: UnitPoint, angle: Angle) ->
some ShapeStyle`

A conic gradient that completes a full turn, optionally starting from a given
angle and anchored to a relative center point within the filled shape.

Available when `Self` is `AngularGradient`.

`static func conicGradient(colors: [Color], center: UnitPoint, angle: Angle)
-> AngularGradient`

A conic gradient defined by a collection of colors that completes a full turn.

Available when `Self` is `AngularGradient`.

`static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle:
Angle) -> AngularGradient`

A conic gradient defined by a collection of color stops that completes a full
turn.

Available when `Self` is `AngularGradient`.

### Elliptical gradients

`static func ellipticalGradient(Gradient, center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(AnyGradient, center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> some ShapeStyle`

A radial gradient that draws an ellipse.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(colors: [Color], center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse defined by a collection of colors.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(stops: [Gradient.Stop], center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse defined by a collection of color
stops.

Available when `Self` is `EllipticalGradient`.

### Linear gradients

`static func linearGradient(Gradient, startPoint: UnitPoint, endPoint:
UnitPoint) -> LinearGradient`

A linear gradient.

Available when `Self` is `LinearGradient`.

`static func linearGradient(AnyGradient, startPoint: UnitPoint, endPoint:
UnitPoint) -> some ShapeStyle`

A linear gradient.

Available when `Self` is `LinearGradient`.

`static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint:
UnitPoint) -> LinearGradient`

A linear gradient defined by a collection of colors.

Available when `Self` is `LinearGradient`.

`static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint,
endPoint: UnitPoint) -> LinearGradient`

A linear gradient defined by a collection of color stops.

Available when `Self` is `LinearGradient`.

### Radial gradients

`static func radialGradient(Gradient, center: UnitPoint, startRadius: CGFloat,
endRadius: CGFloat) -> RadialGradient`

A radial gradient.

Available when `Self` is `RadialGradient`.

`static func radialGradient(AnyGradient, center: UnitPoint, startRadius:
CGFloat, endRadius: CGFloat) -> some ShapeStyle`

A radial gradient.

Available when `Self` is `RadialGradient`.

`static func radialGradient(colors: [Color], center: UnitPoint, startRadius:
CGFloat, endRadius: CGFloat) -> RadialGradient`

A radial gradient defined by a collection of colors.

Available when `Self` is `RadialGradient`.

`static func radialGradient(stops: [Gradient.Stop], center: UnitPoint,
startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient`

A radial gradient defined by a collection of color stops.

Available when `Self` is `RadialGradient`.

### Materials

`static var ultraThinMaterial: Material`

A mostly translucent material.

Available when `Self` is `Material`.

`static var thinMaterial: Material`

A material that’s more translucent than opaque.

Available when `Self` is `Material`.

`static var regularMaterial: Material`

A material that’s somewhat translucent.

Available when `Self` is `Material`.

`static var thickMaterial: Material`

A material that’s more opaque than translucent.

Available when `Self` is `Material`.

`static var ultraThickMaterial: Material`

A mostly opaque material.

Available when `Self` is `Material`.

`static var bar: Material`

A material matching the style of system toolbars.

Available when `Self` is `Material`.

### Image paint styles

`static func image(Image, sourceRect: CGRect, scale: CGFloat) -> ImagePaint`

A shape style that fills a shape by repeating a region of an image.

Available when `Self` is `ImagePaint`.

### Hierarchical styles

`var secondary: some ShapeStyle`

Returns the second level of this shape style.

`var tertiary: some ShapeStyle`

Returns the third level of this shape style.

`var quaternary: some ShapeStyle`

Returns the fourth level of this shape style.

`var quinary: some ShapeStyle`

Returns the fifth level of this shape style.

`static var primary: HierarchicalShapeStyle`

A shape style that maps to the first level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var secondary: HierarchicalShapeStyle`

A shape style that maps to the second level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var tertiary: HierarchicalShapeStyle`

A shape style that maps to the third level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var quaternary: HierarchicalShapeStyle`

A shape style that maps to the fourth level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var quinary: HierarchicalShapeStyle`

A shape style that maps to the fifth level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

### Semantic styles

`static var foreground: ForegroundStyle`

The foreground style in the current context.

Available when `Self` is `ForegroundStyle`.

`static var background: BackgroundStyle`

The background style in the current context.

Available when `Self` is `BackgroundStyle`.

`static var selection: SelectionShapeStyle`

A style used to visually indicate selection following platform conventional
colors and behaviors.

Available when `Self` is `SelectionShapeStyle`.

`static var separator: SeparatorShapeStyle`

A style appropriate for foreground separator or border lines.

Available when `Self` is `SeparatorShapeStyle`.

`static var tint: TintShapeStyle`

A style that reflects the current tint color.

Available when `Self` is `TintShapeStyle`.

`static var placeholder: PlaceholderTextShapeStyle`

A style appropriate for placeholder text.

Available when `Self` is `PlaceholderTextShapeStyle`.

`static var link: LinkShapeStyle`

A style appropriate for links.

Available when `Self` is `LinkShapeStyle`.

`static var fill: FillShapeStyle`

An overlay fill style for filling shapes.

Available when `Self` is `FillShapeStyle`.

`static var windowBackground: WindowBackgroundShapeStyle`

A style appropriate for elements that should match the background of their
containing window.

Available when `Self` is `WindowBackgroundShapeStyle`.

### Modifying a shape style

`func blendMode(BlendMode) -> some ShapeStyle`

Returns a new style based on `self` that applies the specified blend mode when
drawing.

`func opacity(Double) -> some ShapeStyle`

Returns a new style based on `self` that multiplies by the specified opacity
when drawing.

`func shadow(ShadowStyle) -> some ShapeStyle`

Applies the specified shadow effect to the shape style.

### Configuring the default shape style

`static func blendMode(BlendMode) -> some ShapeStyle`

Returns a new style based on the current style that uses `mode` as its blend
mode when drawing.

Available when `Self` is `AnyShapeStyle`.

`static func opacity(Double) -> some ShapeStyle`

Returns a new style based on the current style that multiplies by `opacity`
when drawing.

Available when `Self` is `AnyShapeStyle`.

`static func shadow(ShadowStyle) -> some ShapeStyle`

Returns a shape style that applies the specified shadow style to the current
style.

Available when `Self` is `AnyShapeStyle`.

### Mapping to absolute coordinates

`func `in`(CGRect) -> some ShapeStyle`

Maps a shape style’s unit-space coordinates to the absolute coordinates of a
given rectangle.

### Resolving a shape style in an environment

`func resolve(in: EnvironmentValues) -> Self.Resolved`

Evaluate to a resolved shape style given the current `environment`.

**Required** Default implementation provided.

`associatedtype Resolved : ShapeStyle = Never`

The type of shape style this will resolve to.

**Required**

### Using a shape style as a view

`var body: _ShapeView<Rectangle, Self>`

A rectangular view that’s filled with the shape style.

Available when `Self` conforms to `View` and `Body` is `_ShapeView<Rectangle,
Self>`.

### Supporting types

Construct instances of these styles using the properties and methods of the
shape style protocol.

`struct AngularGradient`

An angular gradient.

`struct EllipticalGradient`

A radial gradient that draws an ellipse.

`struct LinearGradient`

A linear gradient.

`struct RadialGradient`

A radial gradient.

`struct Material`

A background material type.

`struct ImagePaint`

A shape style that fills a shape by repeating a region of an image.

`struct HierarchicalShapeStyle`

A shape style that maps to one of the numbered content styles.

`struct HierarchicalShapeStyleModifier`

Styles that you can apply to hierarchical shapes.

`struct ForegroundStyle`

The foreground style in the current context.

`struct BackgroundStyle`

The background style in the current context.

`struct SelectionShapeStyle`

A style used to visually indicate selection following platform conventional
colors and behaviors.

`struct SeparatorShapeStyle`

A style appropriate for foreground separator or border lines.

`struct TintShapeStyle`

A style that reflects the current tint color.

`struct FillShapeStyle`

A shape style that displays one of the overlay fills.

`struct LinkShapeStyle`

A style appropriate for links.

`struct PlaceholderTextShapeStyle`

A style appropriate for placeholder text.

`struct WindowBackgroundShapeStyle`

A style appropriate for elements that should match the background of their
containing window.

## Relationships

### Inherits From

  * `Sendable`

### Conforming Types

  * `AngularGradient`
  * `AnyGradient`
  * `AnyShapeStyle`
  * `BackgroundStyle`
  * `Color`
  * `Color.Resolved`
  * `EllipticalGradient`
  * `FillShapeStyle`
  * `ForegroundStyle`
  * `Gradient`
  * `HierarchicalShapeStyle`
  * `HierarchicalShapeStyleModifier`
  * `ImagePaint`
  * `LinearGradient`
  * `LinkShapeStyle`
  * `Material`
  * `PlaceholderTextShapeStyle`
  * `RadialGradient`
  * `SelectionShapeStyle`
  * `SeparatorShapeStyle`
  * `Shader`
  * `TintShapeStyle`
  * `WindowBackgroundShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# AnyShapeStyle

A type-erased ShapeStyle value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyShapeStyle

## Topics

### Creating a shape style

`init<S>(S)`

Create an instance from `style`.

## Relationships

### Conforms To

  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# Gradient

A color gradient represented as an array of color stops, each having a
parametric location value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Gradient

## Topics

### Creating a gradient from colors

`init(colors: [Color])`

Creates a gradient from an array of colors.

### Creating a gradient from stops

`init(stops: [Gradient.Stop])`

Creates a gradient from an array of color stops.

`var stops: [Gradient.Stop]`

The array of color stops.

`struct Stop`

One color stop in the gradient.

### Working with color spaces

`func colorSpace(Gradient.ColorSpace) -> AnyGradient`

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

`struct ColorSpace`

A method of interpolating between the colors in a gradient.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `ScaleRange`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# AnyGradient

A color gradient.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyGradient

## Overview

When used as a `ShapeStyle`, this type draws a linear gradient with start-
point [0.5, 0] and end-point [0.5, 1].

## Topics

### Creating a gradient

`init(Gradient)`

Creates a new instance from the specified gradient.

### Working with color spaces

`func colorSpace(Gradient.ColorSpace) -> AnyGradient`

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `ScaleRange`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# ShadowStyle

A style to use when rendering shadows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ShadowStyle

## Topics

### Getting shadow styles

`static func drop(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) ->
ShadowStyle`

Creates a custom drop shadow style.

`static func inner(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) ->
ShadowStyle`

Creates a custom inner shadow style.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

Instance Method

# brightness(_:)

Brightens this view by the specified amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func brightness(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

A value between 0 (no effect) and 1 (full white brightening) that represents
the intensity of the brightness effect.

## Return Value

A view that brightens this view by the specified amount.

## Discussion

Use `brightness(_:)` to brighten the intensity of the colors in a view. The
example below shows a series of red squares, with their brightness increasing
from 0 (fully red) to 100% (white) in 20% increments.

## See Also

### Transforming colors

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# contrast(_:)

Sets the contrast and separation between similar colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contrast(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of color contrast to apply. negative values invert colors in
addition to applying contrast.

## Return Value

A view that applies color contrast to this view.

## Discussion

Apply contrast to a view to increase or decrease the separation between
similar colors in the view.

In the example below, the `contrast(_:)` modifier is applied to a set of red
squares each containing a contrasting green inner circle. At each step in the
loop, the `contrast(_:)` modifier changes the contrast of the circle/square
view in 20% increments. This ranges from -20% contrast (yielding inverted
colors — turning the red square to pale-green and the green circle to mauve),
to neutral-gray at 0%, to 100% contrast (bright-red square / bright-green
circle). Applying negative contrast values, as shown in the -20% square, will
apply contrast in addition to inverting colors.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorInvert()

Inverts the colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorInvert() -> some View
    

## Return Value

A view that inverts its colors.

## Discussion

The `colorInvert()` modifier inverts all of the colors in a view so that each
color displays as its complementary color. For example, blue converts to
yellow, and white converts to black.

In the example below, two red squares each have an interior green circle. The
inverted square shows the effect of the square’s colors: complimentary colors
for red and green — teal and purple.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorMultiply(_:)

Adds a color multiplication effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorMultiply(_ color: Color) -> some View
    

##  Parameters

`color`

    

The color to bias this view toward.

## Return Value

A view with a color multiplication effect.

## Discussion

The following example shows two versions of the same image side by side; at
left is the original, and at right is a duplicate with the `colorMultiply(_:)`
modifier applied with `purple`.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# saturation(_:)

Adjusts the color saturation of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func saturation(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The amount of saturation to apply to this view.

## Return Value

A view that adjusts the saturation of this view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a
view.

The example below shows a series of red squares with their saturation
increasing from 0 (gray) to 100% (fully-red) in 20% increments:

See Also

`contrast(_:)`

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# grayscale(_:)

Adds a grayscale effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func grayscale(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer
to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

A view that adds a grayscale effect to this view.

## Discussion

A grayscale effect reduces the intensity of colors in this view.

The example below shows a series of red squares with their grayscale effect
increasing from 0 (reddest) to 99% (fully desaturated) in approximate 20%
increments:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# hueRotation(_:)

Applies a hue rotation effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hueRotation(_ angle: Angle) -> some View
    

##  Parameters

`angle`

    

The hue rotation angle to apply to the colors in this view.

## Return Value

A view that applies a hue rotation effect to this view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the
angle you specify.

The example below shows a series of squares filled with a linear gradient.
Each square shows the effect of a 36˚ hueRotation (a total of 180˚ across the
5 squares) on the gradient:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# luminanceToAlpha()

Adds a luminance to alpha effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func luminanceToAlpha() -> some View
    

## Return Value

A view with the luminance to alpha effect applied.

## Discussion

Use this modifier to create a semitransparent mask, with the opacity of each
part of the modified view controlled by the luminance of the corresponding
part of the original view. Regions of lower luminance become more transparent,
while higher luminance yields greater opacity.

In particular, the modifier maps the red, green, and blue components of each
input pixel’s color to a grayscale value, and that value becomes the alpha
component of a black pixel in the output. This modifier produces an effect
that’s equivalent to using the `feColorMatrix` filter primitive with the
`luminanceToAlpha` type attribute, as defined by the Scalable Vector Graphics
(SVG) 2 specification.

The example below defines a `Palette` view as a series of rectangles, each
composed as a `Color` with a particular white value, and then displays two
versions of the palette over a blue background:

The unmodified version of the palette contains rectangles that range from
solid black to solid white, thus with increasing luminance. The second version
of the palette, which has the `luminanceToAlpha()` modifier applied, allows
the background to show through in an amount that corresponds inversely to the
luminance of the input.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

Instance Method

# scaledToFill()

Scales this view to fill its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFill() -> some View
    

## Return Value

A view that scales this view to fill its parent, maintaining this view’s
aspect ratio.

## Discussion

Use `scaledToFill()` to scale this view to fill its parent, while maintaining
the view’s aspect ratio as the view scales:

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fill`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaledToFit()

Scales this view to fit its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFit() -> some View
    

## Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect
ratio.

## Discussion

Use `scaledToFit()` to scale this view to fit its parent, while maintaining
the view’s aspect ratio as the view scales.

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fit`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGSize,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`scale`

    

A `CGSize` that represents the horizontal and vertical amount to scale the
view.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Discussion

Use `scaleEffect(_:anchor:)` to scale a view by applying a scaling transform
of a specific size, specified by `scale`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified factor.

visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`s`

    

The scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified size in each dimension.

visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: Size3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`scale`

    

The scale factor for this view in each dimension.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> ModifiedContent<Self, _UniformScaleEffect>

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:anchor:)

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`x`

    

An amount that represents the horizontal amount to scale the view. The default
value is `1.0`.

`y`

    

An amount that represents the vertical amount to scale the view. The default
value is `1.0`.

`anchor`

    

The anchor point that indicates the starting position for the scale operation.

## Discussion

Use `scaleEffect(x:y:anchor:)` to apply a scaling transform to a view by a
specific horizontal and vertical amount.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:z:anchor:)

Scales this view by the specified horizontal, vertical, and depth factors.

visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        z: CGFloat = 1.0,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`x`

    

The horizontal scale factor for this view.

`y`

    

The vertical scale factor for this view.

`z`

    

The depth scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the specified aspect ratio.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGFloat? = nil,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

The ratio of width to height to use for the resulting view. Use `nil` to
maintain the current aspect ratio in the resulting view.

`contentMode`

    

A flag that indicates whether this view fits or fills the parent context.

## Return Value

A view that constrains this view’s dimensions to the aspect ratio of the given
size using `contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGFloat` using the specified content mode.

If this view is resizable, the resulting view will have `aspectRatio` as its
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fit its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the aspect ratio of the given size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGSize,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

A size that specifies the ratio of width to height to use for the resulting
view.

`contentMode`

    

A flag indicating whether this view should fit or fill the parent context.

## Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using
`contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGSize`.

If this view is resizable, the resulting view uses `aspectRatio` as its own
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fill its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotationEffect(_:anchor:)

Rotates a view’s rendered output in two dimensions around the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotationEffect(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view.

`anchor`

    

A unit point within the view about which to perform the rotation. The default
value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content around the axis that points out of
the xy-plane. It has no effect on the view’s frame. The following code rotates
text by 22˚ and then draws a border around the modified view to show that the
frame remains unchanged by the rotation modifier:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated content
onto the original view’s plane. Use the `perspective` value to control the
renderer’s vanishing point. The following example creates the appearance of
rotating text 45˚ about the y-axis:

Important

In visionOS, create this effect with
`perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)` instead. To
truly rotate a view in three dimensions, use a 3D rotation modifier without a
perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

visionOS 1.0+

    
    
    func perspectiveRotationEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated, two-
dimensional content onto the original view’s plane. Use the `perspective`
input to control the renderer’s vanishing point. The following example creates
the appearance of rotating text 45˚ about the y-axis:

Important

To truly rotate a view in three dimensions, use a 3D rotation modifier without
a perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:anchor:)

Rotates the view’s content by the specified 3D rotation value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ rotation: Rotation3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`rotation`

    

A rotation to apply to the view’s content.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: RotationAxis3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transformEffect(_:)

Applies an affine transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: CGAffineTransform) -> some View
    

##  Parameters

`transform`

    

A `CGAffineTransform` to apply to the view.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `CGAffineTransform`.

In the example below, the text is rotated at -30˚ on the `y` axis.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transform3DEffect(_:)

Applies a 3D transformation to the receiver.

visionOS 1.0+

    
    
    func transform3DEffect(_ transform: AffineTransform3D) -> some View
    

##  Parameters

`transform`

    

The 3D transformation to apply to the view, interpreting it as a 3D plane in
space.

## Return Value

A view that renders transformed according to the provided `transform`

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# projectionEffect(_:)

Applies a projection transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func projectionEffect(_ transform: ProjectionTransform) -> some View
    

##  Parameters

`transform`

    

A `ProjectionTransform` to apply to the view.

## Discussion

Use `projectionEffect(_:)` to apply a 3D transformation to the view.

The example below rotates the text 30˚ around the `z` axis, which is the axis
pointing out of the screen:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Structure

# ProjectionTransform

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ProjectionTransform

## Topics

### Creating a transform

`init()`

`init(CGAffineTransform)`

`init(CATransform3D)`

### Getting transform characteristics

`var isAffine: Bool`

`var isIdentity: Bool`

### Manipulating transforms

`func invert() -> Bool`

`func inverted() -> ProjectionTransform`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Enumeration

# ContentMode

Constants that define how a view’s content fills the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum ContentMode

## Topics

### Getting content modes

`case fill`

An option that resizes the content so it occupies all available space, both
vertically and horizontally.

`case fit`

An option that resizes the content so it’s all within the available space,
both vertically and horizontally.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

Instance Method

# mask(alignment:_:)

Masks this view using the alpha channel of the given view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func mask<Mask>(
        alignment: Alignment = .center,
        @ViewBuilder _ mask: () -> Mask
    ) -> some View where Mask : View
    

##  Parameters

`alignment`

    

The alignment for `mask` in relation to this view.

`mask`

    

The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another
view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

## See Also

### Masking and clipping

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipped(antialiased:)

Clips this view to its bounding rectangular frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipped(antialiased: Bool = false) -> some View
    

##  Parameters

`antialiased`

    

A Boolean value that indicates whether the rendering system applies smoothing
to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame.

## Discussion

Use the `clipped(antialiased:)` modifier to hide any content that extends
beyond the layout bounds of the shape.

By default, a view’s bounding frame is used only for layout, so any content
that extends beyond the edges of the frame is still visible.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipShape(_:style:)

Sets a clipping shape for this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipShape<S>(
        _ shape: S,
        style: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The clipping shape to use for this view. The `shape` fills the view’s frame,
while maintaining its aspect ratio.

`style`

    

The fill style to use when rasterizing `shape`.

## Return Value

A view that clips this view to `shape`, using `style` to define the shape’s
rasterization.

## Discussion

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying
a clipping shape to a view, you preserve the parts of the view covered by the
shape, while eliminating other parts of the view. The clipping shape itself
isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the
bounds of the circle.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

Instance Method

# blur(radius:opaque:)

Applies a Gaussian blur to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blur(
        radius: CGFloat,
        opaque: Bool = false
    ) -> some View
    

##  Parameters

`radius`

    

The radial size of the blur. A blur is more diffuse when its radius is large.

`opaque`

    

A Boolean value that indicates whether the blur renderer permits transparency
in the blur output. Set to `true` to create an opaque blur, or set to `false`
to permit transparency.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of
this view.

The example below shows two `Text` views, the first with no blur effects, the
second with `blur(radius:opaque:)` applied with the `radius` set to `2`. The
larger the radius, the more diffuse the effect.

## See Also

### Applying blur and shadows

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Instance Method

# shadow(color:radius:x:y:)

Adds a shadow to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func shadow(
        color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33),
        radius: CGFloat,
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`color`

    

The shadow’s color.

`radius`

    

A measure of how much to blur the shadow. Larger values result in more blur.

`x`

    

An amount to offset the shadow horizontally from the view.

`y`

    

An amount to offset the shadow vertically from the view.

## Return Value

A view that adds a shadow to this view.

## Discussion

Use this modifier to add a shadow of a specified color behind a view. You can
offset the shadow from its view independently in the horizontal and vertical
dimensions using the `x` and `y` parameters. You can also blur the edges of
the shadow using the `radius` parameter. Use a radius of zero to create a
sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each
box displays its radius and offset values for reference.

The example above uses `primary` as the color to make the shadow easy to see
for the purpose of illustration. In practice, you might prefer something more
subtle, like `gray`. If you don’t specify a color, the method uses a semi-
transparent black.

## See Also

### Applying blur and shadows

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Structure

# ColorMatrix

A matrix to use in an RGBA color transformation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct ColorMatrix

## Overview

The matrix has five columns, each with a red, green, blue, and alpha
component. You can use the matrix for tasks like creating a color
transformation `GraphicsContext.Filter` for a `GraphicsContext` using the
`colorMatrix(_:)` method.

## Topics

### Creating an identity matrix

`init()`

Creates the identity matrix.

### First column

`var r1: Float`

`var g1: Float`

`var b1: Float`

`var a1: Float`

### Second column

`var r2: Float`

`var g2: Float`

`var b2: Float`

`var a2: Float`

### Third column

`var r3: Float`

`var g3: Float`

`var b3: Float`

`var a3: Float`

### Fourth column

`var r4: Float`

`var g4: Float`

`var b4: Float`

`var a4: Float`

### Fifth column

`var r5: Float`

`var g5: Float`

`var b5: Float`

`var a5: Float`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Applying blur and shadows

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

Instance Method

# visualEffect(_:)

Applies effects to this view, while providing access to layout information
through a geometry proxy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func visualEffect(_ effect: @escaping (EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset by its own
size, causing its top left corner to appear where the bottom right corner was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Instance Method

# visualEffect3D(_:)

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

visionOS 1.0+

    
    
    func visualEffect3D(_ effect: @escaping (EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy3D`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset in Z by its own
depth, causing its back face to appear where the front face of the view was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Protocol

# VisualEffect

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol VisualEffect : Sendable, Animatable

## Overview

Because effects do not impact layout, they are safe to use in situations where
layout modification is not allowed. For example, effects may be applied as a
function of position, accessed through a geometry proxy:

You don’t conform to this protocol yourself. Instead, visual effects are
created by calling modifier functions (such as `.offset(x:y:)` on other
effects, as seen in the example above.

## Topics

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

## Relationships

### Inherits From

  * `Animatable`
  * `Sendable`

### Conforming Types

  * `EmptyVisualEffect`

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Structure

# EmptyVisualEffect

The base visual effect that you apply additional effect to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct EmptyVisualEffect

## Overview

`EmptyVisualEffect` does not change the appearance of the view that it is
applied to.

## Topics

### Creating an empty visual effect

`init()`

Creates a new empty visual effect.

## Relationships

### Conforms To

  * `Animatable`
  * `Sendable`
  * `VisualEffect`

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

Instance Method

# blendMode(_:)

Sets the blend mode for compositing this view with overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blendMode(_ blendMode: BlendMode) -> some View
    

##  Parameters

`blendMode`

    

The `BlendMode` for compositing this view.

## Return Value

A view that applies `blendMode` to this view.

## Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual
effect to produce the result. The `BlendMode` enumeration defines many
possible effects.

In the example below, the two overlapping rectangles have a
`BlendMode.colorBurn` effect applied, which effectively removes the non-
overlapping portion of the second image:

## See Also

### Compositing views

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# compositingGroup()

Wraps this view in a compositing group.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func compositingGroup() -> some View
    

## Return Value

A view that wraps this view in a compositing group.

## Discussion

A compositing group makes compositing effects in this view’s ancestor views,
such as opacity and the blend mode, take effect before this view is rendered.

Use `compositingGroup()` to apply effects to a parent view before applying
effects to this view.

In the example below the `compositingGroup()` modifier separates the
application of effects into stages. It applies the `opacity(_:)` effect to the
VStack before the `blur(radius:)` effect is applied to the views inside the
enclosed `ZStack`. This limits the scope of the opacity change to the
outermost view.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# drawingGroup(opaque:colorMode:)

Composites this view’s contents into an offscreen image before final display.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func drawingGroup(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear
    ) -> some View
    

##  Parameters

`opaque`

    

A Boolean value that indicates whether the image is opaque. The default is
`false`; if set to `true`, the alpha channel of the image must be `1`.

`colorMode`

    

One of the working color space and storage formats defined in
`ColorRenderingMode`. The default is `ColorRenderingMode.nonLinear`.

## Return Value

A view that composites this view’s contents into an offscreen image before
display.

## Discussion

The `drawingGroup(opaque:colorMode:)` modifier flattens a subtree of views
into a single view before rendering it.

In the example below, the contents of the view are composited to a single
bitmap; the bitmap is then displayed in place of the view:

Note

Views backed by native platform views may not render into the image. Instead,
they log a warning and display a placeholder image to highlight the error.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Enumeration

# BlendMode

Modes for compositing a view with overlapping content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum BlendMode

## Topics

### Getting the default

`case normal`

### Darkening

`case darken`

`case multiply`

`case colorBurn`

`case plusDarker`

### Lightening

`case lighten`

`case screen`

`case colorDodge`

`case plusLighter`

### Adding contrast

`case overlay`

`case softLight`

`case hardLight`

### Inverting

`case difference`

`case exclusion`

### Mixing color components

`case hue`

`case saturation`

`case color`

`case luminosity`

### Accessing porter-duff modes

`case sourceAtop`

`case destinationOver`

`case destinationOut`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Enumeration

# ColorRenderingMode

The set of possible working color spaces for color-compositing operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorRenderingMode

## Overview

Each color space guarantees the preservation of a particular range of color
values.

## Topics

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case linear`

The linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

Structure

# GeometryReader

A container view that defines its content as a function of its own size and
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GeometryReader<Content> where Content : View

## Overview

This view returns a flexible preferred size to its parent layout.

## Topics

### Creating a geometry reader

`init(content: (GeometryProxy) -> Content)`

`var content: (GeometryProxy) -> Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Measuring a view

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryReader3D

A container view that defines its content as a function of its own size and
coordinate space.

visionOS 1.0+

    
    
    @frozen
    struct GeometryReader3D<Content> where Content : View

## Overview

This view returns a flexible preferred size to its own container view.

This container differs from `GeometryReader` in that it also reads available
depth, and thus also returns a flexible preferred depth to its parent layout.
Use the 3D version only in situations where you need to read depth, because it
affects depth layout when used in a container like a `ZStack`.

## Topics

### Creating a geometry reader

`init(content: (GeometryProxy3D) -> Content)`

`var content: (GeometryProxy3D) -> Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryProxy

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct GeometryProxy

## Topics

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryProxy3D

A proxy for access to the size and coordinate space of the container view.

visionOS 1.0+

    
    
    struct GeometryProxy3D

## Overview

You can use a proxy for anchor resolution.

## Topics

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Instance Method

# coordinateSpace(_:)

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func coordinateSpace(_ name: NamedCoordinateSpace) -> some View
    

##  Parameters

`name`

    

A name used to identify this coordinate space.

## Discussion

Use `coordinateSpace(_:)` to allow another function to find and operate on a
view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its
enclosing view’s coordinate space:

Here, the `VStack` in the `ContentView` named “stack” is composed of a red
frame with a custom `Circle` view `overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing
VStack’s coordinate space. As the gesture recognizer’s closure registers
events inside `circle` it stores them in the shared `location` state variable
and the `VStack` displays the coordinates in a `Text` view.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Enumeration

# CoordinateSpace

A resolved coordinate space created by the coordinate space protocol.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum CoordinateSpace

## Overview

You don’t typically use `CoordinateSpace` directly. Instead, use the static
properties and functions of `CoordinateSpaceProtocol` such as `.global`,
`.local`, and `.named(_:)`.

## Topics

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case local`

The local coordinate space of the current view.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

### Testing a space

`var isGlobal: Bool`

`var isLocal: Bool`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Protocol

# CoordinateSpaceProtocol

A frame of reference within the layout system.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol CoordinateSpaceProtocol

## Overview

All geometric properties of a view, including size, position, and transform,
are defined within the local coordinate space of the view’s parent. These
values can be converted into other coordinate spaces by passing types
conforming to this protocol into functions such as `GeometryProxy.frame(in:)`.

For example, a named coordinate space allows you to convert the frame of a
view into the local coordinate space of an ancestor view by defining a named
coordinate space using the `coordinateSpace(_:)` modifier, then passing that
same named coordinate space into the `frame(in:)` function.

You don’t typically create types conforming to this protocol yourself.
Instead, use the system-provided `.global`, `.local`, and `.named(_:)`
implementations.

## Topics

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

### Getting the resolved coordinate space

`var coordinateSpace: CoordinateSpace`

The resolved coordinate space.

**Required**

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct LocalCoordinateSpace`

The local coordinate space of the current view.

`struct NamedCoordinateSpace`

A named coordinate space.

## Relationships

### Conforming Types

  * `GlobalCoordinateSpace`
  * `LocalCoordinateSpace`
  * `NamedCoordinateSpace`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# PhysicalMetric

Provides access to a value in points that corresponds to the specified
physical measurement.

visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct PhysicalMetric<Value>

## Overview

Use this property wrapper inside a `View` or a type that inherits a `View`’s
environment, like a `ViewModifier`. Its value will be the equivalent in points
of the physical measurement of length you specify.

For example, to have a variable that contains the amount of points
corresponding to one meter, you can do the following:

Using this wrapper for a property of a type not associated with a scene’s view
contents, like an `App` or a `Scene`, is unsupported.

## Topics

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

### Getting the value

`var wrappedValue: Value`

A value in points in the coordinate system of the associated scene.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# PhysicalMetricsConverter

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

visionOS 1.0+

    
    
    struct PhysicalMetricsConverter

## Overview

Converters are available from the environment of a `View` or other type that
inherits a `View`‘s environments, and are associated with the scene that
contains that environment. The conversions expect (or emit) values in points
in that scene’s coordinate system, and convert these to (or from) measurements
of length in the user’s reference frame. For example, if the scene is scaled,
that scale will be taken into account.

To obtain a converter, use the `physicalMetrics` key:

When user action modifies a scene so that measurements have changed (e.g., by
changing its scale), the view that accessed that environment key and its
hierarchy will be reevaluated.

Attempting to obtain a converter inside a type not associated with a scene’s
contents (for example, from an `App` or `Scene`’s environment) is not
supported.

## Topics

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

Instance Method

# colorEffect(_:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func colorEffect(
        _ shader: Shader,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply to `self` as a color filter.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function
signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader and `color` its source color, as a pre-multiplied color in the
destination color space. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the modified color
value.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# distortionEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func distortionEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply as a distortion effect.

`maxSampleOffset`

    

The maximum distance in each axis between the returned source pixel position
and the destination pixel position, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the user-space
coordinates of the corresponding source pixel.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# layerEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func layerEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply as a layer effect.

`maxSampleOffset`

    

If the shader function samples from the layer at locations not equal to the
destination position, this value must specify the maximum sampling distance in
each axis, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a layer effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader, and `layer` is a subregion of the rasterized contents
of `self`. `args...` should be compatible with the uniform arguments bound to
`shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file.
It exports a single `sample()` function that returns a linearly-filtered pixel
value from a position in the source content, as a premultiplied RGBA pixel
value:

The function should return the color mapping to the destination pixel,
typically by sampling one or more pixels from `layer` at location(s) derived
from `position` and them applying some kind of transformation to produce a new
color.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Structure

# Shader

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Shader

## Overview

Shader values can be used as filter effects on views, see the
`colorEffect(_:isEnabled:)`, `distortionEffect(_:maxSampleOffset:isEnabled:)`,
and `layerEffect(_:maxSampleOffset:isEnabled:)` functions.

Shaders also conform to the `ShapeStyle` protocol, letting their MSL shader
function provide per-pixel color to fill any shape or text view. For a shader
function to act as a fill pattern it must have a function signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader, and `args...` should be compatible with the uniform arguments bound to
`shader`. The function should return the premultiplied color value in the
color space of the destination (typically extended sRGB).

## Topics

### Creating a shader

`init(function: ShaderFunction, arguments: [Shader.Argument])`

Creates a new shader from a function and the uniform argument values to bind
to the function.

`struct Argument`

A single uniform argument value to a shader function.

### Getting the shader function

`var function: ShaderFunction`

The shader function called by the shader.

`var arguments: [Shader.Argument]`

The uniform argument values passed to the shader function.

### Configuring the shader

`var dithersColor: Bool`

For shader functions that return color values, whether the returned color has
dither noise added to it, or is simply rounded to the output bit-depth. For
shaders generating smooth gradients, dithering is usually necessary to prevent
visible banding in the result.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Structure

# ShaderFunction

A reference to a function in a Metal shader library.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @dynamicCallable
    struct ShaderFunction

## Topics

### Creating a shader function

`init(library: ShaderLibrary, name: String)`

Creates a new function reference from the provided shader library and function
name string.

### Configuring a function

`var library: ShaderLibrary`

The shader library storing the function.

`var name: String`

The name of the shader function in the library.

`func dynamicallyCall(withArguments: [Shader.Argument]) -> Shader`

Returns a new shader by applying the provided argument values to the
referenced function.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderLibrary`

A Metal shader library.

Structure

# ShaderLibrary

A Metal shader library.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @dynamicMemberLookup
    struct ShaderLibrary

## Topics

### Getting the default shader library

`static let `default`: ShaderLibrary`

The default shader library of the main (i.e. app) bundle.

`static func bundle(Bundle) -> ShaderLibrary`

Returns the default shader library of the specified bundle.

### Creating a shader library

`init(url: URL)`

Creates a new Metal shader library from the contents of `url`, which must be
the location of precompiled Metal library. Functions compiled from the
returned library will only be cached as long as the returned library exists.

`init(data: Data)`

Creates a new Metal shader library from `data`, which must be the contents of
precompiled Metal library. Functions compiled from the returned library will
only be cached as long as the returned library exists.

### Access shader functions

`static subscript(dynamicMember _: String) -> ShaderFunction`

Returns a new shader function representing the stitchable MSL function called
`name` in the default shader library.

### Subscripts

`subscript(dynamicMember _: String) -> ShaderFunction`

Returns a new shader function representing the stitchable MSL function in the
library called `name`.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

Enumeration

# Axis

The horizontal or vertical dimension in a 2D coordinate system.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Axis

## Topics

### Getting axes

`case horizontal`

The horizontal dimension.

`case vertical`

The vertical dimension.

### Getting all axes

`struct Set`

An efficient set of axes.

## Relationships

### Conforms To

  * `CaseIterable`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# Angle

A geometric angle whose value you access in either radians or degrees.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Angle

## Topics

### Getting constant angles

`static var zero: Angle`

`static func degrees(Double) -> Angle`

`static func radians(Double) -> Angle`

### Creating an angle

`init()`

`init(degrees: Double)`

`init(radians: Double)`

`init(Angle2D)`

### Getting the angle size

`var degrees: Double`

`var radians: Double`

## Relationships

### Conforms To

  * `Animatable`
  * `Comparable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# UnitPoint

A normalized 2D point in a view’s coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct UnitPoint

## Overview

Use a unit point to represent a location in a view without having to know the
view’s rendered size. The point stores a value in each dimension that
indicates the fraction of the view’s size in that dimension — measured from
the view’s origin — where the point appears. For example, you can create a
unit point that represents the center of any view by using the value `0.5` for
each dimension:

To project the unit point into the rendered view’s coordinate space, multiply
each component of the unit point with the corresponding component of the
view’s size:

You can perform this calculation yourself if you happen to know a view’s size,
or if you want to use the unit point for some custom purpose, but SwiftUI
typically does this for you to carry out operations that you request, like
when you:

  * Transform a shape using a shape modifier. For example, to rotate a shape with `rotation(_:anchor:)`, you indicate an anchor point that you want to rotate the shape around.

  * Override the alignment of the view in a `Grid` cell using the `gridCellAnchor(_:)` view modifier. The grid aligns the projection of a unit point onto the view with the projection of the same unit point onto the cell.

  * Create a gradient that has a center, or start and stop points, relative to the shape that you are styling. See the gradient methods in `ShapeStyle`.

You can create custom unit points with explicit values, like the example
above, or you can use one of the built-in unit points that SwiftUI provides,
like `zero`, `center`, or `topTrailing`. The built-in values correspond to the
alignment positions of the similarly named, built-in `Alignment` types.

Note

A unit point with one or more components outside the range `[0, 1]` projects
to a point outside of the view.

### Layout direction

When a person configures their device to use a left-to-right language like
English, the system places the view’s origin in its top-left corner, with
positive x toward the right and positive y toward the bottom of the view. In a
right-to-left environment, the origin moves to the upper-right corner, and the
positive x direction changes to be toward the left. You don’t typically need
to do anything to handle this change, because SwiftUI applies the change to
all aspects of the system. For example, see the discussion about layout
direction in `HorizontalAlignment`.

It’s important to test your app for the different locales that you distribute
your app in. For more information about the localization process, see
Localization.

## Topics

### Getting the origin

`static let zero: UnitPoint`

The origin of a view.

### Getting top points

`static let topLeading: UnitPoint`

A point that’s in the top, leading corner of a view.

`static let top: UnitPoint`

A point that’s centered horizontally on the top edge of a view.

`static let topTrailing: UnitPoint`

A point that’s in the top, trailing corner of a view.

### Getting middle points

`static let leading: UnitPoint`

A point that’s centered vertically on the leading edge of a view.

`static let center: UnitPoint`

A point that’s centered in a view.

`static let trailing: UnitPoint`

A point that’s centered vertically on the trailing edge of a view.

### Getting bottom points

`static let bottomLeading: UnitPoint`

A point that’s in the bottom, leading corner of a view.

`static let bottom: UnitPoint`

A point that’s centered horizontally on the bottom edge of a view.

`static let bottomTrailing: UnitPoint`

A point that’s in the bottom, trailing corner of a view.

### Creating a point

`init()`

Creates a unit point at the origin.

`init(x: CGFloat, y: CGFloat)`

Creates a unit point with the specified horizontal and vertical offsets.

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# UnitPoint3D

A normalized 3D point in a view’s coordinate space.

visionOS 1.0+

    
    
    @frozen
    struct UnitPoint3D

## Overview

Use a 3D unit point to represent a three-dimensional location in a view
without having to know the view’s rendered size. The point stores a value in
each dimension that indicates the fraction of the view’s size in that
dimension — measured from the view’s origin — where the point appears. For
example, you can create a unit point that represents the center of any view by
using the value `0.5` for each dimension:

Note

If you need a two-dimensional unit point, use `UnitPoint` instead.

To project the unit point into the rendered view’s coordinate space, multiply
each component of the unit point with the corresponding component of the
view’s size:

You can perform this calculation yourself if you happen to know a view’s size,
or if you want to use a unit point for some custom purpose, but SwiftUI
typically does this for you to carry out operations that you request, like
when you rotate a view with the `rotation3DEffect(_:anchor:)` modifier and
indicate the anchor point that you want to rotate the view around.

You can create custom unit points with explicit values, like the example
above, or you can use one of the built-in unit points that SwiftUI provides,
like `zero`, `center`, or `topTrailing`. The built-in values correspond to
common anchor points that you might want to refer to, like the center of one
of a view’s edges.

Note

A unit point with one or more components outside the range `[0, 1]` projects
to a point outside of the view.

### Layout direction

When a person configures their device to use a left-to-right language like
English, the system places the view’s origin in its top-left-back corner, with
positive x toward the right, positive y toward the bottom of the view, and
positive z toward the front. In a right-to-left environment, the origin moves
to the upper-right-back corner, and the positive x direction changes to be
toward the left. You don’t typically need to do anything to handle this
change, because SwiftUI applies the change to all aspects of the system. For
example, see the discussion about layout direction in `HorizontalAlignment`.

It’s important to test your app for the different locales that you distribute
your app in. For more information about the localization process, see
Localization.

## Topics

### Getting the origin

`static let origin: UnitPoint3D`

The origin of a view.

`static let zero: UnitPoint3D`

A 3D unit point with all components equal to zero.

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

### Creating a point

`init()`

Creates a 3D unit point at the origin.

`init(x: CGFloat, y: CGFloat, z: CGFloat)`

Creates a 3D unit point with the specified offsets.

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

`var z: CGFloat`

The normalized distance from the origin to the point in the depth dimension.

## Relationships

### Conforms To

  * `Animatable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# Anchor

An opaque value derived from an anchor source and a particular view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Anchor<Value>

## Overview

You can convert the anchor to a `Value` in the coordinate space of a target
view by using a `GeometryProxy` to specify the target view.

## Topics

### Getting the anchor’s source

`struct Source`

A type-erased geometry value that produces an anchored value of a given type.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.



# DropProposal

Initializer

# init(operation:)

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    init(operation: DropOperation)

## See Also

### Creating a drop proposal

`let operation: DropOperation`

The drop operation that the drop proposes to perform.

Instance Property

# operation

The drop operation that the drop proposes to perform.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    let operation: DropOperation

## See Also

### Creating a drop proposal

`init(operation: DropOperation)`



# Drag and drop

Instance Method

# draggable(_:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single instance or a value conforming to
`Transferable` that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag
and drop to this view. When a drag operation begins, a rendering of this view
is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# draggable(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<V, T>(
        _ payload: @autoclosure @escaping () -> T,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View, T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single class instance or a value conforming to
`Transferable` that represents the draggable data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:preview:)` modifier adds the appropriate gestures
for drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# dropDestination(for:action:isTargeted:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], CGPoint) -> Bool,
        isTargeted: @escaping (Bool) -> Void = { _ in }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the dropped models.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items. The second parameter
contains the drop location in this view’s coordinate space. Return `true` if
the drop operation was successful; otherwise, return `false`.

`isTargeted`

    

A closure that is called when a drag and drop operation enters or exits the
drop target area. The received value is `true` when the cursor is inside the
area, and `false` when the cursor is outside.

## Return Value

A view that provides a drop destination for a drag operation of the specified
type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file
promises.

The drop destination is the same size and position as this view.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

Instance Method

# itemProvider(_:)

Provides a closure that vends the drag representation to be used for a
particular data element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View
    

## See Also

### Moving items using item providers

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func onDrag<V>(
        _ data: @escaping () -> NSItemProvider,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag-and- drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for
drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:)

Activates this view as the source of a drag and drop operation.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and
drop to this view. When a drag operation begins, a rendering of this view is
generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag-and-drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider], CGPoint) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. The second parameter contains the drop location in
this view’s coordinate space. Return `true` if the drop operation was
successful; otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:delegate:)

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        delegate: any DropDelegate
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`delegate`

    

A type that conforms to the `DropDelegate` protocol. You have comprehensive
control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Protocol

# DropDelegate

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    protocol DropDelegate

## Overview

The `DropDelegate` protocol provides a comprehensive and flexible way to
interact with a drop operation. Specify a drop delegate when you modify a view
to accept drops with the `onDrop(of:delegate:)` method.

Alternatively, for simple drop cases that don’t require the full functionality
of a drop delegate, you can modify a view to accept drops using the
`onDrop(of:isTargeted:perform:)` or the `onDrop(of:isTargeted:perform:)`
method. These methods handle the drop using a closure you provide as part of
the modifier.

## Topics

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Structure

# DropProposal

The behavior of a drop.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct DropProposal

## Topics

### Creating a drop proposal

`init(operation: DropOperation)`

`let operation: DropOperation`

The drop operation that the drop proposes to perform.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Enumeration

# DropOperation

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    enum DropOperation

## Topics

### Getting operation types

`case cancel`

Cancel the drag operation and transfer no data.

`case copy`

Copy the data to the modified view.

`case forbidden`

The drop activity is not allowed at this time or location.

`case move`

Move the data represented by the drag items instead of copying it.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`struct DropInfo`

The current state of a drop.

Structure

# DropInfo

The current state of a drop.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct DropInfo

## Topics

### Getting the drop location

`var location: CGPoint`

The location of the drag in the coordinate space of the drop view.

### Checking for items

`func hasItemsConforming(to: [UTType]) -> Bool`

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

`func itemProviders(for: [UTType]) -> [NSItemProvider]`

Finds item providers that conform to at least one of the specified uniform
type identifiers.

### Deprecated symbols

`func hasItemsConforming(to: [String]) -> Bool`

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

Deprecated

`func itemProviders(for: [String]) -> [NSItemProvider]`

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

Deprecated

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

Instance Method

# springLoadingBehavior(_:)

Sets the spring loading behavior this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func springLoadingBehavior(_ behavior: SpringLoadingBehavior) -> some View
    

##  Parameters

`behavior`

    

Whether spring loading is enabled or not. If unspecified, the default behavior
is `.automatic.`

## Discussion

Spring loading refers to a view being activated during a drag and drop
interaction. On iOS this can occur when pausing briefly on top of a view with
dragged content. On macOS this can occur with similar brief pauses or on
pressure-sensitive systems by “force clicking” during the drag. This has no
effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation
effect, allowing the destination to be revealed without pausing the drag
interaction. For example, a button that reveals a list of folders that a
dragged item can be dropped onto.

Unlike `disabled(_:)`, this modifier overrides the value set by an ancestor
view rather than being unioned with it. For example, the below button would
allow spring loading:

## See Also

### Configuring spring loading

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

Instance Property

# springLoadingBehavior

The behavior of spring loaded interactions for the views associated with this
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var springLoadingBehavior: SpringLoadingBehavior { get }

## Discussion

Spring loading refers to a view being activated during a drag and drop
interaction. On iOS this can occur when pausing briefly on top of a view with
dragged content. On macOS this can occur with similar brief pauses or on
pressure-sensitive systems by “force clicking” during the drag. This has no
effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation
effect, allowing the destination to be revealed without pausing the drag
interaction. For example, a button that reveals a list of folders that a
dragged item can be dropped onto.

A value of `enabled` means that a view should support spring loaded
interactions if it is able, and `disabled` means it should not. A value of
`automatic` means that a view should follow its default behavior, such as a
`TabView` automatically allowing spring loading, but a `Picker` with
`segmented` style would not.

## See Also

### Configuring spring loading

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

Structure

# SpringLoadingBehavior

The options for controlling the spring loading behavior of views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SpringLoadingBehavior

## Overview

Use values of this type with the `springLoadingBehavior(_:)` modifier.

## Topics

### Getting the behaviors

`static let automatic: SpringLoadingBehavior`

The automatic spring loading behavior.

`static let enabled: SpringLoadingBehavior`

Spring loaded interactions will be enabled for applicable views.

`static let disabled: SpringLoadingBehavior`

Spring loaded interactions will be disabled for applicable views.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring spring loading

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.



# DefaultTextFieldStyle

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# DismissBehavior

Type Property

# destructive

The destructive dismiss behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let destructive: DismissBehavior

## Discussion

Use this behavior when you want to dismiss a window regardless of any
conditions that would normally prevent the dismissal. Dismissing windows in
this matter may result in loss of state.

On macOS, this behavior will cause windows to dismiss even when they are
currently showing a modal presentation, such as a sheet or alert.
Additionally, a document window will not show the save dialog when there are
unsaved changes and the window is dismissed with this behavior.

On iOS, this behavior behaves the same as `interactive`.

## See Also

### Getting behaviors

`static let interactive: DismissBehavior`

The interactive dismiss behavior.

Type Property

# interactive

The interactive dismiss behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let interactive: DismissBehavior

## Discussion

Use this behavior when you want to dismiss a window in a manner that is
similar to the standard system affordances for window dismissal - for example,
when a user clicks the close button.

This is the default behavior on macOS and iOS.

On macOS, dismissing a window using this behavior will not dismiss a window
which is currently showing a modal presentation, such as a sheet or alert.
Additionally, a document window that is dismissed with this behavior will show
the save dialog if there are unsaved changes to the document.

On iOS, dismissing a window using this behavior will dismiss it regardless of
any modal presentations being shown.

## See Also

### Getting behaviors

`static let destructive: DismissBehavior`

The destructive dismiss behavior.



# DropDelegate

Instance Method

# dropEntered(info:)

Tells the delegate a validated drop has entered the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropEntered(info: DropInfo)

**Required** Default implementation provided.

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

## See Also

### Receiving drop information

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# dropExited(info:)

Tells the delegate a validated drop operation has exited the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropExited(info: DropInfo)

**Required** Default implementation provided.

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# dropUpdated(info:)

Tells the delegate that a validated drop moved inside the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropUpdated(info: DropInfo) -> DropProposal?

**Required** Default implementation provided.

## Discussion

Use this method to return a drop proposal containing the operation the
delegate intends to perform at the drop `location`. The default implementation
of this method returns `nil`, which tells the drop to use the last valid
returned value or else `DropOperation.copy`.

## Default Implementations

### DropDelegate Implementations

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# validateDrop(info:)

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func validateDrop(info: DropInfo) -> Bool

**Required** Default implementation provided.

## Discussion

Specify the expected types when you apply the drop modifier to the view. The
default implementation returns `true`.

## Default Implementations

### DropDelegate Implementations

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# performDrop(info:)

Tells the delegate it can request the item provider data from the given
information.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func performDrop(info: DropInfo) -> Bool

**Required**

## Return Value

A Boolean that is `true` if the drop was successful, `false` otherwise.

## Discussion

Incorporate the received data into your app’s data model as appropriate.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.



# DefaultPickerStyle

Initializer

# init()

Creates a default picker style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# DatePickerStyle

Type Property

# automatic

The default style for date pickers.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static var automatic: DefaultDatePickerStyle { get }

Available when `Self` is `DefaultDatePickerStyle`.

## See Also

### Getting built-in date picker styles

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# compact

A date picker style that displays the components in a compact, textual format.

iOS 14.0+  iPadOS 14.0+  macOS 10.15.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    static var compact: CompactDatePickerStyle { get }

Available when `Self` is `CompactDatePickerStyle`.

## Discussion

Use this style when space is constrained and users expect to make specific
date and time selections. Some variants may include rich editing controls in a
pop up.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# field

A date picker style that displays the components in an editable field.

macOS 10.15+

    
    
    static var field: FieldDatePickerStyle { get }

Available when `Self` is `FieldDatePickerStyle`.

## Discussion

You can use this style when space is constrained and users expect to make
specific date and time selections. However, you should generally use
`stepperField` instead of this style, unless your your app requires hiding the
stepper.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# graphical

A date picker style that displays an interactive calendar or clock.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var graphical: GraphicalDatePickerStyle { get }

Available when `Self` is `GraphicalDatePickerStyle`.

## Discussion

This style is useful when you want to allow browsing through days in a
calendar, or when the look of a clock face is appropriate.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# stepperField

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

macOS 10.15+

    
    
    static var stepperField: StepperFieldDatePickerStyle { get }

Available when `Self` is `StepperFieldDatePickerStyle`.

## Discussion

This style is useful when space is constrained and users expect to make
specific date and time selections.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# wheel

A date picker style that displays each component as columns in a scrollable
wheel.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static var wheel: WheelDatePickerStyle { get }

Available when `Self` is `WheelDatePickerStyle`.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

Instance Method

# makeBody(configuration:)

Returns the appearance and interaction content for a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the date picker.

## Discussion

The system calls this method for each `DatePicker` instance in a view
hierarchy where this style is the current date picker style.

## See Also

### Creating custom date picker styles

`struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`typealias Configuration`

A type alias for the properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Structure

# DatePickerStyleConfiguration

The properties of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DatePickerStyleConfiguration

## Topics

### Establishing the date range

`var minimumDate: Date?`

The oldest selectable date.

`var maximumDate: Date?`

The most recent selectable date.

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`struct Label`

A type-erased label of a `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

### Selecting the date

`var selection: Date`

The date value being displayed and selected.

`var $selection: Binding<Date>`

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` typealias Configuration`

A type alias for the properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Type Alias

# DatePickerStyle.Configuration

A type alias for the properties of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    typealias Configuration = DatePickerStyleConfiguration

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Associated Type

# Body

A view representing the appearance and interaction of a `DatePicker`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`typealias Configuration`

A type alias for the properties of a `DatePicker`.

Structure

# DefaultDatePickerStyle

The default style for date pickers.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DefaultDatePickerStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the default date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# CompactDatePickerStyle

A date picker style that displays the components in a compact, textual format.

iOS 14.0+  iPadOS 14.0+  macOS 10.15.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct CompactDatePickerStyle

## Overview

You can also use `compact` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the compact date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# FieldDatePickerStyle

A date picker style that displays the components in an editable field.

macOS 10.15+

    
    
    struct FieldDatePickerStyle

## Overview

You can also use `field` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the field date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# GraphicalDatePickerStyle

A date picker style that displays an interactive calendar or clock.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct GraphicalDatePickerStyle

## Overview

You can also use `graphical` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the graphical date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# StepperFieldDatePickerStyle

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

macOS 10.15+

    
    
    struct StepperFieldDatePickerStyle

## Overview

You can also use `stepperField` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the field date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# WheelDatePickerStyle

A date picker style that displays each component as columns in a scrollable
wheel.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    struct WheelDatePickerStyle

## Overview

You can also use `wheel` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the wheel date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.



# DefaultMenuStyle

Initializer

# init()

Creates a default menu style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init()



# DatePickerStyleConfiguration

Instance Property

# minimumDate

The oldest selectable date.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var minimumDate: Date?

## See Also

### Establishing the date range

`var maximumDate: Date?`

The most recent selectable date.

Instance Property

# maximumDate

The most recent selectable date.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var maximumDate: Date?

## See Also

### Establishing the date range

`var minimumDate: Date?`

The oldest selectable date.

Instance Property

# label

A description of the `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    let label: DatePickerStyleConfiguration.Label

## See Also

### Labeling the date picker

`struct Label`

A type-erased label of a `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

Structure

# DatePickerStyleConfiguration.Label

A type-erased label of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

Instance Property

# displayedComponents

The date components that the user is able to view and edit.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var displayedComponents: DatePickerComponents

## See Also

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`struct Label`

A type-erased label of a `DatePicker`.

Instance Property

# selection

The date value being displayed and selected.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @Binding
    var selection: Date { get nonmutating set }

## See Also

### Selecting the date

`var $selection: Binding<Date>`

Instance Property

# $selection

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var $selection: Binding<Date> { get }

## See Also

### Selecting the date

`var selection: Date`

The date value being displayed and selected.



# DefaultMenuButtonStyle

Initializer

# init()

macOS 10.15–14.4  Deprecated

    
    
    init()

Deprecated

Use `menuStyle(.automatic)` instead.



# DropOperation

Case

# DropOperation.cancel

Cancel the drag operation and transfer no data.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    case cancel

## See Also

### Getting operation types

`case copy`

Copy the data to the modified view.

`case forbidden`

The drop activity is not allowed at this time or location.

`case move`

Move the data represented by the drag items instead of copying it.

Case

# DropOperation.copy

Copy the data to the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    case copy

## See Also

### Getting operation types

`case cancel`

Cancel the drag operation and transfer no data.

`case forbidden`

The drop activity is not allowed at this time or location.

`case move`

Move the data represented by the drag items instead of copying it.

Case

# DropOperation.forbidden

The drop activity is not allowed at this time or location.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    case forbidden

## See Also

### Getting operation types

`case cancel`

Cancel the drag operation and transfer no data.

`case copy`

Copy the data to the modified view.

`case move`

Move the data represented by the drag items instead of copying it.

Case

# DropOperation.move

Move the data represented by the drag items instead of copying it.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    case move

## See Also

### Getting operation types

`case cancel`

Cancel the drag operation and transfer no data.

`case copy`

Copy the data to the modified view.

`case forbidden`

The drop activity is not allowed at this time or location.



# DismissSearchAction

Instance Method

# callAsFunction()

Dismisses the current search operation, if any.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the
`DismissSearchAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.



# DynamicViewContent

Instance Property

# data

The collection of underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var data: Self.Data { get }

**Required**

## See Also

### Managing the data

`associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

Associated Type

# Data

The type of the underlying collection of data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Data : Collection

**Required**

## See Also

### Managing the data

`var data: Self.Data`

The collection of underlying data.

**Required**

Instance Method

# onDelete(perform:)

Sets the deletion action for the dynamic view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDelete(perform action: Optional<(IndexSet) -> Void>) -> some DynamicViewContent
    

##  Parameters

`action`

    

The action that you want SwiftUI to perform when elements in the view are
deleted. SwiftUI passes a set of indices to the closure that’s relative to the
dynamic view’s underlying collection of data.

## Return Value

A view that calls `action` when elements are deleted from the original view.

## See Also

### Responding to updates

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onInsert(
        of supportedContentTypes: [UTType],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> some DynamicViewContent
    

##  Parameters

`supportedContentTypes`

    

An array of UTI types that the dynamic view supports.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `NSItemProvider` items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# onMove(perform:)

Sets the move action for the dynamic view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onMove(perform action: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent
    

##  Parameters

`action`

    

A closure that SwiftUI invokes when elements in the dynamic view are moved.
The closure takes two arguments that represent the offset relative to the
dynamic view’s underlying collection of data. Pass `nil` to disable the
ability to move items.

## Return Value

A view that calls `action` when elements are moved within the original view.

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Instance Method

# dropDestination(for:action:)

Sets the insert action for the dynamic view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], Int) -> Void
    ) -> some DynamicViewContent where T : Transferable
    

##  Parameters

`payloadType`

    

Type of the models that are dropped.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `Transferable` items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Discussion

## See Also

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func onInsert(
        of acceptedTypeIdentifiers: [String],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> some DynamicViewContent
    

Deprecated

Use `onInsert(of:perform:)` instead.

##  Parameters

`acceptedTypeIdentifiers`

    

An array of UTI types that the dynamic view supports.

`action`

    

A closure that SwiftUI invokes when elements are added to the view. The
closure takes two arguments: The first argument is the offset relative to the
dynamic view’s underlying collection of data. The second argument is an array
of `NSItemProvider` that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.



# DocumentGroup

Initializer

# init(newDocument:editor:)

Creates a document group for creating and editing file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        newDocument: @autoclosure @escaping () -> Document,
        @ViewBuilder editor: @escaping (FileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

##  Parameters

`newDocument`

    

The initial document to use when a user creates a new document.

`editor`

    

The editing UI for the provided document.

## Discussion

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app
can open when you declare your app using the `App` protocol. You initialize a
document group scene by passing in the document model and a view capable of
displaying the document’s contents. The document types you supply to
`DocumentGroup` must conform to `FileDocument` or `ReferenceFileDocument`.
SwiftUI uses the model to add document support to your app. In macOS this
includes document-based menu support including the ability to open multiple
documents. On iOS this includes a document browser that can navigate to the
documents stored on the file system and multiwindow support:

The document types you supply to `DocumentGroup` must conform to
`FileDocument` or `ReferenceFileDocument`. Your app can support multiple
document types by adding additional `DocumentGroup` scenes.

## See Also

### Creating a document group

`init(viewing: Document.Type, viewer: (FileDocumentConfiguration<Document>) ->
Content)`

Creates a document group capable of viewing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

Initializer

# init(viewing:viewer:)

Creates a document group capable of viewing file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        viewing documentType: Document.Type,
        @ViewBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

##  Parameters

`documentType`

    

The type of document your app can view.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Use this method to create a document group that can view files of a specific
type. The example below creates a new document viewer for
`MyImageFormatDocument` and displays them with `MyImageFormatViewer`:

You tell the system about the app’s role with respect to the document type by
setting the `CFBundleTypeRole` `Info.plist` key with a value of `Viewer`.

## See Also

### Creating a document group

`init(newDocument: () -> Document, editor:
(FileDocumentConfiguration<Document>) -> Content)`

Creates a document group for creating and editing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

Initializer

# init(newDocument:editor:)

Creates a document group that is able to create and edit reference file
documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        newDocument: @escaping () -> Document,
        @ViewBuilder editor: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

##  Parameters

`newDocument`

    

The initial document used when the user creates a new document. The argument
should create a new instance, such that a new document is created on each
invocation of the closure.

`editor`

    

The editing UI for the provided document.

## Discussion

The current document for a given editor instance is also provided as an
environment object for its subhierarchy.

Undo support is not automatically provided for this construction of a
`DocumentGroup`, and any updates to the document by the editor view hierarchy
are expected to register undo operations when appropriate.

## See Also

### Creating a reference file document group

`init(viewing: Document.Type, viewer:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to view reference file documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

Initializer

# init(viewing:viewer:)

Creates a document group that is able to view reference file documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        viewing documentType: Document.Type,
        @ViewBuilder viewer: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content
    )

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

##  Parameters

`documentType`

    

The type of document being viewed.

`viewer`

    

The viewing UI for the provided document.

## Discussion

The current document for a given editor instance is also provided as an
environment object for its subhierarchy.

  * See Also: `CFBundleTypeRole` with a value of “Viewer”

## See Also

### Creating a reference file document group

`init(newDocument: () -> Document, editor:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to create and edit reference file
documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

Initializer

# init(editing:contentType:editor:prepareDocument:)

Instantiates a document group for creating and editing documents that store
several model types.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing modelTypes: [any PersistentModel.Type],
        contentType: UTType,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelTypes`

    

The array of model types defining the schema used for each document.

`contentType`

    

The content type of the document. It should conform to `UTType.package`.

`editor`

    

The editing UI for the provided document.

`prepareDocument`

    

The optional closure that accepts `ModelContext` associated with the new
document. Use this closure to set the document’s initial contents before it is
displayed: insert preconfigured models in the provided `ModelContext`.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the Info.plist as well.

## See Also

### Editing a document backed by a persistent store

`init(editing: any PersistentModel.Type, contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store a
specific model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: ()
-> Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(editing:contentType:editor:prepareDocument:)

Instantiates a document group for creating and editing documents that store a
specific model type.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing modelType: any PersistentModel.Type,
        contentType: UTType,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelType`

    

The model type defining the schema used for each document.

`contentType`

    

The content type of the document. It should conform to `UTType.package`.

`editor`

    

The editing UI for the provided document.

`prepareDocument`

    

The optional closure that accepts `ModelContext` associated with the new
document. Use this closure to set the document’s initial contents before it is
displayed: insert preconfigured models in the provided `ModelContext`.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the Info.plist as well.

## See Also

### Editing a document backed by a persistent store

`init(editing: [any PersistentModel.Type], contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store
several model types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: ()
-> Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(editing:migrationPlan:editor:prepareDocument:)

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        editing contentType: UTType,
        migrationPlan: any SchemaMigrationPlan.Type,
        editor: @escaping () -> Content,
        prepareDocument: @escaping ((ModelContext) -> Void) = { _ in }
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`editing`

    

The content type of the document. It should conform to `UTType.package`.

`migrationPlan`

    

The description of steps required to migrate older document versions so that
they can be opened and edited. The last `VersionedSchema` in the plan is
considered to be the current application schema.

`editor`

    

The editing UI for the provided document.

## See Also

### Editing a document backed by a persistent store

`init(editing: [any PersistentModel.Type], contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store
several model types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: any PersistentModel.Type, contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store a
specific model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(viewing:contentType:viewer:)

Instantiates a document group for viewing documents that store several model
types.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing modelTypes: [any PersistentModel.Type],
        contentType: UTType,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelTypes`

    

The model types defining the schema used for each document.

`contentType`

    

The content type of document your app can view. It should conform to
`UTType.package`.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the `Info.plist` as well.

## See Also

### Viewing a document backed by a persistent store

`init(viewing: any PersistentModel.Type, contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store a specific
model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: ()
-> Content)`

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(viewing:contentType:viewer:)

Instantiates a document group for viewing documents that store a specific
model type.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing modelType: any PersistentModel.Type,
        contentType: UTType,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`modelType`

    

The model type defining the schema used for each document.

`contentType`

    

The content type of document your app can view. It should conform to
`UTType.package`.

`viewer`

    

The viewing UI for the provided document.

## Discussion

Important

If your app declares custom uniform type identifiers, include corresponding
entries in the app’s `Info.plist`. For more information, see Defining file and
data types for your app. Also, remember to specify the supported Document
types in the `Info.plist` as well.

## See Also

### Viewing a document backed by a persistent store

`init(viewing: [any PersistentModel.Type], contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store several model
types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: ()
-> Content)`

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

Initializer

# init(viewing:migrationPlan:viewer:)

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    init(
        viewing contentType: UTType,
        migrationPlan: any SchemaMigrationPlan.Type,
        viewer: @escaping () -> Content
    )

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

##  Parameters

`viewing`

    

The content type of the document. It should conform to `UTType.package`.

`migrationPlan`

    

The description of steps required to migrate older document versions so that
they can be opened. The last `VersionedSchema` in the plan is considered to be
the current application schema.

`viewer`

    

The viewing UI for the provided document.

## See Also

### Viewing a document backed by a persistent store

`init(viewing: [any PersistentModel.Type], contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store several model
types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: any PersistentModel.Type, contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store a specific
model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.



# DefaultProgressViewStyle

Initializer

# init()

Creates a default progress view style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# DefaultListStyle

Initializer

# init()

Creates a default list style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# DefaultWindowToolbarStyle

Initializer

# init()

Creates a default window toolbar style.

macOS 11.0+

    
    
    init()

Initializer

# init()

Creates a default window toolbar style.

macOS 11.0+

    
    
    init()



# DefaultNavigationViewStyle

Initializer

# init()

Creates the default navigation view style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init()

Deprecated

Replace a styled `NavigationView` with a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

## Discussion

Use `automatic` to construct this style.



# DoubleColumnNavigationViewStyle

Initializer

# init()

Creates a double column navigation view style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
visionOS 1.0+

    
    
    init()

Deprecated

Use `ColumnNavigationViewStyle` instead.



# DismissWindowAction

Instance Method

# callAsFunction()

Dismisses the current window.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(id:)

Dismisses the window that’s associated with the specified identifier.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction(id: String)

##  Parameters

`id`

    

The identifier of the scene to dismiss.

## Discussion

When the specified identifier represents a `WindowGroup`, all of the open
windows in that group will be dismissed. For dismissing a single window
associated to a `WindowGroup` scene, use `dismissWindow(value:)` or
`dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(id:value:)

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(
        id: String,
        value: D
    ) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the scene to dismiss.

`value`

    

The value which is currently presented.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(value:)

Dismisses the window defined by the window group that is presenting the
specified value type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value which is currently presented.

## Discussion

If multiple windows match the provided value, then they all will be dismissed.
For dismissing a specific window in a specific group, use
`dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.



# DefaultWindowStyle

Initializer

# init()

macOS 11.0+  visionOS 1.0+

    
    
    init()



# Deprecated symbols

Initializer

# init(_:isActive:destination:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `NavigationStack` or `NavigationSplitView`. For
more information, see Migrating to new navigation types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:isActive:destination:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S>(
        _ title: S,
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `NavigationStack` or `NavigationSplitView`. For
more information, see Migrating to new navigation types.

##  Parameters

`title`

    

A string for creating a text label.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(isActive:destination:label:)

Creates a navigation link that presents the destination view when active.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(value:label:)` inside a `NavigationStack` or `NavigationSplitView`.
For more information, see Migrating to new navigation types.

##  Parameters

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:tag:selection:destination:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination
    ) where V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:tag:selection:destination:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S, V>(
        _ title: S,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol, V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`title`

    

A string for creating a text label.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(tag:selection:destination:label:)

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Initializer

# init(destinationName:isActive:label:)

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

watchOS 6.0–10.4  Deprecated

    
    
    init(
        destinationName: String,
        isActive: Binding<Bool>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(value:label:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

`init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () ->
Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init(destinationName: String, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Initializer

# init(destinationName:tag:selection:label:)

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

watchOS 6.0–10.4  Deprecated

    
    
    init<V>(
        destinationName: String,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

`init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init(destinationName: String, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Initializer

# init(destinationName:label:)

Creates a navigation link that presents a view from a WatchKit storyboard.

watchOS 6.0–10.4  Deprecated

    
    
    init(
        destinationName: String,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(destination:label:)` instead.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

`init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () ->
Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:destination:)` instead.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view arguments

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        destination: Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:destination:)` instead.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(destination:label:)

Creates a navigation link that presents the destination view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        destination: Destination,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(destination:label:)` instead.

##  Parameters

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:destination:isActive:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: Destination,
        isActive: Binding<Bool>
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:destination:isActive:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S>(
        _ title: S,
        destination: Destination,
        isActive: Binding<Bool>
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(destination:isActive:label:)

Creates a navigation link that presents the destination view when active.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        destination: Destination,
        isActive: Binding<Bool>,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(value:label:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:destination:tag:selection:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        destination: Destination,
        tag: V,
        selection: Binding<V?>
    ) where V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(_:destination:tag:selection:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S, V>(
        _ title: S,
        destination: Destination,
        tag: V,
        selection: Binding<V?>
    ) where S : StringProtocol, V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(destination:tag:selection:label:)

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        destination: Destination,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated



# DynamicProperty

Instance Method

# update()

Updates the underlying value of the stored value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func update()

**Required** Default implementation provided.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent value.

## Default Implementations

### DynamicProperty Implementations

`func update()`

Updates the underlying value of the stored value.



# DynamicTableRowContent

Instance Property

# data

The collection of underlying data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var data: Self.Data { get }

**Required**

## See Also

### Getting row data

`associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

Associated Type

# Data

The type of the underlying collection of data.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype Data : Collection

**Required**

## See Also

### Getting row data

`var data: Self.Data`

The collection of underlying data.

**Required**

Instance Method

# onInsert(of:perform:)

Sets the insert action for the dynamic table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func onInsert(
        of supportedContentTypes: [UTType],
        perform action: @escaping (Int, [NSItemProvider]) -> Void
    ) -> ModifiedContent<Self, OnInsertTableRowModifier>

##  Parameters

`supportedContentTypes`

    

An array of universal type identifiers types that the rows supports.

`action`

    

A closure that SwiftUI invokes when adding elements to the collection of rows.
The closure takes two arguments. The first argument is the offset relative to
the dynamic view’s underlying collection of data. The second argument is an
array of `NSItemProvider` items that represents the data that you want to
insert.

## Return Value

A view that calls `action` when inserting elements into the original view.

## See Also

### Inserting rows

`struct OnInsertTableRowModifier`

A table row modifier that adds the ability to insert data in some base row
content.

Structure

# OnInsertTableRowModifier

A table row modifier that adds the ability to insert data in some base row
content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct OnInsertTableRowModifier

## See Also

### Inserting rows

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) ->
ModifiedContent<Self, OnInsertTableRowModifier>`

Sets the insert action for the dynamic table rows.

Instance Method

# dropDestination(for:action:)

Sets the insert action for the dynamic table rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping (Int, [T]) -> Void
    ) -> ModifiedContent<Self, OnInsertTableRowModifier> where T : Transferable

##  Parameters

`payloadType`

    

Type of the models that are dropped.

`action`

    

A closure that SwiftUI invokes when elements are added to the collection of
rows. The closure takes two arguments: The first argument is the offset
relative to the dynamic view’s underlying collection of data. The second
argument is an array of `Transferable` items that represents the data that you
want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Discussion



# DefaultLabelStyle

Initializer

# init()

Creates an automatic label style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# Deprecated initializers

Initializer

# init(_:text:onEditingChanged:onCommit:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior. Use `FocusState` and `focused(_:equals:)` for the
`onEditingChanged` behavior.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onEditingChanged:onCommit:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior. Use `FocusState` and `focused(_:equals:)` for the
`onEditingChanged` behavior.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onCommit:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onCommit:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onEditingChanged:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onEditingChanged:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:onCommit:)

Creates an instance which binds over an arbitrary type, `T`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

Deprecated

Use `init(_:value:formatter:prompt:)` instead. Add the `onSubmit(of:_:)` view
modifier for the `onCommit` behavior. Use `FocusState` and
`focused(_:equals:)` for the `onEditingChanged` behavior.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `T`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:onCommit:)

Creates an instance which binds over an arbitrary type, `T`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

Deprecated

Use `init(_:value:formatter:prompt:)` instead. Add the `onSubmit(of:_:)` view
modifier for the `onCommit` behavior. Use `FocusState` and
`focused(_:equals:)` for the `onEditingChanged` behavior.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `T`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onCommit:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onCommit:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.



# DepthAlignment

Type Property

# back

A guide marking the bottom edge of the view.

visionOS 1.0+

    
    
    static let back: DepthAlignment

## See Also

### Getting guides

`static let center: DepthAlignment`

A guide marking the vertical center of the view.

`static let front: DepthAlignment`

A guide marking the top edge of the view.

Type Property

# center

A guide marking the vertical center of the view.

visionOS 1.0+

    
    
    static let center: DepthAlignment

## See Also

### Getting guides

`static let back: DepthAlignment`

A guide marking the bottom edge of the view.

`static let front: DepthAlignment`

A guide marking the top edge of the view.

Type Property

# front

A guide marking the top edge of the view.

visionOS 1.0+

    
    
    static let front: DepthAlignment

## See Also

### Getting guides

`static let back: DepthAlignment`

A guide marking the bottom edge of the view.

`static let center: DepthAlignment`

A guide marking the vertical center of the view.



# DismissAction

Instance Method

# callAsFunction()

Dismisses the view if it is currently presented.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the
`DismissAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

Instance Method

# callAsFunction()

Dismisses the view if it is currently presented.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the
`DismissAction` structure that you get from the `Environment`:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.



# DropInfo

Instance Property

# location

The location of the drag in the coordinate space of the drop view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    var location: CGPoint { get }

Instance Method

# hasItemsConforming(to:)

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func hasItemsConforming(to contentTypes: [UTType]) -> Bool

##  Parameters

`contentTypes`

    

The uniform type identifiers to query for.

## Return Value

Whether at least one item conforms to one of `contentTypes`.

## See Also

### Checking for items

`func itemProviders(for: [UTType]) -> [NSItemProvider]`

Finds item providers that conform to at least one of the specified uniform
type identifiers.

Instance Method

# itemProviders(for:)

Finds item providers that conform to at least one of the specified uniform
type identifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func itemProviders(for contentTypes: [UTType]) -> [NSItemProvider]

##  Parameters

`contentTypes`

    

The uniform type identifiers to query for.

## Return Value

The item providers that conforms to `contentTypes`.

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Checking for items

`func hasItemsConforming(to: [UTType]) -> Bool`

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

Instance Method

# hasItemsConforming(to:)

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func hasItemsConforming(to types: [String]) -> Bool

Deprecated

Use `hasItemsConforming(to:)` instead.

## See Also

### Deprecated symbols

`func itemProviders(for: [String]) -> [NSItemProvider]`

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

Deprecated

Instance Method

# itemProviders(for:)

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func itemProviders(for types: [String]) -> [NSItemProvider]

Deprecated

Use `itemProviders(for:)` instead.

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Deprecated symbols

`func hasItemsConforming(to: [String]) -> Bool`

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

Deprecated



# Divider

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# Documents

Structure

# DocumentGroup

A scene that enables support for opening, creating, and saving documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DocumentGroup<Document, Content> where Content : View

## Overview

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app
can open when you declare your app using the `App` protocol.

Initialize a document group scene by passing in the document model and a view
capable of displaying the document type. The document types you supply to
`DocumentGroup` must conform to `FileDocument` or `ReferenceFileDocument`.
SwiftUI uses the model to add document support to your app. In macOS this
includes document-based menu support, including the ability to open multiple
documents. On iOS this includes a document browser that can navigate to the
documents stored on the file system and multiwindow support:

Any time the configuration changes, SwiftUI updates the contents with that new
configuration, similar to other parameterized builders.

### Viewing documents

If your app only needs to display but not modify a specific document type, you
can use the file viewer document group scene. You supply the file type of the
document, and a view that displays the document type that you provide:

### Supporting multiple document types

Your app can support multiple document types by adding additional document
group scenes:

### Accessing the document’s URL

If your app needs to know the document’s URL, you can read it from the
`editor` closure’s `configuration` parameter, along with the binding to the
document. When you create a new document, the configuration’s `fileURL`
property is `nil`. Every time it changes, it is passed over to the
`DocumentGroup` builder in the updated `configuration`. This ensures that the
view you define in the closure always knows the URL of the document it hosts.

The URL can be used, for example, to present the file path of the file name in
the user interface. Don’t access the document’s contents or metadata using the
URL because that can conflict with the management of the file that SwiftUI
performs. Instead, use the methods that `FileDocument` and
`ReferenceFileDocument` provide to perform read and write operations.

## Topics

### Creating a document group

`init(newDocument: () -> Document, editor:
(FileDocumentConfiguration<Document>) -> Content)`

Creates a document group for creating and editing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

`init(viewing: Document.Type, viewer: (FileDocumentConfiguration<Document>) ->
Content)`

Creates a document group capable of viewing file documents.

Available when `Document` conforms to `FileDocument` and `Content` conforms to
`View`.

### Creating a reference file document group

`init(newDocument: () -> Document, editor:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to create and edit reference file
documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

`init(viewing: Document.Type, viewer:
(ReferenceFileDocumentConfiguration<Document>) -> Content)`

Creates a document group that is able to view reference file documents.

Available when `Document` conforms to `ReferenceFileDocument` and `Content`
conforms to `View`.

### Editing a document backed by a persistent store

`init(editing: [any PersistentModel.Type], contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store
several model types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: any PersistentModel.Type, contentType: UTType, editor: () ->
Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents that store a
specific model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: ()
-> Content, prepareDocument: ((ModelContext) -> Void))`

Instantiates a document group for creating and editing documents described by
the last `Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

### Viewing a document backed by a persistent store

`init(viewing: [any PersistentModel.Type], contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store several model
types.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: any PersistentModel.Type, contentType: UTType, viewer: () ->
Content)`

Instantiates a document group for viewing documents that store a specific
model type.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

`init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: ()
-> Content)`

Instantiates a document group for viewing documents described by the last
`Schema` in the migration plan.

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating a document

Building a Document-Based App with SwiftUI

Create, save, and open documents in a SwiftUI multiplatform app.

Building a document-based app using SwiftData

Code along with the WWDC presenter to transform an app with SwiftData.

Protocol

# FileDocument

A type that you use to serialize documents to and from file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol FileDocument

## Overview

To store a document as a value type — like a structure — create a type that
conforms to the `FileDocument` protocol and implement the required methods and
properties. Your implementation:

  * Provides a list of the content types that the document can read from and write to by defining `readableContentTypes`. If the list of content types that the document can write to is different from those that it reads from, you can optionally also define `writableContentTypes`.

  * Loads documents from file in the `init(configuration:)` initializer.

  * Stores documents to file by serializing their content in the `fileWrapper(configuration:)` method.

Important

If you store your document as a reference type — like a class — use
`ReferenceFileDocument` instead.

Ensure that types that conform to this protocol are thread-safe. In
particular, SwiftUI calls the protocol’s methods on a background thread. Don’t
use that thread to perform user interface updates. Use it only to serialize
and deserialize the document data.

## Topics

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

### Writing a document

`func fileWrapper(configuration: Self.WriteConfiguration) throws ->
FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

## See Also

### Storing document data in a structure instance

`struct FileDocumentConfiguration`

The properties of an open file document.

Structure

# FileDocumentConfiguration

The properties of an open file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentConfiguration<Document> where Document : FileDocument

## Overview

You receive an instance of this structure when you create a `DocumentGroup`
with a value file type. Use it to access the document in your viewer or
editor.

## Topics

### Getting and setting the document

`var document: Document`

The current document model.

`var $document: Binding<Document>`

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a structure instance

`protocol FileDocument`

A type that you use to serialize documents to and from file.

Protocol

# ReferenceFileDocument

A type that you use to serialize reference type documents to and from file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol ReferenceFileDocument : ObservableObject

## Overview

To store a document as a reference type — like a class — create a type that
conforms to the `ReferenceFileDocument` protocol and implement the required
methods and properties. Your implementation:

  * Provides a list of the content types that the document can read from and write to by defining `readableContentTypes`. If the list of content types that the document can write to is different from those that it reads from, you can optionally also define `writableContentTypes`.

  * Loads documents from file in the `init(configuration:)` initializer.

  * Stores documents to file by providing a snapshot of the document’s content in the `snapshot(contentType:)` method, and then serializing that content in the `fileWrapper(snapshot:configuration:)` method.

Important

If you store your document as a value type — like a structure — use
`FileDocument` instead.

Ensure that types that conform to this protocol are thread-safe. In
particular, SwiftUI calls the protocol’s methods on a background thread. Don’t
use that thread to perform user interface updates. Use it only to serialize
and deserialize the document data.

## Topics

### Reading a document

`init(configuration: Self.ReadConfiguration) throws`

Creates a document and initializes it with the contents of a file.

**Required**

` static var readableContentTypes: [UTType]`

The file and data types that the document reads from.

**Required**

` typealias ReadConfiguration`

The configuration for reading document contents.

### Getting a snapshot

`func snapshot(contentType: UTType) throws -> Self.Snapshot`

Creates a snapshot that represents the current state of the document.

**Required**

` associatedtype Snapshot`

A type that represents the document’s stored content.

**Required**

### Writing a document

`func fileWrapper(snapshot: Self.Snapshot, configuration:
Self.WriteConfiguration) throws -> FileWrapper`

Serializes a document snapshot to a file wrapper.

**Required**

` static var writableContentTypes: [UTType]`

The file types that the document supports saving or exporting to.

**Required** Default implementation provided.

`typealias WriteConfiguration`

The configuration for writing document contents.

## Relationships

### Inherits From

  * `ObservableObject`

## See Also

### Storing document data in a class instance

`struct ReferenceFileDocumentConfiguration`

The properties of an open reference file document.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

Structure

# ReferenceFileDocumentConfiguration

The properties of an open reference file document.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument

## Overview

You receive an instance of this structure when you create a `DocumentGroup`
with a reference file type. Use it to access the document in your viewer or
editor.

## Topics

### Getting and setting the document

`var document: Document`

The current document model.

`var $document: ObservedObject<Document>.Wrapper`

### Getting document properties

`var fileURL: URL?`

The URL of the open file document.

`var isEditable: Bool`

A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a class instance

`protocol ReferenceFileDocument`

A type that you use to serialize reference type documents to and from file.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

Instance Property

# undoManager

The undo manager used to register a view’s undo operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var undoManager: UndoManager? { get }

## Discussion

This value is `nil` when the environment represents a context that doesn’t
support undo and redo operations. You can skip registration of an undo
operation when this value is `nil`.

## See Also

### Storing document data in a class instance

`protocol ReferenceFileDocument`

A type that you use to serialize reference type documents to and from file.

`struct ReferenceFileDocumentConfiguration`

The properties of an open reference file document.

Instance Property

# documentConfiguration

The configuration of a document in a `DocumentGroup`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var documentConfiguration: DocumentConfiguration? { get }

## Discussion

The value is `nil` for views that are not enclosed in a `DocumentGroup`.

For example, if the app shows the document path in the footer of each
document, it can get the URL from the environment:

## See Also

### Accessing document configuration

`struct DocumentConfiguration`

Structure

# DocumentConfiguration

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DocumentConfiguration

## Topics

### Getting configuration values

`var fileURL: URL?`

A URL of an open document.

`var isEditable: Bool`

A Boolean value that indicates whether you can edit the document.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Accessing document configuration

`var documentConfiguration: DocumentConfiguration?`

The configuration of a document in a `DocumentGroup`.

Structure

# FileDocumentReadConfiguration

The configuration for reading file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentReadConfiguration

## Topics

### Reading the content

`let contentType: UTType`

The expected uniform type of the file contents.

`let file: FileWrapper`

The file wrapper containing the document content.

## See Also

### Reading and writing documents

`struct FileDocumentWriteConfiguration`

The configuration for serializing file contents.

Structure

# FileDocumentWriteConfiguration

The configuration for serializing file contents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct FileDocumentWriteConfiguration

## Topics

### Writing the content

`let contentType: UTType`

The expected uniform type of the file contents.

`let existingFile: FileWrapper?`

The file wrapper containing the current document content. `nil` if the
document is unsaved.

## See Also

### Reading and writing documents

`struct FileDocumentReadConfiguration`

The configuration for reading file contents.

Instance Property

# newDocument

An action in the environment that presents a new document.

macOS 13.0+

    
    
    var newDocument: NewDocumentAction { get }

## Discussion

Use the `newDocument` environment value to get the instance of the
`NewDocumentAction` structure for a given `Environment`. Then call the
instance to present a new document. You call the instance directly because it
defines a `callAsFunction(_:)` method that Swift calls when you call the
instance.

For example, you can define a button that creates a new document from the
selected text:

The above example assumes that you define a `TextDocument` that conforms to
the `FileDocument` or `ReferenceFileDocument` protocol, and a `DocumentGroup`
that handles the associated file type.

## See Also

### Opening a document programmatically

`struct NewDocumentAction`

An action that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`struct OpenDocumentAction`

An action that presents an existing document.

Structure

# NewDocumentAction

An action that presents a new document.

macOS 13.0+

    
    
    struct NewDocumentAction

## Overview

Use the `newDocument` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to present a new document.
You call the instance directly because it defines a `callAsFunction(_:)`
method that Swift calls when you call the instance.

For example, you can define a button that creates a new document from the
selected text:

The above example assumes that you define a `TextDocument` that conforms to
the `FileDocument` or `ReferenceFileDocument` protocol, and a `DocumentGroup`
that handles the associated file type.

## Topics

### Calling the action

`func callAsFunction<D>(() -> D)`

Presents a new reference type document window.

`func callAsFunction<D>(() -> D)`

Presents a new document window.

`func callAsFunction(contentType: UTType)`

Presents a new document window.

`func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) ->
Void)`

Presents a new document window with preset contents.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`struct OpenDocumentAction`

An action that presents an existing document.

Instance Property

# openDocument

An action in the environment that presents an existing document.

macOS 13.0+

    
    
    var openDocument: OpenDocumentAction { get }

## Discussion

Use the `openDocument` environment value to get the instance of the
`OpenDocumentAction` structure for a given `Environment`. Then call the
instance to present an existing document. You call the instance directly
because it defines a `callAsFunction(at:)` method that Swift calls when you
call the instance.

For example, you can create a button that opens the document at the specified
URL:

The above example uses a `do-catch` statement to handle any errors that the
open document action might throw. It also places the action inside a task and
awaits the result because the action operates asynchronously.

To present an existing document, your app must define a `DocumentGroup` that
handles the content type of the specified file. For a document that’s already
open, the system brings the existing window to the front. Otherwise, the
system opens a new window.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`struct NewDocumentAction`

An action that presents a new document.

`struct OpenDocumentAction`

An action that presents an existing document.

Structure

# OpenDocumentAction

An action that presents an existing document.

macOS 13.0+

    
    
    struct OpenDocumentAction

## Overview

Use the `openDocument` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to present an existing
document. You call the instance directly because it defines a
`callAsFunction(at:)` method that Swift calls when you call the instance.

For example, you can create a button that opens the document at the specified
URL:

The above example uses a `do-catch` statement to handle any errors that the
open document action might throw. It also places the action inside a task and
awaits the result because the action operates asynchronously.

To present an existing document, your app must define a `DocumentGroup` that
handles the content type of the specified file. For a document that’s already
open, the system brings the existing window to the front. Otherwise, the
system opens a new window.

## Topics

### Calling the action

`func callAsFunction(at: URL) async throws`

Opens the document at the specified file URL.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`struct NewDocumentAction`

An action that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

Structure

# RenameButton

A button that triggers a standard rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct RenameButton<Label> where Label : View

## Overview

A rename button receives its action from the environment. Use the
`renameAction(_:)` modifier to set the action. The system disables the button
if you don’t define an action.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation
title modifier automatically configures the environment with the appropriate
rename action.

## Topics

### Creating an rename button

`init()`

Creates a rename button.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating special-purpose buttons

`struct EditButton`

A button that toggles the edit mode environment value.

`struct PasteButton`

A system button that reads items from the pasteboard and delivers it to a
closure.

Instance Method

# renameAction(_:)

Sets the rename action in the environment to update focus state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ isFocused: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`isFocused`

    

The focus binding to update when activating the rename action.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# renameAction(_:)

Sets a closure to run for the rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ action: @escaping () -> Void) -> some View
    

##  Parameters

`action`

    

A closure to run when renaming.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When the user taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Property

# rename

An action that activates the standard rename interaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var rename: RenameAction? { get }

## Discussion

Use the `renameAction(_:)` modifier to configure the rename action in the
environment.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`struct RenameAction`

An action that activates a standard rename interaction.

Structure

# RenameAction

An action that activates a standard rename interaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct RenameAction

## Overview

Use the `renameAction(_:)` modifier to configure the rename action in the
environment.

## Topics

### Calling the action

`func callAsFunction()`

Triggers the standard rename action provided through the environment.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.



# DefaultFocusEvaluationPriority

Type Property

# automatic

Use the default focus preference when focus moves into the affected branch
automatically, but ignore it when the movement is driven by a user-initiated
navigation command.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let automatic: DefaultFocusEvaluationPriority

## See Also

### Getting the priorities

`static let userInitiated: DefaultFocusEvaluationPriority`

Always use the default focus preference when focus moves into the affected
branch.

Type Property

# userInitiated

Always use the default focus preference when focus moves into the affected
branch.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let userInitiated: DefaultFocusEvaluationPriority

## See Also

### Getting the priorities

`static let automatic: DefaultFocusEvaluationPriority`

Use the default focus preference when focus moves into the affected branch
automatically, but ignore it when the movement is driven by a user-initiated
navigation command.



