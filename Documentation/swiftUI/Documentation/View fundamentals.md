Article

# Declaring a custom view

Define views and assemble them into a view hierarchy.

## Overview

SwiftUI offers a declarative approach to user interface design. With a
traditional imperative approach, the burden is on your controller code not
only to instantiate, lay out, and configure views, but also to continually
make updates as conditions change. In contrast, with a declarative approach,
you create a lightweight description of your user interface by declaring views
in a hierarchy that mirrors the desired layout of your interface. SwiftUI then
manages drawing and updating these views in response to events like user input
or state changes.

SwiftUI provides tools for defining and configuring the views in your user
interface. You compose custom views out of built-in views that SwiftUI
provides, plus other composite views that you’ve already defined. You
configure these views with view modifiers and connect them to your data model.
You then place your custom views within your app’s view hierarchy.

### Conform to the view protocol

Declare a custom view type by defining a structure that conforms to the `View`
protocol:

Like other Swift protocols, the `View` protocol provides a blueprint for
functionality — in this case, the behavior of an element that SwiftUI draws
onscreen. Conformance to the protocol comes with both requirements that a view
must fulfill, and functionality that the protocol provides. After you fulfill
the requirements, you can insert your custom view into a view hierarchy so
that it becomes part of your app’s user interface.

### Declare a body

The `View` protocol’s main requirement is that conforming types must define a
`body` computed property:

SwiftUI reads the value of this property any time it needs to update the view,
which can happen repeatedly during the life of the view, typically in response
to user input or system events. The value that the view returns is an element
that SwiftUI draws onscreen.

The `View` protocol’s secondary requirement is that conforming types must
indicate an associated type for the body property. However, you don’t make an
explicit declaration. Instead, you declare the body property as an opaque
type, using the `some View` syntax, to indicate only that the body’s type
conforms to `View`. The exact type depends on the body’s content, which varies
as you edit the body during development. Swift infers the exact type
automatically.

### Assemble the view’s content

Describe your view’s appearance by adding content to the view’s body property.
You can compose the body from built-in views that SwiftUI provides, as well as
custom views that you’ve defined elsewhere. For example, you can create a body
that draws the string “Hello, World!” using a built-in `Text` view:

In addition to views for specific kinds of content, controls, and indicators,
like `Text`, `Toggle`, and `ProgressView`, SwiftUI also provides built-in
views that you can use to arrange other views. For example, you can vertically
stack two `Text` views using a `VStack`:

Views that take multiple input child views, like the stack in the example
above, typically do so using a closure marked with the `ViewBuilder`
attribute. This enables a multiple-statement closure that doesn’t require
additional syntax at the call site. You only need to list the input views in
succession.

For examples of views that contain other views, see Layout fundamentals.

### Configure views with modifiers

To configure the views in your view’s body, you apply view modifiers. A
modifier is nothing more than a method called on a particular view. The method
returns a new, altered view that effectively takes the place of the original
in the view hierarchy.

SwiftUI extends the `View` protocol with a large set of methods for this
purpose. All `View` protocol conformers — both built-in and custom views —
have access to these methods that alter the behavior of a view in some way.
For example, you can change the font of a text view by applying the `font(_:)`
modifier:

For more information about how view modifiers work, and how to use them on
your views, see Configuring views.

### Manage data

To supply inputs to your views, add properties. For example, you can make the
font of the “Hello, World!” string configurable:

If an input value changes, SwiftUI notices the change and redraws only the
affected parts of your interface. This might involve reinitializing your
entire view, but SwiftUI manages that for you.

Because the system may reinitialize a view at any time, it’s important to
avoid doing any significant work in your view’s initialization code. It’s
often best to omit an explicit initializer, as in the example above, allowing
Swift to synthesize a _member-wise initializer_ instead.

SwiftUI provides many tools to help you manage your app’s data under these
constraints, as described in Model data. For information about Swift
initializers, see Initialization in _The Swift Programming Language_.

