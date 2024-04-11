Structure

# ImmersiveSpace

A scene that presents its content in an unbounded space.

visionOS 1.0+

    
    
    struct ImmersiveSpace<Content, Data> where Content : ImmersiveSpaceContent, Data : Decodable, Data : Encodable, Data : Hashable

## Overview

Use an immersive space as a container for a view hierarchy that your app
presents. The hierarchy that you declare as the immersive space’s content
serves as a template for it:

If you want to create a bounded scene instead, use one of the types that
creates a window or a volume, like `WindowGroup` or `DocumentGroup`.

### Style the immersive space

By default, immersive spaces use the `mixed` style which places virtual
content in a person’s surroundings. You can select a different style for the
immersive space by adding the `immersionStyle(selection:in:)` scene modifier
to the scene. For example, you can completely control the visual experience
using the `full` immersion style:

You can change the immersion style after presenting the immersive space by
changing the modifier’s `selection` input, although you can only use one of
the values that you specify in the modifier’s second parameter. For any style
of immersion, the other parts of your app’s interface — namely its windows —
remain visible. However, the immersion style affects how windows interact with
virtual objects in the environment:

  * For the `mixed` style, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.

  * For other styles, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is partially or completely off.

### Open an immersive space

You can programmatically open an immersive space by giving it an identifier.
For example, you can label the solar system view from the previous example:

Elsewhere in your code, you use the `openImmersiveSpace` environment value to
get the instance of the `OpenImmersiveSpaceAction` structure for a given
`Environment`. You call the instance directly — for example, from a button’s
closure, like in the following code — using the identifier:

Mark the call to the action with `await` because it executes asynchronously.
When your app opens an immersive space, the system hides all other visible
apps. The system allows only one immersive space to be open at a time. Be sure
to close the open immersive space before opening another one.

### Dismiss an immersive space

You can dismiss an immersive space by calling the `dismissImmersiveSpace`
action from the environment. For example, you can define a button that
dismisses an immersive space:

The dismiss action runs asynchronously, like the open action. You don’t need
to specify an identifier when dismissing an immersive space because there can
only be one immersive space open at a time.

### Present an immersive space at launch

When an app launches, it opens an instance of the first scene that’s listed in
the app’s body. However, to open an immersive space at launch, you need to
provide additional configuration information in your app’s `Info.plist` file.
In particular, set the `UIApplicationPreferredDefaultSceneSessionRole` key in
the scene manifest to the value UISceneSessionRoleImmersiveSpaceApplication.

To configure the style of the immersive space that opens at launch, add a
scene configuration to the scene session role. Use the
`UISceneInitialImmersionStyle` key together with a value that indicates one of
the mixed, full, or progressive styles. See the initial immersion style key
for more information.

## Topics

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

### Supporting types

`struct ImmersiveSpaceViewContent`

Immersive space content that uses a SwiftUI view hierarchy as the content.

`protocol ImmersiveSpaceContent`

A type that you can use as the content of an immersive space.

### Initializers

`init(content: () -> Content)`

Creates an immersive space.

`init<V>(content: () -> V)`

Creates an immersive space using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, content: () -> V)`

Creates the immersive space associated with the specified identifier using
view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, content: () -> Content)`

Creates the immersive space associated with the specified identifier.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating an immersive space

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

`protocol ImmersionStyle`

The styles that an immersive space can have.

Structure

# ImmersiveSpaceContentBuilder

A result builder for composing a collection of immersive space elements.

visionOS 1.0+

    
    
    @resultBuilder
    struct ImmersiveSpaceContentBuilder

## Topics

### Building content

`static func buildBlock<Content>(Content) -> Content`

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

`protocol ImmersionStyle`

The styles that an immersive space can have.

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

Protocol

# ImmersionStyle

The styles that an immersive space can have.

visionOS 1.0+

    
    
    protocol ImmersionStyle

## Overview

Configure the appearance and behavior of an `ImmersiveSpace` by adding the
`immersionStyle(selection:in:)` scene modifier to the space and specifying a
style that conforms to this protocol, like `mixed` or `full`. For example, the
following app defines a solar system scene that uses full immersion:

## Topics

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

## Relationships

### Conforming Types

  * `AutomaticImmersionStyle`
  * `FullImmersionStyle`
  * `MixedImmersionStyle`
  * `ProgressiveImmersionStyle`

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

Instance Property

# openImmersiveSpace

An action that presents an immersive space.

visionOS 1.0+

    
    
    var openImmersiveSpace: OpenImmersiveSpaceAction { get }

## Discussion

Use this environment value to get the instance of the
`OpenImmersiveSpaceAction` structure for a given `Environment`. Then call the
instance to present a space. You call the instance directly because it defines
`callAsFunction()` methods that Swift calls when you call the instance.

For example, you can define a button that opens a specified planet in an
immersive space:

You indicate which immersive space to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter.

  * A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.

  * Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error
occurs. You can check for errors by inspecting the call’s return value, which
is of type `OpenImmersiveSpaceAction.Result`. For example, the call returns an
error if you already have an immersive space open, because the system enables
only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure
receives a binding to the value that you provide. For best performance, use
lightweight data for the presentation value. For structured model values that
conform to `Identifiable`, the value’s identifier makes a good presentation
value, like the `planet.ID` value in the above code.

