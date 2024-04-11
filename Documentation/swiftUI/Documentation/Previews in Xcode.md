Macro

# Preview(_:body:)

Creates a preview of a SwiftUI view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

Use this macro to display a SwiftUI preview in the canvas. You typically
specify at least one preview macro for every `View` that your app defines to
help you develop, test, and debug the view:

If you include more than one preview in a source file, the canvas provides
controls that enable you to select which to display when that source file is
active. The canvas labels the different previews with the line number where
the preview appears in source. To better identify the previews in the canvas,
you can give them names. For example if your `ContentView` takes a Boolean
input, you can create named previews for each input state:

Inside the preview, you can provide different inputs, model data, and other
infrastructure that the view needs for normal operation. For example, you can
present a custom view as the sidebar inside a `NavigationSplitView` if that’s
how your app uses the view.

Other preview macros provide different customization options. For example, if
you need to modify the appearance of a preview using one or more
`PreviewTrait`, instances, use the `Preview(_:traits:_:body:)` macro.

## See Also

### Creating a preview

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:_:body:)

Creates a preview of a SwiftUI view using the specified traits.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>,
        _ additionalTraits: PreviewTrait<Preview.ViewTraits>...,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

A `PreviewTrait` instance that customizes the appearance of the preview.

`additionalTraits`

    

Optional additional traits that further customize the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This macro behaves like `Preview(_:body:)` except that it also enables you to
customize the appearance of the preview by adding one or more traits, which
are instances of `PreviewTrait`. For example, you can display a preview at a
fixed size using the `fixedLayout(width:height:)` trait:

The macro ignores traits that don’t apply to the current context. For example,
the `portrait` trait has no impact on a visionOS preview.

Other preview macros provide different customization options. For example, if
you want to specify a custom viewpoint for the preview, use
`Preview(_:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:body:cameras:)

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This macro behaves like `Preview(_:traits:_:body:)` except that it also
enables you to specify one or more `PreviewCamera` instances that define
custom, fixed viewpoints from which to view the preview:

If you use one of the preview macros that doesn’t include a `cameras` closure,
the canvas displays the preview from the front by default. It also provides a
camera picker to choose other standard, fixed viewpoints — like the top or the
back. When you do specify one or more preview cameras, the canvas adds a
submenu to the camera picker that lists the viewpoints that you define, like
Corner 1 and Corner 2 in the above example. The canvas also displays the
preview from the first of these custom viewpoints by default when it loads the
preview.

Note

In addition to using fixed camera perspectives, you can also interactively
alter the viewpoint of a preview in the canvas using controls like those that
Simulator provides. For more information, see Interacting with your app in the
visionOS simulator.

Other preview macros provide different customization options. For example, if
you want to preview the view as it would appear in a particular kind of scene,
you can use `Preview(_:immersionStyle:traits:body:cameras:)` or
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

Macro

# Preview(_:immersionStyle:traits:body:)

Creates a preview of a SwiftUI view in an immersive space.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in an immersive space with the specified immersion style, like
the `mixed` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in a window rather than an immersive
space, you can use `Preview(_:windowStyle:traits:body:)`. If you want to add
custom, fixed viewpoints to an immersive space preview, use
`Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:immersionStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:immersionStyle:traits:body:)`
combined with `Preview(_:traits:body:cameras:)`: it enables you to define an
immersive space scene context for the view, and also to define custom, fixed
viewpoints for the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in a window rather than an
immersive space, use `Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:)

Creates a preview of a SwiftUI view in a window.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in a window with the specified window style, like the
`volumetric` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in an immersive space rather than a
window, you can use `Preview(_:immersionStyle:traits:body:)`. If you want to
add custom, fixed viewpoints to a window-based preview, use
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in a window with custom viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:windowStyle:traits:body:)` combined
with `Preview(_:traits:body:cameras:)`: it enables you to define a window
scene context for the view, and also to define custom, fixed viewpoints for
the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in an immersive space rather
than a window, use `Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

Protocol

# PreviewProvider

A type that produces view previews in Xcode.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    protocol PreviewProvider : _PreviewProvider

## Overview

Important

You can use this protocol to define a preview manually, but you typically use
a preview macro like `Preview(_:body:)` instead.

You can create an Xcode preview by declaring a structure that conforms to the
`PreviewProvider` protocol. Implement the required `previews` computed
property, and return the view to display:

Xcode statically discovers preview providers in your project and generates
previews for any providers currently open in the source editor. Xcode
generates the preview using the current run destination as a hint for which
device to display. For example, Xcode shows the following preview if you’ve
selected an iOS target to run on the iPhone 12 Pro Max simulator:

