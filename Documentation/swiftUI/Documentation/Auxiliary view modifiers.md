Article

# Configure your apps navigation titles

Use a navigation title to display the current navigation state of an
interface.

## Overview

On iOS and watchOS, when a view is navigated to inside of a navigation stack,
that view’s title is displayed in the navigation bar. On iPadOS, the primary
destination’s navigation title is reflected as the window’s title in the App
Switcher. Similarly on macOS, the primary destination’s title is used as the
window title in the titlebar, Windows menu and Mission Control.

In its simplest form, you can provide a string or a localized string key to a
navigation title modifier directly.

The title of your apps toolbar can be further customized using additional
navigation related modifiers. For example, you can associate a `URL` or your
own type conforming to `Transferable` to your view using the navigation
document modifier.

In iOS and iPadOS, this will construct a title that can present a menu by
tapping the navigation title in the app’s navigation bar. The menu contains
content providing information related to the URL and a draggable icon for
sharing.

In macOS, this item will construct a proxy icon for manipulating the file
backing the document.

When providing a transferable type, you should typically provide a
`SharePreview` which provides the appropriate content for rendering the
preview in the header of the menu.

### Renaming

You can provide a text binding to the navigation title modifier and SwiftUI
will automatically configure the toolbar to allow editing of the navigation
title on iOS or macOS. SwiftUI automatically syncs the navigation title with
the value of the string binding provided to the text field.

You can provide a string binding to the navigation title to configure the
title’s text field. SwiftUI will automatically place a rename action in the
titl menu alongside the actions originating from your app’s commands.

In iOS, when using a text field in a navigation title, SwiftUI creates a
button in the toolbar title. When triggered, this button updates the
navigation title to display an inline text field that will update the binding
you provide as the user types.

## See Also

### Navigation titles

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

Instance Method

# toolbar(content:)

Populates the toolbar or navigation bar with the specified items.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
    

##  Parameters

`content`

    

The items representing the content of the toolbar.

## Discussion

Use this method to populate a toolbar with a collection of views that you
provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can
provide either by supplying a collection of views with each view wrapped in a
`ToolbarItem`, or by providing a collection of views as a `ToolbarItemGroup`.
The example below uses a collection of `ToolbarItem` views to create a macOS
toolbar that supports text editing features:

Although it’s not mandatory, wrapping a related group of toolbar items
together in a `ToolbarItemGroup` provides a one-to-one mapping between
controls and toolbar items which results in the correct layout and spacing on
each platform. For design guidance on toolbars, see Toolbars in the Human
Interface Guidelines.

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Instance Method

# toolbar(content:)

Populates the toolbar or navigation bar with the views you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The views representing the content of the toolbar.

## Discussion

Use this modifier to add content to the toolbar. The toolbar modifier expects
a collection of toolbar items that you can provide either by supplying a
collection of views with each view wrapped in a `ToolbarItem`, or by providing
a collection of views as a `ToolbarItemGroup`. The example below adds views to
using a toolbar item group to support text editing features:

## See Also

### Populating a toolbar

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`struct ToolbarItem`

A model that represents an item which can be placed in the toolbar or
navigation bar.

`struct ToolbarItemGroup`

A model that represents a group of `ToolbarItem`s which can be placed in the
toolbar or navigation bar.

`struct ToolbarItemPlacement`

A structure that defines the placement of a toolbar item.

`protocol ToolbarContent`

Conforming types represent items that can be placed in various locations in a
toolbar.

`struct ToolbarContentBuilder`

Constructs a toolbar item set from multi-expression closures.

Instance Method

# toolbar(id:content:)

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func toolbar<Content>(
        id: String,
        @ToolbarContentBuilder content: () -> Content
    ) -> some View where Content : CustomizableToolbarContent
    

##  Parameters

`id`

    

A unique identifier for this toolbar.

`content`

    

The content representing the content of the toolbar.

## Discussion