### Add your view to the view hierarchy

After you define a view, you can incorporate it in other views, just like you
do with built-in views. You add your view by declaring it at the point in the
hierarchy at which you want it to appear. For example, you could put `MyView`
in your app’s `ContentView`, which Xcode creates automatically as the root
view of a new app:

Alternatively, you could add your view as the root view of a new scene in your
app, like the `Settings` scene that declares content for a macOS preferences
window, or a `WKNotificationScene` scene that declares the content for a
watchOS notification. For more information about defining your app structure
with SwiftUI, see App organization.

## See Also

### Creating a view

`protocol View`

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

`struct ViewBuilder`

A custom parameter attribute that constructs views from closures.

Protocol

# View

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol View

## Overview

You create custom views by declaring types that conform to the `View`
protocol. Implement the required `body` computed property to provide the
content for your custom view.

Assemble the view’s body by combining one or more of the built-in views
provided by SwiftUI, like the `Text` instance in the example above, plus other
custom views that you define, into a hierarchy of views. For more information
about creating custom views, see Declaring a custom view.

The `View` protocol provides a set of modifiers — protocol methods with
default implementations — that you use to configure views in the layout of
your app. Modifiers work by wrapping the view instance on which you call them
in another view with the specified characteristics, as described in
Configuring views. For example, adding the `opacity(_:)` modifier to a text
view returns a new view with some amount of transparency:

The complete list of default modifiers provides a large set of controls for
managing views. For example, you can fine tune Layout modifiers, add
Accessibility modifiers information, and respond to Input and event modifiers.
You can also collect groups of default modifiers into new, custom view
modifiers for easy reuse.

## Topics

### Implementing a custom view

`var body: Self.Body`

The content and behavior of the view.

**Required** Default implementations provided.

`associatedtype Body : View`

The type of view representing the body of this view.

**Required**

