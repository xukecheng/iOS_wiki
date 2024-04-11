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