Use this modifier when you want to allow the user to customize the components
and layout of elements in the toolbar. The toolbar modifier expects a
collection of toolbar items which you can provide either by supplying a
collection of views with each view wrapped in a `ToolbarItem`.

Note

Customizable toolbars will be displayed on both macOS and iOS, but only apps
running on iPadOS 16.0 and later will support user customization.

The example below creates a view that represents each `ToolbarItem` along with
an ID that uniquely identifies the toolbar item to the customization editor:

Note

Only `secondaryAction` items support customization in iPadOS. Other items
follow the normal placement rules and can’t be customized by the user.

In macOS you can enable menu support for toolbar customization by adding a
`ToolbarCommands` instance to a scene using the `commands(content:)` scene
modifier:

When you add the toolbar commands, the system adds a menu item to your app’s
main menu to provide toolbar customization support. This is in addition to the
ability to Control-click on the toolbar to open the toolbar customization
editor.

## See Also

### Populating a customizable toolbar

`protocol CustomizableToolbarContent`

Conforming types represent items that can be placed in various locations in a
customizable toolbar.

`struct ToolbarCustomizationBehavior`

The customization behavior of customizable toolbar content.

`struct ToolbarCustomizationOptions`

Options that influence the default customization behavior of customizable
toolbar content.

Instance Method

# toolbar(_:for:)