` func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

### Deprecated modifiers

API Reference

Deprecated modifiers

Review unsupported modifiers and their replacements.

### Instance Methods

`func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View`

Sets the button’s style.

`func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View`

Sets the style to be used by the button. (see `PKAddPassButtonStyle`).

`func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some
View`

Presents a modal view that enables users to add devices to their organization.

`func complicationForeground() -> some View`

Promotes this view to the foreground in a complication.

Deprecated

`func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect:
((AVContinuityDevice?) -> Void)?) -> some View`

A `continuityDevicePicker` should be used to discover and connect nearby
continuity device through a button interface or other form of activation. On
tvOS, this presents a fullscreen continuity device picker experience when
selected. The modal view covers as much the screen of `self` as possible when
a given condition is true.

`func lookAroundViewer(isPresented: Binding<Bool>, initialScene:
MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some
View`

`func lookAroundViewer(isPresented: Binding<Bool>, scene:
Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some
View`

`func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes:
(MapCamera) -> some Keyframes<MapCamera>) -> some View`

Uses the given keyframes to animate the camera of a `Map` when the given
trigger value changes.

`func mapControlVisibility(Visibility) -> some View`

Configures all Map controls in the environment to have the specified
visibility

`func mapControls(() -> some View) -> some View`

Configures all `Map` views in the associated environment to have standard size
and position controls

`func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) ->
some View`

Specifies a custom presentation for the currently selected feature.

`func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View`

Specifies which map features should have selection disabled.

`func mapScope(Namespace.ID) -> some View`

Creates a mapScope that SwiftUI uses to connect map controls to an associated
map.

`func mapStyle(MapStyle) -> some View`

Specifies the map style to be used.

`func onApplePayCouponCodeChange(perform: (String) async ->
PKPaymentRequestCouponCodeUpdate) -> some View`

Called when a user has entered or updated a coupon code. This is required if
the user is being asked to provide a coupon code.

`func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async ->
PKPaymentRequestPaymentMethodUpdate) -> some View`

Called when a payment method has changed and asks for an update payment
request. If this modifier isn’t provided Wallet will assume the payment method
is valid.

`func onApplePayShippingContactChange(perform: (PKContact) async ->
PKPaymentRequestShippingContactUpdate) -> some View`

Called when a user selected a shipping address. This is required if the user
is being asked to provide a shipping contact.

`func onApplePayShippingMethodChange(perform: (PKShippingMethod) async ->
PKPaymentRequestShippingMethodUpdate) -> some View`

Called when a user selected a shipping method. This is required if the user is
being asked to provide a shipping method.

`func onMapCameraChange(frequency: MapCameraUpdateFrequency, () -> Void) ->
some View`

Performs an action when Map camera framing changes

`func onMapCameraChange(frequency: MapCameraUpdateFrequency,
(MapCameraUpdateContext) -> Void) -> some View`

Performs an action when Map camera framing changes

`func payLaterViewAction(PayLaterViewAction) -> some View`

Sets the action on the PayLaterView. See `PKPayLaterAction`.

`func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View`

Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.

`func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View`

Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).

`func translationPresentation(isPresented: Binding<Bool>, text: String,
attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction:
((String) -> Void)?) -> some View`

`func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle)
-> some View`

Sets the style to be used by the button. (see `PKIdentityButtonStyle`).

## Relationships

### Inherited By

  * `DynamicViewContent`
  * `InsettableShape`
  * `NSViewControllerRepresentable`
  * `NSViewRepresentable`
  * `Shape`
  * `ShapeView`
  * `UIViewControllerRepresentable`
  * `UIViewRepresentable`
  * `WKInterfaceObjectRepresentable`

### Conforming Types

  * `AngularGradient`
  * `AnyShape`
  * `AnyView`
  * `AsyncImage`
  * `Button`
  * `ButtonBorderShape`
  * `ButtonStyleConfiguration.Label`
  * `Canvas`

Conforms when `Symbols` conforms to `View`.

  * `Capsule`
  * `Circle`
  * `Color`
  * `ColorPicker`
  * `ContainerRelativeShape`
  * `ContentUnavailableView`
  * `ControlGroup`
  * `ControlGroupStyleConfiguration.Content`
  * `ControlGroupStyleConfiguration.Label`
  * `DatePicker`
  * `DatePickerStyleConfiguration.Label`
  * `DefaultDateProgressLabel`
  * `DefaultSettingsLinkLabel`
  * `DefaultShareLinkLabel`
  * `DisclosureGroup`
  * `DisclosureGroupStyleConfiguration.Content`
  * `DisclosureGroupStyleConfiguration.Label`
  * `Divider`
  * `EditButton`
  * `EditableCollectionContent`

Conforms when `Content` conforms to `View`.

  * `Ellipse`
  * `EllipticalGradient`
  * `EmptyView`
  * `EquatableView`
  * `FillShapeView`
  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `Form`
  * `FormStyleConfiguration.Content`
  * `Gauge`
  * `GaugeStyleConfiguration.CurrentValueLabel`
  * `GaugeStyleConfiguration.Label`
  * `GaugeStyleConfiguration.MarkedValueLabel`
  * `GaugeStyleConfiguration.MaximumValueLabel`
  * `GaugeStyleConfiguration.MinimumValueLabel`
  * `GeometryReader`
  * `GeometryReader3D`
  * `Grid`

Conforms when `Content` conforms to `View`.

  * `GridRow`

Conforms when `Content` conforms to `View`.

  * `Group`

Conforms when `Content` conforms to `View`.

  * `GroupBox`
  * `GroupBoxStyleConfiguration.Content`
  * `GroupBoxStyleConfiguration.Label`
  * `HSplitView`
  * `HStack`
  * `HelpLink`
  * `Image`
  * `KeyframeAnimator`
  * `Label`
  * `LabelStyleConfiguration.Icon`
  * `LabelStyleConfiguration.Title`
  * `LabeledContent`

Conforms when `Label` conforms to `View` and `Content` conforms to `View`.

  * `LabeledContentStyleConfiguration.Content`
  * `LabeledContentStyleConfiguration.Label`
  * `LabeledControlGroupContent`
  * `LabeledToolbarItemGroupContent`
  * `LazyHGrid`
  * `LazyHStack`
  * `LazyVGrid`
  * `LazyVStack`
  * `LinearGradient`
  * `Link`
  * `List`
  * `Menu`
  * `MenuButton`
  * `MenuStyleConfiguration.Content`
  * `MenuStyleConfiguration.Label`
  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `MultiDatePicker`
  * `NavigationLink`
  * `NavigationSplitView`
  * `NavigationStack`
  * `NavigationView`
  * `OffsetShape`
  * `OutlineGroup`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Leaf` conforms to `View`, and