When you create a new file (File > New > File) and choose the SwiftUI view
template, Xcode automatically inserts a preview structure at the bottom of the
file that you can configure. You can also create new preview structures in an
existing SwiftUI view file by choosing Editor > Create Preview.

Customize the preview’s appearance by adding view modifiers, just like you do
when building a custom `View`. This includes preview-specific modifiers that
let you control aspects of the preview, like the device orientation:

For the complete list of preview customizations, see Previews in Xcode.

Xcode creates different previews for each view in your preview, so you can see
variations side by side. For example, you might want to see a view’s light and
dark appearances simultaneously:

Use a `Group` when you want to maintain different previews, but apply a single
modifier to all of them:

## Topics

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

` associatedtype Previews : View`

The type to preview.

**Required**

### Specifying the platform

`static var platform: PreviewPlatform?`

The platform on which to run the provider.

**Required** Default implementation provided.

## See Also

### Defining a preview

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Enumeration

# PreviewPlatform

Platforms that can run the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum PreviewPlatform

## Overview

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property as a hint,
and specify one of the preview platforms:

## Topics

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Instance Method

# previewDisplayName(_:)

Sets a user visible name to show in the canvas for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDisplayName(_ value: String?) -> some View
    

##  Parameters

`value`

    

A name for the preview.

## Return Value

A preview that uses the given name.

## Discussion

Apply this modifier to a view inside your `PreviewProvider` implementation to
associate a display name with that view’s preview:

Add a name when you have multiple previews together in the canvas that you
need to tell apart. The default value is `nil`, in which case Xcode displays a
default string.

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

Instance Method

# previewDevice(_:)

Overrides the device for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDevice(_ value: PreviewDevice?) -> some View
    

##  Parameters

`value`

    

A device to use for preview, or `nil` to let Xcode automatically choose a
device based on the run destination.

## Return Value

A preview that uses the given device.

## Discussion

By default, Xcode automatically chooses a preview device based on your
currently selected run destination. If you want to choose a device that
doesn’t change based on Xcode settings, provide a `PreviewDevice` instance
that you initialize with the name or model of a specific device:

You can get a list of supported preview device names, like “iPhone 11”, “iPad
Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## See Also

### Customizing a preview

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# PreviewDevice

A simulator device that runs a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreviewDevice

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like
“iPad8,1”. Use the device in a call to the `previewDevice(_:)` modifier to set
a preview device that doesn’t change when you change the run destination in
Xcode:

You can get a list of supported preview device names by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## Relationships

### Conforms To

  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByStringLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewLayout(_:)

Overrides the size of the container for the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewLayout(_ value: PreviewLayout) -> some View
    

##  Parameters

`value`

    

A layout to use for preview.

## Return Value

A preview that uses the given layout.

## Discussion

By default, previews use the `PreviewLayout/device` layout, which places the
view inside a visual representation of the chosen device. You can instead tell
a preview to use a different layout by choosing one of the `PreviewLayout`
values, like `PreviewLayout/sizeThatFits`:

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewInterfaceOrientation(_:)

Overrides the orientation of the preview.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
    

##  Parameters

`value`

    

An orientation to use for preview.

## Return Value

A preview that uses the given orientation.

## Discussion

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation of a preview using one of the
values in the `InterfaceOrientation` structure:

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# InterfaceOrientation

The orientation of the interface from the user’s perspective.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct InterfaceOrientation

## Overview

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation with a call to the
`previewInterfaceOrientation(_:)` modifier:

## Topics

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Identifiable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

Instance Method

# previewContext(_:)

Declares a context for the preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func previewContext<C>(_ value: C) -> some View where C : PreviewContext
    

##  Parameters

`value`

    

The context for the preview; the default is `nil`.

## See Also

### Setting a context

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContext

A context type for use with a preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContext

## Topics

### Accessing a preview context

`subscript<Key>(Key.Type) -> Key.Value`

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContextKey

A key type for a preview context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContextKey

## Overview

The default value is `nil`.

## Topics

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the value returned by the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.

Macro

# Preview(_:body:)

Creates a preview of a SwiftUI view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

Use this macro to display a SwiftUI preview in the canvas. You typically
specify at least one preview macro for every `View` that your app defines to
help you develop, test, and debug the view:

If you include more than one preview in a source file, the canvas provides
controls that enable you to select which to display when that source file is
active. The canvas labels the different previews with the line number where
the preview appears in source. To better identify the previews in the canvas,
you can give them names. For example if your `ContentView` takes a Boolean
input, you can create named previews for each input state:

Inside the preview, you can provide different inputs, model data, and other
infrastructure that the view needs for normal operation. For example, you can
present a custom view as the sidebar inside a `NavigationSplitView` if that’s
how your app uses the view.

Other preview macros provide different customization options. For example, if
you need to modify the appearance of a preview using one or more
`PreviewTrait`, instances, use the `Preview(_:traits:_:body:)` macro.

## See Also

### Creating a preview

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:_:body:)

Creates a preview of a SwiftUI view using the specified traits.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>,
        _ additionalTraits: PreviewTrait<Preview.ViewTraits>...,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

A `PreviewTrait` instance that customizes the appearance of the preview.

`additionalTraits`

    

Optional additional traits that further customize the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This macro behaves like `Preview(_:body:)` except that it also enables you to
customize the appearance of the preview by adding one or more traits, which
are instances of `PreviewTrait`. For example, you can display a preview at a
fixed size using the `fixedLayout(width:height:)` trait:

The macro ignores traits that don’t apply to the current context. For example,
the `portrait` trait has no impact on a visionOS preview.

Other preview macros provide different customization options. For example, if
you want to specify a custom viewpoint for the preview, use
`Preview(_:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:body:cameras:)

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This macro behaves like `Preview(_:traits:_:body:)` except that it also
enables you to specify one or more `PreviewCamera` instances that define
custom, fixed viewpoints from which to view the preview:

If you use one of the preview macros that doesn’t include a `cameras` closure,
the canvas displays the preview from the front by default. It also provides a
camera picker to choose other standard, fixed viewpoints — like the top or the
back. When you do specify one or more preview cameras, the canvas adds a
submenu to the camera picker that lists the viewpoints that you define, like
Corner 1 and Corner 2 in the above example. The canvas also displays the
preview from the first of these custom viewpoints by default when it loads the
preview.

Note

In addition to using fixed camera perspectives, you can also interactively
alter the viewpoint of a preview in the canvas using controls like those that
Simulator provides. For more information, see Interacting with your app in the
visionOS simulator.

Other preview macros provide different customization options. For example, if
you want to preview the view as it would appear in a particular kind of scene,
you can use `Preview(_:immersionStyle:traits:body:cameras:)` or
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

Macro

# Preview(_:immersionStyle:traits:body:)

Creates a preview of a SwiftUI view in an immersive space.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in an immersive space with the specified immersion style, like
the `mixed` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in a window rather than an immersive
space, you can use `Preview(_:windowStyle:traits:body:)`. If you want to add
custom, fixed viewpoints to an immersive space preview, use
`Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:immersionStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:immersionStyle:traits:body:)`
combined with `Preview(_:traits:body:cameras:)`: it enables you to define an
immersive space scene context for the view, and also to define custom, fixed
viewpoints for the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in a window rather than an
immersive space, use `Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:)

Creates a preview of a SwiftUI view in a window.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in a window with the specified window style, like the
`volumetric` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in an immersive space rather than a
window, you can use `Preview(_:immersionStyle:traits:body:)`. If you want to
add custom, fixed viewpoints to a window-based preview, use
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in a window with custom viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:windowStyle:traits:body:)` combined
with `Preview(_:traits:body:cameras:)`: it enables you to define a window
scene context for the view, and also to define custom, fixed viewpoints for
the preview:

    
    
    #Preview("Volume", windowStyle: .volumetric) {
       ContentView()
    } cameras: {
       PreviewCamera(from: .front)
       PreviewCamera(from: .top, zoom: 2)
       PreviewCamera(from: .leading, zoom: 0.5, name: "close up")
    }
    

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in an immersive space rather
than a window, use `Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

Protocol

# PreviewProvider

A type that produces view previews in Xcode.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    protocol PreviewProvider : _PreviewProvider

## Overview

Important

You can use this protocol to define a preview manually, but you typically use
a preview macro like `Preview(_:body:)` instead.

You can create an Xcode preview by declaring a structure that conforms to the
`PreviewProvider` protocol. Implement the required `previews` computed
property, and return the view to display:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
        }
    }
    

Xcode statically discovers preview providers in your project and generates
previews for any providers currently open in the source editor. Xcode
generates the preview using the current run destination as a hint for which
device to display. For example, Xcode shows the following preview if you’ve
selected an iOS target to run on the iPhone 12 Pro Max simulator:

When you create a new file (File > New > File) and choose the SwiftUI view
template, Xcode automatically inserts a preview structure at the bottom of the
file that you can configure. You can also create new preview structures in an
existing SwiftUI view file by choosing Editor > Create Preview.