Specifies the visibility of a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbar(
        _ visibility: Visibility,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the bar.

`bars`

    

The bars to update the visibility of or `automatic` if empty.

## Discussion

The preferred visibility flows up to the nearest container that renders a bar.
This could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS.

This examples shows a view that hides the navigation bar.

You can provide multiple `ToolbarPlacement` instances to hide multiple bars at
once.

Note

In macOS, if you provide `ToolbarCommands` to the scene of your app, this
modifier disables the toolbar visibility command while the value of the
modifier is not `automatic`.

Depending on the specified bars, the requested visibility may not be able to
be fullfilled.

## See Also

### Setting toolbar visibility

`struct ToolbarPlacement`

The placement of a toolbar.

Instance Method

# toolbar(removing:)

Remove a toolbar item present by default

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func toolbar(removing defaultItemKind: ToolbarDefaultItemKind?) -> some View
    

##  Parameters

`defaultItemKind`

    

The kind of default item to remove

## Discussion

Use this modifier to remove toolbar items other `View`s add by default. For
example, to remove the sidebar toggle toolbar item provided by
`NavigationSplitView`:

## See Also

### Removing default items

`struct ToolbarDefaultItemKind`

A kind of toolbar item a `View` adds by default.

Instance Method

# toolbarBackground(_:for:)

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarBackground<S>(
        _ style: S,
        for bars: ToolbarPlacement...
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The style to display as the background of the bar.

`bars`

    

The bars to use the style for or `automatic` if empty.

## Discussion

The preferred style flows up to the nearest container that renders a bar. This
could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS. This example shows a view that renders the navigation
bar with a blue background and dark color scheme.

You can provide multiple `ToolbarPlacement` instances to customize multiple
bars at once.

When used within a `TabView`, the specified style will be preferred while the
tab is currently active. You can use a `Group` to specify the same preferred
background for every tab.

Depending on the specified bars, the requested style may not be able to be
fullfilled.

## See Also

### Styling a toolbar

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# toolbarBackground(_:for:)

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarBackground(
        _ visibility: Visibility,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the background of the bar.

`bars`

    

The bars to update the color scheme of or `automatic` if empty.

## Discussion

The preferred visibility flows up to the nearest container that renders a bar.
This could be a `NavigationView` or `TabView` in iOS, or the root view of a
`WindowGroup` in macOS.

In iOS, a value of `automatic` makes the visibility of a tab bar or navigation
bar background depend on where a `List` or `ScrollView` settles. For example,
when aligned to the bottom edge of of a scroll view’s content, the background
of a tab bar becomes transparent.

Specify a value of `Visibility.visible` to ensure that the background of a bar
remains visible regardless of where any scroll view or list stops scrolling.

This example shows a view that prefers to always have the tab bar visible when
the middle tab is selected:

You can provide multiple placements to customize multiple bars at once, as in
the following example:

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# toolbarColorScheme(_:for:)

Specifies the preferred color scheme of a bar managed by SwiftUI.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarColorScheme(
        _ colorScheme: ColorScheme?,
        for bars: ToolbarPlacement...
    ) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme of the background of the bar.

`bars`

    

The bars to update the color scheme of or `automatic` if empty.

## Discussion

The preferred color scheme flows up to the nearest container that renders a
bar. This could be a `NavigationView` or `TabView` in iOS, or the root view of
a `WindowGroup` in macOS. Pass in a value of nil to match the current system’s
color scheme.

This examples shows a view that renders the navigation bar with a blue
background and dark color scheme:

You can provide multiple `ToolbarPlacement` instances to customize multiple
bars at once.

Note that the provided color scheme is only respected while a background is
visible in the requested bar. As the background becomes visible, the bar
transitions from the color scheme of the app to the requested color scheme.
You can ensure that the color scheme is always respected by specifying that
the background of the bar always be visible.

Depending on the specified bars, the requested color scheme may not be able to
be fullfilled.

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Instance Method

# toolbarRole(_:)

Configures the semantic role for the content populating the toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarRole(_ role: ToolbarRole) -> some View
    

##  Parameters

`role`

    

The role of the toolbar.

## Discussion

Use this modifier to configure the semantic role for content populating your
app’s toolbar. SwiftUI uses this role when rendering the content of your app’s
toolbar.

## See Also

### Specifying the role of toolbar content

`struct ToolbarRole`

The purpose of content that populates the toolbar.

Instance Method

# toolbarTitleMenu(content:)

Configure the title menu of a toolbar.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func toolbarTitleMenu<C>(@ViewBuilder content: () -> C) -> some View where C : View
    

##  Parameters

`content`

    

The content associated to the toolbar title menu.

## Discussion

A title menu represent common functionality that can be done on the content
represented by your app’s toolbar or navigation title. This menu may be
populated from your app’s commands like `saveItem` or `printItem`.

You can provide your own set of actions to override this behavior.

In iOS and iPadOS, this will construct a menu that can be presented by tapping
the navigation title in the app’s navigation bar.

## See Also

### Setting the toolbar title menu

`struct ToolbarTitleMenu`

The title menu of a toolbar.

Instance Method

# toolbarTitleDisplayMode(_:)

Configures the toolbar title display mode for this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func toolbarTitleDisplayMode(_ mode: ToolbarTitleDisplayMode) -> some View
    

## Discussion

Use this modifier to override the default toolbar title display mode.

See `ToolbarTitleDisplayMode` for more information on the different kinds of
display modes. This modifier has no effect on macOS.

## See Also

### Configuring the toolbar title display mode

`struct ToolbarTitleDisplayMode`

A type that defines the behavior of title of a toolbar.

Instance Method

# ornament(visibility:attachmentAnchor:contentAlignment:ornament:)

Presents an ornament.

visionOS 1.0+

    
    
    func ornament<Content>(
        visibility: Visibility = .automatic,
        attachmentAnchor: OrnamentAttachmentAnchor,
        contentAlignment: Alignment = .center,
        @ViewBuilder ornament: () -> Content
    ) -> some View where Content : View
    

##  Parameters

`visibility`

    

The visibility of the ornament.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the ornament.

`contentAlignment`

    

The alignment of the ornament with its attachment anchor.

`content`

    

The content of the ornament.

## Discussion

Use this method to show an ornament at the specified position. The example
below displays an ornament below the window:

## See Also

### Creating an ornament

`struct OrnamentAttachmentAnchor`

Instance Method

# contextMenu(menuItems:)

Adds a context menu to a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0–7.0  Deprecated  visionOS 1.0+

    
    
    func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

## Return Value

A view that can display a context menu.

## Discussion

Use this modifier to add a context menu to a view in your app’s user
interface. Compose the menu by returning controls like `Button`, `Toggle`, and
`Picker` from the `menuItems` closure. You can also use `Menu` to define
submenus or `Section` to group items.

The following example creates a `Text` view that has a context menu with two
buttons:

People can activate the menu with an action like Control-clicking, or by using
the touch and hold gesture in iOS and iPadOS:

The system dismisses the menu if someone makes a selection, or taps or clicks
outside the menu.

If you want to show a preview beside the menu, use
`contextMenu(menuItems:preview:)`. To add a context menu to a container that
supports selection, like a `List` or a `Table`, and to distinguish between
menu activation on a selection and activation in an empty area of the
container, use `contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(menuItems:preview:)

Adds a context menu with a preview to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    func contextMenu<M, P>(
        @ViewBuilder menuItems: () -> M,
        @ViewBuilder preview: () -> P
    ) -> some View where M : View, P : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

`preview`

    

A view that the system displays along with the menu.

## Return Value

A view that can display a context menu with a preview.

## Discussion

When you use this modifer to add a context menu to a view in your app’s user
interface, the system shows a preview beside the menu. Compose the menu by
returning controls like `Button`, `Toggle`, and `Picker` from the `menuItems`
closure. You can also use `Menu` to define submenus or `Section` to group
items.

Define the preview by returning a view from the `preview` closure. The system
sizes the preview to match the size of its content. For example, you can add a
two button context menu to a `Text` view, and include an `Image` as a preview:

When someone activates the context menu with an action like touch and hold in
iOS or iPadOS, the system displays the image and the menu:

Note

This view modifier produces a context menu on macOS, but that platform doesn’t
display the preview.

If you don’t need a preview, use `contextMenu(menuItems:)` instead. If you
want to add a context menu to a container that supports selection, like a
`List` or a `Table`, and you want to distinguish between menu activation on a
selection and activation in an empty area of the container, use
`contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(forSelectionType:menu:primaryAction:)

Adds an item-based context menu to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func contextMenu<I, M>(
        forSelectionType itemType: I.Type = I.self,
        @ViewBuilder menu: @escaping (Set<I>) -> M,
        primaryAction: ((Set<I>) -> Void)? = nil
    ) -> some View where I : Hashable, M : View
    

##  Parameters

`itemType`

    

The identifier type of the items. Ensure that this matches the container’s
selection type.

`menu`

    

A closure that produces the menu. A single parameter to the closure contains
the set of items to act on. An empty set indicates menu activation over the
empty area of the selectable container, while a non-empty set indicates menu
activation over selected items. Use controls like `Button`, `Picker`, and
`Toggle` to define the menu items. You can also create submenus using `Menu`,
or group items with `Section`. You can deactivate the context menu by
returning nothing from the closure.

`primaryAction`

    

A closure that defines the action to perform in response to the primary
interaction. A single parameter to the closure contains the set of items to
act on.

## Return Value

A view that can display an item-based context menu.

## Discussion

You can add an item-based context menu to a container that supports selection,
like a `List` or a `Table`. In the closure that you use to define the menu,
you receive a collection of items that depends on the selection state of the
container and the location where the person clicks or taps to activate the
menu. The collection contains:

  * The selected item or items, when people initiate the context menu from any selected item.

  * Nothing, if people tap or click to activate the context menu from an empty part of the container. This is true even when one or more items is currently selected.

You can vary the menu contents according to the number of selected items. For
example, the following code has a list that defines an empty area menu, a
single item menu, and a multi-item menu:

The above example assumes that the `Item` type conforms to the `Identifiable`
protocol, and relies on the associated `ID` type for both selection and
context menu presentation.

If you add the modifier to a view hierarchy that doesn’t have a container that
supports selection, the context menu never activates. To add a context menu
that doesn’t depend on selection behavior, use `contextMenu(menuItems:)`. To
add a context menu to a specific row in a table, use
`contextMenu(menuItems:)`.

### Add a primary action

Optionally, you can add a custom primary action to the context menu. In macOS,
a single click on a row in a selectable container selects that row, and a
double click performs the primary action. In iOS and iPadOS, tapping on the
row activates the primary action. To select a row without performing an
action, either enter edit mode or hold shift or command on a keyboard while
tapping the row.

For example, you can modify the context menu from the previous example so that
double clicking the row on macOS opens a new window for selected items. Get
the `OpenWindowAction` from the environment:

Then call `openWindow` from inside the `primaryAction` closure for each item:

The open window action depends on the declaration of a `WindowGroup` scene in
your `App` that responds to the `Item` type:

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

Instance Method

# badge(_:)

Generates a badge for the view from a text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ label: Text?) -> some View
    

##  Parameters

`label`

    

An optional `Text` view to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

Use this initializer when you want to style a `Text` view for use as a badge.
The following example customizes the badge with the `monospacedDigit()`,
`foregroundColor(_:)`, and `bold()` modifiers.

Styling the text view has no effect when the badge appears in a `TabView`.

## See Also

### Displaying a badge on a list item

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge<S>(_ label: S?) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

An optional string to display as a badge. Set the value to `nil` to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:)`. The following example shows a list with a “Default”
badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ key: LocalizedStringKey?) -> some View
    

##  Parameters

`key`

    

An optional string key to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`. The following example shows a list with a
“Default” badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from an integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ count: Int) -> some View
    