`Subgroup` conforms to `View`.

  * `OutlineSubgroupChildren`
  * `PasteButton`
  * `Path`
  * `PhaseAnimator`
  * `Picker`
  * `PlaceholderContentView`
  * `PresentedWindowContent`
  * `PrimitiveButtonStyleConfiguration.Label`
  * `ProgressView`
  * `ProgressViewStyleConfiguration.CurrentValueLabel`
  * `ProgressViewStyleConfiguration.Label`
  * `RadialGradient`
  * `Rectangle`
  * `RenameButton`
  * `RotatedShape`
  * `RoundedRectangle`
  * `ScaledShape`
  * `ScrollView`
  * `ScrollViewReader`
  * `SearchUnavailableContent.Actions`
  * `SearchUnavailableContent.Description`
  * `SearchUnavailableContent.Label`
  * `Section`

Conforms when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

  * `SecureField`
  * `SettingsLink`
  * `ShareLink`
  * `Slider`
  * `Spacer`
  * `Stepper`
  * `StrokeBorderShapeView`
  * `StrokeShapeView`
  * `SubscriptionView`
  * `TabView`
  * `Table`
  * `Text`
  * `TextEditor`
  * `TextField`
  * `TextFieldLink`
  * `TimelineView`

Conforms when `Schedule` conforms to `TimelineSchedule` and `Content` conforms
to `View`.

  * `Toggle`
  * `ToggleStyleConfiguration.Label`
  * `TransformedShape`
  * `TupleView`
  * `UnevenRoundedRectangle`
  * `VSplitView`
  * `VStack`
  * `ViewThatFits`
  * `ZStack`

## See Also

### Creating a view

Declaring a custom view

Define views and assemble them into a view hierarchy.

`struct ViewBuilder`

A custom parameter attribute that constructs views from closures.

Structure

# ViewBuilder

A custom parameter attribute that constructs views from closures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct ViewBuilder

## Overview

You typically use `ViewBuilder` as a parameter attribute for child view-
producing closure parameters, allowing those closures to provide multiple
child views. For example, the following `contextMenu` function accepts a
closure that produces one or more views via the view builder.

Clients of this function can use multiple-statement closures to provide
several child views, as shown in the following example:

## Topics

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

## See Also

### Creating a view

Declaring a custom view

Define views and assemble them into a view hierarchy.

`protocol View`

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

Article

# Configuring views

Adjust the characteristics of a view by applying view modifiers.

## Overview

In SwiftUI, you assemble views into a hierarchy that describes your app’s user
interface. To help you customize the appearance and behavior of your app’s
views, you use _view modifiers_. For example, you can use modifiers to:

  * Add accessibility features to a view.

  * Adjust a view’s styling, layout, and other appearance characteristics.

  * Respond to events, like copy and paste.

  * Conditionally present modal views, like popovers.

  * Configure supporting views, like toolbars.