Customize the preview’s appearance by adding view modifiers, just like you do
when building a custom `View`. This includes preview-specific modifiers that
let you control aspects of the preview, like the device orientation:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeLeft)
        }
    }
    

For the complete list of preview customizations, see Previews in Xcode.

Xcode creates different previews for each view in your preview, so you can see
variations side by side. For example, you might want to see a view’s light and
dark appearances simultaneously:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
            CircleImage()
                .preferredColorScheme(.dark)
        }
    }
    

Use a `Group` when you want to maintain different previews, but apply a single
modifier to all of them:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            Group {
                CircleImage()
                CircleImage()
                    .preferredColorScheme(.dark)
            }
            .previewLayout(.sizeThatFits)
        }
    }
    

## Topics

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

` associatedtype Previews : View`

The type to preview.

**Required**

### Specifying the platform

`static var platform: PreviewPlatform?`

The platform on which to run the provider.

**Required** Default implementation provided.

## See Also

### Defining a preview

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Enumeration

# PreviewPlatform

Platforms that can run the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum PreviewPlatform

## Overview

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property as a hint,
and specify one of the preview platforms:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
        }
    
    
        static var platform: PreviewPlatform? {
            PreviewPlatform.tvOS
        }
    }
    

## Topics

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Instance Method

# previewDisplayName(_:)

Sets a user visible name to show in the canvas for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDisplayName(_ value: String?) -> some View
    

##  Parameters

`value`

    

A name for the preview.

## Return Value

A preview that uses the given name.

## Discussion

Apply this modifier to a view inside your `PreviewProvider` implementation to
associate a display name with that view’s preview:

Add a name when you have multiple previews together in the canvas that you
need to tell apart. The default value is `nil`, in which case Xcode displays a
default string.

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

Instance Method

# previewDevice(_:)

Overrides the device for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDevice(_ value: PreviewDevice?) -> some View
    

##  Parameters

`value`

    

A device to use for preview, or `nil` to let Xcode automatically choose a
device based on the run destination.

## Return Value

A preview that uses the given device.

## Discussion

By default, Xcode automatically chooses a preview device based on your
currently selected run destination. If you want to choose a device that
doesn’t change based on Xcode settings, provide a `PreviewDevice` instance
that you initialize with the name or model of a specific device:

You can get a list of supported preview device names, like “iPhone 11”, “iPad
Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## See Also

### Customizing a preview

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# PreviewDevice

A simulator device that runs a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreviewDevice

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like
“iPad8,1”. Use the device in a call to the `previewDevice(_:)` modifier to set
a preview device that doesn’t change when you change the run destination in
Xcode:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
        }
    }
    

You can get a list of supported preview device names by using the `xcrun`
command in the Terminal app:

    
    
    % xcrun simctl list devicetypes
    

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## Relationships

### Conforms To

  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByStringLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewLayout(_:)

Overrides the size of the container for the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewLayout(_ value: PreviewLayout) -> some View
    

##  Parameters

`value`

    

A layout to use for preview.

## Return Value

A preview that uses the given layout.

## Discussion

By default, previews use the `PreviewLayout/device` layout, which places the
view inside a visual representation of the chosen device. You can instead tell
a preview to use a different layout by choosing one of the `PreviewLayout`
values, like `PreviewLayout/sizeThatFits`:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewLayout(.sizeThatFits)
        }
    }
    

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewInterfaceOrientation(_:)

Overrides the orientation of the preview.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
    

##  Parameters

`value`

    

An orientation to use for preview.

## Return Value

A preview that uses the given orientation.

## Discussion

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation of a preview using one of the
values in the `InterfaceOrientation` structure:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeRight)
        }
    }
    

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# InterfaceOrientation

The orientation of the interface from the user’s perspective.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct InterfaceOrientation

## Overview

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation with a call to the
`previewInterfaceOrientation(_:)` modifier:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeRight)
        }
    }
    

## Topics

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Identifiable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

Instance Method

# previewContext(_:)

Declares a context for the preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func previewContext<C>(_ value: C) -> some View where C : PreviewContext
    

##  Parameters

`value`

    

The context for the preview; the default is `nil`.

## See Also

### Setting a context

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContext

A context type for use with a preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContext

## Topics

### Accessing a preview context

`subscript<Key>(Key.Type) -> Key.Value`

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContextKey

A key type for a preview context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContextKey

## Overview

The default value is `nil`.

## Topics

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the value returned by the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.