##  Parameters

`count`

    

An integer value to display in the badge. Set the value to zero to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count`
represented by a badge on one of the rows:

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badgeProminence(_:)

Specifies the prominence of badges created by this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func badgeProminence(_ prominence: BadgeProminence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply to badges.

## Discussion

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

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

# touchBar(content:)

Sets the content that the Touch Bar displays.

macOS 10.15+

    
    
    func touchBar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A collection of views to be displayed by the Touch Bar.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the
Touch Bar. The content is displayed by the Touch Bar when appropriate,
depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and
then added to the Touch Bar:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBar(_:)

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

macOS 10.15+

    
    
    func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View
    

##  Parameters

`touchBar`

    

A collection of views that the Touch Bar displays.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` to provide a static set of views that are displayed by the
Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content
the Touch Bar displays:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPrincipal(_:)

Sets principal views that have special significance to this Touch Bar.

macOS 10.15+

    
    
    func touchBarItemPrincipal(_ principal: Bool = true) -> some View
    

##  Parameters

`principal`

    

A Boolean value that indicates whether to display this view prominently in the
Touch Bar compared to other views.

## Return Value

A Touch Bar view with one element centered in the Touch Bar row.

## Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in
the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch
Bar view.

Note

Multiple visible bars may each specify a principal view, but the system only
honors one of them.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarCustomizationLabel(_:)

Sets a user-visible string that identifies the view’s functionality.

macOS 10.15+

    
    
    func touchBarCustomizationLabel(_ label: Text) -> some View
    

##  Parameters

`label`

    

A `Text` view containing the customization label.

## Return Value

A Touch Bar element with a set customization label.

## Discussion

This string is visible during user customization.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPresence(_:)

Sets the behavior of the user-customized view.

macOS 10.15+

    
    
    func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View
    

##  Parameters

`presence`

    

One of the allowed `TouchBarItemPresence` descriptions.

## Return Value

A trait that describes the behavior for this Touch Bar view.

## Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a
particular Touch Bar view during customization by the user.

Touch Bar views may be:

  * `.required`: not allowed to be removed by the user.

  * `.default`: shown by default prior to user customization, but removable.

  * `.optional`: not visible by default, but can be added through the customization palette.

Each `TouchBarItemPresence` must be initialized with a string that is a
globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar
by default, except for the “Clubs” item. It’s set to `.optional` but is
configurable by the user:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