Because view modifiers are Swift methods with behavior provided by the `View`
protocol, you can apply them to any type that conforms to the `View` protocol.
That includes built-in views like `Text`, `Image`, and `Button`, as well as
views that you define.

### Configure a view with a modifier

Like other Swift methods, a modifier operates on an instance — a view of some
kind in this case — and can optionally take input parameters. For example, you
can apply the `foregroundColor(_:)` modifier to set the color of a `Text`
view:

Modifiers return a view that wraps the original view and replaces it in the
view hierarchy. You can think of the two lines in the example above as
resolving to a single view that displays red text.

While the code above follows the rules of Swift, the code’s structure might be
unfamiliar for developers new to SwiftUI. SwiftUI uses a declarative approach,
where you declare and configure a view at the point in your code that
corresponds to the view’s position in the view hierarchy. For more
information, see Declaring a custom view.

### Chain modifiers to achieve complex effects

You commonly chain modifiers, each wrapping the result of the previous one, by
calling them one after the other. For example, you can wrap a text view in an
invisible box with a given width using the `frame(width:height:alignment:)`
modifier to influence its layout, and then use the `border(_:width:)` modifier
to draw an outline around that:

The order in which you apply modifiers matters. For example, the border that
results from the code above outlines the full width of the frame.

By specifying the frame modifier after the border modifier, SwiftUI applies
the border only to the text view, which never takes more space than it needs
to render its contents.

Wrapping that view in an invisible one with a fixed 100 point width affects
the layout of the composite view, but has no effect on the border.

### Configure child views

You can apply any view modifier defined by the `View` protocol to any concrete
view, even when the modifier doesn’t have an immediate effect on its target
view. The effects of a modifier propagate to child views that don’t explicitly
override the modifier.

For example, a `VStack` instance on its own acts only to vertically stack
other views — it doesn’t have any text to display. Therefore, applying a
`font(_:)` modifier to the stack has no effect on the stack. Yet the font
modifier does apply to any of the stack’s child views, some of which might
display text. You can, however, locally override the stack’s modifier by
adding another to a specific child view:

### Use view-specific modifiers

While many view types rely on standard view modifiers for customization and
control, some views do define modifiers that are specific to that view type.
You can’t use such a modifier on anything but the appropriate kind of view.
For example, `Text` defines the `bold()` modifier as a convenience for adding
a bold effect to the view’s text. While you can use `font(_:)` on any view
because it’s part of the `View` protocol, you can use `bold()` only on `Text`
views. As a result, you can’t use it on a container view:

You also can’t use it on a `Text` view after applying another general modifier
because general modifiers return an opaque type. For example, the return value
from the padding modifier isn’t `Text`, but rather an opaque result type that
can’t take a bold modifier:

Instead, apply the bold modifier directly to the `Text` view and then add the
padding:

## See Also

### Modifying a view

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Article

# Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

## Overview

To create consistent views, you might reuse the same view modifier or group of
modifiers repeatedly across your views. For example, you might apply the same
font and foreground color to many text instances throughout your app, so they
all match. Unfortunately, this can lead to maintenance challenges, because
even a small change in format, like a different font size, requires changes in
many different parts of your code.

To avoid this overhead, collect a set of modifiers into a single location
using an instance of the `ViewModifier` protocol. Then, extend the `View`
protocol with a method that uses your modifier, making it easy to use and
understand. Collecting the modifiers together provides a single location to
update when you want to change them.

### Create a custom view modifier

When you create your custom modifier, name it to reflect the purpose of the
collection. For example, if you repeatedly apply the `caption` font style and
a secondary color scheme to views to represent a secondary styling, collect
them together as `CaptionTextFormat`:

Apply your modifier using the `modifier(_:)` method. The following code
applies the above example to a `Text` instance:

### Extend the view protocol to provide fluent modifier access

To make your custom view modifier conveniently accessible, extend the `View`
protocol with a function that applies your modifier:

Apply the modifier to a text view by including this extension:

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Instance Method

# modifier(_:)

