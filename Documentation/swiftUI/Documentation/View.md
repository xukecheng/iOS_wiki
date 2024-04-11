Instance Property

# body

The content and behavior of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    var body: Self.Body { get }

**Required** Default implementations provided.

## Discussion

When you implement a custom view, you must implement a computed `body`
property to provide the content for your view. Return a view that’s composed
of built-in views that SwiftUI provides, plus other composite views that
you’ve already defined:

For more information about composing views and a view hierarchy, see Declaring
a custom view.

## Default Implementations

### View Implementations

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

`var body: _ShapeView<Self, ForegroundStyle>`

The content and behavior of the view.

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

## See Also

### Implementing a custom view

`associatedtype Body : View`

The type of view representing the body of this view.

**Required**

` func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

Associated Type

# Body

The type of view representing the body of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## Discussion

When you create a custom view, Swift infers this type from your implementation
of the required `body` property.

## See Also

### Implementing a custom view

`var body: Self.Body`

The content and behavior of the view.

**Required** Default implementations provided.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

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

Collection

API Collection

# Previews in Xcode

Generate dynamic, interactive previews of your custom views.

## Overview

When you create a custom `View` with SwiftUI, Xcode can display a preview of
the view’s content that stays up-to-date as you make changes to the view’s
code. You use one of the preview macros — like `Preview(_:body:)` — to tell
Xcode what to display. Xcode shows the preview in a canvas beside your code.

Different preview macros enable different kinds of configuration. For example,
you can add traits that affect the preview’s appearance using the
`Preview(_:traits:_:body:)` macro or add custom viewpoints for the preview
using the `Preview(_:traits:body:cameras:)` macro. You can also check how your
view behaves inside a specific scene type. For example, in visionOS you can
use the `Preview(_:immersionStyle:traits:body:)` macro to preview your view
inside an `ImmersiveSpace`.

You typically rely on preview macros to create previews in your code. However,
if you can’t get the behavior you need using a preview macro, you can use the
`PreviewProvider` protocol and its associated supporting types to define and
configure a preview.

## Topics

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

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

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

## See Also

### Tool support

API Reference

Xcode library customization

Expose custom views and modifiers in the Xcode library.

Collection

API Collection

# Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

## Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility
support. The framework introspects common elements like navigation views,
lists, text fields, sliders, buttons, and so on, and provides basic
accessibility labels and values by default. You don’t have to do any extra
work to enable these standard accessibility features.

SwiftUI also provides tools to help you enhance the accessibility of your app.
For example, you can explicitly add accessibility labels to elements in your
UI using the `accessibilityLabel(_:)` or the `accessibilityValue(_:)` view
modifier.

To learn more about adding accessibility features to your app, see
Accessibility fundamentals.

## Topics

### Labels

`func accessibilityLabel<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID,
in: Namespace.ID) -> some View`

Pairs an accessibility element representing a label with the element for the
matching content.

### Values

`func accessibilityValue<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