## See Also

### Opening an immersive space

`struct OpenImmersiveSpaceAction`

An action that presents an immersive space.

Structure

# OpenImmersiveSpaceAction

An action that presents an immersive space.

visionOS 1.0+

    
    
    struct OpenImmersiveSpaceAction

## Overview

Use the `openImmersiveSpace` environment value to get the instance of this
structure for a given `Environment`. Then call the instance to present a
space. You call the instance directly because it defines `callAsFunction()`
methods that Swift calls when you call the instance.

For example, you can define a button that opens a specified planet in an
immersive space:

You indicate which immersive space to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter.

  * A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.

  * Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error
occurs. You can check for errors by inspecting the call’s return value, which
is of type `OpenImmersiveSpaceAction.Result`. For example, the call returns an
error if you already have an immersive space open, because the system enables
only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure
receives a binding to the value that you provide. For best performance, use
lightweight data for the presentation value. For structured model values that
conform to `Identifiable`, the value’s identifier makes a good presentation
value, like the `planet.ID` value in the above code.

## Topics

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

### Getting the result

`enum Result`

The outcome of an attempt to open an immersive space.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Opening an immersive space

`var openImmersiveSpace: OpenImmersiveSpaceAction`

An action that presents an immersive space.

Instance Property

# dismissImmersiveSpace

An immersive space dismissal action stored in a view’s environment.

visionOS 1.0+

    
    
    var dismissImmersiveSpace: DismissImmersiveSpaceAction { get }

## Discussion

Use this environment value to get a `DismissImmersiveSpaceAction` instance for
a given `Environment`. Then call the instance to dismiss a space. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

The asynchronous call returns after the system finishes dismissing the space.
Unlike the call to `openImmersiveSpace` that you use to open the space — which
requires an identifier, a value, or both to specify which space to open — the
dismiss action requires no parameters because there can be only one immersive
space open at a time. The call closes the space that is currently open, if
any.

## See Also

### Closing the immersive space

`struct DismissImmersiveSpaceAction`

An action that dismisses an immersive space.

Structure

# DismissImmersiveSpaceAction

An action that dismisses an immersive space.

visionOS 1.0+

    
    
    struct DismissImmersiveSpaceAction

## Overview

Use the `dismissImmersiveSpace` environment value to get an instance of this
type for a given `Environment`. Then call the instance to dismiss a space. You
call the instance directly because it defines a `callAsFunction()` method that
Swift calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

The asynchronous call returns after the system finishes dismissing the space.
Unlike the call to `openImmersiveSpace` that you use to open the space — which
requires an identifier, a value, or both to specify which space to open — the
dismiss action requires no parameters because there can be only one immersive
space open at a time. The call closes the space that is currently open, if
any.

## Topics

### Calling the action

`func callAsFunction() async`

Dismisses the currently opened immersive space.

## See Also

### Closing the immersive space

`var dismissImmersiveSpace: DismissImmersiveSpaceAction`

An immersive space dismissal action stored in a view’s environment.

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

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some View
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some Scene`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# immersiveContentBrightness(_:)

Sets the content brightness of an immersive space.

visionOS 1.0+

    
    
    func immersiveContentBrightness(_ brightness: ImmersiveContentBrightness) -> some Scene
    

##  Parameters

`brightness`

    

The level of content brightness that you prefer.

## Return Value

A scene that has the specified content brightness.

## Discussion

Pass one of the standard brightness levels defined in
`ImmersiveContentBrightness` or a custom one that you create with the
`custom(_:)` method to this scene modifier to set a preference for the content
brightness in an `ImmersiveSpace`. The system takes the value that you set
into account, but might not be able to honor a specific preference.

When you do this to create an environment that’s suitable for video playback,
the standard brightness values provide good results for most use cases. To
optimize further, you can create a custom brightness using a normalized value
that expresses the linear brightness ratio between a standard dynamic range
white video frame and the background that surrounds the player window.

Important

This modifier doesn’t affect scenes other than immersive spaces.

## See Also

### Adjusting content brightness

`struct ImmersiveContentBrightness`

The content brightness of an immersive space.

Structure

# ImmersiveContentBrightness

The content brightness of an immersive space.

visionOS 1.0+

    
    
    struct ImmersiveContentBrightness

## Overview

Use a value of this type as an input to the `immersiveContentBrightness(_:)`
scene modifier to indicate the ambient content brightness of an
`ImmersiveSpace`.

When you do this to create an environment that’s suitable for video playback,
use one of the standard brightness values like `bright`, `dim`, or `dark` to
provide good results for most use cases. To optimize further, you can create a
custom brightness using a normalized value that expresses the linear
brightness ratio between a standard dynamic range white video frame and the
background that surrounds the player window.

## Topics

### Type Properties

`static let automatic: ImmersiveContentBrightness`

The default content brightness.

`static let bright: ImmersiveContentBrightness`

A bright content brightness.

`static let dark: ImmersiveContentBrightness`

A dark content brightness.

`static let dim: ImmersiveContentBrightness`

A dimmed content brightness.

### Type Methods

`static func custom(Double) -> ImmersiveContentBrightness`

Creates a content brightness with a custom value.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Adjusting content brightness

`func immersiveContentBrightness(ImmersiveContentBrightness) -> some Scene`

Sets the content brightness of an immersive space.