Applies a modifier to a view and returns a new view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>

##  Parameters

`modifier`

    

The modifier to apply to this view.

## Discussion

Use this modifier to combine a `View` and a `ViewModifier`, to create a new
view. For example, if you create a view modifier for a new kind of caption
with blue text surrounded by a rounded rectangle:

You can use `modifier(_:)` to extend `View` to create new modifier for
applying the `BorderedCaption` defined above:

Then you can apply the bordered caption to any view:

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Protocol

# ViewModifier

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ViewModifier

## Overview

Adopt the `ViewModifier` protocol when you want to create a reusable modifier
that you can apply to any view. The example below combines several modifiers
to create a new modifier that you can use to create blue caption text
surrounded by a rounded rectangle:

You can apply `modifier(_:)` directly to a view, but a more common and
idiomatic approach uses `modifier(_:)` to define an extension to `View` itself
that incorporates the view modifier:

You can then apply the bordered caption to any view, similar to this:

## Topics

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

### Adding animations to a view

`func animation(Animation?) -> some ViewModifier`

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

`func concat<T>(T) -> ModifiedContent<Self, T>`

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

### Handling view taps and gestures

`func transaction((inout Transaction) -> Void) -> some ViewModifier`

Returns a new version of the modifier that will apply the transaction mutation
function `transform` to all transactions within the modifier.

## Relationships

### Inherited By

  * `AnimatableModifier`
  * `EnvironmentalModifier`
  * `GeometryEffect`

### Conforming Types

  * `AccessibilityAttachmentModifier`
  * `EmptyModifier`
  * `ModifiedContent`

Conforms when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

Available when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Structure

# EmptyModifier

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyModifier

## Overview

Use the empty modifier to switch modifiers at compile time during development.
In the example below, in a debug build the `Text` view inside `ContentView`
has a yellow background and a red border. A non-debug build reflects the
default system, or container supplied appearance.

## Topics

### Creating an empty modifier

`init()`

### Getting the identity modifier

`static let identity: EmptyModifier`

## Relationships

### Conforms To

  * `Sendable`
  * `ViewModifier`

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Structure

# ModifiedContent

A value with a modifier applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ModifiedContent<Content, Modifier>

## Topics

### Creating a modified content view

`init(content: Content, modifier: Modifier)`

A structure that the defines the content and modifier needed to produce a new
view or view modifier.

`var content: Content`

The content that the modifier transforms into a new view or new view modifier.

`var modifier: Modifier`

The view modifier.

### Instance Methods

`func accessibility(activationPoint: CGPoint) -> ModifiedContent<Content,
Modifier>`

Specifies the point where activations occur in the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Content,
Modifier>`

Specifies the unit point where activations occur in the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(addTraits: AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Adds the given traits to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(hidden: Bool) -> ModifiedContent<Content, Modifier>`

Specifies whether to hide this view from system accessibility features.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(hint: Text) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(identifier: String) -> ModifiedContent<Content, Modifier>`

Uses the specified string to identify the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(inputLabels: [Text]) -> ModifiedContent<Content,
Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(label: Text) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(removeTraits: AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Removes the given traits from this view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(selectionIdentifier: AnyHashable) ->
ModifiedContent<Content, Modifier>`

Sets a selection identifier for this view’s accessibility element.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(sortPriority: Double) -> ModifiedContent<Content,
Modifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(value: Text) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Content,
Modifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Content,
Modifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Content,
Modifier>`

Adds the given traits to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Content, Modifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Content, Modifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHeading(AccessibilityHeadingLevel) ->
ModifiedContent<Content, Modifier>`

Set the level of this heading.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHidden(Bool) -> ModifiedContent<Content, Modifier>`

Specifies whether to hide this view from system accessibility features.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint(Text) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint<S>(S) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityIdentifier(String) -> ModifiedContent<Content, Modifier>`