`func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

`func accessibilityValue(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

### Hints

`func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

`func accessibilityHint(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

`func accessibilityHint<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

### Actions

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

### Gestures

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

### Elements

`func accessibilityElement(children: AccessibilityChildBehavior) -> some View`

Creates a new accessibility element, or modifies the
`AccessibilityChildBehavior` of the existing accessibility element.

`func accessibilityChildren<V>(children: () -> V) -> some View`

Replaces the existing accessibility element’s children with one or more new
synthetic accessibility elements.

`func accessibilityHidden(Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies whether to hide this view from system accessibility features.

### Custom controls

`func accessibilityRepresentation<V>(representation: () -> V) -> some View`

Replaces one or more accessibility elements for this view with new
accessibility elements.

`func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Explicitly set whether this Accessibility element responds to user interaction
and would thus be interacted with by technologies such as Switch Control,
Voice Control or Full Keyboard Access.

### Custom content

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID:
KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID:
KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel>(LocalizedStringKey, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor(LocalizedStringKey, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

`func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

`func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

### Replacing system rotors

`func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () ->
Content) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor(AccessibilitySystemRotor, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.
The Rotor will be attached to the current Accessibility element, and each
entry will go the specified range of that element.

### Configuring rotors

`func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View`

Defines an explicit identifier tying an Accessibility element for this view to
an entry in an Accessibility Rotor.

`func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View`

Links multiple accessibility elements so that the user can quickly navigate
from one element to another, even when the elements are not near each other in
the accessibility hierarchy.

`func accessibilitySortPriority(Double) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

### Focus

`func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some
View`

Modifies this view by binding its accessibility element’s focus state to the
given boolean state value.

`func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding,
equals: Value) -> some View`

Modifies this view by binding its accessibility element’s focus state to the
given state value.

### Traits

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

`func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Removes the given traits from this view.

### Identity

`func accessibilityIdentifier(String) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Uses the string you specify to identify the view.

### Color inversion

`func accessibilityIgnoresInvertColors(Bool) -> some View`

Sets whether this view should ignore the system Smart Invert setting.

### Content descriptions

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

### VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

### Charts

`func accessibilityChartDescriptor<R>(R) -> some View`

Adds a descriptor to a View that represents a chart to make the chart’s
contents accessible to all users.

### Large content

`func accessibilityShowsLargeContentViewer() -> some View`

Adds a default large content view to be shown by the large content viewer.

`func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View`

Adds a custom large content view to be shown by the large content viewer.

### Quick actions

`func accessibilityQuickAction<Style, Content>(style: Style, content: () ->
Content) -> some View`

Adds a quick action to be shown by the system when active.

`func accessibilityQuickAction<Style, Content>(style: Style, isActive:
Binding<Bool>, content: () -> Content) -> some View`

Adds a quick action to be shown by the system when active.

## See Also

### Configuring view elements

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

Collection

API Collection

# Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

## Overview

Use these modifiers to configure the appearance of a view, including the use
of color and tint, and the application of overlays and background elements.
Control the visibility of a view and specific elements within a view. Manage
the shape and size of various controls.

For information about configuring views, see View configuration.

## Topics

### Colors and patterns

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func allowedDynamicRange(Image.DynamicRange?) -> some View`

Returns a new view configured with the specified allowed dynamic range.

### Tint

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`func tint(Color?) -> some View`

Sets the tint color within this view.

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

### Light and dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`func preferredSurroundingsEffect(SurroundingsEffect?) -> some View`

Applies an effect to passthrough video.

### Foreground elements

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

### Background elements

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

### Control configuration

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func controlSize(ControlSize) -> some View`

Sets the size for controls within this view.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`func scrollDisabled(Bool) -> some View`

Disables or enables scrolling in scrollable views.

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func menuOrder(MenuOrder) -> some View`

Sets the preferred order of items for menus presented from this view.

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View`

Tells a menu whether to dismiss after performing an action.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

### Symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

### Privacy and redaction

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

### Visibility

`func hidden() -> some View`

Hides this view unconditionally.

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

`func tableColumnHeaders(Visibility) -> some View`

Controls the visibility of a `Table`’s column header views.

`func upperLimbVisibility(Visibility) -> some View`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

### Sensory feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

### Widget configuration

`func widgetAccentable(Bool) -> some View`

Adds the view and all of its subviews to the accented group.

`func widgetCurvesContent(Bool) -> some View`

Displays the widget’s content along a curve if the context allows it.

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

`func dynamicIsland(verticalPlacement:
DynamicIslandExpandedRegionVerticalPlacement) -> some View`

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

## Overview

SwiftUI provides built-in views that display text to the user, like `Text` and
`Label`, or that collect text from the user, like `TextField` and
`TextEditor`. Use text and symbol modifiers to control how SwiftUI displays
and manages that text. For example, you can set a font, specify text layout
parameters, and indicate what kind of input to expect.

To learn more about the kinds of views that you use to display text and the
ways in which you can configure those views, see Text input and output.

## Topics

### Fonts

`func font(Font?) -> some View`

Sets the default font for text in this view.

### Dynamic type

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

### Text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

### Text layout

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

### Multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

### Text selection

`func textSelection<S>(S) -> some View`

Controls whether people can select text within this view.

### Text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

### Find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

### Symbol appearance

`func symbolRenderingMode(SymbolRenderingMode?) -> some View`

Sets the rendering mode for symbol images within this view.

`func symbolVariant(SymbolVariants) -> some View`

Makes symbols within the view show a particular variant.

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

## Overview

Use these modifiers to manage supplemental views that present context-specific
controls and information. For example, you can add titles and buttons to
navigation bars, manage the status bar, create context menus, and add badges
many different kinds of views.

## Topics

### Navigation titles

Configure your apps navigation titles

Use a navigation title to display the current navigation state of an
interface.

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

### Navigation title configuration

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

### Navigation bars

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

### Navigation stacks and columns

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

### Tab views

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

### Toolbars

For information about toolbars, see Toolbars.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(id: String, content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

`func toolbar(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the visibility of a bar managed by SwiftUI.

`func toolbar(removing: ToolbarDefaultItemKind?) -> some View`

Remove a toolbar item present by default

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func toolbarRole(ToolbarRole) -> some View`

Configures the semantic role for the content populating the toolbar.

`func toolbarTitleMenu<C>(content: () -> C) -> some View`

Configure the title menu of a toolbar.

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View`

Configures the toolbar title display mode for this view.

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> some View`

Presents an ornament.

### Context menus

For information about menus in your app, see Menus and commands.

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

### Badges

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

### Help text

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

### Status bar

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

### Touch Bar

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

## See Also

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

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Chart view modifiers

Configure charts that you declare with Swift Charts.

## Overview

Use these modifiers to configure a `Chart` view that you add to your SwiftUI
app.

## Topics

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

### Overlays

`func chartOverlay<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds an overlay to a view that contains a chart.

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

### Visible domain

`func chartXVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the X dimension.

`func chartYVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the Y dimension.

### Interaction

`func chartGesture((ChartProxy) -> some Gesture) -> some View`

## See Also

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

Collection

API Collection

# Style modifiers

Apply built-in styles to different types of views.

## Overview

SwiftUI defines built-in styles for certain kinds of views, and chooses the
appropriate style for a particular presentation context. For example, a
`Label` might appear as an icon, a string title, or both, depending on factors
like the platform, whether the view appears in a toolbar, and so on.

You can override the automatic style by using one of the style modifiers.
These modifiers typically propagate through container views, so you can wrap
an entire view hierarchy in a style modifier to affect all the views of the
given type within the hierarchy. Some view types enable you to create custom
styles, which you also apply using style modifiers.

For more information about styling views, see View styles.

## Topics

### Controls

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`func menuStyle<S>(S) -> some View`

Sets the style for menus within this view.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

### Indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

### Text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

### Collections

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

### Presentation

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

`func presentedWindowStyle<S>(S) -> some View`

Sets the style for windows created by interacting with this view.

`func presentedWindowToolbarStyle<S>(S) -> some View`

Sets the style for the toolbar in windows created by interacting with this
view.

### Groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

## See Also

### Drawing views

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

Collection

API Collection

# Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

## Overview

Use layout modifiers to fine tune the placement of views in a view hierarchy.
You can adjust or constrain the size, position, and alignment of a view. You
can also add padding around a view, and indicate how the view interacts with
system-defined safe areas.

To get started arranging views, see Layout fundamentals. To make adjustments
to a basic layout, see Layout adjustments.

## Topics

### Size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

### Position

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

### Alignment

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

### Padding and spacing

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

### Grid configuration

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

### Safe area and margins

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

### Layer order

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

### Layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

### Custom layout characteristics

`func layoutValue<K>(key: K.Type, value: K.Value) -> some View`

Associates a value with a custom layout property.

## See Also

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

Collection

API Collection

# Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

## Overview

Use these view modifiers to apply many of the rendering effects typically
associated with a graphics context, like adding masks and creating composites.
You can apply these effects to graphical views, like Shapes, as well as any
other SwiftUI view.

When you do need the flexibility of immediate mode drawing in a graphics
context, use a `Canvas` view instead. This can be particularly helpful when
you want to draw an extremely large number of dynamic shapes — for example, to
create particle effects.

For more information about using these effects in your app, see Drawing and
graphics.

## Topics

### Masks and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

`func containerShape<T>(T) -> some View`

Sets the container shape to use for any container relative shape within this
view.

### Scale

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

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

### Rotation and transformation

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

### Graphical effects

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`func opacity(Double) -> some View`

Sets the transparency of this view.

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

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

### Shaders

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

### Composites

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

### Animations

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

## See Also

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

Collection

API Collection

# Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

## Overview

Use input and event modifiers to configure and provide handlers for a wide
variety of user inputs or system events. For example, you can detect and
control focus, respond to life cycle events like view appearance and
disappearance, manage keyboard shortcuts, and much more.

## Topics

### Interactivity

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

### List controls

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

### Scroll controls

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
some View`

Associates a binding to be updated when a scroll view within this view
scrolls.

`func defaultScrollAnchor(UnitPoint?) -> some View`

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

### Taps and gestures

For more information, see Gestures.

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

### Keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

### Keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

### Hover

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect) -> some View`

Applies a hover effect to this view.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

### Focus

For more information, see Focus.

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

### Copy and paste

For more information, see Clipboard.

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

### Drag and drop

For more information, see Drag and drop.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

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

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

### Submission

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`func submitLabel(SubmitLabel) -> some View`

Sets the submit label for this view.

### Movement

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

### Deletion

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

### Commands

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

### Digital crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

### User activities

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

`func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) ->
some View`

Specifies the external events that the view’s scene handles if the scene is
already open.

### View life cycle

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

### File renaming

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

### URLs

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

`func widgetURL(URL?) -> some View`

Sets the URL to open in the containing app when the user clicks the widget.

### Publisher events

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

### Hit testing

`func allowsHitTesting(Bool) -> some View`

Configures whether this view participates in hit test operations.

### Content shape

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

### Import and export

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

### App intents

`func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View`

Sets the given style for ShortcutsLinks within the view hierarchy

`func siriTipViewStyle(SiriTipViewStyle) -> some View`

Sets the given style for SiriTipView within the view hierarchy

## See Also

### Providing interactivity

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# Search modifiers

Enable people to search for content in your app.

## Overview

Use search view modifiers to add search capability to your app. For more
information, see Search.

## Topics

### Displaying a search interface

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
some View`

Configures the search toolbar presentation behavior for any searchable
modifiers within this view.

### Searching with tokens

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

### Searching with editable tokens

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

### Making search suggestions

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

### Limiting search scope

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

### Searching through dictation

`func searchDictationBehavior(TextInputDictationBehavior) -> some View`

## See Also

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# Presentation modifiers

Define additional views for the view to present under specified conditions.

## Overview

Use presentation modifiers to show different kinds of modal presentations,
like alerts, popovers, sheets, and confirmation dialogs.

Because SwiftUI is a declarative framework, you don’t call a method at the
moment you want to present the modal. Rather, you define how the presentation
looks and the condition under which SwiftUI should present it. SwiftUI detects
when the condition changes and makes the presentation for you. Because you
provide a `Binding` to the condition that initiates the presentation, SwiftUI
can reset the underlying value when the user dismisses the presentation.

For more information about how to use these modifiers, see Modal
presentations.

## Topics

### Alerts

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

### Alerts with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

### Confirmation dialogs

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

### Confirmation dialogs with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

### Dialog configuration

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

### Sheets

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

### Popovers

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

### Sheet and popover configuration

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

### File exporter

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

### File importer

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

### File mover

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

### File dialog configuration

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

### Inspectors

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

### Quick look previews

`func quickLookPreview(Binding<URL?>) -> some View`

Presents a Quick Look preview of the contents of a single URL.

`func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some
View`

Presents a Quick Look preview of the URLs you provide.

### Family Sharing

`func familyActivityPicker(isPresented: Binding<Bool>, selection:
Binding<FamilyActivitySelection>) -> some View`

Presents an activity picker view as a sheet.

`func familyActivityPicker(headerText: String?, footerText: String?,
isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) ->
some View`

Presents an activity picker view as a sheet.

### Live Activities

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

### Apple Music

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

### StoreKit

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

### PhotoKit

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

## See Also

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# State modifiers

Access storage and provide child views with configuration data.

## Overview

SwiftUI provides tools for managing data in your app. For example, you can
store values and objects in an environment that’s shared among the views in a
view hierarchy. Any view that shares the environment — typically all the
descendant views of the view that stores the item — can then access the stored
item.

For more information about the types that SwiftUI provides to help manage data
in your app, see Model data.

## Topics

### Identity

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

### Environment values

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

### Preferences

`func preference<K>(key: K.Type, value: K.Value) -> some View`

Sets a value for the given preference.

`func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View`

Applies a transformation to a preference value.

`func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform:
(Anchor<A>) -> K.Value) -> some View`

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

`func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source,
transform: (inout K.Value, Anchor<A>) -> Void) -> some View`

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

`func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View`

Adds an action to perform when the specified preference key’s value changes.

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

### Default storage

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

### Configuring a model

`func modelContext(ModelContext) -> some View`

Sets the model context in this view’s environment.

`func modelContainer(ModelContainer) -> some View`

Sets the model container and associated model context in this view’s
environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

## See Also

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

Collection

API Collection

# Deprecated modifiers

Review unsupported modifiers and their replacements.

## Overview

Avoid using deprecated modifiers in your app. Select a modifier to see the
replacement that you should use instead.

## Topics

### Accessibility modifiers

`func accessibility(label: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

Deprecated

`func accessibility(value: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

Deprecated

`func accessibility(hidden: Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies whether to hide this view from system accessibility features.

Deprecated

`func accessibility(identifier: String) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Uses the specified string to identify the view.

Deprecated

`func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets a selection identifier for this view’s accessibility element.

Deprecated

`func accessibility(hint: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

Deprecated

`func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies the unit point where activations occur in the view.

Deprecated

`func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies the point where activations occur in the view.

Deprecated

`func accessibility(inputLabels: [Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

Deprecated

`func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

Deprecated

`func accessibility(removeTraits: AccessibilityTraits) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Removes the given traits from this view.

Deprecated

`func accessibility(sortPriority: Double) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Deprecated

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

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

### Text modifiers

`func autocapitalization(UITextAutocapitalizationType) -> some View`

Sets whether to apply auto-capitalization to this view.

Deprecated

`func disableAutocorrection(Bool?) -> some View`

Sets whether to disable autocorrection for this view.

Deprecated

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

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

### Style modifiers

`func menuButtonStyle<S>(S) -> some View`

Sets the style for menu buttons within this view.

Deprecated

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

Deprecated

### Layout modifiers

`func frame() -> some View`

Positions this view within an invisible frame.

Deprecated

`func edgesIgnoringSafeArea(Edge.Set) -> some View`

Changes the view’s proposed area to extend outside the screen’s safe areas.

Deprecated

`func coordinateSpace<T>(name: T) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

Deprecated

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

`func cornerRadius(CGFloat, antialiased: Bool) -> some View`

Clips this view to its bounding frame, with the specified corner radius.

Deprecated

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

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

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

`func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some
View`

Presents an alert to the user.

Deprecated

### Search modifiers

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S, suggestions: () -> V) -> some View`

Marks this view as searchable, which configures the display of a search field.

Instance Method

# addOrderToWalletButtonStyle(_:)

Sets the button’s style.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func addOrderToWalletButtonStyle(_ style: AddOrderToWalletButtonStyle) -> some View
    

## Discussion

(see `AddOrderToWalletButtonStyle`).

Instance Method

# addPassToWalletButtonStyle(_:)

Sets the style to be used by the button. (see `PKAddPassButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func addPassToWalletButtonStyle(_ style: AddPassToWalletButtonStyle) -> some View
    

Instance Method

# automatedDeviceEnrollmentAddition(isPresented:)

Presents a modal view that enables users to add devices to their organization.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the view.

## Return Value

The modal view that the system presents to the user.

## Discussion

Use this view modifier to present UI in your app for device administrators to
add devices purchased outside of the official channel to their organization —
Apple School Manager, Apple Business Manager, or Apple Business Essentials.
The system requires sign in with a Managed Apple ID that includes device
enrollment privileges.

The following code example shows one way to present this view to your users:

Example Usage:

Instance Method

# complicationForeground()

Promotes this view to the foreground in a complication.

ClockKit  SwiftUI  watchOS 7.0–10.4  Deprecated

    
    
    func complicationForeground() -> some View
    

Deprecated

On watchOS 9.0 or later, use WidgetKit instead

## Return Value

A view that is in the complication foreground.

## Discussion

A view in the foreground will be tinted alongside other foreground views. The
color for both the foreground and background layers is determined by the watch
face.

Instance Method

# continuityDevicePicker(isPresented:onDidConnect:)

A `continuityDevicePicker` should be used to discover and connect nearby
continuity device through a button interface or other form of activation. On
tvOS, this presents a fullscreen continuity device picker experience when
selected. The modal view covers as much the screen of `self` as possible when
a given condition is true.

AVKit  SwiftUI  tvOS 17.0+

    
    
    func continuityDevicePicker(
        isPresented: Binding<Bool>,
        onDidConnect: ((AVContinuityDevice?) -> Void)? = nil
    ) -> some View
    

##  Parameters

`isPresented`

    

A `Binding` to whether the modal view is presented.

`onDidConnect`

    

A closure executed when the picker successfully, connects AVContinuityDevice
or nil if cancelled by a user.

Instance Method

#
lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func lookAroundViewer(
        isPresented: Binding<Bool>,
        initialScene: MKLookAroundScene?,
        allowsNavigation: Bool = true,
        showsRoadLabels: Bool = true,
        pointsOfInterest: PointOfInterestCategories = .all,
        onDismiss: (() -> Void)? = nil
    ) -> some View
    

Instance Method

#
lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func lookAroundViewer(
        isPresented: Binding<Bool>,
        scene: Binding<MKLookAroundScene?>,
        allowsNavigation: Bool = true,
        showsRoadLabels: Bool = true,
        pointsOfInterest: PointOfInterestCategories = .all,
        onDismiss: (() -> Void)? = nil
    ) -> some View
    

Instance Method

# mapCameraKeyframeAnimator(trigger:keyframes:)

Uses the given keyframes to animate the camera of a `Map` when the given
trigger value changes.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapCameraKeyframeAnimator(
        trigger: some Equatable,
        @KeyframesBuilder<MapCamera> keyframes: @escaping (MapCamera) -> some Keyframes<MapCamera>
    ) -> some View
    

##  Parameters

`trigger`

    

A value to observe for changes.

`keyframes`

    

A keyframes builder closure that is called when starting a new keyframe
animation. The current map camera is provided as the only parameter.

## Discussion

When the trigger value changes, the map calls the `keyframes` closure to
generate the keyframes that will animate the camera. The animation will
continue for the duration of the keyframes that you specify.

If the user performs a gesture while the animation is in progress, the
animation will be immediately removed, allowing the interaction to take
control of the camera.

Instance Method

# mapControlVisibility(_:)

Configures all Map controls in the environment to have the specified
visibility

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapControlVisibility(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

how modified map controls should show or hide

## Discussion

MapCompass, MapScaleView, and MapPitchToggle may automatically show and hide
based on the current state of the Map. That may not be appropriate for all use
cases, where always showing a control may be desirable.

Other controls don’t have an automatic visibility behavior, so they will
always be visible when automatic is specified. Controls may also be hidden via
this modifier when conditionalizing the view is not appropriate

Instance Method

# mapControls(_:)

Configures all `Map` views in the associated environment to have standard size
and position controls

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapControls(@ViewBuilder _ content: () -> some View) -> some View
    

##  Parameters

`content`

    

A view builder returning the controls you wish your `Map`

## Discussion

You provide the controls you want to appear atop your map. When using a
control in conjunction with `.mapControls` you don’t need to specify a scope.
Views that are not MapKit controls will be ignored.

Controls can be modified individually or all at once. Custom frames and
alignments set on controls are ignored.

On watchOS, space is at a premium. When using the mapControls modifier,
MapUserLocationButton and MapCompass are automatically combined if present.

Instance Method

# mapFeatureSelectionContent(content:)

Specifies a custom presentation for the currently selected feature.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func mapFeatureSelectionContent(@MapContentBuilder content: @escaping (MapFeature) -> some MapContent) -> some View
    

##  Parameters

`content`

    

Generates the custom presentation for a given map feature.

## Discussion

The supported presentation options are `Annotation`, and `Marker`. Other types
of map content will be ignored and handled as though no content was returned.

If empty map content is returned, the system presentation will be used.

Instance Method

# mapFeatureSelectionDisabled(_:)

Specifies which map features should have selection disabled.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func mapFeatureSelectionDisabled(_ selectionDisabled: @escaping (MapFeature) -> Bool) -> some View
    

##  Parameters

`selectionDisabled`

    

Determines if selection should be disabled for a given map feature.

## Discussion

The `selectionDisabled` parameter takes a closure which maps map features, to
booleans. If that closure returns true for a given map feature, that map
feature will be considered unselectable.

Instance Method

# mapScope(_:)

Creates a mapScope that SwiftUI uses to connect map controls to an associated
map.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapScope(_ scope: Namespace.ID) -> some View
    

Instance Method

# mapStyle(_:)

Specifies the map style to be used.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapStyle(_ value: MapStyle) -> some View
    

Instance Method

# onApplePayCouponCodeChange(perform:)

Called when a user has entered or updated a coupon code. This is required if
the user is being asked to provide a coupon code.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+

    
    
    func onApplePayCouponCodeChange(perform action: @escaping (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View
    

## Return Value

An update to the payment request with the coupon code.

Instance Method

# onApplePayPaymentMethodChange(perform:)

Called when a payment method has changed and asks for an update payment
request. If this modifier isn’t provided Wallet will assume the payment method
is valid.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayPaymentMethodChange(perform action: @escaping (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View
    

## Return Value

An update to the payment request method.

Instance Method

# onApplePayShippingContactChange(perform:)

Called when a user selected a shipping address. This is required if the user
is being asked to provide a shipping contact.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayShippingContactChange(perform action: @escaping (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View
    

## Return Value

An update to the payment request shipping methods.

Instance Method

# onApplePayShippingMethodChange(perform:)

Called when a user selected a shipping method. This is required if the user is
being asked to provide a shipping method.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayShippingMethodChange(perform action: @escaping (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View
    

## Return Value

An update to the payment request shipping method.

Instance Method

# onMapCameraChange(frequency:_:)

Performs an action when Map camera framing changes

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func onMapCameraChange(
        frequency: MapCameraUpdateFrequency = .onEnd,
        _ action: @escaping () -> Void
    ) -> some View
    

##  Parameters

`frequency`

    

How frequently the action should be performed during a camera interaction.

`action`

    

A closure to run when the camera framing changes.

Instance Method

# onMapCameraChange(frequency:_:)

Performs an action when Map camera framing changes

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func onMapCameraChange(
        frequency: MapCameraUpdateFrequency = .onEnd,
        _ action: @escaping (MapCameraUpdateContext) -> Void
    ) -> some View
    

##  Parameters

`frequency`

    

How frequently the action should be performed during a camera interaction.

`action`

    

A closure to run when the camera framing changes. The closure takes a
`MapCameraUpdateContext` parameter that indicates the camera and the framed
area.

Instance Method

# payLaterViewAction(_:)

Sets the action on the PayLaterView. See `PKPayLaterAction`.

PassKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func payLaterViewAction(_ action: PayLaterViewAction) -> some View
    

Instance Method

# payLaterViewDisplayStyle(_:)

Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.

PassKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func payLaterViewDisplayStyle(_ displayStyle: PayLaterViewDisplayStyle) -> some View
    

Instance Method

# payWithApplePayButtonStyle(_:)

Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func payWithApplePayButtonStyle(_ style: PayWithApplePayButtonStyle) -> some View
    

Instance Method

#
translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)

Translation  SwiftUI  iOS 17.4+  iPadOS 17.4+  macOS 14.4+

    
    
    func translationPresentation(
        isPresented: Binding<Bool>,
        text: String,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        replacementAction: ((String) -> Void)? = nil
    ) -> some View
    

Instance Method

# verifyIdentityWithWalletButtonStyle(_:)

Sets the style to be used by the button. (see `PKIdentityButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func verifyIdentityWithWalletButtonStyle(_ style: VerifyIdentityWithWalletButtonStyle) -> some View
    