Uses the string you specify to identify the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels([LocalizedStringKey]) ->
ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel<S>(S) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel(Text) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityRemoveTraits(AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Removes the given traits from this view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Content,
Modifier>`

Explicitly set whether this Accessibility element responds to user interaction
and would thus be interacted with by technologies such as Switch Control,
Voice Control or Full Keyboard Access.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilitySortPriority(Double) -> ModifiedContent<Content, Modifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Content, Modifier>`

Sets an accessibility text content type.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue(Text) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue<S>(S) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

### Default Implementations

API Reference

DynamicMapContent Implementations

API Reference

MapContent Implementations

## Relationships

### Conforms To

  * `DynamicMapContent`
  * `DynamicTableRowContent`

Conforms when `Content` conforms to `DynamicTableRowContent` and `Modifier`
conforms to `_TableRowContentModifier`.

  * `DynamicViewContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `Equatable`
  * `MapContent`
  * `Scene`

Conforms when `Content` conforms to `Scene` and `Modifier` conforms to
`_SceneModifier`.

  * `TableRowContent`

Conforms when `Content` conforms to `TableRowContent` and `Modifier` conforms
to `_TableRowContentModifier`.

  * `View`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `ViewModifier`

Conforms when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

Available when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Protocol

# EnvironmentalModifier

A modifier that must resolve to a concrete modifier in an environment before
use.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol EnvironmentalModifier : ViewModifier where Self.Body == Never

## Topics

### Resolving a modifier

`func resolve(in: EnvironmentValues) -> Self.ResolvedModifier`

Resolve to a concrete modifier in the given `environment`.

**Required**

` associatedtype ResolvedModifier : ViewModifier`

The type of modifier to use after being resolved.

**Required**

## Relationships

### Inherits From

  * `ViewModifier`

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

Instance Method

# onAppear(perform:)

Adds an action to perform before this view appears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onAppear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` before it appears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure completes before the first
rendered frame appears.

## See Also

### Responding to view life cycle updates

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onDisappear(perform:)

Adds an action to perform after this view disappears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDisappear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure doesn’t execute until the
view disappears from the interface.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(priority:_:)

Adds an asynchronous task to perform before this view appears.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task(
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View
    

##  Parameters

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI will automatically cancel the task at some point after the view
disappears before the action completes.

## Return Value

A view that runs the specified action asynchronously before the view appears.

## Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches
that of the modified view. If the task doesn’t finish before SwiftUI removes
the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to
complete, or to wait on the values of an `AsyncSequence` instance. For
example, you can modify a `Text` view to start a task that loads content from
a remote resource:

This example uses the `lines` method to get the content stored at the
specified `URL` as an asynchronous sequence of strings. When each new line
arrives, the body of the `for`-`await`-`in` loop stores the line in an array
of strings and updates the content of the text view to report the latest line
count.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(id:priority:_:)

Adds a task to perform before this view appears or when a specified value
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task<T>(
        id value: T,
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View where T : Equatable
    

##  Parameters

`id`

    

The value to observe for changes. The value must conform to the `Equatable`
protocol.

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI can automatically cancel the task after the view disappears before the
action completes. If the `id` value changes, SwiftUI cancels and restarts the
task.

## Return Value

A view that runs the specified action asynchronously before the view appears,
or restarts the task when the `id` value changes.

## Discussion

This method behaves like `task(priority:_:)`, except that it also cancels and
recreates the task when a specified value changes. To detect a change, the
modifier tests whether a new value for the `id` parameter equals the previous
value. For this to work, the value’s type must conform to the `Equatable`
protocol.

For example, if you define an equatable `Server` type that posts custom
notifications whenever its state changes — for example, from _signed out_ to
_signed in_ — you can use the task modifier to update the contents of a `Text`
view to reflect the state of the currently selected server:

This example uses the `notifications(named:object:)` method to create an
asynchronous sequence of notifications, given by an `AsyncSequence` instance.
The example then maps the notification sequence to a sequence of strings that
correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

Whenever the server status changes, like after the user signs in, the server
posts a notification of this custom type:

The task attached to the `Text` view gets and displays the status value from
the notification’s user information dictionary. When the user chooses a
different server, SwiftUI cancels the task and creates a new one, which then
waits for notifications from the new server.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

Instance Method

# id(_:)

Binds a view’s identity to the given proxy value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func id<ID>(_ id: ID) -> some View where ID : Hashable
    

## Discussion

When the proxy value specified by the `id` parameter changes, the identity of
the view — for example, its state — is reset.

## See Also

### Managing the view hierarchy

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# tag(_:)

Sets the unique tag value of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func tag<V>(_ tag: V) -> some View where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the view’s tag.

## Return Value

A view with the specified tag set.

## Discussion

Use this modifier to differentiate among certain selectable views, like the
possible values of a `Picker` or the tabs of a `TabView`. Tag values can be of
any type that conforms to the `Hashable` protocol.

In the example below, the `ForEach` loop in the `Picker` view builder iterates
over the `Flavor` enumeration. It extracts the string value of each
enumeration element for use in constructing the row label, and uses the
enumeration value, cast as an optional, as input to the `tag(_:)` modifier.
The `Picker` requires the tags to have a type that exactly matches the
selection type, which in this case is an optional `Flavor`.

If you change `selectedFlavor` to be non-optional, you need to remove the
`Optional` cast from the tag input to match.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the picker’s `selection` input have exactly the same type, you
can omit the explicit tag modifier. To see examples that don’t require an
explicit tag, see `Picker`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# equatable()

Prevents the view from updating its child view when its new value is the same
as its old value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func equatable() -> EquatableView<Self>

Available when `Self` conforms to `Equatable`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

Structure

# AnyView

A type-erased view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyView

## Overview

An `AnyView` allows changing the type of view used in a given view hierarchy.
Whenever the type of view used with an `AnyView` changes, the old hierarchy is
destroyed and a new hierarchy is created for the new type.

## Topics

### Creating a view

`init<V>(V)`

Create an instance that type-erases `view`.

`init<V>(erasing: V)`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# EmptyView

A view that doesn’t contain any content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyView

## Overview

You will rarely, if ever, need to create an `EmptyView` directly. Instead,
`EmptyView` represents the absence of a view.

SwiftUI uses `EmptyView` in situations where a SwiftUI view type defines one
or more child views with generic parameters, and allows the child views to be
absent. When absent, the child view’s type in the generic type parameter is
`EmptyView`.

The following example creates an indeterminate `ProgressView` without a label.
The `ProgressView` type declares two generic parameters, `Label` and
`CurrentValueLabel`, for the types used by its subviews. When both subviews
are absent, like they are here, the resulting type is `ProgressView<EmptyView,
EmptyView>`, as indicated by the example’s output:

## Topics

### Creating an empty view

`init()`

Creates an empty view.

## Relationships

### Conforms To

  * `Sendable`
  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# EquatableView

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EquatableView<Content> where Content : Equatable, Content : View

## Topics

### Creating an equatable view

`init(content: Content)`

`var content: Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# SubscriptionView

A view that subscribes to a publisher with an action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SubscriptionView<PublisherType, Content> where PublisherType : Publisher, Content : View, PublisherType.Failure == Never

## Topics

### Creating a subscription view

`init(content: Content, publisher: PublisherType, action:
(PublisherType.Output) -> Void)`

### Managing the subscription

`var publisher: PublisherType`

The `Publisher` that is being subscribed.

`var action: (PublisherType.Output) -> Void`

The `Action` executed when `publisher` emits an event.

`var content: Content`

The content view.

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# TupleView

A View created from a swift tuple of View values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct TupleView<T>

## Topics

### Creating a tuple view

`init(T)`

`var value: T`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

